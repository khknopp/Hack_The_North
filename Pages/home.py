
from taipy.gui import Gui, navigate

home_md = """
<h1 style="text-align: center;">Welcome to EyeQ!</h1>
---
## 
<|layout|columns=1 2|
<|
<center>
<|{"./llama.jpg"}|image|height=300px|width=300px|>
</center>
|>
<|
# Get started on your learning journey.
### Unlock Your Focus, Master Your Studies: EyeQ.
EyeQ is a productivity tool that improves a student's ability in learning by helping them understand stuff 
they might miss in lecture. **Feel free to get started by pressing** start below!
## 
<a href="watching">
<|Start Now!|button|class_name="custom-btn btn-14 red"|>
</a>
|>
|>
"""
