import threading
import random
import keyboard
import time

import sys

import os

import MusicHandler
from random import shuffle

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
            print('\033[1;96;49m\n////////////PLAY: SEQUENCE MODE\033[0m')
            status.play_mode = 0

        def handle_hotkey_2():
            print('\033[1;96;49m\n////////////PLAY: SHUFFLE MODE\033[0m')
            status.play_mode = 1

        def handle_hotkey_3():

            if(status.track_playing == False and status.player != None):
                status.player.play()
                status.track_playing = True

            if(status.track_playing == True and status.player != None):
                status.player.stop()
                status.track_playing = False

            if(status.track_playing == False and status.player == None):

                if(status.play_mode == 0):
                    status.track_playing = True
                    sequenceThread = threading.Thread(target=musicHandler.playtype_sequence,
                                                      args=(status, files, paths,))
                    sequenceThread.start()

                if(status.play_mode == 1):

                    files_shuf = []
                    paths_shuf = []

                    index_shuf = list(range(len(files)))
                    random.shuffle(index_shuf)

                    for i in index_shuf:
                        files_shuf.append(files[i])
                        paths_shuf.append(paths[i])



                    status.track_playing = True
                    sequenceThread = threading.Thread(target=musicHandler.playtype_sequence,
                                                      args=(status, files_shuf, paths_shuf,))
                    sequenceThread.start()

                # musicHandler.playtype_sequence(status, files, paths)
            else:
                status.track_playing = False

        def handle_hotkey_4():
            status.next = True

        def handle_hotkey_5():
            status.prev = True

        def handle_hotkey_6():
            status.seek_forward = True

        def exit():
            os._exit(0)


        # keyboard.on_press(handle_keystrokes)
        keyboard.add_hotkey('ctrl+-', handle_hotkey_1, args=None)
        keyboard.add_hotkey('ctrl+=', handle_hotkey_2, args=None)
        keyboard.add_hotkey('ctrl+3', handle_hotkey_3, args=None)
        keyboard.add_hotkey('ctrl+2', handle_hotkey_4, args=None)
        keyboard.add_hotkey('ctrl+1', handle_hotkey_5, args=None)
        keyboard.add_hotkey('ctrl+5', handle_hotkey_6, args=None)
        keyboard.add_hotkey('ctrl+q', exit, args=None)

        while True:
            time.sleep(1)
