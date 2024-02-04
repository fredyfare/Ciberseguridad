from cryptography.fernet import Fernet

# Encriptación de mensaje
print("---Encriptacion de mensaje---")
key = Fernet.generate_key()
f = Fernet(key)

print("Key:", key)
token = f.encrypt(b'Quiero chambaaaaaaa')
print("token:", token)

des = f.decrypt(token)
print("Mensaje original:", des)

# Desencriptación de mensaje
print("---Desencriptacion de mensaje---")
f1 = Fernet(b'fsha0l6uV7o0VDmSnJ9XHZHP2g3rn126rgdc8RrSbTk=')

message = f1.decrypt(b'gAAAAABluxAwZlAakKOyFOMgKAOp_wj4tSesqCWI417ZV081S_zWG26mlD69KfDLZaOzziZgU7qkbRFJcMSID6ci47PwhEOBiXHtzA78FCRAiafMuE5cfIs=')
print(message)
