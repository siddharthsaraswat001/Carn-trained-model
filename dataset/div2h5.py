import os
import glob
import h5py
import scipy.misc as misc
import numpy as np
from PIL import Image 
dataset_dir = "DIV2K/"
dataset_type = "train"

f = h5py.File("DIV2K_{}.h5".format(dataset_type), "w")
dt = h5py.special_dtype(vlen=np.dtype('uint8'))

for subdir in ["HR", "X2", "X3", "X4"]:
    print(subdir)
    if subdir in ["HR"]:
        im_paths = glob.glob(os.path.join(dataset_dir, 
                                          "DIV2K_{}_HR".format(dataset_type), 
                                          "*.png"))

    else:
        print("I'm in else")
        im_paths = glob.glob(os.path.join(dataset_dir, 
                                          "DIV2K_{}_LR_bicubic".format(dataset_type), 
                                          subdir, "*.png"))
    im_paths.sort()
    grp = f.create_group(subdir)

    for i, path in enumerate(im_paths):
        im = Image.open(path)
        print(path)
        grp.create_dataset(str(i), data=im)
