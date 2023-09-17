

quiz_md = """
# Quiz!
Let's review the topics that you have recently learned.

<|{data}|table|columns={columns[0]}|>
<|layout|columns=1 2|
<|
### Answer here!
Select which question to answer

<|{questionNum}|number|>

Enter your answer: 

<|{essayAnswer}|input|multiline=True|>

<|Submit!|button|class_name="custom-btn btn-14"|on_action=submitQuiz|>
|>
<|
<|Personalized Notes|expandable|expanded=false|
<|{lastNotes}|text|>
|>
|>
|>

"""
