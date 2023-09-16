from taipy.gui import Gui, Html
from Pages.about import about_md
from Pages.home import home_md
from Pages.watching import watching_md
from Pages.Philosophy import philosophy_md
import time
from video_utils import *
from questionGenerator import *
from summarize import *
from dotenv import load_dotenv
import os
import cohere

load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
co = cohere.Client(COHERE_API_KEY)

generalNavigation = [("/home", "Home"), ("/about", "About"), ("/watching", "Watching")]
watchingNavigation = [("/watching/philosophy", "Philosophy"), ("/watching/history", "History")]

root_md = """
<center>
<|navbar|lov={generalNavigation}|>
</center>

"""

stylekit = {
  "font_family": "Arial",
}

pages = {
    "/": root_md,
    "home": home_md,
    "about": about_md,
    "watching": watching_md,
    "watching/philosophy": philosophy_md,
}

if __name__ == "__main__":
    initialOpen = 0
    lookedAwayStart = 0
    lookedAwayEnd = 0

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

    Gui(pages=pages).run(title='NewApp', stylekit=stylekit, dark_mode=False)


# video = "9syvZr-9xwk"
#video = "4XGGPfaTcSo"

#transcript, transcript_text = run_transcript(video)
# overall_summary = " ".join(summarize_text(co, transcript_text))
#separate based on fullstops to get bullet points

#open, closed, summary = split_execution(co, transcript_text)
#get_questions(co, open, closed)

#fragments = create_fragments(transcript, [[50, 100], [200, 230]])

#print(update_summary(co, summary, fragments))


#print(all_outputs)
