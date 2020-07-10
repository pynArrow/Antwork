# Faster-RCNN

[TOC]

## 简介

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

* RPN整体框架

![img](https://images2018.cnblogs.com/blog/75922/201806/75922-20180606060221885-1218551944.png)

**一、pn_conv/3\*3和rpn_conv/3\*3**

得到feature map后进入RPN层，rpn_conv/3\*3和rpn_conv/3\*3是3\*3的卷积，随后进入rpn_cls_score和rpn_bbox_pred均为1*1的全卷积。

3\*3的卷积不改变feature map大小，仍是60\*40\*512。

全卷积实际上是将不同channel进行线性组合，从而升维或降维 。

![img](https://images2018.cnblogs.com/blog/75922/201803/75922-20180306112401556-1644312461.png)

**二、 rpn_data**

![img](https://images2018.cnblogs.com/blog/75922/201806/75922-20180606060221885-1218551944.png)

这一层主要是生成anchor box，并和GT对比。

- 生成Anchor

 所谓Anchor即region proposal，由（x1,y1,x2,y2）表示，分别代表左上角和右下角坐标。尺寸的3种scale with box areas分别为{128\*128,256\*256,512\*512}，缩放的3种aspect ratios分别为{1:1,2:1,1:2}，一共组合成9种矩形框。对于60*40大小的特征图，共生成60\*40\*9个anchor box。

![img](https://images2018.cnblogs.com/blog/75922/201803/75922-20180306112632912-1507870253.jpg)

当然，这些anchor box存在很多重叠和超边界情况，所以需要对所有的anchor进行过滤和标记。

标记anchor，对应分类任务

1. 去除超过**原图**边界的anchor box。
2. 如果anchor box和GT的IoU最大，则标记为正样本，label=1
3. 如果anchor box和GT的IoU>0.7，则标记为正样本，label=1
4. 如果anchor box和GT的IoU<0.3，则标记为负样本，label=0
5. 余下的样本均丢弃，label=-1

结果返还到rpn_cls_score_reshape。

偏移量，对应定位任务

即计算anchor box和GT之间的偏移量，不断学习减小。

$$\Delta x=\frac{(x^*-x_a)}{w_a}\\\Delta y=\frac{(y^*-y_a)}{h_a}\\\Delta w=log\frac{(w^*)}{w_a}\\\Delta h=log\frac{(h^*)}{h_a}$$

记录四个回归值，返还到rpn_bbox_pred。

**三、 rpn_loss_cls、rpn_loss_bbox、rpn_cls_prob**

![img](https://images2018.cnblogs.com/blog/75922/201806/75922-20180606060221885-1218551944.png)

 rpn_loss_cls和rpn_loss_bbox与Fast RCNN相同，这里不赘述。

rpn_bbox_pred是bbox的预测值（实际上是以前算的偏移值）

**四、proposal**

这一步主要是用NMS进一步矫正region proposal。NMS在RCNN中已经介绍过了，这里不再重复。简单来说就是去重的过程。

### ROI Pooling

输入为RPN层产生的region proposal和VGG提取的feature map。

由于生成region proposal时是以原图为参考的，并不能直接迁移到feature map上 。将坐标值缩小16倍后，才能建立到feature map上的映射。

将feature map的映射区域划分为7*7的区域，每个区域进行max 破欧玲，生成7\*7的feature map。

### FC层

![img](https://images2018.cnblogs.com/blog/75922/201803/75922-20180306114353141-33590742.png)

1. softmax和cls_prob计算物体的类别。
2. bbox_pred学习偏移量，回归出更精准的边框。



reference：

[faster-rcnn原理介绍](https://blog.csdn.net/Lin_xiaoyi/article/details/78214874?ops_request_misc=&request_id=&biz_id=102&utm_term=faster rcnn&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-78214874)

[Faster RCNN 学习笔记](https://www.cnblogs.com/wangyong/p/8513563.html)

