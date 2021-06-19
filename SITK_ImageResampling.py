import torch
import numpy as np
import SimpleITK as sitk


num_images = 10


class MyDataset:
    def __init__(self, paths):
        self.paths = paths

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, index):
        image = sitk.ReadImage(self.paths[index])
        resampler = sitk.ResampleImageFilter()
        resampler.SetInterpolator(sitk.sitkNearestNeighbor)
        resampler.SetReferenceImage(image)
        resampler.SetDefaultPixelValue(0.0)
        resampler.SetOutputPixelType(sitk.sitkFloat32)
        print('Resampling...')
        resampled = resampler.Execute(image)
        print('Resampled!')
        array = sitk.GetArrayFromImage(resampled)
        return array


paths = []
for i in range(num_images):
    image = sitk.GetImageFromArray(np.random.rand(10, 20, 30))
    path = f'/tmp/image_{i}.nii'
    sitk.WriteImage(image, path)
    paths.append(path)

my_dataset = MyDataset(paths)

loader_sp = torch.utils.data.DataLoader(my_dataset, batch_size=4, num_workers=0)
loader_mp = torch.utils.data.DataLoader(my_dataset, batch_size=4, num_workers=2)

print('Extracting batch using one worker...')
batch_sp = next(iter(loader_sp))
print(batch_sp.shape)

print('Extracting batch using two workers...')
batch_mp = next(iter(loader_mp))
print(batch_mp.shape)
