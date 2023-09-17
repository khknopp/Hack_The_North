
from summarize import summarize_text
# import transcription from transcription.py

def generate_questions(co, text, number=5):
  openEndedQuestions = co.generate(
    prompt="List 2 open ended questions based on the key concepts of the following text: " + text,
    max_tokens=128
  )

  multipleChoiceQuestions = co.generate(
    prompt='List 2 quick multiple choice questions and a short correct answer for each question based on the key concepts of the following text:' + text,
    max_tokens=300
  )

  return openEndedQuestions.generations[0].text, multipleChoiceQuestions.generations[0].text


def check_question(co, question):
  answer = co.generate(
    prompt='Act as a student and try to write a brief, but correct answer (such that the grading professor will definitely approve your answer) to the following question:' + question + ". If you do not have the context available to answer the question make sure to only write I do not know.",
    max_tokens=300,
    temperature=3.0
  )
  grader = co.generate(
    prompt='Act as a university professor grading a students work and knowing the content of your course and all information available to you as a professor in the field. Specifically make sure to check if the answer is logical, creative and could be written by a student without external context. If a student answers that they do not know, automatically fail the answer. Be sure that if you think the question is not useful to a student learning about your specialized field (especially if it is below the level of a graduate student, too general or too repetetive), fail the answer. Otherwise, write either Pass or Fail depending on whether you would accept the following answer:' + answer.generations[0].text + 'to the question:' + question,
    max_tokens=5,
    temperature=0.0
  )
  answer = answer.generations[0].text
  grader = grader.generations[0].text
  
  #print(question, answer, grader)

  if("Pass" in grader):
    return answer
  else:
    return None 
  
def get_questions(co, open, closed):
  open = open[0].split("\n")
  closed = [el for el in closed[0].split("\n") if el!=""]

  final_open = []
  final_closed = []
  answers_closed = []
  answers_open = []
  
  for question in open:
    var = check_question(co, question)
    if(var is not None):
      final_open.append(question)
      answers_open.append(var)

  index = 0
  while(index<len(closed) - 1):
    if(check_question(co, closed[index])):
      final_closed.append(closed[index])
      answers_closed.append(closed[index+1])
    index += 2
  return final_open, final_closed, answers_closed, answers_open

def split_execution(co, whole_text):
  n = 1000
  i = 0
  whole_text = whole_text.split(" ")
  openEndedQuestionsList = []
  multipleChoiceQuestionsList = []
  summaryList = []

  
  print(str(len(whole_text)) + "whole text char count")
  while i*n < len(whole_text):
    print(str(i) + " value of i at the beginning of the loop")
    if(len(whole_text) - i*n < 400):
      print("breaking, less than 400 words left")
      break
    

    text = " ".join(whole_text[i*n:(i+1)*n])
    openEndedQuestions, multipleChoiceQuestions = generate_questions(co, text)
    summaryList.extend(summarize_text(co, text))

    openEndedQuestionsList.append(openEndedQuestions)
    multipleChoiceQuestionsList.append(multipleChoiceQuestions)

    print(str(len(summaryList)) + " len of summary list")
    i += 1
  return openEndedQuestionsList, multipleChoiceQuestionsList, summaryList


