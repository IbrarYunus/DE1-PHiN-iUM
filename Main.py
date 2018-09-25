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

from os.path import dirname
import Header
import xml.etree.ElementTree as ET
import Status
import HotKeys
import threading
from os import walk, path


""" METHOD:
    Prints the first 3 read files 
    beautifully 
"""
def beautifully_print_files(files):
    def truncate_middle(s, n):
        if len(s) <= n:
            return s
        return s[:11] + " ... " + s[-7:]

    print("")
    print("\033[0m")
    print("\033[1;47;49m" + truncate_middle(files[0], 20))
    print("\033[0;37;49m" + truncate_middle(files[1], 20))
    print("\033[0;90;49m" + truncate_middle(files[2], 20) + "\n")

""" METHOD: 
    Read the persistence XML file
"""
def read_persistence():
    persistenceDict = {}

    tree = ET.parse(dirname(__file__) + '/persistence.xml')
    root = tree.getroot()
    # print(root.find('previousLocation').attrib['directory'])

    persistenceDict['previousLocation-directory'] = root.find('previousLocation').attrib['directory']

    return persistenceDict

""" METHOD:
    Writes the persistence XML file; the XML file stores
    path to previously used music directory, play-counts,
    etc. 
"""
def write_persistence(updatePersistence):
    data = ET.Element('data')
    previousLocation = ET.SubElement(data, 'previousLocation')
    previousLocation.set('directory', updatePersistence['previousLocation-directory'])

    persistenceObject = ET.tostring(data, encoding="unicode")
    persistenceFile = open("persistence.xml", "w")
    persistenceFile.write(persistenceObject)

""" METHOD: 
    Loads the persistence XML file 
    and creates a list of paths,file-names in the
    music directory
"""
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

""" DEPRECIATED METHOD:
    ...
"""
def initialize_display(files, paths):
    None

""" METHOD:
    The main method
"""
if __name__ == "__main__":
    Header.display_header()
    paths, files = load_files()
    status = Status.Status()
    hotkeys = HotKeys.HotKeys()
    hotkeys.display()

    hotkey_thread = threading.Thread(target = hotkeys.activate, args=(status, paths, files,))
    hotkey_thread.start()

    initialize_display(files, paths)



# FIXME: solve the multi-threaded keypress issue
