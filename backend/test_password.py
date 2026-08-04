from app.modules.auth.utils import hash_password, verify_password

password = "CordiAnce123"

hashed = hash_password(password)

print("Original :", password)
print("Hashed   :", hashed)

print("Verify :", verify_password(password, hashed))