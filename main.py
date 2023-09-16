from video_utils import *
from questionGenerator import *
from summarize import *
from dotenv import load_dotenv
import os

load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
co = cohere.Client(COHERE_API_KEY)

# video = "9syvZr-9xwk"
video = "4XGGPfaTcSo"

transcript, transcript_text = run_transcript(video)
overall_summary = " ".join(summarize_text(co, transcript_text))

unfocused_fragments = []
unfocused_fragments.append(get_fragment(transcript, 30, 55))
unfocused_fragments.append(get_fragment(transcript, 200, 220))
print(unfocused_fragments)

highlighted_summary = []
for fragment in unfocused_fragments:
    section = fragment[1] + fragment[0] + fragment[2]
    if len(section) >= 250:
        highlighted_summary.append(summarize_highlighted(co, section))

highlighted_summary = " ".join(highlighted_summary[0])

combined_summary = combine_summaries(co, overall_summary, highlighted_summary)

print(combined_summary)
#separate based on fullstops to get bullet points

open, closed, summary = split_execution(co, transcript_text)

get_questions(co, open, closed)

#print(all_outputs)