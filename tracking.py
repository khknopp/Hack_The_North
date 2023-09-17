from gaze_tracking import GazeTracking
import cv2

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

text = ""

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    new_frame = gaze.annotated_frame()
    hor = gaze.horizontal_ratio()
    ver = gaze.vertical_ratio()

    if(hor != None and ver != None):
        if(hor > 0.9 or ver > 0.9 or ver < 0.1 or hor < 0.1):
            text = "Not paying attention!"
        else:
            text = "Paying attention!"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)


    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
   
webcam.release()
cv2.destroyAllWindows()