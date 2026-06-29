from results import save_result
from config import MONEY_LEVELS
from game import ask_question
from questions import load_questions
from utils import format_amount


def main():
    print("Ładowanie pytań z Open Trivia Database API...")

    try:
        questions = load_questions(len(MONEY_LEVELS))
    except Exception as error:
        print("Nie udało się pobrać pytań z API.")
        print(f"Szczegóły błędu: {error}")
        return

    current_money = 0

    lifelines = {
        "50": True,
        "audience": True,
        "phone": True
    }

    for index, question in enumerate(questions):
        if index >= len(MONEY_LEVELS):
            break

        print(f"\nPytanie za {format_amount(MONEY_LEVELS[index])} zł")

        is_correct = ask_question(question, lifelines)

        if not is_correct:
            print(f"Koniec gry. Wygrywasz: {format_amount(current_money)} zł")
            save_result(current_money)
            break

        current_money = MONEY_LEVELS[index]
        print(f"Aktualna wygrana: {format_amount(current_money)} zł")

    else:
        print("Gratulacje! Wygrałeś milion złotych!")
        save_result(current_money)


if __name__ == "__main__":
    main()