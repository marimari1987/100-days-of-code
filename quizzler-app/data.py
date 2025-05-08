import requests

parameters = {"amount": 10,
              "type": "boolean"}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
# {
#   "response_code": 0,
#   "results": [
#     {
#       "category": "Geography",
#       "type": "boolean",
#       "difficulty": "medium",
#       "question": "The Southeast Asian island of Borneo is politically divided among 3 countries.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "category": "Entertainment: Video Games",
response.raise_for_status()
question_data = response.json()["results"]
