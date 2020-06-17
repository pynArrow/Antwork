import numpy as np
import timeit
from sklearn import svm
import struct
from sklearn.metrics import confusion_matrix, classification_report

image_train_file_path = r"D:\VS-Code-python\dataset\mnist\train-images.idx3-ubyte "
label_train_file_path = r"D:\VS-Code-python\dataset\mnist\train-labels.idx1-ubyte"
image_test_file_path = r"D:\VS-Code-python\dataset\mnist\t10k-images.idx3-ubyte"
label_test_file_path = r"D:\VS-Code-python\dataset\mnist\t10k-labels.idx1-ubyte"

TRAIN_ITEMS = 50000
TEST_ITEMS = 10000

def loadData():
    data = []
    for img_file,label_file,items in zip([image_train_file_path,image_test_file_path],
                                   [label_train_file_path,label_test_file_path],
                                   [TRAIN_ITEMS, TEST_ITEMS]):
        buf_img = open(img_file, 'rb').read()
        buf_label = open(label_file, 'rb').read()
        
        if 'train' in img_file:
            print('load image for training')
        else:
            print('load image for testing')

        fmt = '>iiii'
        offset = 0
        magic_number, img_number, height, width = struct.unpack_from(fmt, buf_img, offset)
        print('magic number is {}, image number is {}, height is {} and width is {}'.format(magic_number, img_number, height, width))
        
        offset += struct.calcsize(fmt)
        
        image_size = height * width
        
        fmt = '>{}B'.format(image_size)
        
        if items > img_number:
            items = img_number
        images = np.empty((items, image_size))
        for i in range(items):
            images[i] = np.array(struct.unpack_from(fmt, buf_img, offset))
            
            images[i] = images[i]/256
            offset += struct.calcsize(fmt)

        if 'train' in label_file:
            print('load label for training')
        else:
            print('load label for testing')

        fmt = '>ii'
        offset = 0
        magic_number, label_number = struct.unpack_from(fmt, buf_label, offset)
        print('magic number is {} and label number is {}'.format(magic_number, label_number))
        
        offset += struct.calcsize(fmt)
        
        fmt = '>B'
        
        if items > label_number:
            items = label_number
        labels = np.empty(items)
        for i in range(items):
            labels[i] = struct.unpack_from(fmt, buf_label, offset)[0]
            offset += struct.calcsize(fmt)
        
        data.append((images, labels.astype(int)))

        print('finish loading')
    return data

if __name__ == '__main__':
    
    #load data
    train_data, test_data = loadData()


    
    # train
    start_time = timeit.default_timer()
    print('begin the train...')
    clf = svm.SVC(gamma='scale')
    clf.fit(train_data[0], train_data[1])
    train_time = timeit.default_timer()
    print('train cost {}'.format(str(train_time - start_time) ) )
    
    # test
    print('Begin the test...')
    predictions = clf.predict(test_data[0])
    test_time = timeit.default_timer()
    print('test cost {}'.format(str(test_time - train_time) ) )

    print('confusion_matrix\n',confusion_matrix(predictions,test_data[1]))
    print('classicication_report\n',classification_report(predictions,test_data[1]))

