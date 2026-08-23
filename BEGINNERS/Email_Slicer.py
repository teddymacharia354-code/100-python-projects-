def slice_email(email):
    """Extract username and domain from email"""
    if "@" not in email:
        return None
    
    parts = email.split("@")
    username = parts[0]
    domain = parts[1]
    
    return {
        "email": email,
        "username": username,
        "domain": domain,
        "domain_name": domain.split(".")[0],
        "domain_extension": ".".join(domain.split(".")[1:])
    }

def validate_email(email):
    """Validate email format"""
    if "@" not in email or "." not in email.split("@")[1]:
        return False
    return True

def display_email_info(info):
    """Display email information"""
    print(f"{'='*50}")
    print("EMAIL ANALYSIS")
    print(f"{'='*50}")
    print(f"Full Email: {info['email']}")
    print(f"Username: {info['username']}")
    print(f"Domain: {info['domain']}")
    print(f"Domain Name: {info['domain_name']}")
    print(f"Domain Extension: {info['domain_extension']}")
    print(f"{'='*50}")

def main():
    print("=" * 50)
    print("EMAIL SLICER")
    print("=" * 50)
    print("Extract parts from email addresses!")
    
    while True:
        email = input("Enter email address (or 'quit' to exit): ").strip()
        
        if email.lower() == "quit":
            print("Thank you for using Email Slicer!")
            break
        
        if not email:
            print("Please enter an email address!")
            continue
        
        if not validate_email(email):
            print("❌ Invalid email format!")
            continue
        
        info = slice_email(email)
        if info:
            display_email_info(info)
        else:
            print("❌ Error processing email!")

if __name__ == "__main__":
    main()