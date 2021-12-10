#este codigo es para la sustraccion y adicion de imagenes 
import cv2

imagen = cv2.imread('cadena.jpg',0)
imagen2 = cv2.imread('sacapuntas.jpg',0)
#se deben ajustar e igualar los tamaños de las imagenes para poder realizar .add
rz=cv2.resize(imagen, (600,400))
rz2=cv2.resize(imagen2, (600,400))

res = cv2.add(rz, rz2)

cv2.imshow('IMAGEN', rz)
cv2.imshow('IMAGEN 2',rz2)
cv2.imshow('res', res)
cv2.waitKey(0) 
cv2.destroyAllWindows()