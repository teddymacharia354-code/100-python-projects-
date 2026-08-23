def check_password_strength(password):
    """Analyze password and return strength level"""
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters")
    
    if len(password) >= 12:
        score += 1
    
    if len(password) >= 16:
        score += 1
    
    # Uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters (A-Z)")
    
    # Lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters (a-z)")
    
    # Numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("❌ Add numbers (0-9)")
    
    # Special characters
    special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    if any(char in special_chars for char in password):
        score += 1
    else:
        feedback.append("❌ Add special characters (!@#$%^&*...)")
    
    # No common patterns
    common_passwords = ["password", "123456", "qwerty", "abc123", "letmein"]
    if password.lower() not in common_passwords:
        score += 1
    else:
        feedback.append("❌ This is a commonly used password")
    
    # Determine strength level
    if score <= 2:
        strength = "VERY WEAK 🔴"
    elif score <= 4:
        strength = "WEAK 🟠"
    elif score <= 6:
        strength = "MODERATE 🟡"
    elif score <= 7:
        strength = "STRONG 🟢"
    else:
        strength = "VERY STRONG 💚"
    
    return strength, feedback, score

def main():
    print("=" * 50)
    print("PASSWORD STRENGTH CHECKER")
    print("=" * 50)
    
    while True:
        password = input("Enter a password (or 'quit' to exit): ")
        
        if password.lower() == "quit":
            print("Goodbye!")
            break
        
        if len(password) == 0:
            print("Password cannot be empty!")
            continue
        
        strength, feedback, score = check_password_strength(password)
        
        print(f"--- ANALYSIS ---")
        print(f"Strength: {strength}")
        print(f"Score: {score}/9")
        
        if feedback:
            print("Suggestions:")
            for suggestion in feedback:
                print(f"  {suggestion}")
        else:
            print("✅ Perfect password! No suggestions needed.")
        
        print("-" * 50)

if __name__ == "__main__":
    main()