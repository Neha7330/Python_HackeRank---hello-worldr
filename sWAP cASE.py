def swap_case(s):
    output_string = ""
    for letter in s:
        if letter.isupper():
            output_string += letter.lower()
        elif letter.islower():
            output_string += letter.upper()
        else:
            output_string += letter
    return output_string

if __name__ == '__main__':
