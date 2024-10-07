from cryptography.fernet import Fernet

key = Fernet.generate_key()

encrypted_message = input("Geef de tekst door die u wilt versleutelen:")

engine = Fernet(key)



print(engine.encrypt(encrypted_message))