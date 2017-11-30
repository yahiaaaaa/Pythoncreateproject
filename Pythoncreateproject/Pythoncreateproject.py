import cv2
import numpy as np
import matplotlib.pyplot as mpl


###Start load an image
#imLoad = cv2.imread("test.jpg")
#cv2.imshow("Window Name", imLoad)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#mpl.imshow(imLoad)
#mpl.show()

#cv2.imwrite("Output",imLoad)

###Start to capture video
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while True:
    ret,frame = cap.read()
    out.write(frame)
    cv2.imshow("Video",frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

