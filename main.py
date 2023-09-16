from taipy.gui import Gui, Html
from math import cos, exp 

page = Html('''
<style>
.big-title {
  font-family: Roboto;
  text-align: center;
}

.horizontal-align {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5rem;
}

.card {
  width: 260px;
  height: 260px;
  background: #282828;
  border-radius: 16em;
  box-shadow: 0.3em 0.3em 0.7em #00000015;
  transition: border 0.7s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  border: #2d2d2d 0.2em solid;
}

.card p {
  text-align: left;
  padding: 0 1rem;
}

.card:hover {
  border: #0087ca 0.2em solid;
  cursor: pointer;
}
</style>
<h1 class="big-title">What would you like to learn today?</h1>
<center>
<div class="horizontal-align">
    <div class="card">
        <h1>Math</h1>
        <p>Learn math skills here</p>
      </div>
      <div class="card">
        <h1>Physics</h1>
        <p>Learn physics skills here</p>
      </div>
      <div class="card">
        <h1>Chemistry</h1>
        <p>Learn chemistry skills here</p>
      </div>
</div>
</center>
''')
stylekit = {
  "color_primary": "#323232",
  "color_secondary": "#0087ca",
  "color_background_dark": "#323232",
  "font_family": "Arial",
}

Gui(page=page).run(title='NewApp', stylekit=stylekit)