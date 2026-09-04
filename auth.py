import bcrypt 
from db import get_dbConnection

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def login(account_number: str, password: str):
    conn = get_dbConnection()
    if not conn:
        return False, "Database connection error"

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE account_number = %s", (account_number,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user and verify_password(password, user["password_hash"]):
        return True, user
    return False, "Invalid account number or password"