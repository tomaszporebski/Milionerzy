# Milionerzy — projekt w Pythonie

## Opis projektu

Projekt jest prostą konsolową wersją gry „Milionerzy” napisaną w Pythonie.

Gracz odpowiada na pytania jednokrotnego wyboru. Każde pytanie ma cztery odpowiedzi: A, B, C i D. Za poprawną odpowiedź gracz przechodzi do kolejnego pytania i zdobywa wyższą kwotę. Po błędnej odpowiedzi gra się kończy, a wynik zostaje zapisany do pliku.

W aktualnej wersji pytania są pobierane z zewnętrznego API Open Trivia Database.

## Funkcjonalności

* gra działa w konsoli,
* pytania są pobierane z zewnętrznego API,
* każde pytanie ma cztery odpowiedzi,
* tylko jedna odpowiedź jest poprawna,
* gra posiada progi wygranej,
* dostępne są trzy koła ratunkowe:

  * 50/50,
  * pytanie do publiczności,
  * telefon do przyjaciela,
* wynik gry jest zapisywany do pliku JSON,
* projekt zawiera podstawowe testy jednostkowe.

## Zewnętrzne API

Projekt korzysta z Open Trivia Database API:

```text
https://opentdb.com/
```

API służy do pobierania pytań quizowych. W projekcie pobierane są pytania typu `multiple`, czyli pytania z czterema odpowiedziami.

Przykładowy adres zapytania:

```text
https://opentdb.com/api.php?amount=12&type=multiple
```

Znaczenie parametrów:

* `amount=12` — pobranie 12 pytań,
* `type=multiple` — pobranie pytań z czterema odpowiedziami.

Dane zwracane przez API są przekształcane na format używany w grze:

```python
{
    "question": "Treść pytania",
    "answers": ["Odpowiedź A", "Odpowiedź B", "Odpowiedź C", "Odpowiedź D"],
    "correct": 2
}
```

Pole `correct` oznacza indeks poprawnej odpowiedzi w liście `answers`.

## Koła ratunkowe

W grze dostępne są trzy koła ratunkowe.

### 50/50

Usuwa dwie błędne odpowiedzi i zostawia jedną poprawną oraz jedną błędną.

Komenda w grze:

```text
50
```

### Pytanie do publiczności

Pokazuje procentowe głosy publiczności dla każdej odpowiedzi.

Komenda w grze:

```text
P
```

### Telefon do przyjaciela

Wyświetla sugestię poprawnej odpowiedzi.

Komenda w grze:

```text
T
```

Każde koło ratunkowe można wykorzystać tylko raz w trakcie gry.

## Struktura projektu

```text
Milionerzy/
├── main.py
├── game.py
├── questions.py
├── lifelines.py
├── results.py
├── config.py
├── utils.py
├── data/
│   └── results.json
├── tests/
│   ├── test_utils.py
│   ├── test_lifelines.py
│   └── test_questions.py
└── README.md
```

Krótki opis najważniejszych plików:

* `main.py` — uruchamia grę i obsługuje główny przebieg programu,
* `game.py` — odpowiada za zadawanie pytań i sprawdzanie odpowiedzi,
* `questions.py` — pobiera pytania z API i przygotowuje je do użycia w grze,
* `lifelines.py` — zawiera logikę kół ratunkowych,
* `results.py` — zapisuje wynik gry do pliku,
* `config.py` — przechowuje progi wygranej,
* `utils.py` — zawiera funkcje pomocnicze,
* `tests/` — zawiera testy jednostkowe.

## Uruchomienie projektu

Do uruchomienia projektu potrzebny jest Python 3.

Po pobraniu repozytorium należy przejść do folderu projektu i uruchomić:

```bash
python main.py
```

Na Windowsie można też użyć:

```bash
py main.py
```

Po uruchomieniu program pobiera pytania z API i rozpoczyna grę w konsoli.

## Sterowanie w grze

Po wyświetleniu pytania należy wpisać jedną z odpowiedzi:

```text
A
B
C
D
```

Można też użyć koła ratunkowego:

```text
50  - koło 50/50
P   - pytanie do publiczności
T   - telefon do przyjaciela
```

## Testy

Projekt zawiera podstawowe testy jednostkowe napisane przy użyciu biblioteki `pytest`.

Testy sprawdzają między innymi:

* formatowanie kwot,
* działanie koła 50/50,
* działanie pytania do publiczności,
* przekształcanie pytania z API do formatu używanego w grze.

Instalacja pytest:

```bash
python -m pip install pytest
```

Uruchomienie testów:

```bash
python -m pytest
```

Przykładowy poprawny wynik:

```text
6 passed
```

## Wykorzystane elementy Pythona

W projekcie zostały wykorzystane między innymi:

* funkcje,
* listy i słowniki,
* pętle,
* instrukcje warunkowe,
* obsługa plików JSON,
* pobieranie danych z internetu,
* losowanie,
* testy jednostkowe.

## Cel projektu

Celem projektu było przygotowanie prostej gry w Pythonie, która jest podzielona na kilka plików, korzysta z zewnętrznego API i posiada podstawowe testy.

Projekt został napisany w możliwie prosty sposób, tak aby można było dokładnie wyjaśnić działanie poszczególnych plików i funkcji.
