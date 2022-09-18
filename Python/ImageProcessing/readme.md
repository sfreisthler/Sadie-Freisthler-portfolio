## Permutation.py

This program utilizes NumPy and Matplotlib to carry out image processing tasks. 

### Part 1

Function onechannel() takes in parameters pattern and rgb. Given an image file, this function isolates the color passed as an argument and sets 
the rest of the colors to black. 

### Part 2

Function permutecolorchannels() takes in img and permutation as parameters. The colors in the given image are permuted based on the list passed
as an argument.

### Part 3 

Function decrypt() takes in parameters image and key. The image passed as an argument has been encrypted by XORing the image using a given key. Decrypt
takes that image and key returns the image back to normal. 
