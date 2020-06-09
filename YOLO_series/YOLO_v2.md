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

RPN网络预测边界框位置时

$$x=(t_x*w_a)+x_a\\y=(t_y*h_a)+y_a$$

其中$(x,y)$为预测框，$(t_x,t_y)$是偏移值，$(w_a,h_a)$为GT的尺寸，$(x_a,y_a)$是GT的中心坐标。

yolo2弃用了这种方式，yolo2生成的5个anchorbox中，每个box预测5个坐标，$t_x,t_y,t_w,t_h,t_o$。

$$b_x=\sigma(t_x)+c_x\\b_y=\sigma(t_y)+c_y\\b_w=p_we^{t_w}\\b_h=p_he^{t_h}$$

其中网格相对于图片的左上角坐标是$(c_x, c_y)$，边框的宽度和高度是$p_w,p_h$，$\sigma(x)$是Sigmoid激活函数。如下图，虚线框为GT，蓝色框为预测box。

![img](https://img-blog.csdnimg.cn/20181204100032773.png)

#### fine-grained features（细粒度特征）

主要是提出了passthrough层，将较高分辨率的特征与较低分辨率的特征连接起来 。比如26*26\*26的特征图变为13\*13\*2048的特征图，使得后续网络可以在这个特征图上运行。

#### multi-scale training

每10个batches，网络将随机选取新的图片尺寸。由于模型下采样的factor为32，故随机选取的图片尺寸在32的倍数中选择，320,352，···，608。这使得网络能够预测不同分辨率上的物体。

![img](https://img-blog.csdnimg.cn/20181204102345242.png)

### Faster

#### darknet-19

与VGG类似，作者使用3×3的滤波器，在每个池化操作后将通道数加一倍。使用全局average pooling做预测，在3×3的卷积中间使用1×1的滤波器来压缩特征图。作者也使用了BN来稳住训练，加速收敛，以及正则化模型。


![img](https://img-blog.csdnimg.cn/20181204104129436.png)

#### training for classification

在有1000类别的ImageNet数据集上使用随机梯度下降（stochastic gradient descent）训练了160epochs，初始学习率0.1。使用了一些数据增强技巧，如随机裁剪（random crops），旋转，色度、亮度的调整等。

在224*224的数据集上初始化网络后，微调到448\*448的尺寸。10个epochs，初始学习率设为0.001 。由此获得的top-1精度是76.5%，top-5准确率为93.3%。

#### training for detection

对于VOC，预测5个boxes，每个box有5个坐标和20个类别，所以一共需要125个filter。

### Stronger

YOLO9000提出了在分类和检测数据上共同训练的方法。

#### hierarchical classification

显然分类和检测数据标签并不全是互斥的，所以不能直接放入softmax。ImageNet的标签是从WordNet中提取的，WordNet是有向图结构，通过构造一个层级树（hierarchical tree）来简化问题。

#### joint classification and detection

利用Joint training，YOLO9000使用COCO中的检测数据来学习找到图像中的物体，使用ImageNet中的数据来学习分类图像中的物体。



reference：

[YOLOv2 论文学习](https://blog.csdn.net/calvinpaean/article/details/84772908?ops_request_misc=%7B%22request%5Fid%22%3A%22159166428619195162554443%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=159166428619195162554443&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-3-84772908.nonecase&utm_term=yolo+v2)

[YOLO v2学习总结](https://blog.csdn.net/ft_sunshine/article/details/98682310?ops_request_misc=%7B%22request%5Fid%22%3A%22159166428619195162554443%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=159166428619195162554443&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-1-98682310.nonecase&utm_term=yolo+v2)

s