import hashlib

def weak_hash(data):
    return hashlib.md5(data.encode()).hexdigest()

def safe_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()
