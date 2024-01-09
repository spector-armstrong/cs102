def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i, _ in enumerate(plaintext):
        if plaintext[i].isalpha():
            uc = ord(plaintext[i])
            if plaintext[i].isupper() and uc >= 91 - shift:
                ciphertext += chr(uc - 26 + shift)
            elif plaintext[i].islower() and uc >= 123 - shift:
                ciphertext += chr(uc - 26 + shift)
            else:
                ciphertext += chr(uc + shift)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i, _ in enumerate(ciphertext):
        if ciphertext[i].isalpha():
            uc = ord(chiphertext[i])
            if ciphertext[i].isupper() and uc <= 64 + shift:
                plaintext += chr(uc + 26 - shift)
            elif ciphertext[i].islower() and uc <= 96 + shift:
                plaintext += chr(uc + 26 - shift)
            else:
                plaintext += chr(uc - shift)
        elif ciphertext.isspace():
            continue
        else:
            plaintext += ciphertext[i]
    return plaintext