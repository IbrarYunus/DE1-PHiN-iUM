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

""" CLASS:
    Used to define and stats current status of the
    application
"""
class Status:

    """
        defines the current playlist mode, valid options are:
        0 sequence play (default)
        1 randomized play
    """
    play_mode = 0


    """
        Stores the current sequence playlist
    """
    sequence_playlist = []

    """
        Stores the current randomized playlist
    """
    shuffled_playlist = []

    """
        True is any song is currently playing, False otherwise
    """
    track_playing = False

    """
        Current index of the song in the playlist
    """
    track_index = 0

    """
        Pointer to the current song
    """
    player = None

    """
        True if hotkey for NEXT_SONG is just pressed. False otherwise
    """
    next = False

    """
        True if hotkey for PREVIOUS_SONG is just pressed. False otherwise
    """
    prev = False

    """
        True if hotkey for PAUSE_SONG is jst pressed. False otherwise
    """
    pause = False

    """
        True if hotkey for SEEKING FORWARD is just pressed. False otherwise
    """
    seek_forward = False

    """
        True if hotkey for SEEKING BACKWARD is just pressed. False otherwise
    """
    seek_backward = False

    """
        True if song is currently PAUSED
    """
    paused = False