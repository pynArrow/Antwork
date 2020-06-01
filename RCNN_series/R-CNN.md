# R-CNN——Ross Girshick

论文：《Rich feature hierarchies for accurate oject detection and semantic segmentation》

[TOC]

## 简介

R-CNN（region with CNN features）是一类用于处理序列数据的神经网络。R-CNN是使用深度学习进行目标检测的鼻祖论文（Rich feature hierarchies for accurate object detection and semantic segmentation），此后诸如Fast-RCNN和Faster-RCNN都是基于RCNN的改进。

**RCNN的优点**

1. 速度快。以往的目标检测算法使用滑窗依次判断所有可能的区域，而R-CNN则预先提取一系列可能是物体的候选区域，然后在候选去上提取特征。
2. 自动特征提取。传统目标检测算法在区域中提取人工设定的特征（Haar，HOG），而R-CNN训练深度神经网络进行特征提取。

**RCNN的缺点**

1. 候选框没有共享神经网络，参数多。
2. 使用SVM分类，较为复杂。

**RCNN的大致流程**

1. 生成候选区
2. 候选区上使用深度神经网络提取特征
3. 特征用SVM分类器分类
4. 回归器修正候选框位置

![这里写图片描述](https://img-blog.csdn.net/20160405215259014)

## 名词解释

IoU：intersaction over union

NMS：非极大值抑制算法

Bounding Box：把物体位置标注出来的矩形框

Ground Truth：正确的标注数据

Region Proposal：候选区

fine-tune：微调

mAP：mean average precision。

## RCNN基本原理

目标检测主要有两个任务：其一，对于图像中的每个物体，判断出物体的类型，即分类；其二，判断物体的位置，一般选用回归的方法实现。

![img](https://img-blog.csdn.net/20180502184835184)

* 评估分类：准确率
* 评估定位：IoU

整体框架：

![img](https://images2015.cnblogs.com/blog/1093303/201705/1093303-20170504113229570-69371857.png)

### 微调（fine-tune）

采用ImageNet上训练好的模型，然后在PASCAL VOC数据集上微调。这是因为ImageNet上有大量数据集，用CNN学习特征后在小规模数据集上规模化训练。

### 候选区域的生成

生成候选区的方法有：objectness、selective search、category-independen object proposals、constrained parametric min-cuts(CPMC)、multi-scale combinatorial grouping（MCG）、Ciresan等。R-CNN选择的是selective search。

<img src="https://img-blog.csdn.net/20180502185009252" alt="img" style="zoom:50%;" />

* **selective search**

使用Selective Search方法从一张图像生成约2000-3000个候选区域。基本思路：

1. 使用过分割手段，将图像分为小区域。
2. 查看现有区域，**合并可能性最高的两个区域**，从发直到整张图像合并成一个区域位置。
3. 输出候选区

通过Selective Search产生的候选框大小不一，RCNN将所有输入统一变换成227*227的尺寸，在变换还添加了边框。

* **区域的合并**

上述思路的关键在于“合并”的过程。一般来说，**区域的合并**有以下优先规则：

1. 颜色相近的（颜色直方图）
2. 纹理相近的（梯度直方图）
3. 合并后总面积小的$_{[1]}$
4. 合并后在Bounding Box中所占比例大的$_{[2]}$

> [1]：保证每一次合并后的区域相对均匀，避免出现一个大区域不断合并其他小区域的情况。
>
> [2]：也就是说选取合并后在矩形框中占比更大的，否则不合并。目的是使物体形状规则。

### 多样化与后处理

为了尽可能不遗漏候选区，候选区将在多个颜色空间中同时生成，生成后放入分类器。针对梅格雷，通过计算IoU的指标，采取非极大值抑制算法，剔除重复位置的区域。

- **IoU**

IoU的输入：

1. ground-truth的bounding box

2. 预测的bounding box

IoU的输出：

两个矩形交集的面积/两个矩形并集的面积

<img src="https://img-blog.csdn.net/20180105151249336?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVuZG91YmFzYW9uaWFu/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="img" style="zoom:50%;" />

<img src="https://img-blog.csdn.net/20180105151311520?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvZmVuZG91YmFzYW9uaWFu/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="img" style="zoom:50%;" />

- **非极大值抑制算法**

用于对生成的大量候选框进行后处理，去除冗余的候选框。如下图。

![这里写图片描述](https://img-blog.csdn.net/20180120111703066?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQmxhdGV5YW5n/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

具体步骤：

1. 先根据候选框的类别分类概率做排序：A<B<C<D<E<F，并标记最大概率矩形框F是我们要留下来的。
2. 分别判断A-E与F的IoU是否大于某个设定的阈值，如果重叠度超过阈值，就除去。
3. 从剩下的除F之外的矩形框中，选择标记最大概率的候选框，继续重复上述步骤。

### 特征提取

* **预处理**

在使用深度神经网络提取特征之前，首先把候选区**归一化**成统一尺寸227*227。当然，外扩或内缩可以采用不同的方法，如原比例放大/缩小、直接填补灰色区等。不同的方法会轻微影响性能。

* **预训练**

**网络结构**借鉴AlexNet。

<img src="https://img-blog.csdn.net/20160405214721512" alt="这里写图片描述" style="zoom:75%;" />

这里训练的是模型识别物体类型的能力，而不是预测bbox位置的能力。提取4096维特征，经过全连接层后，输出1000维特征。采用SGD训练，初始学习率0.01。

* **微调训练**

同样使用AlexNet，最后一层输出21维（20种类+1背景）。学习率0.001。

* **框架精简**

作者发现同时移除fc6和fc7在fine-tune之前并没有很大损失，所以得出结论：pool5学习了泛化能力，而能力的提升则是通过fine-tune。

### 类别判断

* **SVM分类器**

每个候选框都放入SVM中判断物体类别。每个类别对应一个SVM，输入深度神经网络输出的4096维特征（也就是除去最后一层），输出positive或 negatoive。

![img](https://img-blog.csdn.net/20180502185111157)

由于负样本很多，使用hard negative mining方法。

* **hard negative mining**

hard negative mining解决的是负样本的训练问题。如果仅仅将随机创建的、不与正样本重叠的bounding box作为负样本，训练出的分类器并不好用，会抛出一堆错误的正样本。**负样本不是bounding box中学习的负样本，于是错误地预测为正样本**。

hard negative就是当错误检测到patch（特征图中的块）时，明确地从patch中创建负样本，并添加到训练集中。当再次训练后，分类器就会不断表现得更好。

* **mAP**

作为分类效果的评价指标。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20181210155409619.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JyaWJsdWU=,size_16,color_FFFFFF,t_70)

即每一个类别的AP平均値。具体见[目标检测中的mAP是什么含义？](https://www.zhihu.com/question/53405779)。

### 位置精修

* **回归器bounding box regression**

对于每一类目标，训练一个线性脊回归器精细修正候选框的位置，说白了就是把region proposal往gound truth上靠（图中红框到蓝框的过程）。正则项$\lambda=10000$。输入为深度网络pool5层的4096维特征，输出为xy方向的缩放和平移。

<img src="https://img-blog.csdn.net/20170831205020797?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvemlqaW4wODAyMDM0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="这里写图片描述" style="zoom: 80%;" />

bounding box一般用四维向量（$x, y, w, h$）来表示，分别代表中心点和宽高。

参考资料：

[边框回归(Bounding Box Regression)详解](https://blog.csdn.net/zijin0802034/article/details/77685438#commentsedit)

[什么是hard negative mining](https://blog.csdn.net/u012285175/article/details/77866878)

[目标检测中IOU的介绍（Intersection over Union）](https://blog.csdn.net/fendoubasaonian/article/details/78981636)

[非极大值抑制算法(NMS)及python实现](https://blog.csdn.net/Blateyang/article/details/79113030)

[【目标检测】RCNN算法详解](https://blog.csdn.net/shenxiaolu1984/article/details/51066975)

 [R-CNN论文详解（论文翻译）](https://blog.csdn.net/v1_vivian/article/details/78599229?ops_request_misc=%7B%22request%5Fid%22%3A%22158779391819195239815734%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=158779391819195239815734&biz_id=0&utm_source=distribute.pc_search_result.none-task-blog-2~blog~baidu_landing_v2~default-3)

