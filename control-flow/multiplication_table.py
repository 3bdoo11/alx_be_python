# File: control-flow/multiplication_table.py

def main():
    try:
        number = int(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

if __name__ == "__main__":
    main()
