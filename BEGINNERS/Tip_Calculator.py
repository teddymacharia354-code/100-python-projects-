def calculate_tip(bill_amount, tip_percentage, split_ways=1):
    """Calculate tip and total amount"""
    tip_amount = (bill_amount * tip_percentage) / 100
    total_with_tip = bill_amount + tip_amount
    per_person = total_with_tip / split_ways
    
    return {
        "bill": bill_amount,
        "tip_percentage": tip_percentage,
        "tip_amount": tip_amount,
        "total": total_with_tip,
        "per_person": per_person,
        "split_ways": split_ways
    }

def display_results(result):
    """Display tip calculation results"""
    print("=" * 50)
    print("TIP CALCULATION RESULTS")
    print("=" * 50)
    print(f"Original bill: ${result['bill']:.2f}")
    print(f"Tip percentage: {result['tip_percentage']}%")
    print(f"Tip amount: ${result['tip_amount']:.2f}")
    print(f"Total with tip: ${result['total']:.2f}")
    
    if result['split_ways'] > 1:
        print(f"Split {result['split_ways']} ways:")
        print(f"Per person: ${result['per_person']:.2f}")
    
    print("=" * 50)

def main():
    print("=" * 50)
    print("TIP CALCULATOR")
    print("=" * 50)
    
    while True:
        try:
            bill = float(input("Enter bill amount ($): "))
            if bill < 0:
                print("Bill amount cannot be negative!")
                continue
            
            print("Common tip percentages:")
            print("1. 10% (Poor service)")
            print("2. 15% (Standard)")
            print("3. 18% (Good service)")
            print("4. 20% (Excellent service)")
            print("5. Custom percentage")
            
            tip_choice = input("Select tip percentage (1-5): ").strip()
            
            if tip_choice == "1":
                tip_percent = 10
            elif tip_choice == "2":
                tip_percent = 15
            elif tip_choice == "3":
                tip_percent = 18
            elif tip_choice == "4":
                tip_percent = 20
            elif tip_choice == "5":
                tip_percent = float(input("Enter custom percentage: "))
            else:
                print("Invalid choice!")
                continue
            
            split = input("Split the bill? (yes/no): ").lower()
            if split in ["yes", "y"]:
                num_people = int(input("How many people? "))
            else:
                num_people = 1
            
            result = calculate_tip(bill, tip_percent, num_people)
            display_results(result)
            
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        
        again = input("Calculate another tip? (yes/no): ").lower()
        if again not in ["yes", "y"]:
            print("Thank you for using Tip Calculator!")
            break

if __name__ == "__main__":
    main()