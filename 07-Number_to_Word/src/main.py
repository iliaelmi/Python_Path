from constans import above_100, tens, under_20

def num_to_word(num):
    if num == 0:
        return "Zero"

    if num < 0:
        return "Minus " + num_to_word(abs(num))

    if num < 20:
        return under_20[num]

    if num < 100:
        remainder = num % 10
        if remainder == 0:
            return tens[num // 10]
        return tens[num // 10] + "-" + under_20[remainder]

    pivot = max(k for k in above_100 if k <= num)
    p1 = num_to_word(num // pivot)
    p2 = above_100[pivot]

    if num % pivot == 0:
        return f"{p1} {p2}"

    return f"{p1} {p2} {num_to_word(num % pivot)}"


def menu():
    print("=" * 40)
    print(" Number to Words Converter ")
    print("=" * 40)
    print("1. Convert a number")
    print("2. Exit")
    print()


def run():
    while True:
        menu()
        choice = input("Choose an option (1/2): ").strip()

        if choice == "1":
            user_input = input("Enter a number: ").strip()

            try:
                number = int(user_input)
                result = num_to_word(number)
                print("\nResult:", result)
            except ValueError:
                print("❌ Please enter a valid integer.")

            input("\nPress Enter to continue...")

        elif choice == "2":
            print("Goodbye 👋")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == '__main__':
    run()
