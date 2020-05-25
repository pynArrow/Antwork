# Naive Bayes

## 简介

朴素贝叶斯分类是一种十分简单的分类算法。

* **思路**

对于给出的待分类项，求解在此项出现的条件下各个类别出现的概率，将该待分类项归于概率最大的类别。

* **步骤**

1. 设$x=\{a_1, a_2, ..., a_n\}$为一个待分类项，$a_i$为x的特征属性。
2. 类别集合$C=\{y_1, y_2, ..., y_n\}$。
3. 计算$P(y_1|x), P(y_2|x), ..., P(y_n|x)$。
4. 如果$P(y_k|x)=max\{P(y_1|x), P(y_2|x), ..., P(y_n, x)\}$，则$x\in y_k$。

<img src="https://img-blog.csdn.net/20171227142307769" alt="img" style="zoom:50%;" />

## 基本原理

- **条件概率**

条件概率指事件A在事件B已经发生的条件下发生的概率，直接上公式：

$$P(A|B)=\frac{P(AB)}{P(B)}$$

- **贝叶斯定理**

贝叶斯定理用于计算后验概率。

> **先验概率（prior probability）**：指根据以往经验和分析。在实验或采样前就可以得到的概率。
>
> **后验概率（posterior probability）**：指某件事已经发生，想要计算这件事发生的原因是由某个因素引起的概率。

计算公式：

$$P(B|A)=\frac{P(A|B)P(B)}{P(A)}$$

* **步骤详解**

在上述给出的步骤中，最关键的是第三步中的计算，即$P(y_k|x)$的计算。

首先我们需要统计在不同类别下各个属性的条件概率，即

$$P(a_1|y_1), ..., P(a_m|y_1), ..., P(a_m|y_n)$$

由贝叶斯公式我们将待求转换为：

$$P(y_k|x)=\frac{P(x|y_k)P(y_k)}{P(x)}=\frac{|D_{y_k,x}|}{|D|}$$

由全概率公式得$P(x)$对于所有的划分都为常数，所以要使$P(y_k|x)$最大，只需使$P(x|y_k)P(y_k)$最大。同时朴素贝叶斯**假设各个属性相互独立**，当然这里为了方便计算而牺牲了部分准确率。由此假设，有

$$P(x|y_i)P(y_i)=P(a_1|y_i)...P(a_m|y_i)P(y_i)=P(y_i)\prod_{j=0}^mP(a_j|y_i)$$

所以$h(x)=argmax_{y_i \in y}P(y_i)\prod_{j=0}^mP(a_j|y_i)$。

* **拉普拉斯修正**

当训练样本较少或不充分时，可能出现概率估值为零的情况，引入拉普拉斯修正：

$$P(y_k)=\frac{|D_c|+1}{|D|+N}$$

$$P(x_i|y_k)=\frac{|D_{c, x_i}|+1}{|D|+N_i}$$

同时，对于引入的修正，随着概率的增大可以忽略不计，从而使估值更接近实际概率值。



**reference**：

[朴素贝叶斯分类（Nave Bayes）](https://blog.csdn.net/guoyunfei20/article/details/78911721?ops_request_misc=&request_id=&biz_id=102&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0)