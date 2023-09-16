from gaze_tracking import GazeTracking
import cv2

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

text = ""

while True:
    _, frame = webcam.read()
    gaze.refresh(frame)

    new_frame = gaze.annotated_frame()
    hor = gaze.horizontal_ratio()
    ver = gaze.vertical_ratio()

    #cv2.putText(new_frame, text, (60, 60), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2)
    #cv2.imshow("Demo", new_frame)

    print(f"horizontal: {hor}, right: {ver}")