# Contact book project
#Features: Add, Show, Delete, Update, Search
#data stored using JSON file handling
import json 

friends = []
def save_friends():
    with open("friends.json","w") as file:
        json.dump(friends,file)


try :
      with open("friends.json","r") as file:
        friends = json.load(file)
except json.JSONDecodeError:
    friends = []
    
while True:
    print("="*30)
    print("\n✨ Welcome to Contact Book ✨\n")
    print("="*30)
    print("1. Add friend")
    print("2. Show friends")
    print("3. Delete friend")
    print("4. Update friend")
    print("5. Search friend")
    print("6. Exit")
    print("="*30)
            

    choice = input("Enter your choice:")
    if choice == "1":
     friend = input("Enter friend name: ")

     if friend in friends:
        print("⚠️ Friend already exists!")
     else:
        friends.append(friend)
        save_friends()
        print("Friend added and saved.")
            
    elif choice == "2":
     if len(friends) == 0:
        print("\nNo friends yet 😢")
     else:
        print("\n📒 Your Friends List (A-Z):")
        print("-"*30)

        for i, f in enumerate(sorted(friends), start=1):
            print(f"{i}. {f}")
    elif choice == "3":
            name = input("Enter friend name to delete:")
            if name in friends:
                friends.remove(name)
                save_friends()
                print("Friend deleted")
            else:
                print("Friend not found")
    elif choice == "4":
     old_name = input("Enter name to update: ")

     if old_name in friends:
        new_name = input("Enter new name: ")

        index = friends.index(old_name)
        friends[index] = new_name

        save_friends()
        print("Friend updated successfully!")
     else:
        print("Friend not found")
    elif choice == "5":
         name = input("Enter name to search:").lower()
         found = False
         for f in friends:
              if f.lower() == name:
                   print("Friend found:",f)
                   found = True
                   break
         if not found:
              print("Friend not found")

    elif choice == "6":
            print("Goodbye")
            break
    else:
            print("Invalid choice")
