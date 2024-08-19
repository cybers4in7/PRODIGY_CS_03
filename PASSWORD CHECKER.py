import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[\W_]', password) is not None
    
    strength = 0
    feedback = []
    
    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        
    if uppercase_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
        
    if lowercase_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
        
    if digit_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")
        
    if special_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")
        
    if strength == 5:
        feedback.append("Password is strong.")
    elif strength >= 3:
        feedback.append("Password is moderate.")
    else:
        feedback.append("Password is weak.")
        
    return strength, feedback

def main():
    while True:
        password = input("Enter a password to check its strength (or 'q' to quit): ")
        if password.lower() == 'q':
            break
        
        strength, feedback = check_password_strength(password)
        print(f"Password Strength: {strength}/5")
        for comment in feedback:
            print(f"- {comment}")

if __name__ == "__main__":
    main()
