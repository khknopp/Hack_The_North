from dotenv import load_dotenv
import psycopg
from psycopg.errors import SerializationFailure, Error
from psycopg.rows import namedtuple_row
import pickle as pk
from question_generator import get_questions, split_execution
from summarize import create_fragments, summarize_text, update_summary

from video_utils import run_transcript
import os
import cohere

load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
co = cohere.Client(COHERE_API_KEY)

    

class get_params: 
    def __init__(self, link, title):
        self.link = link
        self.title = title
        
        self.transcription_timestamps, self.transcription = run_transcript(self.link)
        
        # self.transcription = self.transcription[:15000]
        open, closed, self.summary = split_execution(co, self.transcription)
        
        print(str(len(self.summary)) + "Length of summary after splitexec")
        print(self.summary)
        self.summary = " ".join(self.summary)
        
        self.open_questions, self.closed_questions, self.closed_answers, self.open_answers =  get_questions(co, open, closed)
        
        self.boundaries = pk.dumps([[70, 100], [400, 500], [700, 750], [800, 1200]])
        self.highlight_flags = pk.dumps("")

        
    def add_video(self, conn):
        with conn.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS videos (link TEXT PRIMARY KEY, summary TEXT, closed_questions TEXT, closed_answers TEXT, open_questions TEXT, open_answers TEXT, title TEXT, transcript TEXT)"
            )
            conn.commit()
            cur.execute(
                "INSERT INTO videos (link, summary, closed_questions, closed_answers, open_questions, open_answers, title, transcript) VALUES (%s,%s,%s,%s,%s,%s,%s,%s, %s, %s, %s)", (self.link, self.summary, pk.dumps(self.closed_questions), pk.dumps(self.closed_answers), pk.dumps(self.open_questions), pk.dumps(self.open_answers), self.title, self.transcription, self.transcription_timestamps, self.boundaries, self.highlight_flags ))
        conn.commit()
        print("Added succesfully")
        
        
    def update_db(self, conn, link):
        ## GET FROM DB
        with conn.cursor() as cur:
            cur.execute("SELECT title,transcription FROM videos WHERE link = %s", (self.link,))
            data = cur.fetchall()
            print(data)
        # self.link 
        # self.title         
        # self.transcription 
        
        # create_fragments()
        
        
        open, closed, self.summary = split_execution(co, self.transcription)
        
        print(str(len(self.summary)) + "Length after splitexec")
        self.summary = " ".join(self.summary)
        
        self.open_questions, self.closed_questions, self.closed_answers, self.open_answers =  get_questions(co, open, closed)
        
        
        fragments = create_fragments(self.transcription_timestamps, self.boundaries)
        self.summary, self.highlight_flags = update_summary(co, self.summary, fragments)
        
        
        
        
    


#add_video(conn, "9syvZr-9xwk", "This is a summary of the video", ["These are the closed questions"], ["These are the closed answers"], ["These are the open questions"], ["These are the open answers"], "This is the title", "This is the transcript")
