import sys

def transform_line(line, left_arg, right_arg):
    """Transform the input line based on left_arg and right_arg."""
    if left_arg == "a-z":
        if right_arg == "A-Z":
            return line.upper()
        else:
            return ''.join(
                right_arg if letter.islower() else letter
                for letter in line
            )
    elif left_arg == "A-Z":
        if right_arg == "a-z":
            return line.lower()
        else:
            return ''.join(
                right_arg if letter.isupper() else letter
                for letter in line
            )
    else:
        # Perform literal replacement if no special ranges are matched
        return line.replace(left_arg, right_arg)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py letter1 letter2")
        sys.exit(1)

    left_arg = sys.argv[1]
    right_arg = sys.argv[2]

    while True:
        try:
            line = input()
            print(transform_line(line, left_arg, right_arg))
        except EOFError:
            break  # Exit loop when EOF is reached (e.g., Ctrl+D in terminal)

if __name__ == "__main__":
    main()
