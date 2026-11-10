from cryptography.fernet import Fernet

#Creates a key
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key","rb")
    key_val = file.read()
    file.close()
    return key_val


master_password  = input("What is your master password: ")
key = load_key() + master_password.encode()
fer = Fernet(key)


def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            #rstrip returns the line without reading the "\n"
            data = line.rstrip()
            #The split operator returns a list of values separated by the provided char
            account, passw = data.split("|")
            print(f"Account :{account} |  Password:{fer.decrypt(passw.encode()).decode()}")

def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open('password.txt','a') as f:
        f.write(f'{name} | {fer.encrypt(password.encode()).decode()} '+"\n")

while True:
    mode = input("Would you like to add a new password or view the existing passwords? (View/Add) to proceed (Q to quite): ").lower()

    if mode == 'q':
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Please provide a valid input (Add/View/Q): ")
        continue
