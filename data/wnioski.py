tab1 = """
# Spostrzeżenia:

* Z powyższa heatmapa wskazuje na niską korelację liczby opóźnionych lotów Lotniska Daniel K Inouye International Airport(HNL). Możliwe wytłumaczenie: duża odległość od innych lotnisk.
* Zauważmy istnienie grup skorelowanych lotnisk
* Jedne z najbardziej skorelowanych lotnisk to Orlando International Airport(MCO) oraz Tampa International Airport(TPA)
* Wykres szeregów czasowych potwierdza istnienie zależności pomiędzy lotniskami - pokrywanie się pików
* Z wykresów można estymować reakcje innych lotnisk na problemy na innych lotniskach.
* How: Dane powstały na posdstawie agregacji po dacie oraz lotnisku gdzie zliczne były loty opóźnione powyżej 15 min. Aby przyspieszyć generacje wykresów każde lotnisko miało oddzielną kolumnę przechowywującą liczbe opóźnionych lotów danego dnia. Do obliczenia korelacji użyto  pandas.DataFrame.corr z metodą Pearson.

"""

tab2 = """
# Spostrzeżenia:

* Jednym z najbardziej opóźnionych lotnisk jest Chicago O'Hare International Airport (ORD).
* Wykres wcale nie wskazuje zależności pomiędzy odległością bądź kierunkiem a a opoźnieniami
* How: Poagregowano dane względem roku oraz lotniska odlotu i lotniska przylotu samolotu, zliczając liczbę lotów, liczbę lotów opóźnionych, średnie opóźnienia. Wyniki przedstawiono na mapie. 

"""

tab3 = """
# Spostrzeżenia:

* Z wykresu godzin odlotów wynika że największe opóźnienia **pomiędzy 16 a 20**.
* Z wykresu liczby lotów w zależności od godzin widać że w dużym przedziale czasowym liczba wylotów jest stałą
* Wzrost opóźnień jest w przybliżeniu liniowy a liczba lotów stałą -> te obciązenie generuje stały przyrost opóźnienia
* Najlepsze dni do latania to **Sobota** i **Czwartek**
* Najgorszy dnień do latania to **Piątek**
* Z ostatniego wykresu możemy zaobserwować skok opóźneiń wywołanym zamachem z 11 września 2001
* Widzimy również że liczby lotów i opóźnienia są periodyczne w kolejnych latach
* How: Dane powstały na podstawie agregacji planowanych czasów wylotów po odpowiednio godzinach, dniach tygodnia oraz dniach w roku z uwzglednieniem przewoźnika.

"""

tab4 = """
# Spostrzeżenia:

* Boeing miał większe opóźnienia niż Embraer do roku 2006. Następnie nastąpiła zmina.
* Jeszcze większą różnicę widać na przykładzie najczęściej ekspoatowanych modelów tych firm
* W roku 2004 i 2007 wzrosła gwałtownie liczba lotów Boeingiem
* Na podstawie wykresu można estymować datę wprowadzenia modlu np: AIRBUS A321-211 w roku 2007
* Gwałtowny spadek lotów liczby lotów Embraera może być skutkiem kryzysu ekonomicznego - zamykanie mniej uczęszczanych połączeń(Embraer produkuje średniej wielkości samoloty)
* Na postawie numerów ogonów samolotów zostały dopasowane do nich model i producent na podstawie danych zescrapowanych z internetu. Następnie została wykonana agregacja po producentach i modelach licząca liczbę lotów, średnie opóźnienie wylotu i procent opóźnionych.
* Przykład danych: [http://registry.faa.gov/aircraftinquiry/NNum_Results.aspx?NNumbertxt=N212UA](http://registry.faa.gov/aircraftinquiry/NNum_Results.aspx?NNumbertxt=N212UA)

"""
