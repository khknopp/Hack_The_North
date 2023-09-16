import cohere

def summarize_text(co, text):
  transcriptionSummary = co.summarize(
    text=text,
    format="bullets",
    extractiveness="auto",
    additional_command="Create a summary of the text's key takeaways and provide supporting evidence. Ensure that student at this lecture could easily understand it",
  )
  return [element[2:] for element in str(transcriptionSummary.summary).split('\n')]