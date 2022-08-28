import cv2


def main():
    # root = tk.Tk()
    # root.title("OpenCV")
    # root.geometry("400x400")
    # root.resizable(False, False)
    # root.mainloop()
    print("Hello World!")
    # detect face cascade classifier
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # mesh face cascade classifier
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    
    cap = cv2.VideoCapture(
    'udp://127.0.0.1:1235', cv2.CAP_FFMPEG)
    while True:
        ret, frame = cap.read()
        if not ret:
            print('frame empty')
            break
           
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.9, 5)        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)        
        cv2.imshow("Frame", frame)
        # wait for the user to press 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break   
    # release the capture
    cap.release()
    cv2.destroyAllWindows()
    print("Goodbye World!")


if __name__ == "__main__":
    main()