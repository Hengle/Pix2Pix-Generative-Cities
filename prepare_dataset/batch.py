import cv2 as cv
import os
import numpy as np
import barrel
import sys

# ######### RESIZE ##########
d = "../../Video/Frames/r1.3_2x_f"
images = os.listdir(d)
count = 0
for f in images:
    if not f.startswith("."):
        im = cv.imread(d+"/"+f)
        try:
          im = cv.resize(im,(4096,1024))
        except:
          print f
          break
        cv.imwrite(d+"/"+f,im)
        count+=1
        if (count)%10 == 0: print ". (" + str(count) + ")"
        else: sys.stdout.write('.')

# ######### VR DISTORT ##########
# d = "images"
# images = os.listdir(d)
# for f in images:
#     if not f.startswith("."):
#         im = cv.imread(d+"/"+f)
#         im = barrel.barrel(im,0.00002,s=0.8)
#         cv.imwrite(d+"/"+f,im)

######### DOUBLE IMG SIDE BY SIDE ##########
# d = "input_dir"
# images = os.listdir(d)
# for f in images:
#     if not f.startswith("."):
#         im = cv.imread(d+"/"+f)
#         im = np.hstack((im,im))
#         cv.imwrite(d+"/"+".".join(f.split(".")[:-1])+".jpg",im)

# ######### SPLIT DOUBLE IMG ##########
# d = "input_dir"
# images = os.listdir(d)
# for f in images:
#     if not f.startswith("."):
#         im = cv.imread(d+"/"+f)
#         h,w,_ = im.shape
#         iml = im[:,:w//2]
#         imr = im[:,w//2:]
#         cv.imwrite(d+"/lr/"+f.split(".")[0]+"-l.jpg",iml)
#         cv.imwrite(d+"/lr/"+f.split(".")[0]+"-r.jpg",imr)

# ######## DOUBLE IMG SIDE BY SIDE ##########
# d = "images"
# images = os.listdir(d)
# for f in images:
#     if f.endswith("-l-inputs.png"):
#         g = f.split("-l-inputs")[0]
#         f2 = g+"-r-inputs.png"
#         im = cv.imread(d+"/"+f)
#         im2 = cv.imread(d+"/"+f2)
#         print im.shape
#         print im2.shape
#         im = np.hstack((im,im2))
#         cv.imwrite(d+"/"+g+"-combined-input.png",im)

# ######## COMBINE INPUT & OUTPUT IMGS ##########
# d = "images"
# images = os.listdir(d)
# for f in images:
#     if f.endswith("inputs.png"):
#         g = f.split("-")[0]
#         f2 = g+"-outputs.png"
#         im = cv.imread(d+"/"+f)
#         im2 = cv.imread(d+"/"+f2)
#         print im.shape
#         print im2.shape
#         im = np.hstack((im,im2))
#         cv.imwrite(d+"/"+g+"_combined.png",im)