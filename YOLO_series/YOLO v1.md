# YOLO-v1：you look only once

[TOC]

## 简介

YOLO（you look only once）是CVPR2016的一篇文章，广泛运用于工业界，yolo的优点不在于精度，而在于速度。

* **与RCNN系的对比**

RCNN系：two-stage。先找到Region Proposal，然后分类或回归。准确度高但速度慢。

YOLO系：one-stage。只使用一个CNN网络直接预测不同目标的位置和类别。速度更快但准确率稍低。

![这里写图片描述](https://img-blog.csdn.net/20180130220730009?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGlhb2h1MjAyMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

* **YOLO的主要特点**

1. 速度快

2. 使用全图，背景错误比较少
3. 泛化能力强

* **YOLO的核心思想**

用整张图作为网络的输入，直接在输出层回归bounding box的位置和bounding box所属的类别。

## 名词解释

* mAP: mean Average Precision, 即各类别AP的平均值
  * AP: PR曲线下面积
  * PR曲线: Precision-Recall曲线
  * Precision: TP / (TP + FP)
  * Recall: TP / (TP + FN)
  * TP: IoU>0.5的检测框数量（同一Ground Truth只计算一次）
  * FP: IoU<=0.5的检测框，或者是检测到同一个GT的多余检测框的数量
  * FN: 没有检测到的GT的数量
* grid cell：YOLO将整个图像划分为19*19的格子。其中每个格子就是一个grid cell。
* bounding box：网络预测的边框格。
* ground truth：标定的边框格。

## 原理分析

### training

相较于RCNN来说，YOLO是一个同一的框架，速度更快，是end-to-end的。

![这里写图片描述](https://img-blog.csdn.net/20180130221048856?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGlhb2h1MjAyMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

* 大致流程

1. 将图片resize到488*488
2. 送入CNN网络
3. 非极大值抑制去重

* 具体分析

yolo首先将图像分割成S*S个grid（默认为7），对每个grid预测B个bounding box和confidence（默认为2），其中

$$confidence=Pr(Object)*IOU^{truth}_{pred}$$

$$Pr(Object)=\begin{cases}0&\text{,grid中不存在物体}\\1&\text{,grid中存在物体}\end{cases}$$

由上述两个公式我们可以看出，存在物体时confidence为IOU值，否则为0。bounding box的表示与RCNN一致。

同时每个grid预测C个类别的概率，训练时产生S\*S\*(B\*5+C)个参数的张量。

![这里写图片描述](https://img-blog.csdn.net/20180130221547656?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGlhb2h1MjAyMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### 网络结构

网络结构参考GooleNet，都使用了1*1的卷积核压缩信息，构造非线性的特征。但是并未使用Inception Module。

![这里写图片描述](https://img-blog.csdn.net/20180130221342432?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGlhb2h1MjAyMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

* 预训练

在ImageNet上预训练，尺寸为224\*224，然后放大为448\*448。

* 激活函数

最后一层的激活函数时线性激活函数，其它层则使用leaky ReLU：

$$\phi(x)=\begin{cases}x&\text{,x>0}\\0.1x&\text{,otherwise} \end{cases}$$

* **损失函数**

传统的均方误差在这里效果并不好：

1. bbox的维度和class预测向量的维度不同，显然不应该平权。
2. 对于背景box，confidence为0，这会导致网络不稳定，甚至发散。

论文采用的方法是加权处理，即对bbox和confidence施加不同的权重。

1. bbox预测赋予$\lambda_{coord}=5$
2. 对于背景box，confidence的损失为$\lambda_{noobj}=0.5$
3. 有object的box，loss weight=1。 

这里仍然有一个问题：尺寸小的bbox的偏移误差相对于尺寸大的bbox的偏移误差来说更难以接受。

这里作者用了一个比较巧妙的方法，将bbox的width和height取平方根，代替原本的width和height。使得发生相同偏移时，尺寸小的bbox反应大。

> 注：x,y,w,h均已经过归一化处理。

![这里写图片描述](https://img-blog.csdn.net/20160317163417800)

### test time

在测试时将confidence和类别概率相乘，即$$Pr(Class_i|Object)*Pr(Object)*IOU^{truth}_{pred}=Pr(Class_i)*IOU^{truth}_{pred}$$

得到的结果（class-specific confidence）既表征出class的概率，又体现出bbox的准确度。

对得到的分数设置阈值进行过滤，然后执行NMS处理，得到最终检测结果。

reference:

[【深度学习YOLO V1】深刻解读YOLO V1（图解）](https://blog.csdn.net/c20081052/article/details/80236015?ops_request_misc=&request_id=&biz_id=102&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0)

[yoloV1，看过好多篇，这篇感觉讲的最通俗易懂](https://blog.csdn.net/m0_37192554/article/details/81092514?ops_request_misc=&request_id=&biz_id=102&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1) 

