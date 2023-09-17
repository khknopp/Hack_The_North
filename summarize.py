
from video_utils import get_fragment


from final_summary import replace_less_detailed_sentences
def summarize_text(co, text):
  transcriptionSummary = co.summarize(
    text=text,
    length = "long",
    format="bullets",
    extractiveness="auto",
    additional_command="Create a detailed and descriptive summary of the text's key takeaways and provide supporting evidence",
  )

  
  return [element[2:] for element in str(transcriptionSummary.summary).split('\n')]

# highlighted is an array of [[mid, beg, end], [mid, beg, end], [mid, beg, end]], each element is a section of the transcript where the student didnt pay attention
def summarize_highlighted(co, highlighted):
    highlightedSummary = co.summarize(
        text = highlighted,
        format="bullets",
        extractiveness="auto",
        additional_command="Emphasize the text's main takeaways",
    )
    return [element[2:] for element in str(highlightedSummary.summary).split('\n')]

def create_fragments(transcript, boundaries):
  fragments = []
  for boundary in boundaries:
    fragments.append(get_fragment(transcript, boundary[0], boundary[1]))
  return fragments

def update_summary(co, overall_summary, unfocused_fragments):
  highlighted_summary = []
  for fragment in unfocused_fragments:
      section = fragment[1] + fragment[0] + fragment[2]
      if len(section) >= 250:
          highlighted_summary.append(summarize_highlighted(co, section))

#   highlighted_summary = " ".join(highlighted_summary[0])
#   overall_summary = " ".join(overall_summary[0])

  print(overall_summary)
  print(highlighted_summary)
  combined_summary, highlight_flags= replace_less_detailed_sentences(overall_summary, highlighted_summary[0])
  print("combined summary is :" + str(combined_summary))

  return combined_summary, highlight_flags