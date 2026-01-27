```text
3, 10 def print_prosa():
4, 11     print("Melding til alle gaardeiere:")
5, 12     print("Antall dyr paa gaarden: ")

1 antall_dyr = 4
2 print_prosa()
6 print(antall_dyr)
7 antall_nye_dyr = int(input("Hvor mange nye dyr kommer til gaarden:"))
8 antall_dyr = antall_dyr + antall_nye_dyr
9 print_prosa()
13 print(antall_dyr)

14 if antall_dyr > 12:
    print("Det er mer enn ett dusin dyr paa gaarden!")
15 elif antall_dyr == 12:
16     print("Det er ett dusin dyr paa gaarden!")
else:
    print("Det er mindre enn ett dusin dyr paa gaarden!")
```
