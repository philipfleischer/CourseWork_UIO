# vannmengde - input - sjekk at det er et tall
# meny - A for lag kaffe, B for fyll på vann

# Klasser
# ActionList som lister opp alternativer, lar bruker velge og returnerer valget

class ActionList:
    def __init__(self, choices):
        self._choices = dict(choices)

    def _list_options(self):
        for key in self._choices:
            choice_text = self._choices[key]
            print(f"Trykk {key} for å {choice_text}")
        print()

    def _check_input(self, user_input):
        return user_input.upper() in self._choices

    def get_input(self):
        self._list_options()
        input_OK = False
        while not input_OK:
            user_input = input("Skriv inn ditt valg her: ").upper()
            input_OK = self._check_input(user_input)
            if not input_OK:
                print()
                print("Ugyldig valg - velg et gyldig alternativ.")
            else:
                return user_input


class Kaffemaskin:
    def __init__(self, kapasitet):
        self._kapasitet = kapasitet
        self._vann = self._kapasitet

    def lag(self, vann_som_trengs):
        if self._vann >= vann_som_trengs:
            self._vann -= vann_som_trengs
            return True
        else:
            return False

    def fyll_på(self):
        user_input = int(input("Hvor mye vann vil du fylle på: "))
        if self._vann + user_input > self._kapasitet:
            print("Oversømmelse!")
            self._vann = self._kapasitet
        else:
            self._vann += user_input

def main():
    kaffelars = Kaffemaskin(10)

    avslutt = False
    while not avslutt:
        al = ActionList({
            "A": "lage kaffe",
            "B": "fylle på vann",
            "C": "avslutte"
        })

        svar = al.get_input()
        if svar == "A":
            al2 = ActionList({
                "E": "lage espresso",
                "O": "lage kaffekopp",
                "A": "lage kaffekanne",
            })
            svar2 = al2.get_input()
            if svar2 == "E":
                ok = kaffelars.lag(1)
            elif svar2 == "O":
                ok = kaffelars.lag(3)
            else:
                ok = kaffelars.lag(9)
            if ok:
                print(f"Lagde {svar2}")
            else:
                print("Tomt for vann!")
        elif svar == "B":
            ok = kaffelars.fyll_på()
        else: # "C"
            avslutt = True

if __name__ == "__main__":
    main()
