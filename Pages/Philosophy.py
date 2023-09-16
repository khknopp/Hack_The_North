def createMarkdown(link):
    return f"""#Learning geography
    <iframe id="existing-iframe-example"
            width="640" height="360"
            src="{link}"
            frameborder="0"
            style="border: solid 4px #37474F"
    ></iframe>
    <|{link}|input|>
    """
