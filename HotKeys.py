"""
 __         _           _         __
( '\___      \_  (^)  _/      ___/' )
 \ , ' \____   \ / \ /   ____/ ' , /
  \__ ' , ' \___{~V~}___/ ' , ' __/
 ____\_________ {<!>} _________/____
/ , ' , ' , ' ,`{<!>}~, ' , ' , ' , \
\_____________ /{<!>}\______________/
                 \./
                 (~)
                 (~)
                 (~)
                 (~)
                 (~)
                 (~)
                 ,0,
                  "
 * Author: Ibrar Yunus
 * <University of St. Andrews>
 * <Queries:      yunus.ibrar@gmai.com>
 * United Kingdom
 * ------------------------------------
 * Setup Details:
 * ---------- Lenovo Y700 Gaming Laptop
 * ------------------------- Windows 10
 * ------------------------- Python 3.6
 * --------------------- PyCharm 2017.3
 * --------- Interfaced with VLC Player
"""

import threading
import random
import keyboard
import time
import os
import MusicHandler

""" CLASS:
    Defines and activates the hotkeys
"""
class HotKeys:

    """ METHOD:
        Displays the available hotkeys
    """
    def display(self):
        print("\033[1;91;49m////////////////////////////////////////////")
        print("-------------PLAYLIST CONTROLS-------------")
        print("CTRL + - _________Sequence Play____________")
        print("CTRL + = _________Shuffle Play_____________")
        print("\n--------------TRACK CONTROLS---------------")
        print("CTRL + 1 _________Previous Track___________")
        print("CTRL + 2 _________Next Track_______________")
        print("CTRL + 3 _________Play/Pause_______________")
        print("CTRL + 4 _________Seek Forward_____________")
        print("CTRL + 5 _________Seek Backward____________")
        print("\n--------------OTHER CONTROLS---------------")
        print("CTRL + Q _________Exit_____________________")
        print("////////////////////////////////////////////")

    """ METHOD:
        Maps inner methods to hotkeys
    """
    def activate(self, status, paths, files):
        musicHandler = MusicHandler.MusicHandler()

        """ INNER METHOD:
            Changes playtype to sequence
        """
        def handle_hotkey_1():
            print('\033[1;96;49m\n////////////PLAY: SEQUENCE MODE\033[0m')
            status.play_mode = 0

        """ INNER METHOD:
            Changes playtype to random
        """
        def handle_hotkey_2():
            print('\033[1;96;49m\n////////////PLAY: SHUFFLE MODE\033[0m')
            status.play_mode = 1

        """ INNER METHOD:
            Plays/Stops the track
        """
        def handle_hotkey_3():
            # FIXME: Inspect and solve this
            # if(status.paused == True and status.track_playing == False):
            #     # status.player.play()
            #     status.paused = False
            #     status.track_playing = True
            #
            if(status.paused == False and status.player != None):
                # status.player.stop()
                status.paused = True
                # status.track_playing = False
                status.player.pause()
                # print("GONNA PAUSE")

            elif(status.paused == True):
                status.paused = False
                status.player.play()
                # print("GONNA UNPAUSE")

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

            else:
                status.track_playing = False

        """ INNER METHOD:
            Sets status.next to True
        """
        def handle_hotkey_4():
            status.next = True

        """ INNER METHOD:
            Sets status.prev to True
        """
        def handle_hotkey_5():
            status.prev = True

        """ INNER METHOD:
            Sets status.seek_forward to true
        """
        def handle_hotkey_6():
            status.seek_forward = True

        """ INNER METHOD:
            Sets status.seek_backward to true
        """
        def handle_hotkey_7():
            status.seek_backward = True

        """ INNER METHOD:
            Exits the application
        """
        def exit():
            os._exit(0)

            keyboard.add_hotkey('ctrl+-', handle_hotkey_1, args=None)
        keyboard.add_hotkey('ctrl+=', handle_hotkey_2, args=None)
        keyboard.add_hotkey('ctrl+3', handle_hotkey_3, args=None)
        keyboard.add_hotkey('ctrl+2', handle_hotkey_4, args=None)
        keyboard.add_hotkey('ctrl+1', handle_hotkey_5, args=None)
        keyboard.add_hotkey('ctrl+5', handle_hotkey_6, args=None)
        keyboard.add_hotkey('ctrl+4', handle_hotkey_7, args=None)
        keyboard.add_hotkey('ctrl+q', exit, args=None)

        while True:
            time.sleep(1)
