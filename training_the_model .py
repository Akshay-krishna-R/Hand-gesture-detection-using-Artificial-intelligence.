

from keras.layers import Input, Lambda, Dense, Flatten
from keras.models import Model
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
import numpy as np
from glob import glob
import matplotlib.pyplot as plt
from PIL import Image

IMAGE_SIZE = [224, 224]

image_gen = ImageDataGenerator(rotation_range=30, # rotate the image 30 degrees
                               width_shift_range=0.1, # Shift the pic width by a max of 10%
                               height_shift_range=0.1, # Shift the pic height by a max of 10%
                               rescale=1/255, # Rescale the image by normalzing it.
                               shear_range=0.2, # Shear means cutting away part of the image (max 20%)
                               zoom_range=0.2, # Zoom in by 20% max
                               horizontal_flip=True, # Allo horizontal flipping
                               fill_mode='nearest' # Fill in missing pixels with the nearest filled value
                              )

batch_size = 32

train_image_gen = image_gen.flow_from_directory('../hand/train_images',
                                               target_size=IMAGE_SIZE[:2],
                                               batch_size=batch_size,
                                                class_mode='categorical',
                                               )

type(train_image_gen)

test_image_gen = image_gen.flow_from_directory('../hand/test_images',
                                               target_size=IMAGE_SIZE[:2],
                                               batch_size=batch_size,
                                               class_mode='categorical',
                                               )

vgg = VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)

for layer in vgg.layers:
  layer.trainable = False

x = Flatten()(vgg.output)

classes = test_image_gen.class_indices

classes

len(classes)

prediction = Dense(len(classes), activation='softmax')(x)

model = Model(inputs=vgg.input, outputs=prediction)

model.summary()

model.compile(
  loss='categorical_crossentropy',
  optimizer='adam',
  metrics=['accuracy']
)

r=model.fit(train_image_gen,epochs=50,  validation_data= test_image_gen)

model.save("VGG16_fingercount_8jan_50epochs.h5")
