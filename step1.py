import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py letter1 letter2")
        sys.exit(1)

    letter1 = sys.argv[1]
    letter2 = sys.argv[2]

    while True:
        try:
            line = input()
            # Replace all occurrences of letter1 with letter2
            translated_line = line.replace(letter1, letter2)
            print(translated_line)
        except EOFError:
            break  # Exit loop when EOF is reached (e.g., Ctrl+D in terminal)

if __name__ == "__main__":
    main()
