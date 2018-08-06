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


import Header
import xml.etree.ElementTree as ET
import MusicHandler
import _thread
import threading
import time
from os import walk, path
import keyboard


def beautifully_print_files(files):
    def truncate_middle(s, n):
        if len(s) <= n:
            # string is already short-enough
            return s
        return s[:11] + " ... " + s[-7:]

    print("")
    # if(len(files) >= 3):
    #     print("\036[0m" + files[0])
    #     print("\033[0m" + files[1])
    #     print("\033[0m" + files[2])
    print("\033[12;23f\033[30m" + truncate_middle(files[0], 20) + "\033[0m")
    print("\033[12;23f\033[37m" + truncate_middle(files[1], 20) + "\033[0m")
    print("\033[12;23f\033[90m" + truncate_middle(files[2], 20) + "\033[0m")


def read_persistence():
    persistenceDict = {}

    tree = ET.parse('persistence.xml')
    root = tree.getroot()
    # print(root.find('previousLocation').attrib['directory'])

    persistenceDict['previousLocation-directory'] = root.find('previousLocation').attrib['directory']

    return persistenceDict


def write_persistence(updatePersistence):
    data = ET.Element('data')
    previousLocation = ET.SubElement(data, 'previousLocation')
    previousLocation.set('directory', updatePersistence['previousLocation-directory'])

    persistenceObject = ET.tostring(data, encoding="unicode")
    persistenceFile = open("persistence.xml", "w")
    persistenceFile.write(persistenceObject)


def load_files():
    oldPersistence = read_persistence()

    print("[previously used directory] " + oldPersistence['previousLocation-directory'])
    directory = input("Enter directory or press ENTER to load previous: ")

    if (directory == ""):
        print('[!] using previously used directory')
        directory = oldPersistence['previousLocation-directory']
    else:
        updatePersistence = {'previousLocation-directory': directory}
        write_persistence(updatePersistence)

    print("[dir] " + directory)
    print("[file list]")
    files = []
    paths = []
    for (dirpath, dirnames, filenames) in walk(directory):
        files.extend(filenames)
        for x in files:
            paths.append(path.join(dirpath, x))
        break

    beautifully_print_files(files)

    return paths, files


def initialize_display(files, paths):
    print('Select MODE with CTRL+- and CTRL+= keys')
    print('NEXT SONE :: 2')
    print('PREV SONG :: 1')

    # master_thread = _thread.start_new_thread(MusicHandler.playtype_sequence, (files, paths))
    master_thread = threading.Thread(target = MusicHandler.playtype_sequence, args = (files, paths))
    master_thread.start()

    sequence_flag = 1
    random_flag = 0

    print(master_thread)

    def handle_hotkey_1():
        print('hotkey-1')
        nonlocal sequence_flag
        nonlocal master_thread
        nonlocal random_flag

        if (sequence_flag == 0):
            sequence_flag = 1
            random_flag = 0
            master_thread.join()
            # master_thread = _thread.start_new_thread(MusicHandler.playtype_sequence, (files, paths))
            print('playlist mode :: sequence')

    def handle_hotkey_2():
        print('hotkey-2')
        nonlocal sequence_flag
        nonlocal master_thread
        nonlocal random_flag

        if (random_flag == 0):
            random_flag = 1
            sequence_flag = 0
            master_thread.join()
            # master_thread = _thread.start_new_thread(MusicHandler.playtype_sequence(files, paths))
            print('playlist mode :: shuffle')

    # keyboard.on_press(handle_keystrokes)
    keyboard.add_hotkey('ctrl+-', handle_hotkey_1, args=None)
    keyboard.add_hotkey('ctrl+=', handle_hotkey_2, args=None)

    while True:
        time.sleep(1)


if __name__ == "__main__":
    print("displaying graphic")
    Header.display_header()
    paths, files = load_files()
    initialize_display(files, paths)


"""
TODO: solve the multi-threaded keypress issue
"""
