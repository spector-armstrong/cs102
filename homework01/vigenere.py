def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    a = 0
    while len(plaintext) > len(keyword):
        keyword += keyword[a]
        a += 1
    for i, _ in enumerate(keyword):
        if keyword[i].isupper():
            key = ord(keyword[i]) - 65
        elif keyword[i].islower():
            key = ord(keyword[i]) - 97
        if plaintext[i].isalpha():
            b = ord(plaintext[i])
            if plaintext[i].isupper() and b >= 91 - key:
                ciphertext += chr(b - 26 + key)
            elif plaintext[i].islower() and b >= 123 - key:
                ciphertext += chr(b - 26 + key)
            else:
                ciphertext += chr(b + key)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    a = 0
    while len(ciphertext) > len(keyword):
        keyword += keyword[a]
        a += 1
    for i, _ in enumerate(keyword):
        if keyword[i].isupper():
            key = ord(keyword[i]) - 65
        elif keyword[i].islower():
            key = ord(keyword[i]) - 97
        if ciphertext[i].isalpha():
            b = ord(ciphertext[i])
            if ciphertext[i].isupper() and b <= 64 + key:
                plaintext += chr(b + 26 - key)
            elif ciphertext[i].islower() and b <= 96 + key:
                plaintext += chr(b + 26 - key)
            else:
                plaintext += chr(b - key)
        else:
            plaintext += ciphertext[i]
    return plaintext