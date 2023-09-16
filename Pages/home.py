home_md = """
# Welcome to eye tracking stuff
---

<p>Click the button to display the value of the href attribute of the link above.</p>

<button onclick="myFunction()">Try it</button>

<p id="demo"></p>

<script>
function myFunction() {
  var x = document.getElementById("myAnchor").href;
  document.getElementById("demo").innerHTML = x;
}
</script>



"""