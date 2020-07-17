valores = [
    "Wearing elegant clothing",
    "As a model",
    "As a ninja",
    "Wearing pijama",
    "At school",
    "At the 80's",
    "At the swimming pool",
    "Gender toggle/change",
    "Sleeping",
    "Chibi",
    "As a kid",
    "As a bussiness man/woman",
    "As a cashier in any place",
    "As an animal (any)",
    "At a party",
    "Chibi",
    "As a super hero",
    "As a secret agent"
    "As a villian",
    "Hurt/beaten up",
    "As ghost buster",
    "Wearing winter clothing",
    "On a date",
    "At the middle age era",
    "As a bounty hunter",
    "As an elderly person",
    "As a soldier",
    "As Pokemon Trainer",
    "As a wizard/witch",
    "As a hacker",
    "As a neighborhood teenager"
]

numeros = [
    "1",
    "15",
    "2",
    "16",
    "3",
    "17",
    "4",
    "19",
    "5",
    "20",
    "6",
    "21",
    "7",
    "22",
    "8",
    "23",
    "9",
    "24",
    "10",
    "25",
    "11",
    "26",
    "12",
    "27",
    "13",
    "28",
    "14",
    "29",
    "15",
    "30"
]

print(len(valores))
print(len(numeros))
counter = 0

for x in valores:
    print('<div class="variante">')
    print(numeros[counter] + ".- " + x)
    print('</div>')
    counter = counter + 1
    
    