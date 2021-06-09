# monitorowanie-czasu
program monitorujący ilość czasu spędzonego w budynku przez osobę w ciągu dnia


## Założenia

* program domyślnie pobiera jako źródło danych "input.csv"
* struktura pliku wejściowego
	* 'Date' zawiera datę w formacie: yyyy-mm-dd hh:mm:ss
	* 'Event' zawiera informację o rodzaju zdarzenia czy czujnik znajdował się w biurze, czy poza biurem
	* 'Gate' zawiera informację na temat identyfikatora drzwi
* wynikiem programu jest plik result zawierający informacje:
	* ilość godzin spędzonych w biurze w danym dniu
	* literę 'w' (weekend) jeżeli dzień był weekendem
	* litery 'ot' (overtime) jeżeli ktoś spędził w biurze więcej niż 9h
	* litery 'ut' ('undertime') jeżeli ktoś spędził w biurze mniej niż 6h
	* 'i' (inconclusive) jeżeli obliczony czas pracy jest niejednoznaczny
	* każdy ostatni dzień tygodnia (w biurze) dodatkowo zawiera sumę wszystkich godzin spędzonych w tygodniu w biurze, oraz czas nadgodzin w formacie hh:mm:ss, bądź czas niedomiaru godzin spędzonych w tygodniu w biurze w formie -hh:mm:ss
	* domyślny czas pracy dla jednego roboczego dnia to 8h