from taipy.gui import Gui, Html, navigate, notify
from Pages.about import about_md
from Pages.home import home_md
from Pages.watching import watching_md
from Pages.video import createMarkdown
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
from db import add_video


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
}

if __name__ == "__main__":
    initialOpen = 0
    lookedAwayStart = 0
    lookedAwayEnd = 0

    urlLink = ""

    allIntervals = []

    isLookingAway = False

    def startWatching(state):
        state.seconds = time.time()

    def lookedAway(state):
        state.lookedAwayStart = time.time() - initialOpen
        state.isLookingAway = True
    def lookedBack(state):
        if state.isLookingAway:
            state.lookedAwayEnd = time.time() - initialOpen
            # Check if the interval is more than 5 seconds
            if state.lookedAwayEnd - state.lookedAwayStart >= 5:
                # Then mark this guy!
                startEndLst = [state.lookedAwayStart, state.lookedAwayEnd]
                allIntervals.append(startEndLst)

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
conn.close()