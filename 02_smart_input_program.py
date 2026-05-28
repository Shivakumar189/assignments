# Assignment: Smart Input Program (12/02/2026)
# Takes name, age, hobby and prints personalized message with age categorization

def categorize_age(age: int) -> str:
    """Categorize age into life stage."""
    if age < 0:
        return "Invalid"
    elif age <= 12:
        return "Child"
    elif age <= 17:
        return "Teenager"
    elif age <= 25:
        return "Young Adult"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

def get_valid_age() -> int:
    """Get a valid integer age from the user."""
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age > 120:
                print("Please enter a realistic age (0–120).")
            else:
                return age
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("=" * 45)
    print("       👋 Personalized Greeting Program")
    print("=" * 45)

    name = input("Enter your name: ").strip().title()
    age = get_valid_age()
    hobby = input("Enter your favourite hobby: ").strip()

    category = categorize_age(age)

    print("\n" + "=" * 45)
    print(f"Hello, {name}! 😊")
    print(f"You are {age} years old — that makes you a {category}.")
    print(f"It's wonderful that you enjoy {hobby}!")

    # Personalized message based on category
    messages = {
        "Child":       f"Keep exploring the world through {hobby}, {name}! Learning is an adventure.",
        "Teenager":    f"As a teen who loves {hobby}, you're building great skills for the future!",
        "Young Adult": f"Balancing life and {hobby} at your age is impressive, {name}. Keep it up!",
        "Adult":       f"It's great that you still make time for {hobby}, {name}. It keeps life joyful!",
        "Senior":      f"Your passion for {hobby} is truly inspiring, {name}. Age is just a number!",
        "Invalid":     "Please enter a valid age."
    }

    print(f"\n💬 {messages.get(category, 'Have a great day!')}")
    print("=" * 45)

if __name__ == "__main__":
    main()
