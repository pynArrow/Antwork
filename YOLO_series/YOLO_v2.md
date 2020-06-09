# YOLO9000: Better, Faster, Stronger

[TOC]

## 简介

YOLO9000是CVPR2017的最佳论文提名。这篇论文一共介绍了YOLOv2和YOLO9000两种模型，前者是v1的升级版，而后者做了提升可以检测9000多类物体，因此得名。在67帧每秒时，YOLOv2在VOC2007上的精度是76.8。在40帧每秒时，YOLOv2的精度是78.6，超过了主流的方法如Faster R-CNN和SSD，而且速度更快。

## 基本原理

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190807003809740.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z0X3N1bnNoaW5l,size_16,color_FFFFFF,t_70)

### Better

#### batch normalization

在GOOGLeNet中提到过。BN对每一个mini-batch数据的内部进行标准化（normalization），使输出规范化到N（0,1）的正态分布，减少了内部神经元分布的改变。

在所有卷积层后增加一个BN，可以有效提升收敛能力，而不需要其他形式的正则化。同时在去除dropout后不必担心过拟合问题。

#### high resolution classifier

YOLOv2首先在448*448分辨率的ImageNet上微调分类网络，总共10个epochs。这使得网络有时间调整filter，以在更高分辨率的输入上运行。然后在检测数据上微调此输出网络。

#### convolutional with anchor boxes

yolov1直接使用全连接层来预测边框的位置。在v2中，作者移除了YOLO中的全连接层，借鉴Faster RCNN使用anchor boxes来预测边框。经过卷积层后得到13\*13的特征图，每个cell预测9个建议框，总共预测13 * 13 * 9 = 1521个boxes。

对于YOLOv1，每个cell都预测2个boxes，每个boxes包含5个值：(x,y,w,h,c)(x, y, w, h, c)(x,y,w,h,c) ，前4个值是边界框位置与大小，最后一个值是置信度（confidence scores，包含两部分：含有物体的概率以及预测框与ground truth的IOU）。但是每个cell只预测一套分类概率值（class predictions，其实是置信度下的条件概率值）,供2个boxes共享。YOLOv2使用了anchor boxes之后，每个位置的各个anchor box都单独预测一套分类概率值，这和SSD比较类似（但SSD没有预测置信度，而是把background作为一个类别来处理）。

#### dimension clusters

在Faster RCNN中，anchor box的长度是手动设定的，不一定适合所有尺寸的物体。而YOLOv2采用kmeans聚类方法对训练集中的边界框做了聚类分析，采取的评判标准并非传统的欧式距离，因为这会使较大的box产生更大的距离。实际上作者采用IOU来评判，使其与尺度无关。

$$d(box,centroid)=1-IOU(box,centroid)$$

![img](https://img-blog.csdnimg.cn/20181204092324932.png)

最终是选择了k=5，也就是5种anchor box，但Avg IOU已经达到了Faster RCNN的水平。

![img](https://img-blog.csdnimg.cn/20181204093018757.png)

#### direct location prediction



#### fine-grained features



#### multi-scale training



### Faster

#### darknet-19

#### training for classification

#### training for detection

### Stronger

#### hierarchical classification

#### joint classification and detection

