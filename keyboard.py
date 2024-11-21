from convert import str_to_float

def gather_numbers() -> list[float]:
    numbers = []

    while True:
        user_input = input("Put numbers and finish with done").strip()

        if user_input.lower() == "done":
            break
        num = str_to_float(user_input)
        if num is not None:
            numbers.append(num)
    return numbers

if __name__ == "__main__":
    numbers = gather_numbers()
    total = sum(numbers)
    print(f"sum of numbers is {total}")
