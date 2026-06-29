<div align="center">

🎮 Milionerzy — Python Console Game

Prosta konsolowa wersja gry „Milionerzy” napisana w języku Python.
Projekt wykorzystuje zewnętrzne API do pobierania pytań quizowych.

<br>







</div>

📌 Spis treści
Opis projektu
Najważniejsze funkcjonalności
Zewnętrzne API
Koła ratunkowe
Struktura projektu
Jak uruchomić projekt
Jak grać
Testy
Technologie
Cel projektu
🧾 Opis projektu

Projekt jest konsolową wersją gry „Milionerzy”.

Gracz odpowiada na pytania jednokrotnego wyboru. Każde pytanie ma cztery możliwe odpowiedzi:

A, B, C, D

Tylko jedna odpowiedź jest poprawna. Za każdą poprawną odpowiedź gracz przechodzi dalej i zdobywa coraz większą kwotę.

Pytania nie są zapisane lokalnie w projekcie. Program pobiera je z zewnętrznego API — Open Trivia Database.

✨ Najważniejsze funkcjonalności
Funkcjonalność	Opis
🎮 Gra konsolowa	Cała rozgrywka odbywa się w terminalu
🌐 Pytania z API	Pytania są pobierane z Open Trivia Database
✅ Jedna poprawna odpowiedź	Każde pytanie ma dokładnie jedną poprawną odpowiedź
💰 Progi wygranej	Gracz zdobywa kolejne kwoty za poprawne odpowiedzi
🛟 Koła ratunkowe	Dostępne są 3 koła ratunkowe
💾 Zapis wyników	Wynik końcowy jest zapisywany do pliku JSON
🧪 Testy	Projekt zawiera proste testy jednostkowe
🌐 Zewnętrzne API

Projekt korzysta z API:

Open Trivia Database
https://opentdb.com/

API służy do pobierania pytań quizowych.

Program pobiera pytania typu:

multiple

czyli pytania z czterema odpowiedziami i jedną poprawną odpowiedzią.

Przykładowy adres API:

https://opentdb.com/api.php?amount=12&type=multiple

Znaczenie parametrów:

Parametr	Znaczenie
amount=12	pobranie 12 pytań
type=multiple	pobranie pytań z czterema odpowiedziami

Po pobraniu danych z API program przekształca pytanie do formatu używanego przez grę:

{
    "question": "Treść pytania",
    "answers": ["Odpowiedź A", "Odpowiedź B", "Odpowiedź C", "Odpowiedź D"],
    "correct": 2
}

Pole correct przechowuje indeks poprawnej odpowiedzi.

Przykład:

"answers": ["Berlin", "Paryż", "Madryt", "Rzym"],
"correct": 1

Oznacza to, że poprawną odpowiedzią jest:

answers[1]

czyli:

Paryż
🛟 Koła ratunkowe

W grze dostępne są trzy koła ratunkowe:

Koło ratunkowe	Komenda	Opis
50/50	50	Usuwa dwie błędne odpowiedzi
Publiczność	P	Pokazuje procentowe głosy publiczności
Telefon do przyjaciela	T	Przyjaciel sugeruje poprawną odpowiedź

Każde koło ratunkowe może zostać użyte tylko raz w trakcie gry.

📁 Struktura projektu
Milionerzy/
├── main.py              # główny plik uruchamiający grę
├── game.py              # logika zadawania pytań i sprawdzania odpowiedzi
├── questions.py         # pobieranie i przygotowanie pytań z API
├── lifelines.py         # obsługa kół ratunkowych
├── results.py           # zapisywanie wyników gry
├── config.py            # konfiguracja progów wygranej
├── utils.py             # funkcje pomocnicze
├── data/
│   └── results.json     # zapisane wyniki graczy
├── tests/
│   ├── test_utils.py
│   ├── test_lifelines.py
│   └── test_questions.py
└── README.md
🚀 Jak uruchomić projekt
1. Pobierz projekt

Można sklonować repozytorium:

git clone https://github.com/tomaszporebski/Milionerzy.git

Następnie przejść do folderu projektu:

cd Milionerzy
2. Uruchom grę
python main.py

Jeżeli na Windowsie komenda python nie działa, można użyć:

py main.py

Po uruchomieniu program pobierze pytania z Open Trivia Database API i rozpocznie grę w konsoli.

🎯 Jak grać

Po wyświetleniu pytania wpisz jedną z odpowiedzi:

A
B
C
D

Przykład:

Pytanie za 500 zł

What is the capital of France?
A. Berlin
B. Paris
C. Madrid
D. Rome

Twoja odpowiedź: B

Możesz też skorzystać z kół ratunkowych:

50  - koło 50/50
P   - pytanie do publiczności
T   - telefon do przyjaciela
🧪 Testy

Projekt zawiera proste testy jednostkowe napisane z użyciem biblioteki pytest.

Testy sprawdzają między innymi:

formatowanie kwot,
działanie koła 50/50,
działanie pytania do publiczności,
przekształcanie pytania z API do formatu używanego przez grę.
Instalacja pytest
python -m pip install pytest
Uruchomienie testów
python -m pytest

Przykładowy poprawny wynik:

6 passed
🧰 Technologie
Technologia	Zastosowanie
Python	główny język projektu
JSON	format danych zwracany przez API i zapis wyników
urllib	pobieranie danych z internetu
random	mieszanie odpowiedzi i losowanie podpowiedzi
html	odkodowanie znaków specjalnych z API
pytest	testy jednostkowe
Git / GitHub	kontrola wersji i udostępnienie projektu
🧠 Cel projektu

Celem projektu było przygotowanie prostej gry w Pythonie, która:

jest podzielona na czytelne moduły,
działa w konsoli,
korzysta z zewnętrznego API,
posiada proste testy jednostkowe,
jest możliwa do omówienia linijka po linijce.

Projekt został przygotowany tak, aby kod był możliwie prosty, czytelny i zrozumiały dla osoby początkującej.

📚 Najważniejsze pliki
Plik	Rola w projekcie
main.py	start programu i główna pętla gry
questions.py	pobieranie pytań z API i konwersja danych
game.py	zadawanie pytań i obsługa odpowiedzi gracza
lifelines.py	logika kół ratunkowych
results.py	zapis wyniku do pliku
config.py	lista progów wygranej
utils.py	funkcje pomocnicze
tests/	testy jednostkowe

<div align="center">

🎉 Projekt zaliczeniowy — Python

</div>