from taipy.gui import Gui, navigate
home_md = """
# <p style="text-align: center;">Welcome to EyeTracker!</p>
---

<center>
<|{"image1.webp"}|image|height=400px|width=800px|on_action=image_action|class_name="shadow_fx"|>
</center>

## 

<center>
<a href="http://127.0.0.1:5000/watching"><|Start|button|></a>
</center>


<p id="demo"></p>




"""

def on_menu(state, var_name, function_name, info):
    page = info['args'][0]
    navigate(state, to=page)