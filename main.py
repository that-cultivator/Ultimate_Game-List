print("\n1. Trending PC Games")
print("2. Top PC Titles")
print("3. Top xbox Titles")
print("4. Top PS Titles")
print("5. New Releases\n")
def func():
    inp=input("> ")

    if inp == '1':
        print("Trending")

    elif inp == '2':
        print("Trending games")

    elif inp == '3':
        print("pc")

    elif inp == '4':
        print("ps")


    elif inp == '5':
        print("release")
    else:
        print("incvalid choice")
func()
