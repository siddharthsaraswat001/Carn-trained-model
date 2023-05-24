import os

# specify the path to your directory
path = "dataset\celeba_hq_10K\celeba_hq_valid_LR_bicubic_2K\X2"

def rename_files():
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            base = os.path.splitext(filename)[0]
            new_filename = base + "x2.jpg"
            source = os.path.join(path, filename)
            destination = os.path.join(path, new_filename)

            # rename the file
            os.rename(source, destination)  

if __name__ == '__main__':
    rename_files()


'''

import os

# specify the path to your directory
path = "dataset\celeba_hq_10K\celeba_hq_valid_LR_bicubic_2K\X2"

def rename_files():
    i = 8001
    for filename in sorted(os.listdir(path)):
        if filename.endswith(".jpg"):
            new_filename = f"{i:05}.jpg"
            source = os.path.join(path, filename)
            destination = os.path.join(path, new_filename)

            # rename the file
            os.rename(source, destination)
            i += 1

if __name__ == "__main__":
    rename_files()
'''