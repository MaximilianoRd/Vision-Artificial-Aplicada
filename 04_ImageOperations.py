import numpy as np
import cv2

img=cv2.imread('RandomImg.jpg',cv2.IMREAD_COLOR)
#Se selecciona un pixel y le cabia el color
#     pixel    nuevos valores del pixel
img[10,10]=[150,200,0]
pixel=img[10,10]
print(pixel)
#cambia de color un conjunto de pixeles selecionados
#           rango       nuevos valores
img[30:150,200:300]=[255,255,255]
print(img.shape)
print(img.size)
print(img.dtype)
#copypaste de pixeles
#copy
seccion=img[100:250,400:500]
#paste
img[20:170,20:120]=seccion

cv2.imshow('imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows()