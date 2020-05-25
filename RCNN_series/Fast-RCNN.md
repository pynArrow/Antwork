# Faster-RCNN——Ross Girshick

## 简介

Fast-RCNN是 Ross Girshick继RCNN之后，在2015年推出的目标检测算法，大幅提升了目标检测的速度。同样使用最大规模的网络，Fast RCNN和RCNN相比，训练时间从84小时减少为9.5小时，测试时间从47秒减少为0.32秒。在PASCAL VOC 2007上的准确率相差无几，约在66%-67%之间。

**Fast-RCNN的优点**

1. 不用selective search，先卷积，加快了速度
2. 在特征图上找对应原始图像上的框
3. RoI Pooling
4. 回归加分类

**Fast-RCNN的缺点**

1. 在特征图上找选框费时

**Fast-RCNN对RCNN的对比**

* 测试速度加快
  * RCNN在不同颜色空间内同时选框，将会产生大量重叠，提取特征操作冗余。
  * Fast-RCNN直接将整张图片归一化后送入深度神经网络。在邻接时，在加入候选框信息，在末尾的基层处理每个候选框。
* 训练速度加快
* 训练所需空间减小
  * RCNN需要大量特征作为训练样本，而fastRCNN不需要。

**Fast-RCNN流程**

1. Selective Search获取候选框
2. CNN提取图片特征
3. 卷积后得到feature map。根据RoI框选择出相应的区域，即将feature map映射回原图像，最后一次卷积前，用RoI池化层来同一相应的比例。











[【目标检测】Fast RCNN算法详解](https://blog.csdn.net/shenxiaolu1984/article/details/51036677)