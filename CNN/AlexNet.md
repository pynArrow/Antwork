# AlexNet——Alex&Hinton

[TOC]

## 简介

AlexNet是Alex和Hinton参加2012年imagenet比赛时提出的卷积网络框架，夺得了当年ImageNet LSVRC的冠军，且准确率远超第二名，带来了深度学习的又一次高潮。

### AlexNet整体架构

AlexNet一共有8层，网络结构图：

<img src="https://pic4.zhimg.com/v2-c06c669bfd7c5b5bacb782d946c9eafb_1200x500.jpg" alt="AlexNet的三点革命性启示" style="zoom:50%;" />

前五层为卷积层：

![img](https://img-blog.csdn.net/20180624204850119?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI2Nzk3MDc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

后三层为全连接层：

<img src="https://img-blog.csdn.net/20180624204954232?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI2Nzk3MDc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="img" style="zoom:50%;" />

### 前五层：卷积

前两层结构类似

* 第1层：

  **卷积**：原始图像经预处理变为227×227×3，使用96个11×11×3的卷积核进行卷积计算，分成两份输入到两个GPU中，stride为4，输出size为55×55×48。

  **ReLU**：将55×55×48的特征图放入ReLU激活函数，生成激活图。

  **池化**：激活后的图像进行最大重叠池化，size为3×3，stride为2，池化后的特征图size为27×27×48。池化后进行LRN处理。

* 第2层：与第一层操作类似

  卷积层使用用第1卷积层的输出作为输入，增加了2个像素值的padding，并使用256个核进行滤波，核大小为5 × 5 × 48。

第3，4，5卷积层互相连接，中间没有接入池化层或归一化层。

* 第3层：

  卷积层有384（192×2）个核，核大小为3 × 3 × 256，与第2卷积层的输出相连，padding为1。

* 第4层：

  同第三层。

* 第5层：

  与3、4层相比多了个池化，卷积核256个，核大小为3 × 3 × 192，其余同第三层。池化选用最大池化，size为3×3，stride为2，输出特征图尺寸6×6×256。

### 后三层：全连接

每个全连接层有4096个神经元。

* 第6层：

  **卷积**：因为是全连接层，卷积核size为6×6×256，4096个卷积核生成4096个特征图，尺寸为1×1。然后放入ReLU函数、Dropout处理。

* 第7层：

  同第六层

* 第8层：

  最后一层全连接层的输出是1000维softmax的输入，softmax会产生1000个类别预测的值。

逐层网络结构图：

![img](https://static.oschina.net/uploads/space/2018/0312/011252_WjZo_876354.png)

## 基本原理

### ReLU修正线性单元

模拟神经元输出的激活函数一般是单双极性的sigmoid函数，但是二者在x非常大或小时，函数的输出基本不变，训练速度很慢；而ReLU函数则是非饱和函数，训练更快。同时，此函数具有线性性质（正值部分），在反向传播时，不会有由于非线性引起的剃度弥散现象（顶层误差较大，由于逐层递减误差传递，引起低层误差很小，导致深度网络地层权值更新量很小，导致深度网络局部最优）。所以 ReLU 函数可以用于训练更深层次的网络。

ReLU函数如图：

 ![下载](C:\Users\Administrator\Desktop\cs\ML\blog_image\CNN\下载.png)

在一个4层的卷积网络中使用ReLU函数在CIFAR-10数据集上达到25%的训练错误率要比在相同网络相同条件下使用tanh函数快6倍。

![v2-057e48787a4e618d3e22134ec67723d4_720w (1)](C:\Users\Administrator\Desktop\cs\ML\blog_image\CNN\v2-057e48787a4e618d3e22134ec67723d4_720w (1).jpg)

> **梯度弥散现象**
>
> 当神经网络的层数不断增大时，sigmoid函数等作为激活函数时，靠近输入层的hidden layer梯度小，参数更新慢，很难收敛；靠近输出层的hidden layer梯度大，参数更新快，很快可以收敛。这种现象称为**梯度弥散**。同时，有一个与之相应的问题是，当前面的hidden layer梯度在不断训练变大后，后面的hidden layer梯度指数级增大，称为**梯度爆炸**。

### 多GPU训练

AlexNet采用两个GPU并行训练。先回到开始介绍的网络结构图，可以分为上下两个部分，上方的层和下方的层分别在两个GPU上运行。两个GPU只在特定的层通信（二、四、五层之间就不相互连接）

<img src="https://pic4.zhimg.com/v2-c06c669bfd7c5b5bacb782d946c9eafb_1200x500.jpg" alt="AlexNet的三点革命性启示" style="zoom:50%;" />

* **局部响应归一化层Local Response Normalization**

> ##### 为什么要引入LRN层？
>
> 首先要引入一个神经生物学的概念：**侧抑制（lateral inhibitio），即指被激活的神经元抑制相邻的神经元。**归一化（normaliazation）的目的就是**“抑制”**,LRN就是借鉴这种侧抑制来实现局部抑制，尤其是我们使用ReLU的时候，这种“侧抑制”很有效 ，由于ReLU的相应结果是无界的，所以需要归一化。
>
> ###### 归一化有什么好处？
>
> **1.归一化有助于快速收敛；**
>
> **2.对局部神经元的活动创建竞争机制，使得其中响应比较大的值变得相对更大，并抑制其他反馈较小的神经元，增强了模型的泛化能力。**

公式如下：

![010857_080B_876354](C:\Users\Administrator\Desktop\cs\ML\blog_image\CNN\010857_080B_876354.png)

### 重叠的最大池化

之前的CNN中普遍使用平均池化，而AlexNet使用最大池化，避免平均池化的模糊化效果。并且，池化的步长小于核尺寸，这样使得池化层的输出之间会有重叠和覆盖，提升了特征的丰富性。

## 减少过拟合overfitting

### Dropout方法

训练时使用dropout随机互留一部分神经元，避免过拟合。

> 过拟合的表现：模型在训练数据上损失函数较小，预测准确率较高；但是在测试数据上损失函数比较大，预测准确率较低。

Dropout说的简单一点就是：我们在前向传播的时候，让某个神经元的激活值以一定的概率p停止工作，这样可以使模型泛化性更强，因为它不会太依赖某些局部的特征。

<img src="https://pic2.zhimg.com/80/v2-5530bdc5d49f9e261975521f8afd35e9_720w.jpg" alt="img" style="zoom:50%;" />

 因为dropout程序导致两个神经元不一定每次都在一个dropout网络中出现。这样权值的更新不再依赖于有固定关系的隐含节点的共同作用，阻止了某些特征仅仅在其它特定特征下才有效果的情况 。在同一次训练时，即前向和后向的过程中，删除的神经元相同。

### 数据增强data augmentation

AlexNet主要有两种增强方式：

* 镜像反射和随机裁剪。

1. 训练时。从256\*256的图像（原图）上随机提取224\*224的图像块，并在图像块上训练。这样就将样本增加了$(（256-224）^2)*2=2048$倍。
2. 测试时。对左上、左下、右上、右下、中间分别做5次裁剪，加上翻转后，一共10个图像块，测试后对softmax层取平均。

-  改变RGB通道强度

  在整个ImageNet训练集上对RGB像素值执行PCA。对于每幅图像加上多倍找到的主成分，大小成正比的对应特征值乘以一个随机变量，随机变量通过均值为0，标准差为0.1的高斯分布得到。



**reference:**

[大话CNN经典模型：AlexNet](https://my.oschina.net/u/876354/blog/1633143)

[梯度弥散与梯度爆炸](https://www.cnblogs.com/yangmang/p/7477802.html)

[深度学习中Dropout原理解析](https://zhuanlan.zhihu.com/p/38200980)

[局部响应归一化层（LRN）](https://www.jianshu.com/p/c014f81242e7)

[AlexNet网络介绍](https://blog.csdn.net/m0_37876745/article/details/79439623?ops_request_misc=&request_id=&biz_id=102&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0)

[AlexNet 论文翻译——中英文对照](https://blog.csdn.net/weixin_42546496/article/details/87808274?ops_request_misc=%7B%22request%5Fid%22%3A%22158859553119724846431550%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=158859553119724846431550&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-2)

