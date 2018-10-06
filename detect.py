import dlib
import cv2
alpha = 0.2
detector = dlib.fhog_object_detector("detector.svm")
cap = cv2.VideoCapture(0)
if (cap.isOpened() == False):
  print("Error opening Camera")
  
while (cap.isOpened()):
    ret,frame = cap.read()
    output = frame.copy()
    dets = detector(frame)
    for d in dets:
        cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), -1)
        cv2.addWeighted(frame,alpha,output,1-alpha,1,output)
    cv2.imshow("output",output)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
    
cap.release()
cv2.destroyAllWindows()
