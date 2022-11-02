from module.utils import *

clear()

print_introduction()

while True:
    input_choice = input("Enter your choice text or voice: ")
    if input_choice == 'text' or input_choice == 'voice':
        break
    else:
        print("[Invalid choice][Valid Options: text, voice]")

main_cmd(input_choice)