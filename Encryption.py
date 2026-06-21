from Crypto.Cipher import DES, AES

def encrypt_des(data):
    key = b"12345678"
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

def encrypt_aes(data):
    key = b"0123456789abcdef0123456789abcdef"
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(data)
