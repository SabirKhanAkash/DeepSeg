import os, shutil


dir1 = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/DeepSeg/DATASET/BraTS19_train_preprocessed_val/Data_Validation/'
dirFlair = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/DeepSeg/DATASET/BraTS19_train_preprocessed_val/image_flair/'
dirT1 = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/DeepSeg/DATASET/BraTS19_train_preprocessed_val/image_t1/'
dirT2 = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/DeepSeg/DATASET/BraTS19_train_preprocessed_val/image_t2/'
dirT1ce = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/DeepSeg/DATASET/BraTS19_train_preprocessed_val/image_t1ce/'
# dirTruth = 'D:/Study Materials/Study/4th Year/7th Semester/CSE 4000/Code/DeepSeg-master/DeepSeg-master/DATASET/BraTS19_train_preprocessed_val/truth/'


fileformatFlair = 'flair'
fileformatT1 = 't1'
fileformatT2 = 't2'
fileformatT1ce = 't1ce'
# fileformatTruth = 'truth'


for files in os.listdir(dir1):
    try:
        # print("I'm here at 22")
        dir3 = dir1+files+'/'
        for f in os.listdir(dir3):
            print("I'm here at 25")
            # if fileformatFlair in f:
            #     # print("I'm here at 27")
            #     shutil.move(dir3+f, dirFlair+f)
            #
            # if fileformatT1ce in f:
            #     # print("I'm here at 33")
            #     shutil.move(dir3+f, dirT1ce+f)
            #
            # if fileformatT1 in f:
            #     # print("I'm here at 28")
            #     shutil.move(dir3+f, dirT1+f)

            if fileformatT2 in f:
                # print("I'm here at 33")
                shutil.move(dir3+f, dirT2+f)
            
            # if fileformatTruth in f:
            #     # print("I'm here at 33")
            #     shutil.move(dir3+f, dirTruth+f)
                
    except:
        print('Something went wrong!')
        pass


