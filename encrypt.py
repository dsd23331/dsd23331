def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  # Non-alphabetic characters are not changed
    return encrypted_message

def decrypt(encrypted_message, shift):
    return encrypt(encrypted_message, -shift)  # Decrypting is just encrypting with a negative shift

if __name__ == "__main__":
    shift = 3  # You can change the shift value
    original_message = "Hello, World!"
    print(f"Original Message: {original_message}")

    encrypted = encrypt(original_message, shift)
    print(f"Encrypted Message: {encrypted}")

    decrypted = decrypt(encrypted, shift)
    print(f"Decrypted Message: {decrypted}")
