from cryptography.fernet import Fernet
import PySimpleGUI as sg



def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    values = window.read()
    with open("key.key", "rb") as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(values("-IN-"), "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(values("-IN-"), "wb") as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt():
    values = window.read()
    with open("key.key", "rb") as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(values("-IN-"), "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(values("-IN-"), "wb") as dec_file:
        dec_file.write(decrypted)

write_key()


sg.theme("DarkTeal2")

layout = [[sg.Text("What would you like to encrypt?"), sg.Input(), sg.FileBrowse(key = "-IN-")], [sg.Button("Encrypt"), sg.Button("Decrypt")]]

window = sg.Window("Demo", layout, size = (600, 150))

event, values = window.read()

while True:
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Encrypt":
        load_key()
    elif event == "Decrypt":
        decrypt()
