#!/usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################################
# Music Player Project                                              #
# Ibrar Yunus  University of St. Andrews                            #
# July 2018                                                         #
#####################################################################
#####################################################################


"""
Plays all kinds of media files

"""

"""

  _____        _____        _____
 /     \      /     \      /     \
<       >----<       >----<       >
 \_____/      \_____/      \_____/
 /     \      /     \      /     \
<       >----<       >----<       >----.
 \_____/      \_____/      \_____/      \
       \      /     \      /     \      /
        >----<       >----<       >----<
       /      \_____/      \_____/      \_____
       \      /     \      /     \      /     \
        `----<       >----<       >----<       >
              \_____/      \_____/      \_____/
                           /     \      /
                          <       >----'
                           \_____/

"""

import libvlc as vlc
import keyboard
import time
import _thread
import random
from progressbar.Bars import Bars

def playtype_sequence(files, paths):
    total = len(files)
    assert(len(files) == len(paths))

    for x in range (0, total):
        play_thread = _thread.start_new_thread(play_path, (paths[x], files[x],))

        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('1'):
                    play_thread.join()
                    x = x - 1
                    if (x < 0):
                        x = 0
                    break
                elif keyboard.is_pressed('2'):
                    play_thread.join()
                    x = x + 1
                    break
                else:
                    pass
            except:
                None


def playtype_random(files, paths):

    # the shuffling operation
    shuffle = random.shuffle(list(zip(files, paths)))
    files, paths = zip(*shuffle)


    total = len(files)
    assert(len(files) == len(paths))

    for x in range (0, total):
        play_thread = _thread.start_new_thread(play_path, (paths[x], files[x],))

        while True:  # making a loop
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed('1'):
                    play_thread.join()
                    x = x - 1
                    if (x < 0):
                        x = 0
                    break
                elif keyboard.is_pressed('2'):
                    play_thread.join()
                    x = x + 1
                    break
                else:
                    pass
            except:
                None




def play_path(path, name):
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(path)

    player.set_media(media)

    player.play()
    time.sleep(1.5)

    duration = player.get_length() / 1000
    print(duration)
    print(str(int(duration/60)) + ' minutes  ' +  str(int(duration%60)) + ' seconds', end=" --- ")
    print('playing :: ' + name)

    progress = Bars(int(duration), 1)
    progress.set_params(_length=100, _carriage_return=True, _units=' seconds', _display_edges=False)
    progress.display()

    for x in range(int(duration)):
        time.sleep(1)
        progress.next()



def play_song_progress(duration):
    None


def handle_keystrokes(master_thread, files, paths):
    None


