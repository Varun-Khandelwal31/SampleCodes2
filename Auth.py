from Crypto.PublicKey import RSA
import hashlib

def generate_keys():
    key = RSA.generate(2048)
    return key

def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()
