import numpy as np
import cv2
img = cv2.imread('RandomImg.jpg', cv2.IMREAD_COLOR)
        #Comando para dibujar la linea
             #inicio  fin         B   G    R   grosor
cv2.line(img, (0,0), (200,200), (255, 75, 100), 15)
                #posicion  tamaño      B  G   R  grosor
cv2.rectangle(img, (0,25), (390,150), (0,255,255), 5)
             #posicion  radio   B  G  R   grosor
cv2.circle(img, (100,63), 30, (255,0,255), 5)
#Para poner un polígono se definen los vertices de esta manera
pts = np.array([[200,200],[180,180],[150,200],[200,250]],np.int32)
#Aquí se unen los puntos          B   G   R  grosor
cv2.polylines(img, [pts], True, (200,200,100),5)
#Se elige la fuente de texto
font = cv2.FONT_HERSHEY_SIMPLEX
#                Texto    lugar  fuente tamaño B   G   R  grosor
cv2.putText(img, 'CETI', (250,250), font, 2, (100,255,100), 5, cv2.LINE_AA)

cv2.imshow('imagen tuneada',img)
cv2.waitKey(0)
cv2.destroyAllWindows()