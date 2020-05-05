from PIL import Image
import os, glob
import numpy as np
from sklearn.model_selection import train_test_split

classes = ["monkey", "boar", "crow"]
num_classes = len(classes)
image_size = 50

X = []
Y = []

for index, cl in enumerate (classes):
    photos_dir = "./dev_rsc/animals_data/" + cl
    files = glob.glob(photos_dir + '/*.jpg')
    for i, file in enumerate (files):
        if i>= 200:break
        image = Image.open(file)
        image.convert("RGB").resize((image_size, image_size))
        data = np.asarray(image)
        X.append(data)
        Y.append(index)

X = np.array(X)
y = np.array(Y)

X_train, X_test, y_train, y_test = train_test_split(X, y)
xy = (X_train, X_test, y_train, y_test)
np.save("./animals.npy", xy)