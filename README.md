# ogrzewanie_podlogowe

> **Status:** Prototyp kalkulatora inżynierskiego.

## Cel i rzeczywista zawartość

Repozytorium modeluje parametry wodnego ogrzewania podłogowego dla pomieszczenia. Dane wejściowe obejmują straty ciepła, warstwy podłogi i jastrychu, geometrię rur oraz temperatury czynnika; klasa obliczeniowa generuje podsumowanie instalacji.

## Zakres potwierdzony w repozytorium

- model i równania w `equations.py`
- kompletny przykład parametrów pomieszczenia w `main.py`
- wielkości opisane jednostkami i komentarzami dziedzinowymi

## Gdzie leży wartość merytoryczna

- przeniesienie zestawu obliczeń instalacyjnych do kodu umożliwia szybkie wariantowanie parametrów
- może służyć jako zalążek audytowalnego kalkulatora projektowego lub materiał dydaktyczny

## Ograniczenia rzetelnej oceny

- brak wskazania normy lub publikacji będącej źródłem równań i współczynników
- brak testów z przypadkami referencyjnymi oraz analizy zakresu ważności modelu
- wyników nie należy traktować jako projektu wykonawczego bez weryfikacji przez uprawnionego specjalistę

## Jak zweryfikować wartość projektu

- porównać co najmniej kilka przypadków z niezależnym kalkulatorem lub przykładem normowym
- dodać testy jednostek, granicznych temperatur i niepoprawnych danych wejściowych
- wartość oceniać po zgodności fizycznej i przejrzystości założeń

## Uwagi

Opis sporządzono na podstawie plików obecnych na domyślnej gałęzi repozytorium. Nie zakłada on funkcji, wyników ani gotowości produkcyjnej, których nie da się potwierdzić z zawartości.

Obecność kodu lub danych nie oznacza automatycznie gotowości produkcyjnej, poprawności naukowej ani prawa do redystrybucji materiałów zewnętrznych. Licencję i pochodzenie danych należy oceniać na podstawie odpowiednich plików źródłowych oraz warunków ich dostawców.
