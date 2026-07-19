passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]
special_characters = "!@#$%^&*"

for password in passwords:
    print(f"Checking: {password}")
    
    # Tracking variables (Flags)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    # Check each character in the current password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
            
    # Check length
    has_length = len(password) >= 8
    
    # Report missing criteria
    missing = []
    if not has_length:
        missing.append("At least 8 characters long")
    if not has_upper:
        missing.append("At least one uppercase letter")
    if not has_lower:
        missing.append("At least one lowercase letter")
    if not has_digit:
        missing.append("At least one digit")
    if not has_special:
        missing.append("At least one special character (!@#$%^&*)")
        
    # Print the final result
    if len(missing) == 0:
        print("-> Status: Strong Password")
    else:
        print("-> Status: Weak Password")
        print("   Missing criteria:")
        for reason in missing:
            print(f"   - {reason}")
    print("-" * 30)