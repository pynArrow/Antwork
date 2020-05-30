import struct
import numpy as np
import collections
import time
import matplotlib.pyplot as plt

# read the image file
# input: file path
#output: the list of piexl array for each image
def read_image(file_path):
    binfile = open(file_path,"rb")
    buf = binfile.read()
    index=0
    magic, num_images,num_rows,num_columns=struct.unpack_from(">IIII",buf,index)
    print("number of images:"+str(num_images))
    print("number of rows:"+str(num_rows))
    print("number of columns:"+str(num_columns))
    index+=struct.calcsize(">IIII")
    img_piexl=[]
    for i in range(num_images):
        piexl_all=[]
        for j in range(num_columns):
            for k in range(num_rows):
                piexl=struct.unpack_from(">B",buf,index)
                ### This way using the original piexl
                #piexl=int(piexl[0])
                ### This way using the processed piexl
                ### if piexl<127 then it becomes 0
                ### else it becomes 1
                piexl=int(piexl[0])
                '''if piexl<127:
                    piexl=0
                else:
                    piexl=1'''
                piexl_all.append(piexl)
                index+=struct.calcsize(">B")
        piexl_all=np.array(piexl_all)
        img_piexl.append(piexl_all)
        """
        print(piexl_all)
        piexl_all=piexl_all.reshape(28,28)
        fig=plt.figure()
        plotwindow=fig.add_subplot(111)
        plotwindow.imshow(piexl_all,cmap="gray")
        plt.show()
        """
        if i%1000==0:
            print(str(i)+"images have been processed")
    binfile.close()
    return img_piexl

# read label file
# input: file path
# output: list of labels
def read_label(file_path):
    binfile = open(file_path,"rb")
    buf = binfile.read()
    index=0
    magic, num_items=struct.unpack_from(">II",buf,index)
    print("number of labels:"+str(num_items))
    index+=struct.calcsize(">II")
    label_num=[]
    for i in range(num_items):
        label=struct.unpack_from(">B",buf,index)
        label_num.append(int(label[0]))
        index+=struct.calcsize(">B")
        if i%1000==0:
            print(str(i)+"labels have been processed!")
    binfile.close()
    return label_num

# for each train image and test image, calculating their distance
# input: list of piexls for train image, list of piexls for test image
# output: the distance between train image and test image
def calc_dis(train_image,test_image):
    dist = np.linalg.norm(train_image-test_image)
    return dist

# find labels for test image
# input: the number of neighbors, the list of training images the list of training labels, the test image
# output: the dictionary whose key is label and value is its corresponding appearing time
def find_labels(k,train_images,train_labels,test_image):
    all_dis = []
    # defaultdict key不存在时返回0
    labels = collections.defaultdict(int)
    for i in range(len(train_images)):
        # 默认是二维范数
        # linalg = linear+algebra
        dis = np.linalg.norm(train_images[i]-test_image)
        all_dis.append(dis)
    # np.argsort返回列表元素从小到大的索引值
    sorted_dis_index = np.argsort(all_dis)
    count = 0
    while (count < k):
        labels[train_labels[sorted_dis_index[count]]]+=1
        count += 1
    return labels

# for all test images, finding its labels by knn
# input: number of neighbors, list of train images, list of train labels, list of test images
# output: result of labels for each image
def knn_all(k,train_images,train_labels,test_images):
    print("start knn_all!")
    pred = []
    count = 0
    for i in range(len(test_images)):
        labels = find_labels(k,train_images,train_labels,test_images[i])
        pred.append(max(labels))
        if count%100==0:
            print("%d has been processed!"%(count))
        count+=1
    return pred 

# calculate the precision of knn result
# input: the list of result labels, the list of test labels
# output: the precision of label results
def calc_precision(res,test_labels):
    precision=0
    for i in range(len(res)):
        if res[i]==test_labels[i]:
            precision+=1
    return precision/len(res)

if __name__ == '__main__':

    image_train_file_path = r"D:\VS-Code-python\dataset\mnist\train-images.idx3-ubyte"
    label_train_file_path = r"D:\VS-Code-python\dataset\mnist\train-labels.idx1-ubyte"
    image_test_file_path = r"D:\VS-Code-python\dataset\mnist\t10k-images.idx3-ubyte"
    label_test_file_path = r"D:\VS-Code-python\dataset\mnist\t10k-labels.idx1-ubyte"
    image_train_piexl = read_image(image_train_file_path)
    label_train = read_label(label_train_file_path)
    image_test_piexl = read_image(image_test_file_path)
    label_test = read_label(label_test_file_path)
    print("reading all files completed!")

    image_test_piexl = image_test_piexl[:1000]
    image_train_piexl = image_train_piexl[:10000]
    label_train = label_train[:10000]
    label_test = label_test[:1000]

    pred = []

    for k in range(1, 15):
        print('k='+str(k))

        #start_time = time.clock()
        pre_label = knn_all(k,image_train_piexl,label_train,image_test_piexl)
        #end_time = time.clock()
        
        precision = calc_precision(pre_label,label_test)
        #time = end_time-start_time

        print("precision:"+str(precision))
        #print("running time"+str(time))

        pred.append(precision)

    print(pred)
    plt.plot(np.arange(k), pred)
    plt.savefig('k.jpg')
    plt.show()

