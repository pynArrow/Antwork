# YOLO-v1：you look only once

## 简介

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

## 原理分析

**滑动窗口与CNN**

用不同尺寸的窗口在图片上滑动，对区域内做图像分类。

### 整体结构

相较于RCNN来说，YOLO是一个同一的框架，速度更快，是end-to-end的。

![这里写图片描述](https://img-blog.csdn.net/20180130221048856?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGlhb2h1MjAyMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

1. 将图片resize到488*488
2. 送入CNN网络
3. 非极大值抑制去重

### 网络设计

网络结构参考GooleNet

![这里写图片描述](https://img-blog.csdn.net/20180130221342432?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGlhb2h1MjAyMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

网络输出为边框预测结果

![这里写图片描述](https://img-blog.csdn.net/20180130221547656?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGlhb2h1MjAyMg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)







reference:

[【深度学习YOLO V1】深刻解读YOLO V1（图解）](https://blog.csdn.net/c20081052/article/details/80236015?ops_request_misc=&request_id=&biz_id=102&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0)

[yoloV1，看过好多篇，这篇感觉讲的最通俗易懂](https://blog.csdn.net/m0_37192554/article/details/81092514?ops_request_misc=&request_id=&biz_id=102&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1)