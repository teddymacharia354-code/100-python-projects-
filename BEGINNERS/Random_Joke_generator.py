import requests
import random

def get_joke_from_api():
    """Fetch a random joke from API"""
    try:
        response = requests.get("https://api.jokes.one/joke")
        if response.status_code == 200:
            data = response.json()
            return data['contents']['jokes'][0]['joke']
        return None
    except:
        return None

def get_local_jokes():
    """Local jokes database (in case API fails)"""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? He was outstanding in his field!",
        "I told my computer I needed a break, and now it won't stop sending me Kit-Kat ads.",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you call a fake noodle? An impasta!",
        "Why did the math book look so sad? Because it had too many problems!",
        "I used to hate facial hair, but then it grew on me.",
        "Why don't eggs tell jokes? They'd crack each other up!",
        "What's the best thing about Switzerland? I don't know, but their flag is a big plus.",
        "Why did the chicken cross the road? To get to the other side!"
    ]
    return jokes

def display_joke(joke):
    """Display joke with formatting"""
    print(f"{'='*50}")
    print("HERE'S A JOKE FOR YOU!")
    print(f"{'='*50}")
    print(f"{joke}")
    print(f"{'='*50}")

def main():
    print("=" * 50)
    print("RANDOM JOKE GENERATOR")
    print("=" * 50)
    
    while True:
        print("Options:")
        print("1. Get a joke from internet (requires connection)")
        print("2. Get a local joke")
        print("3. Exit")
        
        choice = input("Select option (1-3): ").strip()
        
        if choice == "1":
            print("Fetching joke...")
            joke = get_joke_from_api()
            if joke:
                display_joke(joke)
            else:
                print("❌ Could not fetch joke. Using local joke instead.")
                local_jokes = get_local_jokes()
                joke = random.choice(local_jokes)
                display_joke(joke)
        
        elif choice == "2":
            local_jokes = get_local_jokes()
            joke = random.choice(local_jokes)
            display_joke(joke)
        
        elif choice == "3":
            print("Thank you for using Joke Generator!")
            break
        
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()