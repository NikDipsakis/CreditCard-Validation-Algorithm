def is_valid_credit_card(card_number):
    # Αφαίρεση κενών/παυλών
    card_number = card_number.replace(" ", "").replace("-", "")

    # Έλεγχος μη επιτρεπτών χαρακτήρων
    if not card_number.isdigit():
        invalid_char = next((char for char in card_number if not char.isdigit()), None)
        if invalid_char:
            print(f"Μη επιτρεπτός χαρακτήρας: {invalid_char}")
            return False

    # Τα ψηφία να είναι 16
    if len(card_number) != 16:
        print("Ο αριθμός πρέπει να έχει 16 ψηφία.")
        return False

    # Ελέγχος εγκυρότητας
    checksum = 0
    for i in range(len(card_number)):
        digit = int(card_number[i])
        if i % 2 == 0:
            doubled_digit = digit * 2
            if doubled_digit > 9:
                doubled_digit -= 9
            checksum += doubled_digit
        else:
            checksum += digit

    if checksum % 10 == 0:
        formatted_card_number = "-".join(
            [card_number[i : i + 4] for i in range(0, 16, 4)]
        )
        print(f"Ο αριθμός {formatted_card_number} είναι ΕΓΚΥΡΟΣ.")
        return True
    else:
        formatted_card_number = "-".join(
            [card_number[i : i + 4] for i in range(0, 16, 4)]
        )
        print(f"Ο αριθμός {formatted_card_number} είναι ΑΚΥΡΟΣ.")
        return False


while True:
    card_number = input("Πληκτρολογήστε τον αριθμό της κάρτας: ")
    if is_valid_credit_card(card_number):
        break
