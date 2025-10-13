#Laget variabelen "jaNei"
jaNei = input("Kan du tenke deg en brus?  ")
#Under er det en if-test, der det blir printet ut forskjellige svar avhengige av hva brukeren svarer
if jaNei == "ja":
    print("Her har du en brus")
elif jaNei == "nei":
    print("Den er grei")
else:
    print("Det forstod jeg ikke helt")
