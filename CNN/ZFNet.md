# ZFNet——Zeiler&Fergus

[TOC]

## 简介

AlexNet的提出使得大型卷积网络开始变得流行起来，但是人们对于CNN网络究竟为什么能表现这么好，以及怎么样能变得更好尚不清楚，因此为了解决上述两个问题，ZFNet提出了一种可视化技术，用于理解网络中间的特征层和最后的分类器层，并且找到改进神经网络的结构的方法。ZFNet是Matthew D.Zeiler 和 Rob Fergus 在2013年撰写的论文[Visualizing and Understanding Convolutional Networks](https://arxiv.org/abs/1311.2901)中提出的，是当年ILSVRC的冠军。ZFNet使用反卷积（deconv）和可视化特征图来达到可视化AlexNet的目的，并指出不足，最后修改网络结构，提升分类结果。

## 原理

### 反卷积网络结构

论文使用反卷积网络(deconvnet)进行可视化。反卷积网络可以看成是卷积网络的逆过程，但它不具有学习的能力，只是用于探测卷积网络。

反卷积网络依附于网络中的每一层，不断的间特征图映射回输入图并可视化。过程中将需要检测的激活图送入反卷积网络，而其余激活图都设置为0。进入反卷积网络后，经过1.unpool；2.rectify；3.filter；不断生成新的激活图，直到映射回原图。大致流程如下：

![TIM图片20200616230024](C:\Users\Administrator\Desktop\cs\ML\blog_image\ZFNet\TIM图片20200616230024.png)

下面具体看一下反卷积网络中的三个步骤。

* unpooling

首先说明，AlexNet中使用的max pooling是不可逆的，因为最大池化丢失了一部分图像信息。但是，如果我们记录了最大池化过程中最大值所在的位置，就可以近似地反池化。

为了记录池化过程中最大值的位置，论文中使用了一种开关（switch）结构，如上图所示。需要说明的一点是，当输入图像确定时，最大池化过程中最大值的位置时固定的，所以开关设置是特定的。

* rectification

AlexNet使用非线性的ReLU作为激活函数，从而修正特征图，使其始终为正。“反激活”的过程，仍使用ReLU进行映射。

* filtering

反卷积的过程使用了一个转置卷积，顾名思义即卷积网络中卷积矩阵的转置（具体查阅[一文搞懂反卷积，转置卷积](https://blog.csdn.net/LoseInVain/article/details/81098502)），直接作用在修正后的反池化图上。

### training details

ZFNet基本沿袭了AlexNet的结构，一个不同点在于AlexNet使用两块GPU并行计算，这也使得AlexNet将训练任务“稀疏”成了两部分，而ZFNet去掉了这一结构。

![TIM图片20200617100651](C:\Users\Administrator\Desktop\cs\ML\blog_image\ZFNet\TIM图片20200617100651.jpg)

* 预处理

1. 每张图片被resize到256\*256，减去该图片中像素值的均值。
2. 做了一个数据增强的处理：四个角+中心的224\*224图像，以及它们的水平翻转图像，作为输入图。

* 训练

训练时使用大小为128的mini-batch随机梯度下降，初始学习率0.01，动量（momentum）为0.9。并且在验证集的错误率稳定时，手动调整学习率。沿用了AlexNet的dropout结构，并设置为0.5的概率。

### 卷积网络可视化

在训练结束后，我们在测试集上运用反卷积网络可视化激活特征图。

* 特征可视化（feature visualization）

![TIM图片20200617090859](C:\Users\Administrator\Desktop\cs\ML\blog_image\ZFNet\TIM图片20200617090859.jpg)

在每一层中，随机选取9个激活程度最高的特征图，反卷积结果如下：

1. 第二层主要相应图像的角点、边缘和颜色。
2. 第三层具有更复杂的不变形，主要捕获相似的纹理。
3. 第四层提取具有类别性的内容，例如狗脸、鸟腿等。
4. 第五层提取具有重要意义的整个对象，例如键盘、狗等。

* 训练时的特征演变（evolution）

![TIM图片20200617091147](C:\Users\Administrator\Desktop\cs\ML\blog_image\ZFNet\TIM图片20200617091147.jpg)

图中每一行代表同一张图片在不同epoch时反卷积的结果（论文中选取1,2,5,10,,20,30,40,64epoch）。结果表明：较低层的特征收敛更快，在几个epoch之后就会收敛、固定；较高层特征收敛更慢，在40-50epochs之后在完全收敛。

* 特征不变性

![TIM图片20200617092535](C:\Users\Administrator\Desktop\cs\ML\blog_image\ZFNet\TIM图片20200617092535.jpg)

论文分别对5张图像进行了三种处理：（从上到下分别是）水平平移、尺寸缩放、旋转图像。第二列的图像表示卷积网络第一层中原始图和特征图向量间的欧式距离。第三列是第七层的欧氏距离。第四列则代表处理后归属正确标签的概率。

实验表明，在前期（layer1），微小的转变（transformation）会导致一个明显的变化。而后期（layer7），水平平移和尺寸缩放带来的改变逐渐稳定，近似呈线性。旋转处理仍有较大变化。这说明CNN具有平移、缩放不变性，而不具有旋转不变性。

### 改进AlexNet

AlexNet中第一层使用11\*11，步长为4的卷积核。然而在可视化时发现，第一层提取的信息多为高、低频，而中频的信息很少提取出。同时在可视化第二层是会发现由于步长过大引起的混叠伪像（aliasing artifact）。所以论文采用更小的卷积核（7\*7）和更短的步长（2）。

![TIM图片20200617100357](C:\Users\Administrator\Desktop\cs\ML\blog_image\ZFNet\TIM图片20200617100357.jpg)