from lifelines import fifty_fifty, audience_help


def test_fifty_fifty_leaves_two_answers():
    question = {
        "question": "Testowe pytanie",
        "answers": ["A", "B", "C", "D"],
        "correct": 1
    }

    result = fifty_fifty(question)

    assert len(result) == 2


def test_fifty_fifty_keeps_correct_answer():
    question = {
        "question": "Testowe pytanie",
        "answers": ["A", "B", "C", "D"],
        "correct": 1
    }

    result = fifty_fifty(question)

    assert 1 in result


def test_audience_help_percentages_sum_to_100():
    question = {
        "question": "Testowe pytanie",
        "answers": ["A", "B", "C", "D"],
        "correct": 2
    }

    result = audience_help(question)

    assert sum(result.values()) == 100