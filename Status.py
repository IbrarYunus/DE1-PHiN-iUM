class Status:

    # defines the current playlist mode, valid options are:
    # 0 sequence play (default)
    # 1 randomized play
    play_mode = 0

    # stores the current playlist
    sequence_playlist = []

    shuffled_playlist = []

    # True is any song is currently playing, False otherwise
    track_playing = False

    # Current index of the song in the playlist
    track_index = 0

    # pointer to the current song
    track = None

    next = False

    prev = False