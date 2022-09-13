import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

# this makes image look better on a macbook pro
def imageshow(img, dpi=200):
    if dpi > 0:
        F = plt.gcf()
        F.set_dpi(dpi)
    plt.imshow(img)


def rgb_ints_example():
    '''should produce red,purple,green squares
    on the diagonal, over a black background'''
    # RGB indexes
    red,green,blue = range(3)
    # img array 
    # all zeros = black pixels
    # shape: (150 rows, 150 cols, 3 colors)
    img = np.zeros((150,150,3), dtype=np.uint8)
    for x in range(50):
        for y in range(50):
            # red pixels
            img[x,y,red] = 255
            # purple pixels
            # set all 3 color components
            img[x+50, y+50,:] = (128, 0, 128)
            # green pixels
            img[x+100,y+100,green] = 255
    return img

def onechannel(pattern, rgb):
    '''takes pattern and rgb value as inputs and returns pattern with given
    color isolated'''
    pattern_copy = np.copy(pattern)
    
    # depending on the given rgb input make all of the rest of the colors 
    # set to black using slicing
    if rgb == 0:
        pattern_copy[:,:,1] = 0
        pattern_copy[:,:,2] = 0
        
    elif rgb == 1:
        pattern_copy[:,:,0] = 0
        pattern_copy[:,:,2] = 0
    
    elif rgb == 2:
        pattern_copy[:,:,0] = 0
        pattern_copy[:,:,1] = 0
    
    return pattern_copy

def permutecolorchannels(img, perm):
    '''takes img and color permutation as inputs and returns image with given
    color permutation'''
    img_copy = np.copy(img)
    
    img_copy[:,:,perm[0]] = img[:,:,0]
    img_copy[:,:,perm[1]] = img[:,:,1]
    img_copy[:,:,perm[2]] = img[:,:,2]
    
    return img_copy


def decrypt(image, key):
    array = np.zeros(image.shape, dtype=image.dtype)
    for x in range(key.shape[0]):
        for y in range(len(image)):
            array[y,x,:] = key[x]^image[y,x]
        
    return array 
        

# part 1 setup    
pattern = plt.imread('pattern.png' ) 

# part 2 setup
permcolors = plt.imread('permcolors.jpg')

# part 3 setup 
secret = plt.imread('secret.bmp')
key = np.load('key.npy')

# function calls

# part 1
plt.imshow(onechannel(pattern, 0))
plt.pause(0.001)
plt.imshow(onechannel(pattern, 1))
plt.pause(0.001)
plt.imshow(onechannel(pattern, 2))
plt.pause(0.001)

# part 2
plt.imshow(permutecolorchannels(pattern, [1,0,2]))
plt.pause(0.001)
plt.imshow(permutecolorchannels(pattern, [2,0,1]))
plt.pause(0.001)
plt.imshow(permutecolorchannels(permcolors, [1,2,0]))
plt.pause(0.001)

# part 3
plt.imshow(decrypt(secret, key))

