home_md = """
# Welcome to eye tracking stuff
---
<p><a id="myAnchor" href="https://www.w3schools.com/">W3Schools</a></p>

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