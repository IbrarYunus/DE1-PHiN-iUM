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
import threading

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
from mutagen.mp3 import MP3


class MusicHandler:

    def playtype_sequence(self,status,files, paths):
        total = len(files)
        assert(len(files) == len(paths))

        instance = vlc.Instance()
        player = instance.media_player_new()

        x = 0

        while x < total:
            x = x + 1

            path = paths[x]
            name = files[x]

            media = instance.media_new(path)
            media.parse()
            media.get_duration()
            # instance = vlc.Instance()
            # player = instance.media_player_new()
            media = instance.media_new(path)

            player.set_media(media)

            player.play()
            # vlc.libvlc_media_parse(p_md=path)
            # time.sleep(1.5)

            audio = MP3(path)

            duration = audio.info.length
            # print(duration)
            print('\n' + str(int(duration / 60)) + ' minutes  ' + str(int(duration % 60)) + ' seconds', end=" --- ")
            print('playing :: ' + name)

            progress = Bars(int(duration), 1)
            progress.set_params(_length=100, _carriage_return=True, _units=' seconds', _display_edges=False)
            progress.display()

            for y in range(int(duration)):
                if (status.next == True):
                    status.next = False
                    player.stop()
                    break

                if (status.prev == True):
                    status.prev = False
                    player.stop()
                    x = x-2
                    break

                time.sleep(1)
                progress.next()



            # while(playThread.isAlive):
            #     if(status.next) == True:
            #
            #         status.next = False
            #
            #         break;


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
        progress.set_params(_length=100, _carriage_return=True, _units=' seconds', _display_edges=False)
        progress.display()

        for x in range(int(duration)):
            time.sleep(1)
            progress.next()



    def play_song_progress(duration):
        None


    def handle_keystrokes(master_thread, files, paths):
        None


