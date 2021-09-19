#!/usr/bin/env python3
import secrets
import string
from argparse import ArgumentParser


class Config:
    def __init__(self):
        self.args = Config.create_args()
        self.clipboard = self.args.clipboard
        self.invisible = self.args.invisible
        self.length = self.args.n
        # only touches if one of them is mentioned
        self.punctuation = self.uppercase = self.lowercase = self.digits = True
        self.specified = False
        if self.args.pun or self.args.upc or self.args.lwc or self.args.digits:
            self.digits = self.args.digits
            self.lowercase = self.args.lwc
            self.uppercase = self.args.upc
            self.punctuation = self.args.pun
            self.specified = True

    @staticmethod
    def create_args():
        parser = ArgumentParser()
        parser.add_argument_group('General Arguments')
        parser.add_argument('n', metavar='length', type=int, nargs='?', default=20,
                            help='Defines length of Password (Default is 20)')
        parser.add_argument('-c', action='store_const', dest='clipboard',
                            const=True, default=False,
                            help='Copy password to clipboard')
        parser.add_argument('-i', action='store_const', dest='invisible',
                            const=True, default=False,
                            help='Disables commandline Output')

        symbols = parser.add_argument_group('Enable use of... (Default is all)')
        symbols.add_argument('-p', action='store_const', dest='pun',
                             const=True, default=False,
                             help='Symbols')
        symbols.add_argument('-u', action='store_const', dest='upc',
                             const=True, default=False,
                             help='Uppercase-letters')
        symbols.add_argument('-l', action='store_const', dest='lwc',
                             const=True, default=False,
                             help='Lowercase-letters')
        symbols.add_argument('-d', action='store_const', dest='digits',
                             const=True, default=False,
                             help='Digits')
        return parser.parse_args()


def validate_modifiers(s):
    if not cfg.specified:
        return True
    if cfg.punctuation and not bool([ele for ele in string.punctuation if(ele in s)]):
        print("punctuation failed")
        return False
    if cfg.uppercase and not bool([ele for ele in string.ascii_uppercase if(ele in s)]):
        print("uc failed")
        return False
    if cfg.lowercase and not bool([ele for ele in string.ascii_lowercase if(ele in s)]):
        print("lc failed")
        return False
    if cfg.digits and not bool([ele for ele in string.digits if(ele in s)]):
        print("digits failed")
        return False
    return True


def generate():
    charset = assemble_charset()
    while True:
        s = pick_chars(charset)
        if validate_modifiers(s):
            break
    return s


def assemble_charset():
    chars = ''
    if cfg.punctuation:
        chars += string.punctuation
    if cfg.uppercase:
        chars += string.ascii_uppercase
    if cfg.lowercase:
        chars += string.ascii_lowercase
    if cfg.digits:
        chars += string.digits
    return chars


def pick_chars(charset):
    s = ''.join(secrets.choice(charset) for _ in range(cfg.length))
    return s


def output():
    if not cfg.invisible:
        print(pw)
    if cfg.clipboard:
        try:
            import pyperclip as pc
            pc.copy(pw)
            print('Copied to Clipboard')
        except ModuleNotFoundError:
            print("module 'pyperclip' is not installed use 'pip install pyperclip'")


if __name__ == "__main__":
    cfg = Config()
    pw = generate()
    output()
