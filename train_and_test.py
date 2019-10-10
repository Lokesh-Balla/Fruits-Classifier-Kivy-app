import pickle

import numpy as np
import tensorflow as tf

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

print("loading in pickled data complete")

label_to_id = {v: k for k, v in enumerate(np.unique(training_label))}
id_to_label = {v: k for k, v in label_to_id.items()}

label_to_id_file = open('label_to_id_file', 'wb')
pickle.dump(label_to_id, label_to_id_file)
label_to_id_file.close()

id_to_label_file = open('id_to_label_file', 'wb')
pickle.dump(id_to_label, id_to_label_file)
id_to_label_file.close()

training_label_id = np.array([label_to_id[i] for i in training_label])
test_label_id = np.array([label_to_id[i] for i in test_label])

print("labels ready and pickled")

training_fruit_img, test_fruit_img = training_fruit_img / 255.0, test_fruit_img / 255.0

print("values normalized")

# Actual Model
model = tf.keras.Sequential()
model.add(tf.keras.layers.Conv2D(16, (3, 3), padding="same", activation="relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

model.add(tf.keras.layers.Conv2D(32, (3, 3), padding="same", activation="relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

model.add(tf.keras.layers.Conv2D(32, (3, 3), padding="same", activation="relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

model.add(tf.keras.layers.Conv2D(64, (3, 3), padding="same", activation="relu"))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(256, activation="relu"))
model.add(tf.keras.layers.Dense(75, activation="softmax"))

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=['accuracy'])
model.fit(training_fruit_img, training_label_id, batch_size=32, epochs=15)

loss, accuracy = model.evaluate(test_fruit_img, test_label_id)
print("Loss:", loss)
print("Accuracy:", accuracy)
model.save("model.h5")
