home_md = """
# Welcome to eye tracking stuff
---

<style>
        /* CSS for the image with box shadow */
        .image-container {
            width: 300px; /* Adjust the width as needed */
            box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.3); /* Box shadow properties */
        }
</style>
    <div class="image-container">
        <img src="image1.webp" alt="Your Image">
    </div>

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