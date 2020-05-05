# YOLO-v1：you look only once

## 简介

* **与RCNN系的对比**

RCNN系：先找到Region Proposal，然后分类或回归。准确度高但速度慢。

YOLO系：只使用一个CNN网络直接预测不同目标的位置和类别。速度更快但准确率稍低。

* **YOLO的主要特点**

1. 速度快

2. 使用全图，背景错误比较少
3. 泛化能力强

* **YOLO的核心思想**

用整张图作为网络的输入，直接在输出层回归bounding box的位置和bounding box所属的类别。

## 名词解释

* mAP: mean Average Precision, 即各类别AP的平均值
  * AP: PR曲线下面积，后文会详细讲解
  * PR曲线: Precision-Recall曲线
  * Precision: TP / (TP + FP)
  * Recall: TP / (TP + FN)
  * TP: IoU>0.5的检测框数量（同一Ground Truth只计算一次）
  * FP: IoU<=0.5的检测框，或者是检测到同一个GT的多余检测框的数量
  * FN: 没有检测到的GT的数量

## 原理分析

* **滑动窗口与CNN**

用不同尺寸的窗口在图片上滑动，对区域内做图像分类。





[【深度学习YOLO V1】深刻解读YOLO V1（图解）](https://blog.csdn.net/c20081052/article/details/80236015?ops_request_misc=&request_id=&biz_id=102&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0)

[yoloV1，看过好多篇，这篇感觉讲的最通俗易懂](https://blog.csdn.net/m0_37192554/article/details/81092514?ops_request_misc=&request_id=&biz_id=102&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1)