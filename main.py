from video_utils import *
from questionGenerator import *
from dotenv import load_dotenv
import os

load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
co = cohere.Client(COHERE_API_KEY)

# video = "9syvZr-9xwk"
video = "4XGGPfaTcSo"

transcript = run_transcript(video)

all_outputs = split_execution(co, transcript)

print(all_outputs)