# Linear Regression

[TOC]

## 简介

线性回归是一种回归学习方法，一般用于处理连续性变量，算是机器学习的入门算法。虽然线性模型的形式很简单，但是线性模型的思想是很重要的，许多非线性模型都是在线性模型的基础上通过引入高维映射而得。

* **优点**

1. 建模速度快，不需要复杂计算
2. 可解释性好

* **缺点**

1. 不适用与非线性数据
2. 可能出现过拟合

## 基本原理

* **基本形式**

给定数据集$D=\{(x_1,y_1), ..., (x_m, y_m\}$，其中$x_i=(x_{i1}, ..., x_{id})$，线性回归模型试图学习到$\hat y=w^Tx+b$，使得$\hat y$近似等于$y$。

* **损失函数Loss Function**

一般选用**均方误差(mean square error， MSE)**，采用**最小二乘法(least square method)**求解，简单来说就是找到一条直线，使所有样本到直线上的欧氏距离之和最小。

均方误差即$L=\frac1{2m}\Sigma_{i=1}^m(\hat y-y)^2$，这里乘了$\frac12$是为了使后面的计算式更为简洁。

* **梯度下降Gradient Decent**

基本思路：首先赋予$w$、$b$初始值，用链式法则求出梯度，沿着梯度的反方向不断更新参数，使损失函数不断减小至收敛。具体求法为：

$$\frac{\partial L}{\partial w}=\frac{\partial L}{\partial \hat y}\frac{\partial \hat y}{\partial w}=\frac 1m\Sigma_{i=0}^m(\hat y_i-y_i)x_i$$

$$\frac{\partial L}{\partial b}=\frac{\partial L}{\partial \hat y}\frac{\partial \hat y}{\partial b}=\frac 1m\Sigma_{i=0}^m(\hat y_i-y_i)$$

参数更新：

$$w_j←w_j+α(y−\hat y)x_j$$

$$b←b+α(y−\hat y)$$

其中$\alpha$称为学习率（learning rate）。

![这里写图片描述](https://img-blog.csdn.net/20180414153645111?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0thdGhlcmluZV9oc3I=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## sklearn实现

* **代码**

```python
from sklearn import linear_model, datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


if __name__ == '__main__':
    #load data
    diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

    # Use only one feature
    diabetes_X = diabetes_X[:, np.newaxis, 2]

    # Split the data into training/testing sets
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    # Split the targets into training/testing sets
    diabetes_y_train = diabetes_y[:-20]
    diabetes_y_test = diabetes_y[-20:]

    # Create linear regression object
    regr = linear_model.LinearRegression()

    # Train the model using the training sets
    regr.fit(diabetes_X_train, diabetes_y_train)

    # Make predictions using the testing set
    diabetes_y_pred = regr.predict(diabetes_X_test)

    # The coefficients
    print('Coefficients: \n', regr.coef_)
    # The mean squared error
    print('Mean squared error: %.2f'
        % mean_squared_error(diabetes_y_test, diabetes_y_pred))
    # The coefficient of determination: 1 is perfect prediction
    print('Coefficient of determination: %.2f'
        % r2_score(diabetes_y_test, diabetes_y_pred))

    # Plot outputs
    plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
    plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

    plt.xticks(())
    plt.yticks(())

    plt.show()
```

* **Out：**

```python
Coefficients:
[938.23786125]
Mean squared error: 2548.07
Coefficient of determination: 0.47
```

* **可视化：**

![TIM图片20200517090928](C:\Users\Administrator\Desktop\cs\ML\blog_image\linear_regression\TIM图片20200517090928.png)

**reference**：

[机器学习中的五种回归模型及其优缺点](https://blog.csdn.net/Katherine_hsr/article/details/79942260?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158883567719725219939967%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=158883567719725219939967&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v25-3)

