import random
import time

print("Welcome to the Hide and Seek game!")
print("You are the seeker. Try to find where your friends are hiding!")

hiding_spots = ["behind the tree", "under the table", "in the closet", "behind the couch", "in the attic"]
hider = random.choice(hiding_spots)

print("\nYour friends are hiding...")
time.sleep(2)
print("Ready or not, here you come!\n")

attempts = 3

while attempts > 0:
    print("Where do you want to search?")
    for i, spot in enumerate(hiding_spots, 1):
        print(f"{i}. {spot}")
    
    choice = input("\nEnter the number of your choice: ")
    
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(hiding_spots):
        print("Invalid choice. Try again.\n")
        continue
    
    choice = int(choice) - 1
    
    if hiding_spots[choice] == hider:
        print("\nYou found your friend! They were hiding", hider + "!")
        break
    else:
        print("\nNo one is hiding there. Keep looking!")
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts left.\n")
        else:
            print("You're out of attempts! Game over.")
            print("Your friend was hiding", hider + ".")