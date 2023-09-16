from taipy.gui import Gui, Html
from math import cos, exp 

page = Html("""
<h1>Page title</h1>

Any <a href="https://en.wikipedia.org/wiki/HTML"><i>HTML</i></a>
content can be used here.
""")

# def print_link(decay):
#     return [cos(i/16) * exp(-i*decay/6000) for i in range(720)]

# def on_change(state, var_name, var_value):
#     if var_name == 'link':
#         state.data = print_link(var_value)

#data = print_link(decay) 

Gui(page=page).run(title='SmarTranscribe',
    		       dark_mode=True)