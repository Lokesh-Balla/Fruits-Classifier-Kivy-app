import glob
import os
import pickle

import cv2
import numpy as np

training_fruit_img = []
training_label = []
for dir_path in glob.glob("Training/*"):
    img_label = dir_path.split("/")[-1]
    for img_path in glob.glob(os.path.join(dir_path, "*.jpg")):
        img = cv2.imread(img_path)
        img = cv2.resize(img, (64, 64))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        training_fruit_img.append(img)
        training_label.append(img_label)
training_fruit_img = np.array(training_fruit_img)
training_label = np.array(training_label)

training_fruit_img_file = open('training_fruit_img_file', 'wb')
pickle.dump(training_fruit_img, training_fruit_img_file)
training_fruit_img_file.close()

training_label_file = open('training_label_file', 'wb')
pickle.dump(training_label, training_label_file)
training_label_file.close()

test_fruit_img = []
test_label = []
for dir_path in glob.glob("Test/*"):
    img_label = dir_path.split("/")[-1]
    for img_path in glob.glob(os.path.join(dir_path, "*.jpg")):
        img = cv2.imread(img_path)
        img = cv2.resize(img, (64, 64))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        test_fruit_img.append(img)
        test_label.append(img_label)
test_fruit_img = np.array(test_fruit_img)
test_label = np.array(test_label)

test_fruit_img_file = open('test_fruit_img_file', 'wb')
pickle.dump(test_fruit_img, test_fruit_img_file)
test_fruit_img_file.close()

test_label_file = open('test_label_file', 'wb')
pickle.dump(test_label, test_label_file)
test_label_file.close()
#
# test_fruits_img = []
# tests_label = []
# for img_path in glob.glob(os.path.join("test-multiple_fruits", "*.jpg")):
#     img = cv2.imread(img_path)
#     img = cv2.resize(img, (64, 64))
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     test_fruits_img.append(img)
#     tests_label.append(img_label)
# test_fruits_img = np.array(test_fruits_img)
# tests_label = np.array(tests_label)
#
# test_fruits_img_file = open('test_fruits_img_file', 'wb')
# pickle.dump(test_fruits_img, test_fruits_img_file)
# test_fruits_img_file.close()
#
# tests_label_file = open('tests_label_file', 'wb')
# pickle.dump(tests_label, tests_label_file)
# tests_label_file.close()
