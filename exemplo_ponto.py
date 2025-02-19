import cv2
import numpy as np

# Criar uma imagem preta
img = np.zeros((500, 500, 3), dtype=np.uint8)

# Definir um ponto e desenhá-lo
ponto = (250, 250)  # Coordenadas (x, y)
cv2.circle(img, ponto, 5, (0, 255, 0), -1)  # Desenha um ponto verde

cv2.imshow("Imagem", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
