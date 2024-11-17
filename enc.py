from fernet import Fernet

key = b'Y6jp1k09psK7NBg_HFJ8VOyuDIW3yoEtcUZy1BcuhzE='
print(key)
f = Fernet(key)

token = f.encrypt(b"@sonjed2024")
print(token)
token
b'...'

a = f.decrypt(token)
b'@sonjed2024'
print(a)