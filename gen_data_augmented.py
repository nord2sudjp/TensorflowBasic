from PIL import Image
import os, glob
import numpy as np
from sklearn.model_selection import train_test_split

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50
num_testdata = 100

X_train = []
X_test = []
y_train = []
y_test = []

for index, cl in enumerate (classes):
    photos_dir = "./dev_rsc/animals_data/" + cl
    files = glob.glob(photos_dir + '/*.jpg')
    for i, file in enumerate (files):
        if i>= 200:break
        image = Image.open(file)
        image.convert("RGB").resize((image_size, image_size))
        data = np.asarray(image)

        if i < num_testdata:
            X_test.append(data)
            y_test.append(index)
        else:
            X_train.append(data)
            y_train.append(index)

            for angle in range(-20, 20, 5):
                # 回転
                img_r = image.rotate(angle)
                data = np.asarray(img_r)
                X_train.append(data)
                y_train.append(index)

                # 反転
                img_trans = image.transpose(Image.FLIP_LEFT_RIGHT)
                data = np.asarray(img_trans)
                X_train.append(data)
                y1_train.append(index)

#X = np.array(X)
#y = np.array(Y)

X_train = np.array(X_train)
X_test = np.array(X_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

# X_train, X_test, y_train, y_test = train_test_split(X, y)
xy = (X_train, X_test, y_train, y_test)
np.save("./dev_rsc/animals_aug.npy", xy)