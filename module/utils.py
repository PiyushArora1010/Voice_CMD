import sys
import os
import webbrowser
import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
import pygame
import time

def takeCommandVoice():
    r = sr.Recognizer()
    query = "None"
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.dynamic_energy_threshold = True
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print_(f"[Query Interpreted by me: {query}]")
    except Exception as e:
        print_("[I am really sorry, Say that again please...]")
    return query

def takeCommand():
    query = input()
    return query

def command_voice_text(inp):
    if inp == 'text':
        return takeCommand()
    elif inp == 'voice':
        return takeCommandVoice()

def get_audio(text, lang = 'en'):
    mp3_fo = BytesIO()
    tts = gTTS(text=text, lang=lang)
    tts.write_to_fp(mp3_fo)
    return mp3_fo

def print_(text):
    print(text)
    pygame.init()
    pygame.mixer.init()
    music = get_audio(text)

    pygame.mixer.music.load(music, 'mp3')

    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    

def print_introduction():
    print_("Welcome to the all new CMD controlled by your voice!")

def print_cwd(ch):
    if ch == 'text':
        print(f"{os.getcwd()}$ ", end="")
    elif ch == 'voice':
        print(os.getcwd(), end = '')
        print_(': Try saying a command')
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
            print_(file.read())
    except OSError as error:
        print_error(error)

def echo(text):
    print_(text)

def ls(path):
    try:
        for file in os.listdir(path):
            print_(file)
    except OSError as error:
        print_error(error)

def cd(path):
    try:
        os.chdir(path)
    except OSError as error:
        print_error(error)

def pwd():
    print_(os.getcwd())

def exit():
    sys.exit()

def print_help():
    print_("help - print this message")
    print_("clear - clear the screen")
    print_("exit - exit the program")
    print_("cd - change directory")
    print_("ls - list files in directory")
    print_("pwd - print working directory")
    print_("mkdir - make directory")
    print_("rmdir - remove directory")
    print_("rm - remove file")
    print_("mv - move file")
    print_("cp - copy file")
    print_("cat - print file contents")
    print_("echo - print text")
    print_("google - search on google")
    print_("youtube - play music on youtube")
    print_("snake - play snake and ladder")
    print_("chess - play chess")


def try_google(command):
    try:
        print_("Searching on Google...")
        webbrowser.open("https://www.google.com/search?q=" + command)
    except Exception as e:
        print_(e)

def play_music_on_youtube(command):
    try:
        print_("Playing on YouTube...")
        webbrowser.open("https://www.youtube.com/results?search_query=" + command)
    except Exception as e:
        print_(e)

def snake_and_ladder():
    try:
        print_("Opening Snake and Ladder...")
        webbrowser.open("https://toytheater.com/snakes-and-ladders/")
    except Exception as e:
        print_(e)

def chess():
    try:
        print_("Opening Chess...")
        webbrowser.open("https://www.chess.com/play/computer")
    except Exception as e:
        print_(e)

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
        print_("[Bye!][Thanks for using me]")
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
        print_("[Unknown command]")
        opt = input("Wanna google this? (y/n): ")
        if opt == 'y':
            try_google(command)
        else:
            continue