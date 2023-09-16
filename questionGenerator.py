import cohere
from summarize import summarize_text
# import transcription from transcription.py

def generate_questions(co, text, number=5):
  openEndedQuestions = co.generate(
    prompt="List 5-10 open ended questions based on the following text: " + text,
    max_tokens=128
  )

  multipleChoiceQuestions = co.generate(
    prompt='List 5-8 multiple choice questions and the correct answer for each question based on the following text:' + text,
    max_tokens=300
  )

  return openEndedQuestions.generations[0].text, multipleChoiceQuestions.generations[0].text


def split_execution(co, whole_text):
  n = 2000
  i = 0
  whole_text = whole_text.split(" ")
  openEndedQuestionsList = []
  multipleChoiceQuestionsList = []
  summaryList = []


  while i*n < len(whole_text):
    if(len(whole_text) - i*n < 400):
      break

    text = " ".join(whole_text[i*n:(i+1)*n])
    openEndedQuestions, multipleChoiceQuestions = generate_questions(co, text)
    summaryList.append(summarize_text(co, text))

    openEndedQuestionsList.append(openEndedQuestions)
    multipleChoiceQuestionsList.append(multipleChoiceQuestions)
    i += 1

    return openEndedQuestionsList, multipleChoiceQuestionsList, summaryList