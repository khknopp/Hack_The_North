def createMarkdown(link):
    return f"""<h1 style="text-align: center;">Have fun watching!</h1>
    \n<p align="center">
    \n<iframe id="existing-iframe-example" width="1080" height="520" src="{link}"frameborder="0" style="border: solid 4px #37474F"></iframe>
    </p>
    \n<center>
    <|Start Session|button|class_name="custom-btn btn-14 red"|on_action=startWatching|>
    <a href = "watching/quiz">
    <|End Session|button|class_name="custom-btn btn-14 red|on_action=startWatching"|>
    </a>
    </center>
    """