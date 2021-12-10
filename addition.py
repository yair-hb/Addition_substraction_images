#este codigo es para la sustraccion y adicion de imagenes 
import cv2

imagen = cv2.imread('cadena.jpg')
imagen2 = cv2.imread('sacapuntas.jpg')
#se deben ajustar e igualar los tamaños de las imagenes para poder realizar .add
rz=cv2.resize(imagen, (600,400))
rz2=cv2.resize(imagen2, (600,400))

res = cv2.add(rz, rz2)
res2 = cv2.addWeighted(rz,0.5,rz2,0.9,0)
res3 = cv2.subtract(rz,rz2)
res4 = cv2.absdiff(rz,rz2)

cv2.imshow('IMAGEN', rz)
cv2.imshow('IMAGEN 2',rz2)
cv2.imshow('RESULTADO DE LA FUNCION ADD', res)
cv2.imshow('RESULTADO DE LA FUNCION ADDWEIGHTED',res2)
cv2.imshow('RESULTADO DE LA FUNCION SUBTRACT',res3)
cv2.imshow('RESULTADO DE LA FUNCION ABSDIFF',res4)
cv2.waitKey(0) 
cv2.destroyAllWindows()