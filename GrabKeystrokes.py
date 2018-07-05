import curses


screen = curses.initscr()
curses.cbreak()
screen.keypad(1)
screen.addstr("Enter q to quit ")
screen.refresh()
key = ''
while key != ord('q'): key = screen.getch()
screen.addch(key)
screen.refresh()
curses.endwin()