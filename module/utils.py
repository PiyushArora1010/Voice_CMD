import sys
import os
import webbrowser
import speech_recognition as sr

def takeCommandVoice():
    r = sr.Recognizer()
    query = "None"
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"[Query Interpreted by me: {query}]\n")
    except Exception as e:
        print(e)
        print("[I am really sorry, Say that again please...]")
    return query

def takeCommand():
    query = input()
    return query

def command_voice_text(inp):
    if inp == 'text':
        return takeCommand()
    elif inp == 'voice':
        return takeCommandVoice()


def print_introduction():
    print("Welcome to the all new CMD controlled by your voice!")
    print("Type 'help' to see all the commands available.")

def print_cwd(ch):
    if ch == 'text':
        print(f"{os.getcwd()}$ ", end="")
    elif ch == 'voice':
        print(os.getcwd()+': Try saying a command')
    else:
        print("Invalid choice")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_error(error):
    print(f"Error: {error}")

def mkdir(path):
    try:
        os.mkdir(path)
    except OSError as error:
        print_error(error)

def rmdir(path):
    try:
        os.rmdir(path)
    except OSError as error:
        print_error(error)

def rm(path):
    try:
        os.remove(path)
    except OSError as error:
        print_error(error)

def mv(src, dst):
    try:
        os.rename(src, dst)
    except OSError as error:
        print_error(error)

def cp(src, dst):
    try:
        with open(src, 'r') as src_file:
            with open(dst, 'w') as dst_file:
                dst_file.write(src_file.read())
    except OSError as error:
        print_error(error)

def cat(path):
    try:
        with open(path, 'r') as file:
            print(file.read())
    except OSError as error:
        print_error(error)

def echo(text):
    print(text)

def ls(path):
    try:
        for file in os.listdir(path):
            print(file)
    except OSError as error:
        print_error(error)

def cd(path):
    try:
        os.chdir(path)
    except OSError as error:
        print_error(error)

def pwd():
    print(os.getcwd())

def exit():
    sys.exit()

def print_help():
    print("help - print this message")
    print("clear - clear the screen")
    print("exit - exit the program")
    print("cd - change directory")
    print("ls - list files in directory")
    print("pwd - print working directory")
    print("mkdir - make directory")
    print("rmdir - remove directory")
    print("rm - remove file")
    print("mv - move file")
    print("cp - copy file")
    print("cat - print file contents")
    print("echo - print text")

def try_google(command):
    try:
        print("Searching on Google...")
        webbrowser.open("https://www.google.com/search?q=" + command)
    except Exception as e:
        print(e)

def play_music_on_youtube(command):
    try:
        print("Playing on YouTube...")
        webbrowser.open("https://www.youtube.com/results?search_query=" + command)
    except Exception as e:
        print(e)

def snake_and_ladder():
    try:
        print("Opening Snake and Ladder...")
        webbrowser.open("https://toytheater.com/snakes-and-ladders/")
    except Exception as e:
        print(e)

def chess():
    try:
        print("Opening Chess...")
        webbrowser.open("https://www.chess.com/play/computer")
    except Exception as e:
        print(e)

def main_cmd(input_choice):
  while True:
    print_cwd(input_choice)

    command = command_voice_text(input_choice).lower()
    if command == 'none':
        continue
    if command == "help":
        print_help()
    elif command == "clear":
        clear()
    elif command == "exit":
        print("[Bye!][Thanks for using me]")
        exit()
    elif command == "pwd":
        pwd()
    elif command.startswith("cd "):
        cd(command[3:])
    elif command == "ls":
        ls(os.getcwd())
    elif command.startswith("ls "):
        ls(command[3:])
    elif command.startswith("echo "):
        echo(command[5:])
    elif command.startswith("cat "):
        cat(command[4:])
    elif command.startswith("cp "):
        cp(command[3:].split(" ")[0], command[3:].split(" ")[1])
    elif command.startswith("mv "):
        mv(command[3:].split(" ")[0], command[3:].split(" ")[1])
    elif command.startswith("rm "):
        rm(command[3:])
    elif command.startswith("rmdir "):
        rmdir(command[6:])
    elif command.startswith("mkdir "):
        mkdir(command[6:])
    elif command.startswith("google "):
        try_google(command[7:])
    elif command.startswith("youtube "):
        play_music_on_youtube(command[8:])
    elif command.startswith("snake and ladder"):
        snake_and_ladder()
    elif command.startswith("chess"):
        chess()
    else:
        print("[Unknown command]")
        opt = input("Wanna google this? (y/n): ")
        if opt == 'y':
            try_google(command)
        else:
            continue