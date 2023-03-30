age = int(input("Alter des Hundes: "))

if age <= 0:
    print("Das kann wohl nicht stimmen!")
elif age == 1:
    print("Das entspricht 14 Menschenjahren!")
elif age == 2:
    print("Das entspricht 22 Menschenjahren!")
elif age > 2:
    human = 22 + (age -2)*5
    print("Das entspricht " + str(human) + " Menschenjahren!")
