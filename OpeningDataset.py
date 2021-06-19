import matplotlib
# matplotlib.use('TkAgg')
from matplotlib import pylab as plt
import numpy as np
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D
from nibabel.testing import data_path

example_filename  = 'DATASET/MICCAI_BraTS_2019_Data_Training/HGG/BraTS19_2013_2_1/BraTS19_2013_2_1_flair.nii.gz'

img = nib.load(example_filename)
imgShape = img.shape

print(img)
# print(img.header['db_name'])
print()

width, height, queue = img.dataobj.shape
print("WIDTH:  ",width)
print("HEIGHT:  ",height)
print("QUEUE:  ",queue)
# OrthoSlicer3D(img.dataobj).show()

num = 1
for i in range(0, queue, 10):
    img_arr = img.dataobj[:, :, i]
    plt.subplot(5, 4, num)
    plt.imshow(img_arr, cmap='gray')
    num += 1

plt.show()

print("---------------------------------------------------")
print()

ImgaffShape = img.affine.shape
print(imgShape)

var = img.get_data_dtype() == np.dtype(np.int16)
print(var)

