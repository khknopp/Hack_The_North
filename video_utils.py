from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(link):
    return YouTubeTranscriptApi.get_transcript(link)

def no_timestamps(transcript):
    return " ".join([line['text'] for line in transcript])

def run_transcript(link):
    transcript = get_transcript(link)
    return no_timestamps(transcript)