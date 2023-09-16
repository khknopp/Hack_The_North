import psycopg
from psycopg.errors import SerializationFailure, Error
from psycopg.rows import namedtuple_row
import pickle as pk

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

#add_video(conn, "9syvZr-9xwk", "This is a summary of the video", ["These are the closed questions"], ["These are the closed answers"], ["These are the open questions"], ["These are the open answers"], "This is the title", "This is the transcript")