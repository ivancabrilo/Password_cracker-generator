import random
import string
import time

the_code_is_on = True

while the_code_is_on:
    purpose = input("Press C to crack a password and G to generate a password or E to exit the program: \n").lower()

    #This part of the code is used to crack a password
    if purpose == "c":
        def guesser():
            possible_characters = string.ascii_letters + string.digits + string.punctuation
            target = input(">>> Enter your target text: ")
            print()
            target.lower()
            start = time.time()
            attempt_this = ''.join(random.choice(possible_characters) for i in range(len(target)))
            completed = False
            generation = 0

            while not completed:
                print(">>>> ", attempt_this, " <<<<")
                attempt_next = ""
                completed = True
                for i in range(len(target)):
                    if attempt_this[i] != target[i]:
                        completed = False
                        attempt_next += random.choice(possible_characters)
                    else:
                        attempt_next += target[i]
                generation += 1
                attempt_this = attempt_next

            end = time.time()
            print(f"\n- {target} took {generation:d} generation(s) and {end - start:.3f} seconds.")


        guesser()

    elif purpose == "g":
        #This part of the code is used to generate a secure password
        import random
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password = []

        print("Welcome to the PyPassword Generator!")
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        for ina in range(1, nr_letters + 1):
            password += random.choice(letters)


        for symbol in range(1, nr_symbols+1):
            random_symbol = random.choice(symbols)
            password.append(random_symbol)


        for num in range(1, nr_numbers +1):
            random_nu = random.choice(numbers)
            password.append(random_nu)
        print(password)
        random.shuffle(password)
        sifra = ""
        for i in password:
            sifra += i

        print(f'Your password is {sifra}')

    elif purpose == "e":
        the_code_is_on = False



