# Aaron Pope
# 05/22/2018
# Treehouse TechDegree - Python, Unit 2: Secret Messages

import string

from affine import Affine

class Atbash(Affine):
    """A subset of the Affine cipher, using uppercase letters only"""
    def __init__(self):
        """Initializes a new Atbash instance with default values
        
        a: Magnitude of cipher shift
        b: Offset of cipher shift
        Defaults: a=23, b=50
        """
        super().__init__(b=25)
        self.characters = string.ascii_uppercase
        self.a = 25

    # Atbash is only designed to function with a single set of letters
    #   and should not be case-sensitive.
    # So I'm calling the superclass with a cast to uppercase
    def encrypt(self, text):
        return super().encrypt(text.upper())


    def decrypt(self, text):
        return super().decrypt(text.upper())
