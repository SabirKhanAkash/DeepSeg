import os,shutil

src = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/DeepSeg/DATASET/dataset_brats19/val_images/image_t2/'
dest = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/DeepSeg/DATASET/dataset_brats19/val_images/Destination/'

for files in os.listdir(src):
    try:
        dir3 = src+files+'/'
        for f in os.listdir(dir3):
            shutil.move(dir3+f,dest+f)

    except:
        print('Something went wrong!')
        pass
