def validate_password(password):
    if len(password) < 8:
        return False

        has_lowercase = False
    has_uppercase = False
    has_digit = False

    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char.isspace():
            return False
            
            password1 = "Passw0rd"
            password2 = "securePassword"
            password3 = "1234567"
            password4 = "Password with spaces"

            validate_password(password1)
            validate_password(password2) 
            validate_password(password3)
            validate_password(password4)

