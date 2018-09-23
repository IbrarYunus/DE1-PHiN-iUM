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

"""
Plays music!
"""
from os.path import dirname

import Header
import xml.etree.ElementTree as ET
import MusicHandler
import Status
import HotKeys
import _thread
import threading
import time
from os import walk, path, get_terminal_size
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
    # print("\033[12;23f\033[30m" + truncate_middle(files[0], 20) + "\033[0m")
    # print("\033[12;23f\033[37m" + truncate_middle(files[1], 20) + "\033[0m")
    # print("\033[12;23f\033[90m" + truncate_middle(files[2], 20) + "\033[0m\n")

    print("\033[0m")
    print("\033[1;47;49m" + truncate_middle(files[0], 20))
    print("\033[0;37;49m" + truncate_middle(files[1], 20))
    print("\033[0;90;49m" + truncate_middle(files[2], 20) + "\n")


def read_persistence():
    persistenceDict = {}

    tree = ET.parse(dirname(__file__) + '/persistence.xml')
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

    print("\033[1;96;49m[previously used directory] \033[1;95;49m" + oldPersistence['previousLocation-directory'])
    directory = input("\033[1;96;49mEnter directory or press ENTER to load previous: ")

    if (directory == ""):
        print('\033[1;96;49m[!] using previously used directory')
        directory = oldPersistence['previousLocation-directory']
    else:
        updatePersistence = {'previousLocation-directory': directory}
        write_persistence(updatePersistence)

    print("\033[1;96;49m[dir] \033[1;95;49m" + directory)
    print("\033[1;96;49m[file list]")
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
    None


    # master_thread = _thread.start_new_thread(MusicHandler.playtype_sequence, (files, paths))
    # master_thread = threading.Thread(target = MusicHandler.playtype_sequence, args = (files, paths))
    # master_thread.start()


if __name__ == "__main__":
    # width = get_terminal_size().columns


    Header.display_header()
    paths, files = load_files()

    status = Status.Status()

    hotkeys = HotKeys.HotKeys()
    hotkeys.display()

    hotkey_thread = threading.Thread(target = hotkeys.activate, args=(status, paths, files,))
    hotkey_thread.start()

    initialize_display(files, paths)


"""
TODO: solve the multi-threaded keypress issue
"""
