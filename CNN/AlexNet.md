# AlexNet——Alex&Hinton

## 简介

AlexNet是Alex和Hinton参加2012年imagenet比赛时提出的卷积网络框架。

* **AlexNet结构**

<img src="https://pic4.zhimg.com/v2-c06c669bfd7c5b5bacb782d946c9eafb_1200x500.jpg" alt="AlexNet的三点革命性启示" style="zoom:50%;" />

前五层为卷积层：

![img](https://img-blog.csdn.net/20180624204850119?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI2Nzk3MDc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

后三层为全连接层：

<img src="https://img-blog.csdn.net/20180624204954232?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTI2Nzk3MDc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70" alt="img" style="zoom:50%;" />

第1卷积层使用96个核对224 × 224 × 3的输入图像进行滤波，核大小为11 × 11 × 3，步长是4个像素（核映射中相邻神经元感受野中心之间的距离）。第2卷积层使用用第1卷积层的输出（响应归一化和池化）作为输入，并使用256个核进行滤波，核大小为5 × 5 × 48。第3，4，5卷积层互相连接，中间没有接入池化层或归一化层。第3卷积层有384个核，核大小为3 × 3 × 256，与第2卷积层的输出（归一化的，池化的）相连。第4卷积层有384个核，核大小为3 × 3 × 192，第5卷积层有256个核，核大小为3 × 3 × 192。每个全连接层有4096个神经元。最后一层全连接层的输出是1000维softmax的输入，softmax会产生1000类标签的分布。我们的网络最大化多项逻辑回归的目标，这等价于最大化预测分布下训练样本正确标签的对数概率的均值。

## 基本原理

### 架构

* **ReLU修正线性单元**

模拟神经元输出的激活函数一般是单双极性的sigmoid函数，但是二者在x非常大或小时，函数的输出基本不变，训练速度很慢；而ReLU函数则是非饱和函数，训练更快。同时，此函数具有线性性质（正值部分），在反向传播时，不会有由于非线性引起的剃度弥散现象（顶层误差较大，由于逐层递减误差传递，引起低层误差很小，导致深度网络地层权值更新量很小，导致深度网络局部最优）。所以 ReLU 函数可以用于训练更深层次的网络。

![Activation Functions: ReLU & Softmax – mc.ai](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPYAAADNCAMAAAC8cX2UAAAAilBMVEX///8REhYAAAcAAAD6+vrj4+P8/Pz39/f09PSEhIR/f3/x8fHe3t7Z2dnu7u6QkJB4eHjU1NQNDhKwsLB0dHSZmZnNzc2fn5/AwMDKysqVlZWKiopBQUFgYGBsbGxNTU2kpKS2trYoKChYWFgyMjIfHx9mZmZTU1M8PDwbGxsjIyM4ODhISEipqqs7NVnaAAAP60lEQVR4nO0dC3uyvK47vSGXAhO5iCCor+6i///vnRbEoYBCh65zX7bHlkobQtqkTdMIXv4kgP/9SQD/wX/wH/wHYwCdrZPEZtWl6Zn8k6XiMwvIzz3XnUFLksN8lVYEuv98/omh+HRS9IMPdl/QkhkAwcoCrh2HCLgrlxfiV0G27j052bOVGW1S7yP4O2Rvk8xe6XQ/54N5Q/8O2Qtn+e7if4v1egGx9VfITuZI26bWR5xPp3nFbRjxT895ZknOx7b7mr8FxWVJtvF+AABtggc/C5lMUJiGj0DFuU0AStPgZZJNPOC+6LPZzJp9xFmyMR/xAHWwJkzHjvEATDSe8k9/jcNkuc2Bud7v94uQZOulZz0A/TmwGE+Ax27f+FzAYqYDzwBRaOHnBTMKz8dRvg4nWYzYPrYFzO0K5hdpPVcDT28rvQ6iocSZ90J2WTJJh+PjsIH7M7J9zuWQAbyV7C2W5PjIJcczc2Vq+e9w3fqFJ6k5saQ0jCTJNrBMpR3ceq3fPHrCYD5SZ9lw5U5aCZTlNtPk6slyW5MYVO4LzIx2vspym0jWsyS5TYbP3rU1TBDSx+U2lavnS3KbDuf2DP5zwcjcRo/m9uDX7K4gXwzQkbktObYfxm20hUv+jL+d20PH9gEW5jpFuC0tyQfqbfwBbZGycbktCw/S2ySF+2JYkF/O7WFjO4ewNCaMzG1ZvS3L7WH48AbqZW5sva20JHfg21EW/HZJPkRvn7p4pyRvIduvXqx1RXoa7Y/hdlfRfIHqEdzGC3had13nNrLXa91xxDsKs0pFMr2biHZuWzMD+PEsaHsnJBOtP0Jvx3B1evAbepvtY0qt9wPA3tdK2nc6m24d23TiA7x3kTNvq6KlWJ7bAyR5BGF+urgxttk/zgv6MQFB9vUl9fxBz+bzlxgsOeK31ofM7G/o7d6yhC1h+tXbbkjySNisw5eQpgWlFBuAcz2bXd6vMaIxBrRyEBuMGUQMPEYYvz3OxOYt78mvFyYgUYPwMUceMEubwVXt1d7Q2/Y+CgMnAmwn2kfzD+8Q8JexFe/NmpZwyAGapfPssMumwVr0WC/TlxjQQ7YNJntG9j6gCR8YFjzvJdHbfhozQJfu/Wdp/ivMapc3Zmlrx4x2/H5LLFsAi8yDGInuUvRWHB4hAm5o7xhIUor3IedeDvIFA3kEPMfyNI1LEprweYJ5Qbbv+ls+hlCS331sazuY1MXOdW6zDZcCwQYBf12KTCsWXLf2F9gYW3OWc3LNTxfYb7xfcyoZIbucDz68MvhkuIXbgM6FkCHp9O6SvLAt1DFf5Xb4wamMPxBwd4U4cDnVpOK2OztCJqZ9FnA3DEyXhrGeALI7iAasDQYaYCt+d8zHtvt+zlPDDkVraCvP7Z562/qA59uJ1yX57I0ALVkQZpaE6hbiXZfzXmgz5h6BP3LE+X/YEZDOrXB9AObKzenUnS4omwL0yW/I9whkaw2YXzKI2lNqTSlA6/DOszS6hbtzzXqN2yzcb3xE4s88x2tLcCdL90J/5413ZfNOPbF5f7UDmun+fD+L2Hpir8PMBIRzE9A0iJIQaOvFqc50Zu92vNsbfKJ8X25n8OVieF3jNsunuY+AEUYM6Fz2aCbwc8Fne3p5v+CWUF445KMgipgVUmBG2IoEc6exaCyMxOj6muoQiyMoitbfmKX10dvmqrQt1KDvCiys3ceSTm3ZajnF6df9pLllr+f3XW8jDy4vb+u73iZ2dMrPDgMfbpqdslFjgudP0H2tK1MIo8uyFr2taW3rbTarWOZn3T2rfb2NshMz2WVdo2j3jtzGGxg3CpvcdtM0alt4nobRtTV1x1i7MgRLWXw/6wpx4KI5JptjOzxEc9C9xroO6u2K5PWF1wmaktxaLzm3KQEyfxSVaflffpDaRUc1YFlS6AjvK63tVRgBe4PeCb0oKG5ARoPbhxzrYBuZiCEMMGGUIUZ4DolcvYSnRY4hQytyyDAwEzlD04yijFImcoYmbhU5zSBFTisq8hxPRZORX6YCyQkZLwGt6OkJvWHV0Wtl7oReo4YDV5hfn6NnUd7Y3/ZTbwo8phHEXyWfQx1TStBFCTqWlKn44y8flan4QLWP49c8BWUOHXNFU4RwbqMKyRkyegO9UUN/bLeGEYQQTgH5egxSNsRwU5IbXNq2b/bfhkdbTm9IcraE7TbgkS2nsnAnvW3Df+0NK2Inv4/e9iHsmFmNvSsiV+0+tjRtB7cdClURbt9FbwcXtoUa/PZdkSvWFfcddroq998V6QUduyI3wZXldrcfnJZc2hZq0JyuFCBLNlVnD6xpW6jB2N4MyszJrQ1sWPO/4FnHNqr8FtrhWX1X2mwLNXhS3xVhW7hGgiK+KyPPyYkD91d3xxTxXRnZchp++S20w1P6nOJPeMM8NLIkl9bbkmS362395JrTBc84SwtfYWP/4gJU0dsjctvYw/TWYyiit8eU5DHc3PRxUOT0wIh28qjTtlADRdbb41lXjG7bQg0U0dvjcXsGP3q8wg5uy5L943rbfe22LdTgyfQ2WZ+75nTBk+ntAL73Ov44tnVFMqrCSNw2Pxp+C+3wVNYVmsJ9P1WiiN4ex7pyw7ZQA0VmaaPobXPTs4u36m0zYr/SukId2O7C3AJN6wqOp1heb//grkh+y7ZQg+bYzpOJKe3E8YOWU/wJ2w9lt0FzlhYE7qTY1qeNffWihDR22stUlCOmoeL7+rb+aXsfoWLTnqDziiJ1XXCO7AxtHX3tQXhtykjVng43JiEVetSGnlTomdngdphZk6MTB6u7bBz9KtixhOeocXLiMI5eFOzMicOglH80nTgoLyqcOIpUIHE7nThQHT0u0R+dODhSalboQ77woprW7kMibtC0mhNH2OjOzHZM4Em57AAiZmmXLjtlb6yltQpV6sq57IixXbYrjv3U2qs5CdX8d04PQLpWYH0HyQX82B5YDAeFJBp5Tv5T1pXw5ab57AwUmaV9c73NdnA7aDWgiHXlm9yew49h721k68rP6G3//ezYTw94hvW21tO2UANF1tuyZCPxmjP4MTS00hNw23qHrYdHr4H2+7l9zTWnC0YmW5bb31iBXXXN6QJV9sCk9bbVdibiJihiXZHmNk7hQiKK1i/fFRlgPjuDkXdFHi3J8WaAbaEGiuhtSTs50vubz85gZL2tPZbbYeuxnx4wsgLTHqq32RuUfFBF9LYc2RO4kQr4qcwsTWpsR69wKvucv3d/my3hVibypYBfPEuz4bsJJHvX7+V2EVJEIvJlAb/Wm8FIeBeXiHxZwth6+2EKrPRbQJJrgN+qt63y2M8fI5smcC2G9R8jO4PvxcJLEbIfNEs7+S1cOQd2FVQ5BzaIbJLCRUnviJKczani1pUpfD36LYyot/ONofYszXyDk2NWIj55AU1u42xrSG/0PkSk1VxzZEVak+w89BhILUY0YgBGDMRTwoBBNJGrUp7jaZkjGtWQSCllhshplIp//j3S6OmCCtBEg2Va5EokmuuWyIioziq0oEBbpah8DJqLeAtH9BTX0BftluhpiREVyCv0orxEajWjWM68jwxsXd5e6bKBjNJlg19XT1SWGLydIlfQJr7VNGYYlBVk8xKBxxA5kSKRE2QykePPIdwxilQ0eSRbIDPqyEANPS1L8AY6J/QUV+iJQKsVfiUVeqMLveFGLd05JCp38gn8/DoTMV4nL0Dd6UoE634LikxX7k42W5wd+1GE7Luvt+2zcKV/Zb0dvZ8f+1FkvX3nObkhfgqlXqDKnPy+YzuAFzFDkRrcvi/ZzZAiiiiwu3ZybQuTi04t28l/kwI7wNdLvwVFFNg9t/6sf80zEUgNbt+xk6O0Ga5UlU5+xz2wQ9uZCEUk+f24LfwWmqXPPksj7cd+FJml3U2Sdxz7UUSS36uT4wVsfdDnFmnkzLZQg+cWaZ2uOYpw+z5j29hDp71hRcb2fcjuPvajCNl36eTRa+eZCEU6+T1EmrGDSdfbVESk3aOTz+G/zm8V6eR3WIG51479KEL2+JNTEa60+10qMjkd32Ccwcuf06qDKkuRsUWa9e9auFJVuD22AkO8i19jqCIKbGxJPoWvV89EjCfSotSRj8QxMtnmqs22UIPxyDbILFSkkxPv1rGfETs5cUxFuH07pMh43EYBR7X1MToGoKhiQpBTSIrKwaARkuLozcCvaREGonAnELnC7UG4ExxDUmhVSApqHL0Z/KppWvouiLAT/gLqJXp2FhHjeE8RkgKX7gnHiBilN4NRRp84ohcPVz1GFZLCb4akyBeBCVIsIntogP8VqVGkRUmZ8hxPUZE7puKaGUUOoeKfIvEVLS7KXHkjOqsomvTdL2RFifjOgZ+Y1h+j+uYLvYZP6L/aFWhogRHV0aMv9NhtdGfsWkyJcDN9jv3IOmipGxSQLbpsCzX45bO0pkgjdp+QIoosRcZbgUWvPcKVqrIHNpoCo8teIUVU4fZYZM/hqs/eryJkjzW2/Ss/hVIHRYxKI01OxZmIXnyUluTjkj2S3g7gaz8fnvEcqwv4WTd66/2qbaEGqujtMWxpNO0dUuSZrCsH+NI33oIi7nhjKDD80T+kiCIKbIxZWptrTheoQvb3uT0kXKkqZH9/bONPqPevp4jl9Nt6mzhwM0ApPYveHhhS5EmCFLD9sJAiI3P7pwJ+xnB186dQ6vAcs7TzYz894ClmabyLp8N6rSKS/HvrbRuuBkbNeQa9fdVvoR1U4fY3xra2huuhnUWRsf0dO/mVXxLuBEUk+TeCArqrvraFEfApE7oZbeFu+ECVnaUpE7r5AOHwcKVjztIwlo9GLy3J8/4/hVKHb1tOpxXMFosg301rMCBchCy3zf0A20INvs1tp4Jlst17G6cOvdsm7qAZ9QlQ9vLa37ZQA+bKvWdcHQLXK1im6d77WNTgTZ/0hdTpfWsd9M+X6645nWRLyAMg2NMge50kO/0FPhbeP+xZNg/mwYz/zbNTWuTm9ZIy5TmRzuK0uL78C2ZVWubK4llZlX/qyfKSbO/z09NTDl56hK1l9gaMcf+b69UsKeBVpWqdrDnhLApxQbejO4fQsqfT0LUtK+MvYoDcsEKp0J2uLzdGzVAm4qfvAxaWUogTO4kcPcjsKScbzvPNYj6bZjEv8/prJRLPZEabpcdSEo3Ecxllf9iy+BAXMyvXcUKbs9o3Bcc3rr7Rw3SCMS8bQDYI0oME3w6hKaO1AeHoJKqxGDtALxSm6+j8X7f9MN4lXh57m+kkDee635vbKD8cQkpjiV6eRVhOkhMaS/TyOtleGHA225NtnGzD8JCtrE/n4Id5b7KJG0UuYzJkh0EuwzVADCl0WMcO1osVAKdY/5LmSRonu0R37LkzqJOjwBtmDCtBs3W5eNuBJ/O6giQLvVKY6N0wZGz/NviP7L9E9pUZs+wq9DfA6xX439MCePmT8H9ttFMlSYkuNQAAAABJRU5ErkJggg==)

> **梯度弥散现象**
>
> 当神经网络的层数不断增大时，sigmoid函数等作为激活函数时，靠近输入层的hidden layer梯度小，参数更新慢，很难收敛；靠近输出层的hidden layer梯度大，参数更新快，很快可以收敛。这种现象称为**梯度弥散**。同时，有一个与之相应的问题是，当前面的hidden layer梯度在不断训练变大后，后面的hidden layer梯度指数级增大，称为**梯度爆炸**。

* **多GPU训练**

* **局部响应归一化层Local Response Normalization**

> ##### 为什么要引入LRN层？
>
> 首先要引入一个神经生物学的概念：**侧抑制（lateral inhibitio），即指被激活的神经元抑制相邻的神经元。**归一化（normaliazation）的目的就是**“抑制”**,LRN就是借鉴这种侧抑制来实现局部抑制，尤其是我们使用RELU的时候，这种“侧抑制”很有效 ，因而在alexnet里使用有较好的效果。
>
> ###### 归一化有什么好处？
>
> **1.归一化有助于快速收敛；**
>
> **2.对局部神经元的活动创建竞争机制，使得其中响应比较大的值变得相对更大，并抑制其他反馈较小的神经元，增强了模型的泛化能力。**

公式如下：

<img src="https://upload-images.jianshu.io/upload_images/14512145-79998a5bbd55b2a2.png?imageMogr2/auto-orient/strip|imageView2/2/w/756/format/webp" alt="img" style="zoom:50%;" />

* **重叠的最大池化**

之前的CNN中普遍使用平均池化，而AlexNet使用最大处化，避免平均池化的模糊化效果。并且，池化的步长小于核尺寸，这样使得池化层的输出之间会有重叠和覆盖，提升了特征的丰富性。

### 减少过拟合overfitting

- **Dropout方法**

训练时使用dropout随机互留一部分神经元，避免过拟合。

> 过拟合的表现：模型在训练数据上损失函数较小，预测准确率较高；但是在测试数据上损失函数比较大，预测准确率较低。

Dropout说的简单一点就是：我们在前向传播的时候，让某个神经元的激活值以一定的概率p停止工作，这样可以使模型泛化性更强，因为它不会太依赖某些局部的特征。

<img src="https://pic2.zhimg.com/80/v2-5530bdc5d49f9e261975521f8afd35e9_720w.jpg" alt="img" style="zoom:50%;" />

 因为dropout程序导致两个神经元不一定每次都在一个dropout网络中出现。这样权值的更新不再依赖于有固定关系的隐含节点的共同作用，阻止了某些特征仅仅在其它特定特征下才有效果的情况 。

* **数据增强data augmentation**

AlexNet主要有两种增强方式：

1. 产生图像变换和水平翻转。从256\*256的图像上随机提取224\*224的图像块，并在图像块上训练。
2. 改变图像RGB通道的强度。



**reference:**

[梯度弥散与梯度爆炸](https://www.cnblogs.com/yangmang/p/7477802.html)

[深度学习中Dropout原理解析](https://zhuanlan.zhihu.com/p/38200980)

[局部响应归一化层（LRN）](https://www.jianshu.com/p/c014f81242e7)

[AlexNet网络介绍](https://blog.csdn.net/m0_37876745/article/details/79439623?ops_request_misc=&request_id=&biz_id=102&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0)

[AlexNet 论文翻译——中英文对照](https://blog.csdn.net/weixin_42546496/article/details/87808274?ops_request_misc=%7B%22request%5Fid%22%3A%22158859553119724846431550%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=158859553119724846431550&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-2)

