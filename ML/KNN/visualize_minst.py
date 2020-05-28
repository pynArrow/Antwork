import numpy as np
import struct
import matplotlib.pyplot as plt

# 文件结构
# [offset] [type]          [value]          [description]
# 0000     32 bit integer  0x00000803(2051) magic number # 用于确认文件没有损坏
# 0004     32 bit integer  60000            number of images
# 0008     32 bit integer  28               number of rows
# 0012     32 bit integer  28               number of columns
# 0016     unsigned byte   ??               pixel
# 0017     unsigned byte   ??               pixel
# ........
# xxxx     unsigned byte   ??               pixel

filename = r'D:\VS-Code-python\dataset\train-images.idx3-ubyte'
binfile = open(filename, 'rb')
buf = binfile.read()

# '>IIII'是说使用大端法读取4个unsinged int32
# '>784B'的意思就是用大端法读取784个unsigned byte

# 跳过前4*4个32 bit integer
index = 0
index += struct.calcsize('>IIII')

for i in range(100):
    # 创建子图
    plt.subplot(10,10,i+1)
    # 读取784个unsigned byte，相当于读取一张图
    im = struct.unpack_from('>784B', buf, index)
    index += struct.calcsize('>784B')
    # 读取的是列表，转换成array后，reshape成28*28的图像
    im = np.array(im)
    im = im.reshape(28, 28)
    # 隐藏坐标轴
    plt.xticks([])
    plt.yticks([])
    # 绘图
    plt.imshow(im, cmap='gray')

plt.show()