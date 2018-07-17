import cv2


def main():
    capture = cv2.VideoCapture(0)
    path = "../classifier/haarcascade_frontalface_default.xml"

    face_cascade = cv2.CascadeClassifier(path)

    while (True):
        _, frame = capture.read()

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.05, minNeighbors=5, minSize=(40, 40))

        print("Number of faces : " + str(len(faces)))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Live Capture", frame)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    capture.release()


if __name__ == '__main__':
    main()
