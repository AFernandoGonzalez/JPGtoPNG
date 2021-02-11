import sys
import os
import time
from tqdm import tqdm
from PIL import Image


# grabing the first and second argument
# folder : images/ new/
image_folder = sys.argv[1]
output_folder = sys.argv[2]


#  check if the folder new exists if not make a new one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# loop throught the images/ folder

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')

    # separating names and tupe of file
    cleaned_name = os.path.splitext(filename)[0]
    # you can print them to see it

    # print(cleaned_name)

    # conver them to png
    # # save it to the new/ folder
    img.save(f'{output_folder}{cleaned_name}.png', 'png')

    # Initial call to print 0% progress
    for i in tqdm(range(100)):
        time.sleep(0.005)
print('All Pictures are Converted')

# print the progress of each coverted img
# print('All Done')


target_pics = ('new')

for file in os.listdir(target_pics):
    f_img = target_pics + "/" + file
    img = Image.open(f_img)

    # use a variable to input max height , width
    MAX_SIZE = (300, 300)

    # thumbnail has a value of MAX_SIZE
    img.thumbnail(MAX_SIZE)

    # save the image
    img.save(f_img)

    # Initial call to print 0% progress
    for i in tqdm(range(100)):
        time.sleep(0.005)
print('Resize Successfull!')

# printing in the terminal once each image has done resizing
# print(f'{file} its done resizing!')
