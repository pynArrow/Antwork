# Faster-RCNN

[TOC]

## 简介

**流程**



**主要贡献**

1. 使用RPN（Region Proposal Network）产生建议窗口
2. 产生建议窗口的CNN和目标检测的CNN共享

## 基本原理

### 整体结构

![img](https://images2018.cnblogs.com/blog/75922/201803/75922-20180306111740935-464767956.jpg)

1. 卷积层。跟Fast RCNN差不多。
2. RPN层。

主要用于生成Region Proposals，首先生成一堆Anchor box，生成两个分支，其中一个分支对其reshape后用softmax判断anchors属于前景还是背景（一个二分类）；另一个分支bbox regression修正anchor box，形成较精确的proposal。

3. roi pooling层。

输入为feature map和proposal，得到固定大小的proposal feature map，送入全连接层。

![img](https://images2018.cnblogs.com/blog/75922/201803/75922-20180306111851933-70273855.png)

### 特征提取

对于任意大小的图片，padding成固定尺寸，如上图M\*N。

1. 卷积层：size=3，pad=1，stride=1；feature map和原图尺寸一样。
2. ReLU层
3. pooling层：size=2，stride=2；池化后尺寸减半。

经过CNN后feature map变为原来的1/16。

### RPN（Region Proposal Network）

得到feature map后进入RPN层。先经过3*3的卷积，然后进行两个全卷积。

![img](https://images2018.cnblogs.com/blog/75922/201803/75922-20180306112401556-1644312461.png)

全卷积实际上是将不同channel进行线性组合，从而升维或降维 。

* **生成Anchor**

 