import cv2

img = cv2.imread ("jo.jpg", 0)

negatif = 255 - img

cv2.imshow("Gambar Warna Original", img)
cv2.imshow("Gambar Warna Negatif", negatif)

cv2.waitKey(0)
cv2.destroyAllWindows()