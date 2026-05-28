# Assignment: Password Authentication (07/02/2026)
# Strong password authentication system

import hashlib
import os
import re
import getpass

# In-memory user store (simulates a database)
users = {}

def hash_password(password: str, salt: bytes = None) -> tuple:
    """Hash a password with a salt using SHA-256."""
    if salt is None:
        salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, key

def check_password_strength(password: str) -> bool:
    """
    Password must:
    - Be at least 8 characters long
    - Contain uppercase and lowercase letters
    - Contain at least one digit
    - Contain at least one special character
    """
    if len(password) < 8:
        print("❌ Password must be at least 8 characters long.")
        return False
    if not re.search(r'[A-Z]', password):
        print("❌ Password must contain at least one uppercase letter.")
        return False
    if not re.search(r'[a-z]', password):
        print("❌ Password must contain at least one lowercase letter.")
        return False
    if not re.search(r'\d', password):
        print("❌ Password must contain at least one digit.")
        return False
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        print("❌ Password must contain at least one special character.")
        return False
    return True

def register(username: str, password: str) -> bool:
    """Register a new user."""
    if username in users:
        print("❌ Username already exists.")
        return False
    if not check_password_strength(password):
        return False
    salt, hashed = hash_password(password)
    users[username] = {'salt': salt, 'password': hashed}
    print(f"✅ User '{username}' registered successfully!")
    return True

def login(username: str, password: str) -> bool:
    """Authenticate a user."""
    if username not in users:
        print("❌ Username not found.")
        return False
    stored = users[username]
    _, hashed = hash_password(password, stored['salt'])
    if hashed == stored['password']:
        print(f"✅ Welcome, {username}! Login successful.")
        return True
    else:
        print("❌ Incorrect password.")
        return False

def main():
    MAX_ATTEMPTS = 3
    print("=" * 40)
    print("   🔐 Password Authentication System")
    print("=" * 40)

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            username = input("Enter username: ").strip()
            password = getpass.getpass("Enter password: ")
            register(username, password)

        elif choice == '2':
            username = input("Enter username: ").strip()
            attempts = 0
            while attempts < MAX_ATTEMPTS:
                password = getpass.getpass("Enter password: ")
                if login(username, password):
                    break
                attempts += 1
                remaining = MAX_ATTEMPTS - attempts
                if remaining > 0:
                    print(f"⚠️ {remaining} attempt(s) remaining.")
                else:
                    print("🚫 Account locked due to too many failed attempts.")

        elif choice == '3':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
