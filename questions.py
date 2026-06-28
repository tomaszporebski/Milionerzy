import html
import json
import random
from urllib.parse import urlencode
from urllib.request import urlopen


API_URL = "https://opentdb.com/api.php"


def convert_api_question(api_question: dict) -> dict:
    question_text = html.unescape(api_question["question"])
    correct_answer = html.unescape(api_question["correct_answer"])

    incorrect_answers = [
        html.unescape(answer)
        for answer in api_question["incorrect_answers"]
    ]

    answers = incorrect_answers + [correct_answer]
    random.shuffle(answers)

    correct_index = answers.index(correct_answer)

    return {
        "question": question_text,
        "answers": answers,
        "correct": correct_index
    }


def load_questions(amount: int = 12) -> list:
    query_params = urlencode({
        "amount": amount,
        "type": "multiple"
    })

    url = f"{API_URL}?{query_params}"

    with urlopen(url, timeout=10) as response:
        data = json.load(response)

    if data["response_code"] != 0:
        raise ValueError("Nie udało się pobrać pytań z Open Trivia Database API.")

    questions = [
        convert_api_question(api_question)
        for api_question in data["results"]
    ]

    return questions