import sys


def delete_char(line , right_arg):

    def ccdel(function):
        return ''.join(
            '' if getattr(letter, function)() else letter
            for letter in line 
        )
    
    match right_arg:
        case "A-Z"|"[:upper:]":
            return ccdel("isupper")
        case "a-z"|"[:lower:]":
            return ccdel("islower")
        case "[:alnum:]":
            return ccdel("isalphanum")
        
        case "[:alpha:]":
            return ccdel("isalpha")

        case "[:digit:]":    
            return ccdel("isdigit")
        case _:
            constructed_line =""
            chars_to_delete = list(right_arg)
            for letter in line:
                if not(letter in chars_to_delete):
                    constructed_line += letter
            return constructed_line
            

def transform_line(line, left_arg, right_arg):

    """Transform the input line based on left_arg and right_arg."""
    
    if( right_arg=="[:alpha:]" or right_arg=="[:alnum:]" or right_arg=="[:digit:]" ):
        return  "tr: when translating, the only character classes that may appear in string2 are 'upper' and 'lower'"

    if( (left_arg=="[:alpha:]" or left_arg=="[:alnum:]" or left_arg=="[:digit:]" ) and (right_arg == "[lower]" or right_arg == "[:upper:]")
       or right_arg =="a-z" or right_arg == "A-Z"):
        return "tr: misaligned [:upper:] and/or [:lower:] construct"

    def cctr(function):
        return ''.join(
            right_arg if getattr(letter, function)() else letter
            for letter in line 
        )

    
    match left_arg:
        case "a-z"|"[:lower:]":
            if right_arg == "A-Z" or right_arg == "[:upper:]":
                return line.upper()
            else:
                return cctr("islower")
            
        case "A-Z"|"[:upper:]":
            if right_arg == "a-z" or right_arg == "[:lower:]":
                return line.lower()
            else:
                return cctr("isupper")
            
        case "[:alnum:]":
            return cctr("isalphanum")
        
        case "[:alpha:]":
            return cctr("isalpha")

        case "[:digit:]":    
            return cctr("isdigit")
        case _:
            return line.replace(left_arg,right_arg)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py letter1 letter2")
        sys.exit(1)

    left_arg = sys.argv[1]
    right_arg = sys.argv[2]

    while True:
        try:
            line = input()

            #if we have a flag for deletion : -d we do this 
            if(left_arg =="-d"):
                print(delete_char(line,right_arg))
            else:
            
                print(transform_line(line, left_arg, right_arg))
        except EOFError:
            break  # Exit loop when EOF is reached (e.g., Ctrl+D in terminal)

if __name__ == "__main__":
    main()
