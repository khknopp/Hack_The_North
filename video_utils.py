from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(link):
    transcript = YouTubeTranscriptApi.get_transcript(link)
    for i in range(len(transcript)):
        transcript[i]['index'] = i
    return transcript

def no_timestamps(transcript):
    return " ".join([line['text'] for line in transcript])

def run_transcript(link):
    transcript = get_transcript(link)
    return transcript, no_timestamps(transcript)

def get_fragment(transcript, start, end):
    
    middle = [line for line in transcript if line['start'] >= start and line['start'] <= end]
    middle_indexes = [line['index'] for line in middle]
    middle_text = " ".join([line['text'] for line in middle])

    beginning_text = " ".join([el['text'] for el in transcript[max(0, middle_indexes[0]-5):middle_indexes[0]]])

    end_text = " ".join([el['text'] for el in transcript[middle_indexes[-1]:min(len(transcript)-1, middle_indexes[-1]+5)]])
    return middle_text, beginning_text, end_text