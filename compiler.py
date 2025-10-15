import time
import sys
import os
import pygame


print("Compiler Started")

def configure():
    print("Preparing Audio channels via PYGAME")
    pygame.mixer.init(frequency=44100, size=-16, channels=2) 
    print("Audio channels ready")

def module_insert():
    premodule = input("")
    if "import:" in premodule:
        module = premodule.replace("import: ", "")
        try:
            __import__(module)
            print(f"module {module} imported successfully")
            random = input("")
        except ImportError:
            print(f"Import Error: module {module} could not be imported")
    else:
        print("Syntax Error: The command you provided doesn't exist please check the documentation")

def wiki():
    print("To check the documentaion please visit")
    print("wiki-ratcode.netlify.app")


def exit():
    sys.exit()

def variable():
    prevariable = input("")
    if "create:" in prevariable:
        variable = prevariable.replace("create: ", "")
        try:
            exec(f"{variable} = None")
            print(f"Variable {variable} created successfully")
            random = input("")
        except Exception as e:
            print(f"Error creating variable {variable}: {e}")
    else:
        print("Syntax Error: The command you provided doesn't exist please check the documentation")

def time_delay():
    prepretime = input("")
    if "time:" in prepretime:
        pretime = prepretime.replace("time: ", "")
        try:
            delay_seconds = int(pretime)
        except ValueError:
            print("Value Error: the number for sleep time you provided is not an number please check documentation")
        time.sleep(delay_seconds)

    else:
        print("Syntax Error: The command you provided doesn't exist please check the documentation")

def play_sound():
    presound = input("")
    if "music:" in presound:
        sound = presound.replace("music:", "")
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
        fi = input("")
    else:
        print('\a')
        print("Syntax Error: The command you provided doesn't exist please check the documentation")   
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def write():
    pretext = input("")
    if "write:" in pretext:
        text = pretext.replace("write:", "")    
        print(text)
        wait = input("")
    else:
        print('\a')
        print("Syntax Error: The command you proved doesn't exist please check the documentation for commands")
    
def main():
    clear_terminal()
    start = input("")
    if "clear/" in start:
        clear_terminal()
    if "write/" in start:
        write()
    if "play/" in start:
        play_sound()
    if "time/" in start:
        time_delay()
    if "exit/" in start:
        exit()
    if "import/" in start:
        module_insert()
    else:
        print("Processing Error: The command you provided doesn't exist please check the documentation")
        print('\a')


clear_terminal()
configure()
clear_terminal()
main()

if __name__ == "__main__":
    main()
