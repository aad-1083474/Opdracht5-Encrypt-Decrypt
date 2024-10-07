from cryptography.fernet import Fernet

key = Fernet.generate_key()

encrypted_message = input("Geef de tekst door die u wilt versleutelen:")

engine = Fernet(key)

# Omzetten naar bytes
encoded_message = encrypted_message.encode()

print(engine.encrypt(encoded_message))