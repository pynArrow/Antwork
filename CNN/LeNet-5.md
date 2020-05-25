## LeNet5 by Yann LeCun

[机器之心](https://www.jiqizhixin.com/graph/technologies/6c9baf12-1a32-4c53-8217-8c9f69bd011b)、[卷积神经网络Lenet-5实现](https://blog.csdn.net/d5224/article/details/68928083)、[反向传播极简入门](https://www.hankcs.com/ml/back-propagation-neural-network.html)

### 简介

**LeNet-5结构图**

![img](https://img-blog.csdn.net/20150903212346407?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

LeNet包含七层

- 输入层：32*32\*1像素的手写数字图片，相当于32\*32=1024个神经元
- C1层：卷积层，包含具有6个5\*5卷积核的卷积层，步长为1，**特征图的大小**为28\*28，**神经元的个数**为28\*28\*6=784。**参数个数**为(5\*5+1)\*6=156，**连接数**为156\*28\*28=122304。
- S2层：池化层，max pooling。padding=0,size=2\*2,stride=2，输出6张大小为14\*14的特征图。
- C3层：卷积层，卷积核大小为5\*5，步长为1，所以得到的特征图为10\*10。16个卷积核一共生成16张特征图$_{[1]}$。每张特征图生成时都需要加上偏置项，并用激活函数映射。**参数个数**：(5\*5\*3+1)\*6+(5\*5\*4+1)\*6+(5\*5\*4+1)\*3+(5\*5\*6+1)=1516。**连接数**为1516\*10\*10=151600。
- S4层：池化层，max pooling。padding=0,size=2\*2,stride=2。**特征图**为16张5\*5，**神经元个数**为16\*5\*5=400个。
- C5层：卷积层，卷积核5\*5，最终生成120张特征图，每张大小为1。
- 输出层：分类结果，数字0-9。

> [1]：为什么是16张特征图？
>
> C3的前六个特征图(0,1,2,3,4,5)由S2的相邻三个特征图作为输入，接下来的6个特征图(6,7,8,9,10,11)由S2的相邻四个特征图作为输入，12,13,14号特征图由S2间断的四个特征图作为输入，15号特征图由S2全部(6个)特征图作为输入。
>
> ![img](https://img-blog.csdn.net/20180606094255999)

### 理论基础

- **卷积神经网络和卷积**

图像处理中卷积核是已知的，有某种特定用途的，比如边缘检测算子等。卷积神经网络中卷积核是未知的，需要通过不断训练得到。就相当于机器学习线性回归中学习$w$和$b$一样。

- **池化方式**

均值采样、最大值采样、重叠采样、均方采样、归一化采样、随机采样、形变约束采样等。最常用的是最大值采样，具体见上一篇博客。

- **特征图**

CNN中的每张图片都可以称作特征图，即包含图像特征的图片。在卷积层中，输入图每和一个卷积核进行卷积计算后，就会得到一个特征图。并作为输入图传递到下一层。

- **神经网络和神经元**

多个神经元加权连接形成神经网络。每个神经元由输入向量（矩阵）和输出值（矩阵）构成。输入向量经过权值、偏置的计算，引入激活函数后得到输出值。其中$h_{w,b}(x)$为激活函数。

![](https://ww1.sinaimg.cn/large/6cbb8645gw1exsm4yho09j208c044t8o.jpg)

- **激活函数**

  sigmoid函数分为单极性和双极性（按正负性分）

  - 单极性Sigmoid函数

    $$f(x)=\frac{1}{1+\exp(-x)}$$。

    其导数$$f'(x)=f(x)*(1-f(x))$$。

    ![sigmoid及tanh的函数图像.png](https://ww3.sinaimg.cn/large/6cbb8645gw1exsmps4xz7j20b408cmx8.jpg)

  - 双极性Sigmoid函数

    $$f(x)=tanh(x)=\frac{exp(x)-exp(-x)}{exp(x)+exp(-x)}$$，或$$f(z)=\frac{1-exp(-z)}{1+exp(-z)}$$$（令z=2x）$。

    导数为$$f'(x)=1-f^2(x)$$。

  ![tanh的函数图像.png](https://ww4.sinaimg.cn/large/6cbb8645gw1exsmq4drggj20b408ct8r.jpg)

- **前向传播和后向传播**

  前向传播目的是预测分类，后向传播目的是训练参数。

  **前向传播**

  没什么好说的，和线性回归里是一样的。

  ![神经网络15.png](https://ww2.sinaimg.cn/large/6cbb8645gw1exsp4xmrvqj20d603k74q.jpg)

  **反向传播**

  反向传播是指根据最终输出的预测结果和真实标签的误差，来调整倒数第二层、倒数第三层······第一层中间的权值矩阵和偏置矩阵。

  - 符号定义

    $X_j^l$：第l层的第j个节点的输入。

    $W^l_{ij}$：从l-1层第i个节点到l层第j个节点的权值。

    $O^l_j$：第l层的第j个节点输出。

    $t_k$：真实标签的值。

  - 输出层权值调整

    **损失函数**

    输出层的损失函数$E=\frac 12*\Sigma(O_k-t_k)^2$，这里的1/2是为了使后面的式子更简洁。而神经网络训练的目的就是是这个损失函数尽可能地小，也就是结果尽可能接近。

    **梯度下降**

    梯度下降法即用$f(x)-=\eta f'(x)$，从而取到极小值。所以我们先推导出损失函数的导数。

    首先是输出层的权值：

    ![img](file:///C:\Users\Administrator\Documents\Tencent Files\3284799532\Image\C2C\E2BF6A048884D0B402CDE3A45FE7551B.png)

    (E->y，y->x，x->W)

    ![img](file:///C:\Users\Administrator\Documents\Tencent Files\3284799532\Image\C2C\4EC625B715D3FFD75D405B76146A3DB5.png)

    再看隐层的权值：

    ![img](file:///C:\Users\Administrator\Documents\Tencent Files\3284799532\Image\C2C\B869BB5DAC74D510B181091113751F26.png)

    (E->y，y->x，x->W)

    ![img](file:///C:\Users\Administrator\Documents\Tencent Files\3284799532\Image\C2C\1B037F6BE4EACFA739E981036B18B21A.png)

    最后关于偏置：

    ![img](file:///C:\Users\Administrator\Documents\Tencent Files\3284799532\Image\C2C\7821F4DC3610081BEFE84369E6103445.png)

实现代码以后再更吧。