import sys

def main():
    total = 0.0
    for arg in sys.argv[1:]:
        try:
            total += float(arg)
        except ValueError:
            print(f"{arg} not valid, skip")
    print(f"Total sum is {total}")

if __name__ == "__main__":
    main()

