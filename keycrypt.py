#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from cryptography.fernet import Fernet

def generate_key():
    """Generates a new Fernet key for encryption."""
    return Fernet.generate_key()


