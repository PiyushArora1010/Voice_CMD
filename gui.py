from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Scrollbar
from tkinter import scrolledtext
from tkinter import INSERT, WORD, END, DISABLED, RIGHT
import tkinter.scrolledtext as tkk
from module.utils import *
command=""
import speech_recognition as sr
import pyttsx3


def print_gui(text):
	text_area.insert(END, text + "\n")
	engine = pyttsx3.init()
	engine.setProperty('rate', 150)
	engine.say(text)
	engine.runAndWait()

flag = False

def what_to_do_gui(command):
	global flag
	if command == 'turn siri off' and flag == True:
		flag = False
		return
	elif command == 'turn siri off' and flag == False:
		print_gui("siri is already off")
		return
	if flag:
		command_ , action= input_text_stark(command)
		if command_ != "":
			command = command_
		
		if "smalltalk" in action:
			print_gui(command)
			return

		text_area.insert(END,'Command for Terminal: ')
		print_gui(command)
	if command == 'none':
		return
	if command == "help":
		print_help()
	elif command == "clear":
		clear()
	elif command == "exit":
		print_gui("[Bye!][Thanks for using me]")
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
	elif command.startswith("open "):
		open_app(command[5:])
	elif command.startswith("turn siri on"):
		print_gui("Hello User! I am here to assist you!")
		flag = True
	elif command.startswith("turn siri off"):
		print_gui("Turning off...")
		flag = False
	else:
		print_gui("[Unknown command]")


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
	except Exception as e:
		print("[I am really sorry, Say that again please...]")
	return query

def switch():
	command = takeCommandVoice().lower()
	text_area.insert(END,'Query interpreted: ')
	text_area.insert(END, command + "\n")
	what_to_do_gui(command)

def input(event):

	command=entry_1.get() 
	what_to_do_gui(command.lower())
	entry_1.delete(0, "end")
window = Tk()

window.geometry("850x650")
window.title("Roger Virtual Assistant")
window.configure(bg = "#FFFFFF")
window.iconbitmap("images/favicon (1).ico")

canvas = Canvas(
	window,
	bg = "#FFFFFF",
	height = 650,
	width = 850,
	bd = 0,
	highlightthickness = 0,
	relief = "ridge"
)

canvas.place(x = 0, y = 0)



listen = PhotoImage(file = "images/listen.png")
stop = PhotoImage(file = "images/stop.png")

button_1 = Button(
	image=listen,
	borderwidth=0,
	highlightthickness=0,
	command=switch,
	relief="flat",
	fg="#FFFFFF",
	bg="#FFFFFF",
	highlightbackground="#FFFFFF",
)
button_1.place(
	x=377.0,
	y=568.0,
	width=172.554931640625,
	height=69.0
)

entry_image_1 = PhotoImage(
	file="images/textbox.png")
entry_bg_1 = canvas.create_image(
	702.0,
	602.5,
	image=entry_image_1
)
entry_1 = Entry(
	bd=0,
	bg="#D9D9D9",
	fg="#000000",
	highlightthickness=0,
	disabledforeground="#D9D9D9",
	disabledbackground="#D9D9D9"
)
entry_1.place(
	x=595.5,
	y=568.0,
	width=213.0,
	height=67.0
)
entry_1.bind("<Return>", input)

image_image_1 = PhotoImage(
	file="images/image_1.png")
image_1 = canvas.create_image(
	184.0,
	368.0,
	image=image_image_1
)

text_area=tkk.ScrolledText(window,width=50,height=25,relief="flat",font=("Elephant",11),wrap=WORD)
text_area.grid(column=0,pady=37,padx=400)

window.resizable(False, False)
window.mainloop()
