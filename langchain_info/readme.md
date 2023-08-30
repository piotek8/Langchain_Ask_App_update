# Langchain - co to? po co? do czego to komus potrzebne?

Cześć, Postaram się zaprezentować wiedzę stricte czym jest, po co to komu i jak ułatwi nam zrozumienie świata AI - a dokładniej pokaże freamwork Langchain. Oczywiście należy brać wszystko z "przymrużeniem oka", bo póki co ani ze mnie specjalista, ani też gość z dużym zapleczem wiedzy w tej dziedzinie. 

### Langchain 

Hmmmm. Możemy przeczytać, że jest to biblioteka, która została stworzona do tworzernia aplikacji z użyciem modeli językowych. Co to znaczy?
Mianowicie mamy zestaw poszczególnych funkcjonalności, narzędzi w jednym miejscu za pomocą których jesteśmy w stanie stworzyć program, łączac się z innymi źródłami informacji - jakbyśmy mieli przed sobą duużo książek. Do tego nasz program poza liczną wiedzą, próbuje myśleć( bądź zgadywać, tak wspominał Olaf w swoim artykule ) i odpowiadać na nasze pytania.
 
Kilka przydatnych pojęć, które musimy znać podczas korzystania:

LLM (Large Language Model) - to taka sztuczna inteligencja, stworzona, żeby zrozumieć i generować ludzki język. Jest oparta i wytrenowana na licznych ilościach tekstowych danych ( z książek, pdf, internetu, artykułów, blogów, gazet itd.), żeby nasz model mógł stworzyć odpowiedź na zadane pytanie.  Niemniej jednak model jest omylny i istnieje kilka powodów, dlaczego jego odpowiedzi nie zawsze są prawdziwe: ograniczona wiedza, błędna interpretacja, niedostateczne dane czy bycie generatywnym ( tworzenie tekstu, który jest "prawdopodobny", ale nie dokońca prawdziwy )

Vector Databases - to takie bazy danych, w których są zawarte dane w postaci wektorów. Co to daje ? Podam to na praktycznym przykładzie. 
Aby reprezentować cechy kota jako wektor, możemy użyć różnych liczbowych wartości, które odpowiadają jego cechom. Na przykład, sierść biała może być reprezentowana jako liczba 1, a kolor ciemnoniebieski oczu jako liczba 2. Możemy utworzyć wektor [1, 2] dla tego kota, gdzie pierwsza wartość odpowiada kolorowi sierści, a druga wartość odpowiada kolorowi oczu.

Teraz możemy umieścić te informacje w vector database. Vector database to specjalna baza danych, która przechowuje różne wektory reprezentujące dane. W naszym przypadku, możemy utworzyć taką wektorową bazę, w której przechowujemy wektory reprezentujące różne koty, każdy z nich reprezentujący unikalne kombinacje cech koloru sierści i oczu.

Kiedy mamy vector database z wektorowymi reprezentacjami kotów, możemy użyć tego narzędzia do wyszukiwania podobieństw. Na przykład, jeśli chcielibyśmy znaleźć podobnego kota do naszego, wystarczy podać wektor reprezentujący naszego kota jako zapytanie do vector database. Algorytm wyszukiwania podobieństw porówna te wektory i znajdzie kota o najbliższych cechach do tego, który jest wyszukiwany.

### W skrócie:

Vector database używamy do: 
  - dużych modeli językowych z pamięcią długotrwałą
  - wyszukiwań niedokładnych dopasowań ciągów
  - znalezienia podobieństwa tzn. wyszukiwanie tekstu, obrazków, plików audio czy wideo
  - sugerowanie przedmitów podobnych do poprzednich zakupów klienta 

Moduły:

Model I/O: Pozwala na gadanie z modelami językowymi i korzystanie z nich.
Przykład: Aplikacja chatbota, który potrafi odpowiadać na pytania użytkowników na temat historii lub nauki, korzystając z zaawansowanego modelu językowego.
Ciekawym zastosowaniem może być przewodnik w zwiedzanym mieście. Cała grupa zwiedzających mogłaby uzyskiwać inwidualne informację na temat historii, architektury czy też według własnych upodobań.

Data connection: Umożliwia łączenie aplikacji z różnymi danymi, np. z bazą danych czy plikami.
Przykład: Aplikacja do zarządzania zadaniami, która łączy się z bazą danych, aby przechowywać i odczytywać listę zadań użytkowników.

Chains: Pozwalają na budowanie sekwencji kroków, żeby wykonywać bardziej skomplikowane rzeczy.
Przykład: Aplikacja do przetwarzania tekstu, która najpierw dzieli tekst na zdania, następnie analizuje każde zdanie pod kątem kluczowych słów, a potem generuje podsumowanie całego tekstu.

Agents: Pomagają łańcuchom wybierać narzędzia do użycia.
Przykład: Aplikacja rekomendująca filmy, która korzysta z różnych modeli rekomendujących w zależności od preferencji użytkownika, takich jak preferowany gatunek czy oceny wcześniej obejrzanych filmów.

Memory: Pozwala na zachowywanie informacji między różnymi "właśnie włączonymi" seansami.
Przykład: Aplikacja do notatek, która zapamiętuje i przywraca notatki użytkownika między różnymi sesjami, dzięki czemu użytkownik może kontynuować pracę w dowolnym momencie.

Callbacks: Pozwalają na śledzenie, co aplikacja robi i rejestrowanie kroków.
Przykład: Aplikacja do przetwarzania obrazów, która rejestruje każdy krok w procesie analizy obrazu, od jego wczytania do wykrycia różnych elementów na obrazie.

### Kilka dodatkowych funkcjonalności, które można wprowadzić w mojej aplikacji :
[Langchain_Ask_App](https://github.com/th33ngineers/Langchain_Ask_App.git)

  - dockerfile: plik tekstowy, w którym są podane instrukcje ( takie jak: FROM, RUN, COPY, CMD ), żeby zbudować obraz kontenera
  - dockercompose: narzędzie, w którym wykorzystujemy zbudowane obrazy i tworzymy "zapakowany produkt", dzięki czemu inny użytkownik na swoim urządzeniu może pobrać i zbudować aplikację w łatwy sposób.Przejść do scieżki docker-compose.yml i wewnątrz niej wykonać: docker-compose build. 
  - wykorzystać poetry ( taki virtualenv z pipem na sterydach ), a dzięki niemu stworzyć plik pyproject.toml - tutaj requirements.txt na sterydach z rozbudowanymi konfiguracjami oraz dodać plik makefile.





