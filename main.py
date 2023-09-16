from video_utils import *
from questionGenerator import *
from dotenv import load_dotenv
import os

load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
co = cohere.Client(COHERE_API_KEY)

# video = "9syvZr-9xwk"
video = "4XGGPfaTcSo"

transcript, transcript_text = run_transcript(video)

m, b, e = get_fragment(transcript, 30, 55)
print(m,"$$$$$$$$$$$$", b, "$$$$$$$$$$$$$$$$", e)

#all_outputs = split_execution(co, transcript_text)

#print(all_outputs)