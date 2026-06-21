import ssl

context = ssl.create_default_context()

context.set_ciphers(
    "ECDHE-RSA-AES256-SHA"
)
