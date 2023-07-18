from usd import USD
from ils import ILS

def welcome_screen():
    print("Welcome to currency converter")
    print("Please choose an option (1/2):")
    print("1. Dollars to Shekels")
    print("2. Shekels to Dollars")

def choice_screen():
    while True:
        try:
            amount = float(input("Please enter an amount to convert: "))
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def result_screen(result):
    print("Result: ", result)
    print("--------")

def end_screen(results):
    print("Thanks for using our currency converter")
    print("Previous results:")
    for result in results:
        print(result)
    with open("results.txt", "w") as file:
        for result in results:
            file.write(str(result) + "\n")

def main():
    results = []
    while True:
        welcome_screen()
        choice = input()
        if choice == "1":
            usd = USD()
            amount = choice_screen()
            result = usd.calculate(amount)
            results.append(result)
            result_screen(result)
        elif choice == "2":
            ils = ILS()
            amount = choice_screen()
            result = ils.calculate(amount)
            results.append(result)
            result_screen(result)
        else:
            print("Invalid choice, please try again.")
            continue

        restart = input("Do you want to start over? (Y/N): ")
        if restart.upper() == "N":
            end_screen(results)
            break

if __name__ == "__main__":
    main()
