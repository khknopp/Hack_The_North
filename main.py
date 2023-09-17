from taipy.gui import Gui, Html, navigate, notify
from Pages.about import about_md
from Pages.home import home_md
from Pages.watching import watching_md
from Pages.video import createMarkdown
from Pages.landingp import landingp_md
from Pages.landingpt import landingpt_md
from Pages.landingcs import landingcs_md
import time
from video_utils import *
from question_generator import *
from summarize import *
from dotenv import load_dotenv
import os
import cohere
import psycopg
from psycopg.errors import SerializationFailure, Error
from psycopg.rows import namedtuple_row
import pickle as pk
from db import get_params
import threading
from gaze_tracking import GazeTracking
import cv2


load_dotenv()


# co = cohere.Client(COHERE_API_KEY)
# db_url = f"postgresql://{COCKROACH_USERNAME}:{COCKROACH_PASSWORD}@cuter-falcon-5491.g8z.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"


# conn = psycopg.connect(db_url, application_name="$ defaultdb", row_factory=namedtuple_row)

generalNavigation = [("/home", "Home"), ("/about", "About"), ("/watching", "Watching")]
watchingNavigation = [("/watching/video", "Video"), ("/watching/history", "History")]

root_md = """
<center>
<|navbar|lov={generalNavigation}|>
</center>

"""

        
#add_video(conn, "9syvZr-9xwk", "This is a summary of the video", ["These are the closed questions"], ["These are the closed answers"], ["These are the open questions"], ["These are the open answers"], "This is the title", "This is the transcript")
video_md = createMarkdown("https://www.youtube.com/embed/9syvZr-9xwk")
pages = {
    "/": root_md,
    "home": home_md,
    "about": about_md,
    "watching": watching_md,
    "watching/video": video_md,
    "watching/landingp": landingp_md,
    "watching/landingpt": landingpt_md,
    "watching/landingcs": landingcs_md
}

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

text = ""

initialOpen = time.time()

isLookingAway = False

initialOpen = 0
lookedAwayStart = 0
lookedAwayEnd = 0
urlLink = ""
allIntervals = []


def camera():
    global allIntervals
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
                lookedAway()
            else:
                text = "Paying attention!"
                lookedBack()
        else:
            text = "Not paying attention!"
            lookedAway()

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)


        cv2.imshow("Demo", frame)

        if cv2.waitKey(1) == 27:
            break
    
    print(allIntervals)
    webcam.release()
    cv2.destroyAllWindows()

def lookedAway():
    global lookedAwayStart
    global isLookingAway
    if(isLookingAway == False):
        lookedAwayStart = time.time() - initialOpen
    isLookingAway = True
        
def lookedBack():
    global isLookingAway
    global lookedAwayStart
    global lookedAwayEnd
    global allIntervals
    if isLookingAway == True:
        lookedAwayEnd = time.time() - initialOpen
        if lookedAwayEnd - lookedAwayStart >= 3:
            allIntervals.append([lookedAwayStart, lookedAwayEnd])
        isLookingAway = False


if __name__ == "__main__":
    
    b = threading.Thread(name='background', target=camera)
    b.start()

    def on_menu(state, var_name, function_name, info):
        page = info['args'][0]
        navigate(state, to=page)

    Gui(pages=pages).run(title='NewApp', dark_mode=False)


# video = "9syvZr-9xwk"
#video = "4XGGPfaTcSo"
#video = "9syvZr-9xwk"
# video = "4XGGPfaTcSo"

#transcript, transcript_text = run_transcript(video)
# overall_summary = " ".join(summarize_text(co, transcript_text))
#separate based on fullstops to get bullet points

#open, closed, summary = split_execution(co, transcript_text)
#

#fragments = create_fragments(transcript, [[50, 100], [200, 230]])
#fragments = create_fragments(transcript, [[50, 100], [200, 230], [200, 230]])

#print(update_summary(co, summary, fragments))


#print(all_outputs)
# conn.close()