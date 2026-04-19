# Beginner Python Key Logger

This is a software surveillance tool that is able to listen to the keyboard and record every keystroke onto a txt file. I built it to understand how key logging works and the utility of it.

## What it does

- Listens to keyboard
- Create, open and write in a file
- Write every keystroke that is done onto a txt file
- Can be ended silently (Ends with a key not quitting)

## What I learned

- What key logging is
- how key logging works
- What and how to use the keyboard module in pynput
- How to open and write in a txt file
- How to use AttributeError in try/except
- The dangers of keylogging

## How to run it
- NOTE: Both files are the same but one contains the notes that explicitly
        explain everything while the other is just the code so you can read
        it easier.

1. Download or clone this repository
2. Have pynput installed
3. Run the keylogger
4. Start typing anything
   e.g. "Hello welcome to my key logger"
   This can be written anywhere and on anything, even on nothing
5. Press 'Esc' to stop logging
6. Type something else
   e.g. "Thank You for using my key logger"
7. Open the file named: keylog.txt

## Example output

"Hello welcome to my key logger"

## Limitations
- If any special keys like "Backspace" or "Shift" are used, it will show [BACKSPACE] or [Key.shift]
- Does not record mouse
- If paused, it cannot be started again without restarting the whole program

## Tools used

- Python 3
- pynput (pip install pynput)
- keylog.txt 

## Ethical Note
This tool was made for educational purposes only
Using this tool on any machine without permission is illegal
