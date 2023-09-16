from dotenv import load_dotenv
import psycopg
from psycopg.errors import SerializationFailure, Error
from psycopg.rows import namedtuple_row
import pickle as pk
from question_generator import get_questions, split_execution
from summarize import create_fragments, summarize_text

from video_utils import run_transcript
import os
import cohere

load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
co = cohere.Client(COHERE_API_KEY)

def add_video(conn, link, summary, closed_questions, closed_answers, open_questions, open_answers, title, transcription):
    with conn.cursor() as cur:
        cur.execute(
            "CREATE TABLE IF NOT EXISTS videos (link TEXT PRIMARY KEY, summary TEXT, closed_questions TEXT, closed_answers TEXT, open_questions TEXT, open_answers TEXT, title TEXT, transcript TEXT)"
        )
        conn.commit()
        cur.execute(
            "INSERT INTO videos (link, summary, closed_questions, closed_answers, open_questions, open_answers, title, transcript) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (link, summary, pk.dumps(closed_questions), pk.dumps(closed_answers), pk.dumps(open_questions), pk.dumps(open_answers), title, transcription))
    conn.commit()
    print("Added succesfully")
    

class get_params: 
    def __init__(self, link, summary, closed_questions, closed_answers, open_questions, open_answers, title, transcription):
        self.link = link 
        self.summary = summary
        self.closed_questions = closed_questions
        self.closed_answers = closed_answers
        self.open_questions = open_questions
        self.open_answers = open_answers
        self.title = title
        self.transcription = transcription
    
    def create_vars(self):
        video = self.link
        self.title = "youtube title from api"
        timestamp_array = [] #GEt from frontend
        
        self.transcription = run_transcript(video)
        self.summary = " ".join(summarize_text(co, self.transcription))

        open, closed = split_execution(co, self.transcription)
        self.open_questions, self.closed_questions, self.closed_answers, self.open_answers =  get_questions(co, open, closed)
        
        
        
        
    


#add_video(conn, "9syvZr-9xwk", "This is a summary of the video", ["These are the closed questions"], ["These are the closed answers"], ["These are the open questions"], ["These are the open answers"], "This is the title", "This is the transcript")