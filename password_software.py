import hashlib as h
import getpass


def main():
    username = input("Enter your username: \n")
    password = getpass.getpass("Enter your password: \n")

    if check_for_user_password(username, password):
        open_menu(username)


def open_menu(username):
    while True:
        choice = int(input(
            "Enter '1' to add a new user or '2' to change password or '3' to delete another user or '4' to log out: "))
        if choice == 1:
            add_user()
        elif choice == 4:
            break
        elif choice == 2:
            change_password(username, getpass.getpass("Enter your old password: \n"),
                            getpass.getpass("Enter your new password: \n"))
        elif choice == 3:
            remove_user(input("Please enter the username for the user you would like to remove: \n"))


def add_user():
    with open("users.txt", "a") as f:
        username = input("Please enter the  username of the new account:\n")
        password = getpass.getpass("Please enter the password of the new account:\n")
        password_encrypted = h.md5(str.encode(password))
        print(password_encrypted)
        f.write(username + " , " + str(password_encrypted.digest()) + "\n")


def check_for_user_password(username, password):
    with open("users.txt", "r") as f:
        for line in f:
            if line.startswith(username):
                password_encrypted_infile = line.split(" , ")[1][:-1]
                result = h.md5(str.encode(password))
                if password_encrypted_infile == str(result.digest()):
                    return True
                else:
                    print("Wrong password")
        return False


def change_password(username, password, newpassword):
    with open("users.txt", "r") as f:
        users = f.read()
        users = users.split("\n")
        for i in range(len(users)):
            if users[i].startswith(username):
                user_data = users[i].split(" , ")
                password_encrypted_infile = user_data[1]
                result = h.md5(str.encode(password))
                if password_encrypted_infile == str(result.digest()):
                    result = h.md5(str.encode(newpassword))
                    user_data[1] = str(result.digest())
                    users[i] = " , ".join(user_data)

    with open("users.txt", "w") as f:
        for user in users:
            f.write(user + "\n")


def remove_user(user):
    with open("users.txt", "r+") as f:
        users = f.read()
        users = users.split("\n")
        print(len(users))
        for i in range(len(users)):
            if users[i].startswith(user):
                f.write("")


if __name__ == "__main__":
    main()
