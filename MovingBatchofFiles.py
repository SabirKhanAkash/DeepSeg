import os,shutil

src = 'G:/Shared drives/Shared_Drive_1/DATASET/BraTS20_train_images/image_t1ce/'
dest = 'G:/Shared drives/Shared_Drive_1/DATASET/dataset_brats20/train_images/image_t1ce/'

for files in (os.listdir(src)):
    try:
        dir3 = src+files+'/'
        for f in os.listdir(dir3):
            shutil.move(dir3+f,dest+f)

    except:
        print('Something went wrong!')
        pass
