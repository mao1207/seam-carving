# Seam Carving

## Algorithm Principle
Seam Carving is an algorithm that handles the scaling of an image, keeping as much of the important areas of the image, avoiding the distortion caused by direct scaling.The principle of the algorithm is to calculate the gradient of each pixel as the "energy" of the pixel, and the image can be considered as a discrete function, where the gradient in the x-direction can be reduced to the difference of neighboring pixels, and the same for the y-direction, the gradient of the pixel can be replaced by the sum of the absolute values of the gradients in the x and y directions for simplicity. This is only one way to calculate the gradient, but there are various operators defined in OpenCV for gradient calculation. There are various operators defined in OpenCV for gradient calculation, such as the Sobel operator. Then we find a gap (path) with the lowest energy in the corresponding direction and delete it. 

## Results Show
input image

![imageBefore](https://raw.githubusercontent.com/mao1207/seam-carving/main/in/images/image.png)
output image

![imageAfter](https://raw.githubusercontent.com/mao1207/seam-carving/main/out/images/image_result.png)
