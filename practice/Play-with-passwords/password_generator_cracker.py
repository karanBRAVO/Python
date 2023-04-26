import random
import hashlib
import json

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '#', '$']


def passwordGenerator(number_of_passwords):
    number_of_passwords = number_of_passwords

    for num in range(0, number_of_passwords):
        new_lst = []

        for i in range(1, 9, 1):
            char = lst[random.randint(0, len(lst) - 1)]
            new_lst.append(char)

        password = "".join(new_lst)
        hashedPassword = hashlib.sha256(password.encode()).hexdigest()

        print(f"password_{num + 1}: ", password, f"\nHashed_password_{num + 1}: ", hashedPassword)


def passwordCracker():
    password_input = input("Enter password(8-digit): ")

    password = password_input
    print("checking_password:", hashlib.sha256(password.encode('utf-8', 'not hashed!')).hexdigest())

    try:
        if len(password_input) == 8:
            for a in range(0, len(lst)):
                lst1 = [lst[a]]
                for b in range(0, len(lst)):
                    lst1.append(lst[b])
                    for c in range(0, len(lst)):
                        lst1.append(lst[c])
                        for d in range(0, len(lst)):
                            lst1.append(lst[d])
                            for e in range(0, len(lst)):
                                lst1.append(lst[e])
                                for f in range(0, len(lst)):
                                    lst1.append(lst[f])
                                    for g in range(0, len(lst)):
                                        lst1.append(lst[g])
                                        for h in range(0, len(lst)):
                                            lst1.append(lst[h])
                                            check = "".join(lst1)
                                            with open("passwords.txt", 'a') as p:
                                                json.dump(check, p)
                                            if check == password:
                                                check = hashlib.sha256(check.encode()).hexdigest()
                                                print("found!:", check)
                                                raise StopIteration
                                            lst1.pop(-1)
                                        lst1.pop(-1)
                                    lst1.pop(-1)
                                lst1.pop(-1)
                            lst1.pop(-1)
                        lst1.pop(-1)
                    lst1.pop(-1)
        else:
            print("must be of 8-digits...")
    except StopIteration:
        p.close()
        pass


if __name__ == "__main__":
    # passwordGenerator(10)
    passwordCracker()
