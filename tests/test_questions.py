from questions import convert_api_question


def test_convert_api_question_returns_game_format():
    api_question = {
        "question": "What is 2 + 2?",
        "correct_answer": "4",
        "incorrect_answers": ["1", "2", "3"]
    }

    result = convert_api_question(api_question)

    assert result["question"] == "What is 2 + 2?"
    assert len(result["answers"]) == 4
    assert "4" in result["answers"]
    assert result["answers"][result["correct"]] == "4"