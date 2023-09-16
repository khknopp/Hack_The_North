from video_utils import *
from questionGenerator import *

video = "9syvZr-9xwk"

transcript = run_transcript(video)

questions = generate_questions(transcript)

print(questions)