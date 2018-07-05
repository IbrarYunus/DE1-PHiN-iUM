import keyboard
import time

def test_1(key):
    if(key.name == 'a'):
        print('in test one, ')

def test_2():
    None
#
# def key_press(key):
#     print(key.name)
#
# keyboard.on_press(key_press)

if __name__ == '__main__':

    keyboard.on_press(test_1)

    while True:
        time.sleep(1)
