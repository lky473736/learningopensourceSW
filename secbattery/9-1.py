from keras.datasets import mnist 
# mnist data : 이미지를 숫자로 변환 -> 밝기차이를 통해 component 가짐

(x_train, t_train), (x_test, t_test) = mnist.load_data()

print (x_train.shape)
print (x_train)

print (t_train.shape)
print(x_test.shape)
print(t_test.shape)