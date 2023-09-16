from taipy.gui import Gui, Html
from Pages.about import about_md
from Pages.home import home_md
from Pages.watching import watching_md


root_md = """
<center>
<|navbar|>
</center>
"""

stylekit = {
  "font_family": "Arial",
}

pages = {
    "/": root_md,
    "home": home_md,
    "about": about_md,
    "watching": watching_md
}

Gui(pages=pages).run(title='NewApp', stylekit=stylekit, dark_mode=False)