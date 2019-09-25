import pickle

import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, Dense, MaxPooling2D, Flatten

training_fruit_img_file = open('training_fruit_img_file', 'rb')
training_label_file = open('training_label_file', 'rb')
training_fruit_img = pickle.load(training_fruit_img_file)
training_label = pickle.load(training_label_file)
training_fruit_img_file.close()
training_label_file.close()

test_fruit_img_file = open('test_fruit_img_file', 'rb')
test_label_file = open('test_label_file', 'rb')
test_fruit_img = pickle.load(test_fruit_img_file)
test_label = pickle.load(test_label_file)
test_fruit_img_file.close()
test_label_file.close()

test_fruits_img_file = open('test_fruits_img_file', 'rb')
tests_label_file = open('tests_label_file', 'rb')
test_fruits_img = pickle.load(test_fruits_img_file)
tests_label = pickle.load(tests_label_file)
test_fruits_img_file.close()
tests_label_file.close()

print("milestone 1")

label_to_id = {v: k for k, v in enumerate(np.unique(training_label))}
id_to_label = {v: k for k, v in label_to_id.items()}

label_to_id_file = open('label_to_id_file', 'wb')
pickle.dump(label_to_id, label_to_id_file)
label_to_id_file.close()

id_to_label_file = open('id_to_label_file', 'wb')
pickle.dump(id_to_label, id_to_label_file)
id_to_label_file.close()

print("milestone 2")

training_label_id = np.array([label_to_id[i] for i in training_label])
test_label_id = np.array([label_to_id[i] for i in test_label])

print("milestone 3")

training_fruit_img, test_fruit_img = training_fruit_img / 255.0, test_fruit_img / 255.0

# Actual Model
model = Sequential()
model.add(Conv2D(16, (3, 3), input_shape=(64, 64, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(256, activation="relu"))
model.add(Dense(75, activation="softmax"))

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=['accuracy'])
model.fit(training_fruit_img, training_label_id, batch_size=32, epochs=1)

loss, accuracy = model.evaluate(test_fruit_img, test_label_id)
print("Loss:", loss)
print("Accuracy:", accuracy)
model.save("model.h5")
