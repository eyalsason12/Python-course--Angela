from cipher_art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            if shift_amount > 26:
                n_amount_of_shifts = shift_amount % 26
                position = alphabet.index(char)
                new_position = position + n_amount_of_shifts
                end_text += alphabet[new_position]
            else:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text} \n ")


continue_code = True
while continue_code:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    user_answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if user_answer == "no":
        continue_code = False
        print("goodbye")
