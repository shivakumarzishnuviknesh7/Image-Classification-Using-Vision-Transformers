# -*- coding: utf-8 -*-
"""Image Classification Using Vision Transformers.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rkzsb-M4YHfKQ7EWcDvVT3ApQcL1SnJo
"""

!pip install transformers
!pip install torch
!pip install torchvision
!pip install matplotlib

import torch
from transformers import ViTFeatureExtractor, ViTForImageClassification
from PIL import Image
import matplotlib.pyplot as plt
from google.colab import files

# Load a pre-trained Vision Transformer model and feature extractor
model_name = "google/vit-base-patch16-224"
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

# Function to upload an image
def upload_image():
    uploaded = files.upload()
    for filename in uploaded.keys():
        image = Image.open(filename)
        return image

# Upload your own image
image = upload_image()

# Preprocess the image
inputs = feature_extractor(images=image, return_tensors="pt")

# Run inference
with torch.no_grad():
    outputs = model(**inputs)

# Get the predicted label
logits = outputs.logits
predicted_label = logits.argmax(-1).item()

# Load the labels for the model
labels = model.config.id2label[predicted_label]

# Display the image and the predicted label
plt.imshow(image)
plt.title(f"Predicted Label: {labels}")
plt.axis("off")
plt.show()

!pip install transformers
!pip install torch
!pip install torchvision
!pip install matplotlib

import torch
from transformers import ViTFeatureExtractor, ViTForImageClassification
from PIL import Image
import matplotlib.pyplot as plt
from google.colab import files

# Load a pre-trained Vision Transformer model and feature extractor
model_name = "google/vit-base-patch16-224"
feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
model = ViTForImageClassification.from_pretrained(model_name)

# Function to upload an image
def upload_image():
    uploaded = files.upload()
    for filename in uploaded.keys():
        image = Image.open(filename)
        return image

# Upload your own image
image = upload_image()

# Preprocess the image
inputs = feature_extractor(images=image, return_tensors="pt")

# Run inference
with torch.no_grad():
    outputs = model(**inputs)

# Get the predicted label
logits = outputs.logits
predicted_label = logits.argmax(-1).item()

# Get the labels from the model config
labels = model.config.id2label

# Display the image and the predicted label
plt.imshow(image)
plt.title(f"Predicted Label: {labels[predicted_label]}")
plt.axis("off")
plt.show()