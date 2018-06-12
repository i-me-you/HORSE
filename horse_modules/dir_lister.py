# list directories
import os

def run():
    print('[*] in the directory lister modules')
    files = os.listdir('.')
    return str(files)