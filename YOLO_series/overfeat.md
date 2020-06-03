# Overfeat

## 简介

one-stage算法，基于AlexNet，实现了识别、定位、检测共用一个网络框架，2013年ILSVRC定位比赛冠军。

* **主要贡献**

1. multiscale
2. sliding window 
3. offset pooling

## 基本原理

### Multiscale

OverFeat的训练方法与AlexNet基本相同，创新点主要在于测试阶段。测试阶段没有采用AlexNet的muli-crop，而是直接采用了六种不同尺度的测试图像输入。

### offset pooling

![img](https://images2018.cnblogs.com/blog/1160281/201807/1160281-20180721220445683-716828679.png)

### sliding window（敲黑板！！）

![img](https://images2018.cnblogs.com/blog/1160281/201807/1160281-20180721220438599-1957099965.png)

https://www.cnblogs.com/liaohuiqiang/p/9348276.html

