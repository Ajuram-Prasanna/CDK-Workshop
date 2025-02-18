

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift_amount) % 26 + 97)
            elif char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift_amount) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)
