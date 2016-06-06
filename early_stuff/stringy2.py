#! /usr/bin/python

import random

name = ['Alex', 'Efecan', 'Grace']
greeting = [ 'welcome', 'sup', 'howdy', 'good afternoon']
space = ['\n', ' ', '\t']


def random_item( list ):
    return list[ random.randint(0, len(list) - 1 )]

