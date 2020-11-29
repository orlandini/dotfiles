#!/usr/bin/env python3
# https://askubuntu.com/questions/832720/how-can-i-center-a-window-with-a-keyboard-shortcut
# Author: Serg Kolo
# Date: Oct 3rd, 2016
# Description: Script for aligning the center of 
#     user's active window with the center of the monitor
# Tested on: Ubuntu 16.04
# Written for: http://askubuntu.com/q/832720/295286
from __future__ import print_function
import gi
gi.require_version('Gdk','3.0')
from gi.repository import Gdk
import subprocess

def get_offset(*args):
    command = ['xprop','-notype','_NET_FRAME_EXTENTS',
               '-id',str(args[0])
    ]

    out = subprocess.check_output(command)
    if 'not found' in out.decode():
        return 0
    return int(out.decode().strip().split(',')[-2])

def main():

    screen = Gdk.Screen.get_default()
    window = screen.get_active_window()
    window.unmaximize()
    window_width = window.get_width()
    window_height = window.get_height()

    window_monitor = screen.get_monitor_at_window(window)
    mon_g = screen.get_monitor_geometry(window_monitor)
    print(mon_g.width,mon_g.height)
    monitor_center_x = mon_g.x + mon_g.width/2
    monitor_center_y = mon_g.y + mon_g.height/2

    # if centers of window and screen are aligned
    new_position_x = monitor_center_x - window_width /2
    new_position_y = monitor_center_y - window_height /2

    window.move(new_position_x,new_position_y)
    print(window.get_origin()) 

if __name__ == '__main__':
    main()
