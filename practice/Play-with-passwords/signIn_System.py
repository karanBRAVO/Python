import json
import hashlib
import maskpass

print("""
*** Sign In System ***
- press left-Ctrl key to show password
- press F_P to change your password
""")

# password-12345678

userName_chance = 1
userPassword_chance = 1
Code = 1010101010

with open("p.txt", 'r') as f:
    data = json.load(f)
f.close()

while userName_chance <= 3 and userPassword_chance <= 3:
    u_name = str(input("Enter Username: "))

    if u_name == data["username"]:
        u_pass = maskpass.advpass(prompt="Enter Password: ", mask="*")
        u_pass_hashed = hashlib.sha256(u_pass.encode('utf-8')).hexdigest()
        if u_pass_hashed == data["password"]:
            print(f"Welcome {u_name}")
            break
        elif u_pass == 'F_P':
            userPassword_chance = 4
            break
        else:
            print("password is wrong.")
            userPassword_chance += 1
    elif u_name == 'F_P':
        userPassword_chance = 4
        break
    else:
        print("username is wrong.")
        userName_chance += 1


def changeUserName():
    new_username = input("Set new User Name: ")
    new_data_changed_username = {
        'username': new_username,
        'password': data['password'],
    }
    with open('p.txt', 'w') as f:
        json.dump(new_data_changed_username, f)
    f.close()
    print('username changed.')


def changePassword():
    new_password = maskpass.advpass(prompt="Set New Password: ", mask="#")
    if len(new_password) < 8:
        print("must be of atleast (8-digits) for more security")
        changePassword()
    elif len(new_password) >= 8:
        new_password_hash = hashlib.sha256(new_password.encode('utf-8')).hexdigest()
        new_data_changed_password = {
            'username': data['username'],
            'password': new_password_hash,
        }
        with open('p.txt', 'w') as f:
            json.dump(new_data_changed_password, f)
        f.close()
        print('password changed.')


def checkCode():
    try:
        code = int(input("Code(10-digit): "))
        if code == Code:
            print("*** Use strong password that you don't use for other things ***")
            changePassword()
        else:
            print("Not matched")
            checkCode()
    except:
        print("it must have numbers only.")
        checkCode()


if userName_chance > 3:
    captcha_code = int(input("type (1) to change username: "))
    if captcha_code == 1:
        changeUserName()
    else:
        print("can't change the username")

if userPassword_chance > 3:
    print("Type the (10-digit) code given to you to reset password.")
    checkCode()
