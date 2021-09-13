import cv2

img = cv2.imread('./images/dog-01.jpg')

while True:
  cv2.imshow('Puppy',img)

  # if we've waited at least 1 ms & we've hit the esc key
  # 27 = esc key
  if cv2.waitKey(1) & 0xFF == 27:
      break

cv2.destroyAllWindows()



