import os
import random
import shutil

# Define paths to your dataset
dataset_dir = 'C:/Users/HP/Desktop/SEM 8/Major Project-II/yolo model/tomato_dataset'  # Update this path to where your dataset is located
images_dir = os.path.join(dataset_dir, 'images')  # Correct path for images
labels_dir = os.path.join(dataset_dir, 'labels')  # Correct path for labels

# Create directories for train and valid datasets
train_dir = os.path.join(dataset_dir, 'train')
valid_dir = os.path.join(dataset_dir, 'valid')

os.makedirs(os.path.join(train_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(train_dir, 'labels'), exist_ok=True)
os.makedirs(os.path.join(valid_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(valid_dir, 'labels'), exist_ok=True)

# List all image files in the images directory
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png'))]  # Update the extensions if needed

# Shuffle the image files randomly
random.shuffle(image_files)

# Split ratio (e.g., 80% train, 20% valid)
split_ratio = 0.8
train_size = int(len(image_files) * split_ratio)
train_files = image_files[:train_size]
valid_files = image_files[train_size:]

# Function to move files to respective directories
def move_files(files, src_images_dir, src_labels_dir, dest_images_dir, dest_labels_dir):
    for file in files:
        # Move image files
        image_file = file
        label_file = file.replace('.jpg', '.txt').replace('.png', '.txt')  # Adjust if using different formats

        # Move image and label
        shutil.move(os.path.join(src_images_dir, image_file), os.path.join(dest_images_dir, image_file))
        shutil.move(os.path.join(src_labels_dir, label_file), os.path.join(dest_labels_dir, label_file))

# Move the training and validation files
move_files(train_files, images_dir, labels_dir, os.path.join(train_dir, 'images'), os.path.join(train_dir, 'labels'))
move_files(valid_files, images_dir, labels_dir, os.path.join(valid_dir, 'images'), os.path.join(valid_dir, 'labels'))

# Output sizes of train and valid sets
print(f"Training set size: {len(train_files)}")
print(f"Validation set size: {len(valid_files)}")
