from taipy.gui import Gui, Html, navigate, notify
from Pages.about import about_md
from Pages.home import home_md
from Pages.watching import watching_md
import Pages.Philosophy as phil
import time

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
    "watching/philosophy": phil.createMarkdown("https://www.youtube.com/embed/tgbNymZ7vqY")
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

    Gui(pages=pages).run(title='NewApp', stylekit=stylekit, dark_mode=False)


