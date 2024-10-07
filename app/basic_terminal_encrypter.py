from cryptography.fernet import Fernet

key = Fernet.generate_key()

encrypted_message = input("Hoi Diederik! Geef de tekst door die u wilt versleutelen:")

engine = Fernet(key)

# Omzetten naar bytes
encoded_message = encrypted_message.encode()

# Geëncrypte uitkomst
encrypted_output = engine.encrypt(encoded_message)
print(f"Versleutelde boodschap: {encrypted_output}")

#Gedecrypte uitkomst
decrypted_output = engine.decrypt(encrypted_output)
print(f"Ontsleutelde boodschap: {decrypted_output.decode()}")