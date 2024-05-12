import json
from surveys.models import SurveyQuestion

with open('scripts/questions.json', 'r') as file:
    questions_data = json.load(file)
    
for question_data in questions_data:
    question = SurveyQuestion(
        statement=question_data["statement"],
        asociated_risk=question_data["asociated_risk"],
        type_question=question_data["type_question"],
        question_config=question_data["question_config"]
    )
    question.save()  

print("Preguntas creadas exitosamente.")
