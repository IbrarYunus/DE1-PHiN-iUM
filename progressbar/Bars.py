#!/usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################################
# Component of upcoming Progress Module                             #
# Ibrar Yunus  University of St. Andrews                            #
# July 2018                                                         #
#####################################################################
#####################################################################


"""
Specification of the bar-type progress of processes

"""


import time
import libvlc as vlc

class Bars:
    duration = 0
    current = 0
    done = False

    clear = '_'
    fill = ' '
    edges = '[]'
    length = 20
    carriage_return = True
    display_duration = False
    units = ''
    display_edges = True

    def __init__(self, _duration, _current, _done = False):
        self.duration = _duration
        self.current = _current
        self.done = _done

    def set_params(self, _clear = '_', _fill = None, _edges = '[]', _length = 20, _carriage_return = True, _display_duration = True, _units = '', _display_edges = True):
        self.clear = _clear
        self.fill = _fill
        assert(len(_edges) == 2)
        self.edges = _edges
        self.length = _length
        self.carriage_return = _carriage_return
        self.display_duration = _display_duration
        self.units = _units
        self.display_edges = _display_edges


    def display(self):
        string_builder =''

        edge_start = self.edges[0]
        edge_end = self.edges[1]
        filled = int((self.current * self.length)/self.duration)



        if(self.display_edges == True):
            string_builder = string_builder + edge_start

        for x in range(0,filled):
            # print(self.fill, end='')
            string_builder = string_builder + self.fill

        for x in range(filled, self.length):
            # print(self.clear, end='')
            string_builder = string_builder + self.clear

        if(self.display_edges == True):
            string_builder = string_builder + edge_end

        if (self.display_duration == False):
            None
        else:
            string_builder = string_builder + str(self.current) + '/' + str(self.duration) + self.units



        if (self.carriage_return == False):
            print(string_builder)
        else:
            # print("'\r{0}".format(random.randint(1,200)), end='')
            print("\r" + string_builder, end='')
    #

    def next(self):
        self.current = self.current + 1
        self.display()

    def skip15(self):
        self.current = self.current + 15
        self.display()


#
# if __name__ == '__main__':
#     None
#     duration = 350
#     current = 1
#
#     print('creating new bars object')
#     a = Bars(345,100)
#     print('testing params setting')
#     a.set_params(_length=100, _carriage_return=True, _units=' seconds', _display_edges=False)
#     print('testing printing')
#     a.display()
#
#     for x in range(100,345):
#         time.sleep(0.09)
#         a.next()
#         # sys.stdout.flush()
#         # print('', flush=True)
#
