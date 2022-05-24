from email.mime import image
import cv2    #clase estatica
import numpy as np #clase dinamica
import imutils #clase estatica


#1)Rangos en donde se encuentra presente el color rojo para deteccion de color-----------------------------------
#rojo en HSV= 0 a 8
#azul en HSV= 80  a   120
#amarillo en HSV= 13 a 40 


#lo siguiente detectara el color rojo
          # HSV =  [valor,matiz,saturacion]
        
colorBajo1 = np.array([0,140,90], np.uint8)    #rango de color bajo (de rojo) entre 0 y 179
colorAlto1 = np.array([8,255,255], np.uint8)    #rango de color alto
colorBajo2 = np.array([160,140,90], np.uint8)   #rango de color bajo
colorAlto2 = np.array([180,255,255], np.uint8)  #rango de color alto



#lo siguiente detectara el color azul  (utilizar imagen 'color.jpg')
"""
colorBajo1 = np.array([80,140,90], np.uint8)  
colorAlto1 = np.array([110,255,255], np.uint8)
colorBajo2 = np.array([100,140,90], np.uint8)
colorAlto2 = np.array([120,255,255], np.uint8)

#"""


#lo siguiente detectara el color amarillo  (utilizar imagen 'color.jpg')
"""
colorBajo1 = np.array([13,140,90], np.uint8)  
colorAlto1 = np.array([40,255,255], np.uint8)
colorBajo2 = np.array([20,140,90], np.uint8)
colorAlto2 = np.array([30,255,255], np.uint8)

#"""

#2)leer imagen --------------------------------------------------------------------------------------------------

image = cv2.imread('rojo4.jpg')     #lectura de la imagen |  imread busca la imagen siempre que se mantenga con el mismo nombre y formato

#para probar con color rojo:
#image = cv2.imread('rojo3.jpg')
#image = cv2.imread('rojo2.jpg')
#image = cv2.imread('rojo1.jpg')

image = imutils.resize(image, width=500)  #redimencion de la imagen mientras mantiene la relacion del aspecto de la imagen


#3)transformacion a escala de grises-----------------------------------------------------------------------------
imageGray =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #convertidor de color a gris
imageGray =cv2.cvtColor(imageGray,cv2.COLOR_GRAY2BGR)  # convertidor de gris de vuelta a una imagen BGR
imageHSV = cv2.cvtColor(image,cv2.COLOR_BGR2HSV) #convertidor de color en HSV, matiz, color y saturacion


#4)detectar color------------------------------------------------------------------------------------------------

#La función inRange espera tres argumentos: el primero es la imagen donde vamos a realizar la detección de color, 
# el segundo es el límite inferior del color que desea detectar y
#  el tercer argumento es el límite superior del color que desea detectar.

maskColor1 =cv2.inRange(imageHSV,colorBajo1,colorAlto1)  #funcion que mide los valores cercanos a los 0° |matiz
maskColor2 =cv2.inRange(imageHSV,colorBajo2,colorAlto2) #funcion que mide los valores cercanos a los 360°
mask =cv2.add(maskColor1,maskColor2)  #union entre la mascara 1 y mascara 2 segun rangos
mask =cv2.medianBlur(mask,7)        #filtro que suaviza bordes
colorDetected= cv2.bitwise_and(image,image,mask=mask)  #bitwise_and observar el color original de las uniones de la mascara |mascara en color rojo

#5)fondo en grises------------------------------------------------------------------------------------------------

invMask =cv2.bitwise_not(mask)  # condicional "no". invierte la mascara| muestra fondo en blanco y negro
bgGray= cv2.bitwise_and(imageGray,imageGray,mask=invMask) #condicional "y" devuelve el inverso de lo anterior y forma el fondo en escala de grises

#Sumar BgGray y red detected
resultado= cv2.add(bgGray,colorDetected) #union entre el fondo y la deteccion de zona roja

#6)visualizacion ---------------------------------------------------------------------------------------------------


cv2.imshow('image',image)                    #visualiza imagen original
#cv2.imshow('redDetected',redDetected)       #visualiza solo el color rojo
#cv2.imshow('invMask',invMask)               #inverso a la primera mascara visualiza forma 
#cv2.imshow('bgGray',bgGray)                  # visualiza en escala de grises la imagen
cv2.imshow('resultado',resultado)            # visualiza el resultado de unir la imagen gris y el color detectado rojo

cv2.waitKey(0)                          #evita que se cierre la ventana
cv2.destroyAllWindows()                 #cierre de ventana

