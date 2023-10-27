alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'    
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'    
            'w', 'x', 'y', 'z']
def ceasr(start_text, shift_number, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_number *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(end_text)

should_end = False
while not should_end:
    direction = input("type 'encode' to encrypt, and type 'decode' to 'decrypt': \n")
    text = input("type message here: \n").lower()
    shift = int(input("type the shift number: \n"))

    shift = shift % 26

    ceasr(text, shift, direction)

    restart = input("type 'yes' if you want to go again, otherwise type 'no'\n")
    if restart == 'no':
        should_end = True
        print("Good Bye")

