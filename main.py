import time
import keyboard

def do_phrase(phrase, pause_for):
    time.sleep(pause_for)
    keyboard.write(phrase)
    keyboard.send('enter')
    if keyboard.is_pressed('esc'):
        return


def main():
    """Setup keyboard shortcuts"""

    while True:
        do_phrase("furyiff", 17)


if __name__ == "__main__":
    main()
