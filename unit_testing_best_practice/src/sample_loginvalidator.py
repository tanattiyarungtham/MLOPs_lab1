import re

def validate_username(username):
    """Validate username: not empty, no spaces."""
    if not username:
        return False
    if " " in username:
        return False
    return True

def validate_password(password):
    """Validate password: at least 8 characters, one number, one letter, one special character."""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    if not any(char in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for char in password):
        return False
    return True

def validate_email(email):
    """Validate email: contains @ and ."""
    if "@" not in email and "." not in email:
        return False
    return True

