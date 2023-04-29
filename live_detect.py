# importe a biblioteca opencv 
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/Pedro/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haardcascade_eye.xml')

# Defina um objeto VideoCapture
vid = cv2.VideoCapture(0)

while(True):
   
    # Capture o vídeo quadro a quadro
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detectar rosto
    faces = face_cascade.detectMultiScale(gray, 1.1,5)
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 5)
    # desenhar retrangulo ao redor do rosto
    for (x,y,w,h) in faces:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
       roi_color = frame[y:y+h, x:x+w]
       cv2.imwrite('fri.jpg', roi_color)

    for (x,y,w,h) in eyes:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
       roi_color = frame[y:y+h, x:x+w]
       cv2.imwrite('fri.jpg', roi_color)


    # Exiba o quadro resultante
    cv2.imshow("Web cam", frame)
      
    # Saia da tela ao pressionar a barra de espaço
    if cv2.waitKey(25) == 32:
        break
  
# Após o loop, libere o objeto capturado
vid.release()

# Destrua todas as telas
cv2.destroyAllWindows()