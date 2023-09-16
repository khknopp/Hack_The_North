from video_utils import *
from questionGenerator import *
from summarize import *
from dotenv import load_dotenv
import os
import cohere

load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
co = cohere.Client(COHERE_API_KEY)

# video = "9syvZr-9xwk"
video = "4XGGPfaTcSo"

transcript, transcript_text = run_transcript(video)
# overall_summary = " ".join(summarize_text(co, transcript_text))
#separate based on fullstops to get bullet points

open, closed, summary = split_execution(co, transcript_text)
#get_questions(co, open, closed)

fragments = create_fragments(transcript, [[50, 100], [200, 230]])

print(update_summary(co, summary, fragments))


#print(all_outputs)