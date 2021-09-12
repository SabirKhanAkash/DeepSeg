# Splitting Files

import splitfolders  # or import split_folders

input_folder = 'G:/Shared drives/Shared_Drive_1/DATASET/dataset_brats20/train_images'
output_folder = 'G:/Shared drives/Shared_Drive_1/DATASET/dataset_brats20/val_images'
# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=(.75, .25), group_prefix=None)
