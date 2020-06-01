# Fast-RCNN——Ross Girshick

[TOC]

## 简介

Fast-RCNN是 Ross Girshick继RCNN之后，在2015年推出的目标检测算法，大幅提升了目标检测的速度。同样使用最大规模的网络，Fast RCNN和RCNN相比，训练时间从84小时减少为9.5小时，测试时间从47秒减少为0.32秒。在PASCAL VOC 2007上的准确率相差无几，约在66%-67%之间。

![img](https://images2015.cnblogs.com/blog/1093303/201705/1093303-20170504113546570-1486555910.png)

**RCNN的缺点**

1. 每一个候选框都要经过CNN，时间开销大。
2. 训练所需空间大。RCNN使用多个独立的SVM分类器，需要大量特征作为样本。
3. 步骤繁琐。RCNN需要先fine-tune预训练网络，region proposal需要单独selective search，然后每个类别分别训练分类器，还要用regressors对bbox回归。

**Fast RCNN的改进**

1. 先将整图放入CNN，选取候选框时，直接选取在特征图上的映射。从而避免重复卷积计算。
2. 把类别判断和位置精调统一用深度网络实现，不再需要额外存储。

**Fast-RCNN流程**

1. Selective Search获取候选框
2. CNN提取图片特征
3. 卷积后得到feature map。根据RoI框选择出相应的区域，即将feature map映射回原图像，最后一次卷积前，用RoI池化层来同一相应的比例。

## 基本原理

### 基本结构

框架基于VGGNet。图像归一化为224*224后直接送入网络。先提取出特征，再输入候选区。

![这里写图片描述](https://img-blog.csdn.net/20160411214438672)

### ROI POOLING

在五层卷积层后，有一个roi pooling层。输入卷积后的feature map，和region proposal，提取固定大小的feature map。

在实际训练中，每个mini-batch包含2张图像和128个region proposal（或者叫ROI），也就是每张图像有64个ROI。然后从这些ROI中挑选约25%的ROI，这些ROI和ground truth的IOU值都大于0.5。另外只采用随机水平翻转的方式增加数据集。
测试的时候则每张图像大约2000个ROI。

- 前向

roi pooling将每个候选区均匀分成M*N块，对每块进行Max pooling。将大小不一的候选区域转换为大小统一的数据。

- 后向

### 参数初始化

去除末尾部分，先用CNN网络训练，结果参数作为相应层的初始化参数，其余参数随机初始化。

![这里写图片描述](https://img-blog.csdn.net/20160411214618571)

### SVD（singular value decomposition）

由于全连接层的计算占整个网络的将近一半，Fast RCNN采用SVD分解改进全连接层。一个大的矩阵可以近似分解为三个小矩阵的乘积，分解后的矩阵的元素数目远小于原始矩阵的元素数目，从而达到减少计算量的目的。通过对全连接层的权值矩阵进行SVD分解，使得处理一张图像的速度明显提升。

## 分类和定位

将提取的特征输入到两个并行的全连接层中，cls_score和bbox_predict。

其中cls_score层用于分类，输出K+1维数组，表示属于k类和背景的概率。

bbox_predict层用于调整候选区域位置，输出对应类时，平移缩放的参数。

![这里写图片描述](https://img-blog.csdn.net/20160411154103099)

Fast RCNN使用softmax代替SVM分类，使得目标检测的步骤减少。将整个过程简化为提取roi和CNN训练两个阶段。

### training

![这里写图片描述](https://img-blog.csdn.net/20170603120846321?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDM4MDE2NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### test time

![这里写图片描述](https://img-blog.csdn.net/20170603120943777?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDM4MDE2NQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

### Multi-task Loss

loss_cls层评估分类代价。由真实分类u对应的概率决定：
$Lcls=−logp_u$
loss_bbox评估检测框定位代价。比较真实分类对应的预测参数tu和真实平移缩放参数为v的差别：
$Lloc=Σ^4_{i=1}g(t_i−v_i)$

g为Smooth L1误差，对outlier不敏感：
$g(x)=\begin{cases}0.5x^2 &|x|<1\\|x|−0.5&otherwise\end{cases}$
总代价为两者加权和，如果分类为背景则不考虑定位代价：
$L=\begin{cases}L_{cls}+λL_{loc}&\text{u为前景}\\L_{cls}&\text u为背景\end{cases}$

reference:

[【目标检测】Fast RCNN算法详解](https://blog.csdn.net/shenxiaolu1984/article/details/51036677)

[目标检测算法Fast R-CNN简介]([https://blog.csdn.net/fengbingchun/article/details/87091740?ops_request_misc=&request_id=&biz_id=102&utm_term=fast%20rcnn&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-3-87091740](https://blog.csdn.net/fengbingchun/article/details/87091740?ops_request_misc=&request_id=&biz_id=102&utm_term=fast rcnn&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-3-87091740))

[Fast RCNN算法详解]([https://blog.csdn.net/u014380165/article/details/72851319?ops_request_misc=&request_id=&biz_id=102&utm_term=fast%20rcnn&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-72851319](https://blog.csdn.net/u014380165/article/details/72851319?ops_request_misc=&request_id=&biz_id=102&utm_term=fast rcnn&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-72851319))

