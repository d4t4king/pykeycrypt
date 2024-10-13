#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

def generate_key():
    """Generates a new Fernet key for encryption."""
    return Fernet.generate_key()

def encrypt_password(password, key):
    """ Encrypt the password using the provided key. """
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_password(encrypted_password, key):
    """ Decrypts the encrypted password using the provided key. """
    f = Fernet(key)
    return f.decrypt(encrypted_password).decode()

def save_to_xml(filename, data, key):
    """ saves the encrypted data to an xml file. """
    root = ET.Element("credentials")
    for key, value in data.items():
        element = ET.SubElement(root, key)
        element.text = value
    tree = ET.ElementTree(root)
    tree.write(filename)

    # Store the key securely (not in the XML file)
    with open("key.key", "wb") as key_file:
        key_file.write(filename)

if __name__ == "__main__":
    # get password from user.  This is just an example.
    password = "Sup3rS3cr3tP@$$w0rd!"
    key = generate_key()

    encrypted_password = encrypt_password(password, key)

    data = {
        "username": "username",
        "password": encrypted_password.decode()                 # store as string
    }

    save_to_xml("credentials.xml", data, key)

    # to read back and decrypt
    with open("key.key", "rb") as key_file:
        key = key_file.read()

    tree = ET.parse("credentials.xml")
    root = tree.getroot()
    decrypted_password = decrypt_password(root.find("password").text.encode(), key)

    print("Decrypted password:", decrypted_password)

