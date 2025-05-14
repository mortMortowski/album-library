import random
import sys

def main():
    albums = open('albums.txt')
    print("Album Library v.0.2")
    print("1. View all albums")
    print("2. Select random album")
    print("3. Exit")
    option = input("Select option: ")
    if (option == "1"):
        for line in albums:
            print(line)
    elif (option == "2"):
        lines = albums.readlines()
        print(random.choice(lines))
    elif (option == "3"):
        sys.exit()
    else:
        print("No such option. Exiting program...")
    
    input("Press enter to exit")

if __name__ == "__main__":
    main()