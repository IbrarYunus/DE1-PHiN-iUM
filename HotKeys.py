import threading

import keyboard
import time
import MusicHandler

class HotKeys:

    def display(self):

        print("////////////////////////////////////////////")
        print("-------------PLAYLIST CONTROLS-------------")
        print("CTRL + - _________Sequence Play____________")
        print("CTRL + = _________Shuffle Play_____________")
        print("\n--------------TRACK CONTROLS---------------")
        print("CTRL + 1 _________Previous Track___________")
        print("CTRL + 2 _________Next Track_______________")
        print("////////////////////////////////////////////")

    def activate(self, status, paths, files):
        musicHandler = MusicHandler.MusicHandler()


        # print('hotkeys defined')

        def handle_hotkey_1():
            print('////////////PLAY: SEQUENCE MODE')
            status.play_mode = 0

        def handle_hotkey_2():
            print('////////////PLAY: SHUFFLE MODE')
            status.play_mode = 1

        def handle_hotkey_3():
            if(status.track_playing == False):
                status.track_playing = True
                sequenceThread = threading.Thread(target=musicHandler.playtype_sequence, args=(status, files, paths,))
                sequenceThread.start()
                # musicHandler.playtype_sequence(status, files, paths)
            else:
                status.track_playing = False

        def handle_hotkey_4():
            status.next = True

        def handle_hotkey_5():
            status.prev = True


        # keyboard.on_press(handle_keystrokes)
        keyboard.add_hotkey('ctrl+-', handle_hotkey_1, args=None)
        keyboard.add_hotkey('ctrl+=', handle_hotkey_2, args=None)
        keyboard.add_hotkey('ctrl+3', handle_hotkey_3, args=None)
        keyboard.add_hotkey('ctrl+2', handle_hotkey_4, args=None)
        keyboard.add_hotkey('ctrl+1', handle_hotkey_5, args=None)

        while True:
            time.sleep(1)
