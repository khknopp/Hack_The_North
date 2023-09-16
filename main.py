from taipy.gui import Gui, Html
from math import cos, exp 

page = Html("""
<style>
body {
	background: white;
}
</style>
<center>
<h1>Project title goes here</h1>
</center>
<h1>What subject do you want to learn?</h1>
<button>Math</button>
<button>Physics</button>
<button>Chemistry</button>
""")

# def print_link(decay):
#     return [cos(i/16) * exp(-i*decay/6000) for i in range(720)]

# def on_change(state, var_name, var_value):
#     if var_name == 'link':
#         state.data = print_link(var_value)

#data = print_link(decay) 

Gui(page=page).run(title='SmarTranscribe')