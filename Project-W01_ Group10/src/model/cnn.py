from keras.models import Sequential
from keras.layers import Conv2D,Dense,Dropout,Flatten,MaxPooling2D,BatchNormalization
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam


def CNN(input_shape, labels):

    # Build CNN
    """
    Convolution takes local features.
    The function of the convolution layer
    is to determine the valuable convolution kernels of the featuares of the picture 
    by constantly changing the convolution kernels and then
    multiplying them with the corresponding convolution kernels to obtain the matrix
    """
    # 1st layer
    model = Sequential()
    model.add(Conv2D(filters=16, kernel_size=(3, 3),activation='relu',input_shape= input_shape))
    model.add(BatchNormalization())
    model.add(Conv2D(filters=16, kernel_size=(3, 3),activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
    model.add(Dropout(0.25))

    # 2nd layer
    model.add(Conv2D(filters=32, kernel_size=(3, 3),activation='relu'))
    model.add(BatchNormalization())
    model.add(Conv2D(filters=32, kernel_size=(3, 3),activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))
    model.add(Dropout(0.25))

    # 3rd layer
    model.add(Conv2D(filters=64, kernel_size=(3, 3),activation='relu'))
    model.add(BatchNormalization())
    model.add(Conv2D(filters=64, kernel_size=(3, 3),activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2,2),strides=(2,2)))

    model.add(Flatten())
    model.add(Dense(filters=16*16,activation='relu'))
    model.add(Dropout(0.2))

    model.add(Dense(labels,activation='softmax'))

    return model

if __name__ == "__main__":
    input_shape = (64, 64, 1)
    labels = 7
    model = CNN((48, 48, 1), labels)
    model.summary()
