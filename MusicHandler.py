#!/usr/bin/env python
# -*- coding: utf-8 -*-


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

from io import StringIO
import sys
import libvlc as vlc
import keyboard
import time
import _thread
import random
from progressbar.Bars import Bars
from mutagen.mp3 import MP3

""" CLASS:
    Handles playback, stoppping, pausing, skipping, reversing of 
    music files in the playlist
"""
class MusicHandler:

    """ METHOD:
        Plays the files (passes as the 'files' parameter) in
        sequence
        The passes Status() object is updated when the state of
        MusicHandler object changes (e.g.  when pausing a track, or
        skipping track)
    """
    def playtype_sequence(self,status,files, paths):
        total = len(files)
        assert(len(files) == len(paths))

        instance = vlc.Instance()
        status.player = instance.media_player_new()

        x = 0

        while x < total:
            x = x + 1

            path = paths[x]
            name = files[x]

            media = instance.media_new(path)
            media.parse()
            media.get_duration()

            media = instance.media_new(path)

            status.player.set_media(media)

            status.player.play()


            sys.stdout = StringIO();
            sys.stderr = StringIO();

            audio = MP3(path)

            duration = audio.info.length

            sys.stdout = sys.__stdout__;
            sys.stderr = sys.__stderr__;
            print('\n\033[1;30;105m ' + str(int(duration / 60)) + ' minutes  ' + str(int(duration % 60)) + ' seconds \033[1;39;49m', end=" --- ")
            print('playing :: ' + name)
            progress = Bars(int(duration), 1)
            progress.set_params(_length=100, _carriage_return=True, _units=' seconds', _display_edges=False, _fill='\033[1;35;49m>', _clear="\033[1;36;49m-")
            progress.display()
            status.track_playing = True

            while(((vlc.libvlc_media_player_get_time(status.player)/1000) <= duration)):

                if (status.next == True):
                    status.next = False
                    status.player.stop()
                    status.track_playing = False
                    break

                if (status.prev == True):
                    status.prev = False
                    status.player.stop()
                    status.track_playing = False
                    x = x-2
                    break

                if (status.track_playing != False):

                    progress.next()
                    time.sleep(1)

                if(status.seek_forward == True):
                    vlc.libvlc_media_player_set_time(status.player, vlc.libvlc_media_player_get_time(status.player) + (15*1000) + (1*1000))
                    status.seek_forward = False
                    progress.skip15()

                if (status.seek_backward == True):
                    vlc.libvlc_media_player_set_time(status.player,vlc.libvlc_media_player_get_time(status.player) - (15 * 1000) - (1 * 1000))
                    status.seek_backward = False
                    progress.rewind15()

                if (vlc.libvlc_media_player_is_playing(status.player) == False):
                    break


    """ DEPRECIATED METHOD!
        Shuffles songs before playing them
    """
    def playtype_random(self,files, paths):

        # the shuffling operation
        shuffle = random.shuffle(list(zip(files, paths)))
        files, paths = zip(*shuffle)


        total = len(files)
        assert(len(files) == len(paths))

        for x in range (0, total):
            play_thread = _thread.start_new_thread(self.play_path, (paths[x], files[x],))

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



    """ METHOD:
        Plays a song and generates it's progress bar
    """
    def play_path(self,path, name):
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
        progress.set_params(_length=100, _carriage_return=True, _units=' seconds', _display_edges=False, _fill='T')
        progress.display()

        for x in range(int(duration)):
            time.sleep(1)
            progress.next()
