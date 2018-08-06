import keyboard
import time
import threading


def define_hotkeys():
    print('hotkeys defined')

    def handle_hotkey_1():
        print('CTRL- PRESSED')

    def handle_hotkey_2():
        print('CTRL= PRESSED')

    # keyboard.on_press(handle_keystrokes)
    keyboard.add_hotkey('ctrl+-', handle_hotkey_1, args=None)
    keyboard.add_hotkey('ctrl+=', handle_hotkey_2, args=None)

    while True:
        time.sleep(1)

def print_nums():
    print('aaaaaaaaa')
    for x in range (1,100000):
        print('num: ' + str(x), flush=True)
        time.sleep(1)

# def key_press(key):
#     print(key.name)
#
# keyboard.on_press(key_press)

if __name__ == '__main__':
    print('fresh start')
    thread_1 = threading.Thread(target=define_hotkeys)
    thread_2 = threading.Thread(target=print_nums)
    thread_2.start()
    thread_1.start()

