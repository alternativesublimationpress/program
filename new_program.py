from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.text import Label as ButtonText
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import NumericProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.text import Label as CoreLabel

from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.lang import Builder
from kivy.clock import Clock
import math
import serial
import time as delay

import termios                                                                                                        

path = '/dev/ttyACM0'                                                                                                  
#path = 'COM4'
# Disable reset after hangup
# with open(path) as f:                                                                                                 
    attrs = termios.tcgetattr(f)                                                                                       
    attrs[2] = attrs[2] & ~termios.HUPCL                                                                               
    termios.tcsetattr(f, termios.TCSAFLUSH, attrs)                                                                     

MasterModule = serial.Serial(path, 115200)

Window.size = (1024, 600)

set_hours                       = 0
set_minutes                     = 0
set_seconds                     = 0
set_time                        = 0
set_time_2                      = 0

hours_1                         = 0
minutes_1                       = 0
seconds_1                       = 0
hours_2                         = 0
minutes_2                       = 0
seconds_2                       = 0

time_1                          = 0
time_2                          = 0
time_counter                    = 0

string_set_hours                = "00"
string_set_minutes              = "00"
string_set_seconds              = "00"

string_hours_1                  = "00"
string_minutes_1                = "00"
string_seconds_1                = "00"
string_hours_2                  = "00"
string_minutes_2                = "00"
string_seconds_2                = "00"

start                           = 1
counter                         = 0

remaining_time                  = 0

remaining_hours                 = 0
remaining_minutes               = 0
remaining_seconds               = 0

string_remaining_hours          = ""
string_remaining_minutes        = ""
string_remaining_seconds        = ""

readValue                       = 0
readMode                        = 0
readRelay                       = 10

which_time                      = 1

Builder.load_string("""


<MainMenu>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 1,1,1,.80
            Rectangle:
                pos: root.pos
                size: root.size
        orientation: 'vertical'
        color: (1,1,1,0)
        BoxLayout:
            canvas.before:
                Color:
                    rgba: 0,0,0, 0.75
                Rectangle:
                    pos: self.pos
                    size: self.size
            orientation: 'horizontal'
            size_hint: 1, .95
            orientation: 'horizontal'
            Label:
                size_hint: 0.025 ,1
            Label:
                text: 'SUBLIMATION PRESS SYSTEM'
                markup: 'True'
                font_size: self.parent.width/25
            Label:
                size_hint: 0.3 , 1
            Image:
                source: 'logo_white.png'
                size_hint: 0.3 , 1
            Label:
                size_hint: 0.05 , 1
        Label:
            size_hint: 1 , 1.1
        BoxLayout:
            size_hint: 1, 2.3
            Label:
                size_hint: .2, 1
            Button:
                background_color: 0, .6156, .48235, 1
                background_normal: ''
                text: '[b]SET MODE[b]'
                font_size: self.parent.width/35
                text_size: self.parent.width/8, None
                halign: 'center'
                valign: 'middle'
                markup: 'True'
                on_press: root.manager.current = 'set'
            Label:
                size_hint: .1, 1
            Button:
                background_color: 0, .6156, .48235, 1
                background_normal: ''
                text: '[b]RUN MODE[b]'
                font_size: self.parent.width/35
                text_size: self.parent.width/8, None
                halign: 'center'
                valign: 'middle'
                markup: 'True'
                on_press: root.manager.current = 'run'
            Label:
                size_hint: .1, 1
            Button:
                background_color: 0, .6156, .48235, 1
                background_normal: ''
                text: '[b]MANUAL MODE[b]'
                font_size: self.parent.width/35
                text_size: self.parent.width/8, None
                halign: 'center'
                valign: 'middle'
                markup: 'True'
                on_press: root.manager.current = 'manual'
            Label:
                size_hint: .1, 1
            Button:
                background_color: 0, .6156, .48235, 1
                background_normal: ''
                text: '[b]EXIT[b]'
                font_size: self.parent.width/35
                text_size: self.parent.width/8, None
                halign: 'center'
                valign: 'middle'
                markup: 'True'
                on_press: dupa
            Label:
                size_hint: .2, 1
        Label:
            size_hint: 1, 1
        BoxLayout:
            orientation: 'horizontal'
            Image:
                source: 'logo_black.png'
                size_hint: 2 , 2
        Label:
            size_hint: 1, .0025




<SetMode>:
    on_enter: root.display_to_set_time(); root.display_set_time()
    BoxLayout:
        canvas.before:
            Color:
                rgba: 1,1,1,.80
            Rectangle:
                pos: root.pos
                size: root.size
        orientation: 'vertical'
        color: (1,1,1,0)
        BoxLayout:
            canvas.before:
                Color:
                    rgba: 0,0,0, 0.75
                Rectangle:
                    pos: self.pos
                    size: self.size
            orientation: 'horizontal'
            size_hint: 1, .2
            orientation: 'horizontal'
            Label:
                size_hint: 0.025 ,1
            Label:
                text: 'SUBLIMATION PRESS SYSTEM'
                markup: 'True'
                font_size: self.parent.width/25
            Label:
                size_hint: 0.3 , 1
            Image:
                source: 'logo_white.png'
                size_hint: 0.3 , 1
            Label:
                size_hint: 0.05 , 1
        Label:
            size_hint: 1, .05
        BoxLayout:
            orientation: 'horizontal'
            Label:
                size_hint: .050 , 1
            BoxLayout:
                orientation: 'vertical'
                size_hint: .9, 1
                BoxLayout:
                    orientation: 'horizontal'
                    BoxLayout:
                        orientation: 'vertical'
                        Label:
                            size_hint: 1 ,.3
                        Label:
                            text: 'TIME 1'
                            font_size: self.parent.width/8.5
                            color: .1,.1,.1,.8
                            size_hint: 1, .4
                            halign: 'center'
                            valign: 'bottom'
                            text_size: self.parent.width, self.parent.height/5
                        Label:
                            size_hint: 1, .1
                        Label:
                            id: set_time_display_1
                            text: '00:00:00'
                            font_size: self.parent.width/5
                            color: .1,.1,.1,.8
                            size_hint: 1, .4
                    BoxLayout:
                        orientation: 'vertical'
                        Label:
                            size_hint: 1 ,.3
                        Label:
                            text: 'TIME 2'
                            font_size: self.parent.width/8.5
                            color: .1,.1,.1,.8
                            size_hint: 1, .4
                            halign: 'center'
                            valign: 'bottom'
                            text_size: self.parent.width, self.parent.height/5
                        Label:
                            id: set_time_display_2
                            text: '00:00:00'
                            font_size: self.parent.width/5
                            color: .1,.1,.1,.8
                            size_hint: 1, .4
                Label:
                    size_hint: 1, .3
                BoxLayout:
                    orientation: 'horizontal'
                    Label:
                        size_hint: .1 ,1
                    BoxLayout:
                        orientation: 'vertical'
                        Label:

                        Label:
                            text: '       SET TIME'
                            font_size: self.parent.width/9
                            color: .1, .1, .1, .8
                            halign: 'left'
                            valign: 'bottom'
                            text_size: self.parent.width, self.parent.height/5
                        Label:
                            id: to_set_time_display_1
                            text: '00:00:00'
                            font_size: self.parent.width/4
                            color: .1, .1, .1, .8
                            halign: 'left'
                            valign: 'middle'
                            text_size: self.parent.width*1.1, self.parent.height/5
                        Label:

                    Label:
                        size_hint: .2 ,1
                    BoxLayout:
                        orientation: 'vertical'
                        Button:
                            text: '[b]+30 SEC[b]'
                            background_color: .1, .1, .1, .8
                            background_normal: ''
                            font_size: self.parent.width/10
                            markup: 'True'
                            on_press: self.background_color = (1,1,1,1); root.add_30();root.display_to_set_time()
                            on_release: self.background_color = (.1, .1, .1, .8)
                        Label:
                            size_hint: 1 , .15
                        Button:
                            text: '[b]+15 SEC[b]'
                            background_color: .1, .1, .1, .8
                            background_normal: ''
                            font_size: self.parent.width/10
                            markup: 'True'
                            on_press: self.background_color = (1,1,1,1); root.add_15(); root.display_to_set_time()
                            on_release: self.background_color = (.1, .1, .1, .8)
                        Label:
                            size_hint: 1 , .15
                        Button:
                            text: '[b]+1 SEC[b]'
                            background_color: .1, .1, .1, .8
                            background_normal: ''
                            font_size: self.parent.width/10
                            markup: 'True'
                            on_press: self.background_color = (1,1,1,1); root.add_1(); root.display_to_set_time()
                            on_release: self.background_color = (.1, .1, .1, .8)
                    Label:
                        size_hint: .1 ,1
                    BoxLayout:
                        orientation: 'vertical'
                        Button:
                            text: '[b]-30 SEC[b]'
                            background_color: .1, .1, .1, .6
                            background_normal: ''
                            font_size: self.parent.width/10
                            markup: 'True'
                            on_press: self.background_color = (1,1,1,1); root.minus_30(); root.display_to_set_time()
                            on_release: self.background_color = (.1, .1, .1, .6)
                        Label:
                            size_hint: 1 , .15
                        Button:
                            text: '[b]-15 SEC[b]'
                            background_color: .1, .1, .1, .6
                            background_normal: ''
                            font_size: self.parent.width/10
                            markup: 'True'
                            on_press: self.background_color = (1,1,1,1); root.minus_15(); root.display_to_set_time()
                            on_release: self.background_color = (.1, .1, .1, .6)
                        Label:
                            size_hint: 1 , .15
                        Button:
                            text: '[b]-1 SEC[b]'
                            background_color: .1, .1, .1, .6
                            background_normal: ''
                            font_size: self.parent.width/10
                            markup: 'True'
                            on_press: self.background_color = (1,1,1,1); root.minus_1(); root.display_to_set_time()
                            on_release: self.background_color = (.1, .1, .1, .6)
            Label:
                size_hint: .05 , 1
            BoxLayout:
                orientation: 'vertical'
                size_hint: .3 , 1
                Button:
                    background_color: .1, .1, .1, .8
                    background_normal: ''
                    text: '[b]MAIN MENU[b]'
                    font_size: self.parent.width/8
                    text_size: self.parent.width/2, None
                    halign: 'center'
                    valign: 'middle'
                    markup: 'True'
                    on_press: root.manager.current = 'main'
                Label:
                    size_hint: 1 , .2
                Button:
                    id: button_set_time_1
                    background_color: 0, .6156, .48235, 1
                    background_normal: ''
                    text: '[b]SET TIME 1 [b]'
                    font_size: self.parent.width/8
                    text_size: self.parent.width, None
                    halign: 'center'
                    valign: 'middle'
                    markup: 'True'
                    on_press: self.background_color = (1,1,1,1); root.fix_time_1(); root.display_set_time()
                    on_release: self.background_color = (0, .6156, .48235, 1)
                Label:
                    size_hint: 0.075,0.2
                Button:
                    id: button_set_time_2
                    background_color: 0, .6156, .48235, 1
                    background_normal: ''
                    text: '[b]SET TIME 2[b]'
                    font_size: self.parent.width/8
                    text_size: self.parent.width, None
                    halign: 'center'
                    valign: 'middle'
                    markup: 'True'
                    on_press: self.background_color = (1,1,1,1); root.fix_time_2(); root.display_set_time()
                    on_release: self.background_color = (0, .6156, .48235, 1)
                    disabled: True
            Label:
                size_hint: .050, 1
        Label:
            size_hint: 1 , .08




<RunMode>:
    on_enter: root.display_time(); root.change_ConnectReset_label()
    BoxLayout:
        canvas.before:
            Color:
                rgba: 1,1,1,.80
            Rectangle:
                pos: root.pos
                size: root.size
        orientation: 'vertical'
        color: (1,1,1,0)
        BoxLayout:
            canvas.before:
                Color:
                    rgba: 0,0,0, 0.75
                Rectangle:
                    pos: self.pos
                    size: self.size
            orientation: 'horizontal'
            size_hint: 1, .2
            orientation: 'horizontal'
            Label:
                size_hint: 0.025 ,1
            Label:
                text: 'SUBLIMATION PRESS SYSTEM'
                markup: 'True'
                font_size: self.parent.width/25
            Label:
                size_hint: 0.3 , 1
            Image:
                source: 'logo_white.png'
                size_hint: 0.3 , 1
            Label:
                size_hint: 0.05 , 1
        Label:
            size_hint: 1, .1
        BoxLayout:
            orientation: 'horizontal'
            Label:
                size_hint: .2 ,1
            BoxLayout:
                orientation: 'vertical'
                size_hint: 1.1, 1
                Label:
                    size_hint: 1, .4
                Label:
                    text: 'SET  TIME'
                    color: .1, .1, .1, .8
                    font_size: self.parent.width/8
                    halign: 'center'
                    valign: 'middle'
                Label:
                    size_hint: 1, 1
                Label:
                    id: run_mode_current_time
                    text: '00:00:00'
                    color: .1, .1, .1, .8
                    font_size: self.parent.width/6
                    halign: 'center'
                    valign: 'top'
                    text_size: self.parent.width, self.parent.height/3.5
                Label:
                    size_hint: 1, 1.2
                Label:
                    text: '[b]REMAINING[b]'
                    color: .8, 0, 0, 1
                    font_size: self.parent.width/6
                    halign: 'center'
                    valign: 'middle'
                    markup: 'True'
                Label:

                Label:
                    id: remaining_time
                    text: '[b]00:00:00[b]'
                    color: .8, 0, 0, 1
                    font_size: self.parent.width/4
                    halign: 'center'
                    valign: 'middle'
                    markup: 'True'
                Label:
            Label:
                size_hint: .3, 1
            BoxLayout:
                orientation: 'vertical'
                size_hint: 1.6 , 1
                Label:
                    text: '[b]STATUS[b]'
                    markup: 'True'
                    color: .1, .1, .1, .2
                    font_size: self.parent.width/10
                    halign: 'center'
                    valign: 'bottom'
                    size_hint: 1, .9
                    text_size: self.parent.width, None
                Label:
                    id: status_label
                    text: 'DISCONNECTED'
                    color: 1, 0, 0, .8
                    font_size: self.parent.width/10
                    halign: 'center'
                    valign: 'top'
                    size_hint: 1, .9
                    text_size: self.parent.width, self.parent.height/3.5
                Label:
                    size_hint: 1, .05
                BoxLayout:
                    orientation: 'horizontal'
                    size_hint: 1, 1.5
                    Button:
                        id: connect/reset
                        background_color: 0, .6156, .48235, 1
                        background_normal: ''
                        text: '[b]CONNECT[b]'
                        font_size: self.parent.width/17
                        text_size: self.parent.width, None
                        halign: 'center'
                        valign: 'middle'
                        markup: 'True'
                        on_press: self.background_color = (1,1,1,1); root.module_init()
                        on_release: self.background_color = (0, .6156, .48235, 1)
                    Label:
                        size_hint: .3, 1
                    Button:
                        background_color: .1, .1, .1, .8
                        background_normal: ''
                        text: '[b]MAIN MENU[b]'
                        font_size: self.parent.width/17
                        text_size: self.parent.width/4, None
                        halign: 'center'
                        valign: 'middle'
                        markup: 'True'
                        on_press: root.hold_counting(); root.module_sleep();root.manager.current = 'main'
            Label:
                size_hint: .2, 1
        Label:
            size_hint: 1, .075




<ManualMode>:
    on_enter: root.module_init()
    BoxLayout:
        canvas.before:
            Color:
                rgba: 1,1,1,.80
            Rectangle:
                pos: root.pos
                size: root.size
        orientation: 'vertical'
        color: (1,1,1,0)
        BoxLayout:
            canvas.before:
                Color:
                    rgba: 0,0,0, 0.75
                Rectangle:
                    pos: self.pos
                    size: self.size
            orientation: 'horizontal'
            size_hint: 1, .19
            orientation: 'horizontal'
            Label:
                size_hint: 0.025 ,1
            Label:
                text: 'SUBLIMATION PRESS SYSTEM'
                markup: 'True'
                font_size: self.parent.width/25
            Label:
                size_hint: 0.3 , 1
            Image:
                source: 'logo_white.png'
                size_hint: 0.3 , 1
            Label:
                size_hint: 0.05 , 1
        BoxLayout:
            orientation: 'vertical'
            Label:
                size_hint: 1, .2
            Label:
                text: '[b]STATUS[b]'
                markup: 'True'
                size_hint: 1, .2
                color: .1, .1, .1, .2
                font_size: self.parent.width/22
                halign: 'center'
                valign: 'top'
                size_hint: 1, .9
                text_size: self.parent.width, self.parent.height/8
            Label:
                id: manual_status_label
                text: 'DISCONNECTED'
                color: 1, 0, 0, 1
                font_size: self.parent.width/20
                halign: 'center'
                valign: 'top'
                size_hint: 1, .9
                text_size: self.parent.width, self.parent.height/4
            Label:
                size_hint: 1, .2
            BoxLayout:
                orientation: 'horizontal'
                size_hint: 1, 1.8
                Label:
                    size_hint: .6, 1
                Button:
                    background_color: 0, .6156, .48235, 1
                    background_normal: ''
                    text: '[b]UP[b]'
                    font_size: self.parent.width/35
                    text_size: self.parent.width/4, None
                    halign: 'center'
                    valign: 'middle'
                    markup: 'True'
                    on_press: self.background_color = (1,1,1,1); root.up()
                    on_release: self.background_color = (0, .6156, .48235, 1)
                Label:
                    size_hint: .3, 1
                Button:
                    background_color: 0, .6156, .48235, 1
                    background_normal: ''
                    text: '[b]DOWN[b]'
                    font_size: self.parent.width/35
                    text_size: self.parent.width/4, None
                    halign: 'center'
                    valign: 'middle'
                    markup: 'True'
                    on_press: self.background_color = (1,1,1,1); root.down()
                    on_release: self.background_color = (0, .6156, .48235, 1)
                Label:
                    size_hint: .3, 1
                Button:
                    background_color: .1, .1, .1, .8
                    background_normal: ''
                    text: '[b]MAIN MENU[b]'
                    font_size: self.parent.width/35
                    text_size: self.parent.width/12, None
                    halign: 'center'
                    valign: 'middle'
                    markup: 'True'
                    on_press: root.zero(); root.module_sleep(); root.manager.current = 'main'
                Label:
                    size_hint: .6, 1

        Label:
            size_hint: 1, .1





<InfoMode>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 1,1,1,.80
            Rectangle:
                pos: root.pos
                size: root.size
        orientation: 'vertical'
        color: (1,1,1,0)
        BoxLayout:
            canvas.before:
                Color:
                    rgba: 0,0,0, 0.75
                Rectangle:
                    pos: self.pos
                    size: self.size
            orientation: 'horizontal'
            size_hint: 1, .19
            orientation: 'horizontal'
            Label:
                size_hint: 0.025 ,1
            Label:
                text: 'SUBLIMATION PRESS SYSTEM'
                markup: 'True'
                font_size: self.parent.width/25
            Label:
                size_hint: 0.3 , 1
            Image:
                source: 'logo_white.png'
                size_hint: 0.3 , 1
            Label:
                size_hint: 0.05 , 1
            Label:
                text: 'Created by CiociaCoco'


""")

class uC:

    def serial_write(data_to_send):
        MasterModule.write(str(data_to_send).encode('utf-8'))
        MasterModule.flush()
        delay.sleep(0.01)

    def serial_clear():
        if (MasterModule.inWaiting() > 0):
            MasterModule.read(MasterModule.inWaiting())
            MasterModule.flush()

    def serial_read():
        myData = MasterModule.read(MasterModule.inWaiting())
        return myData

    def set_relay_up():

        global readRelay

        while (readRelay != 1):
            uC.serial_clear()
            uC.serial_write('AF1E')
            myData = uC.serial_read()
            readRelay = int(myData[2:3])

    def set_relay_down():

        global readRelay

        while (readRelay != 2):
            uC.serial_clear()
            uC.serial_write('AF2E')
            myData = uC.serial_read()
            readRelay = int(myData[2:3])

    def set_relay_zero():

        global readRelay

        while (readRelay != 3):
            uC.serial_clear()
            uC.serial_write('AF3E')
            myData = uC.serial_read()
            readRelay = int(myData[2:3])


class MainMenu(Screen):
    pass


class SetMode(Screen):

    def __init__(self, **kwargs):
        super(SetMode, self).__init__(**kwargs)
        Clock.schedule_interval(self.check_times, 0.01)

    def add_30(self):
        global set_time

        if (set_time < 7171):
            set_time = set_time + 30

    def add_15(self):
        global set_time

        if (set_time < 7186):
            set_time = set_time + 15

    def add_1(self):
        global set_time

        if (set_time < 7200):
            set_time = set_time + 1

    def minus_30(self):
        global set_time
        if (set_time > 29):
            set_time = set_time - 30

    def minus_15(self):
        global set_time
        if (set_time > 14):
            set_time = set_time - 15

    def minus_1(self):
        global set_time
        if (set_time > 0):
            set_time = set_time - 1

    def display_to_set_time(self):

        global set_hours
        global set_minutes
        global set_seconds
        global set_time
        global string_set_hours
        global string_set_minutes
        global string_set_seconds

        set_hours = int(math.floor(set_time / 3600))
        set_minutes = int(math.floor((set_time - set_hours * 3600) / 60))
        set_seconds = int(set_time - set_hours * 3600 - set_minutes * 60)

        if (set_hours >= 0 and set_hours < 10):
            string_set_hours = '0' + str(set_hours)
        else:
            string_set_hours = str(set_hours)

        if (set_minutes >= 0 and set_minutes < 10):
            string_set_minutes = '0' + str(set_minutes)
        else:
            string_set_minutes = str(set_minutes)

        if (set_seconds >= 0 and set_seconds < 10):
            string_set_seconds = '0' + str(set_seconds)
        else:
            string_set_seconds = str(set_seconds)

        label1 = self.ids['to_set_time_display_1']
        label1.text = string_set_hours + ":" + string_set_minutes + ":" + string_set_seconds

    def fix_time_1(self):

        global set_time
        global time_1
        global remaining_time

        time_1 = set_time
        remaining_time = time_1
        set_time = 0
        self.display_to_set_time()

    def fix_time_2(self):

        global time_2
        global set_time

        time_2 = set_time
        set_time = 0
        self.display_to_set_time()

    def display_set_time(self):

        global hours
        global minutes
        global seconds
        global time_1
        global time_2
        global string_hours_1
        global string_minutes_1
        global string_seconds_1
        global string_hours_2
        global string_minutes_2
        global string_seconds_2

        hours_1 = int(math.floor(time_1 / 3600))
        minutes_1 = int(math.floor((time_1 - hours_1 * 3600) / 60))
        seconds_1 = int(time_1 - hours_1 * 3600 - minutes_1 * 60)

        if (hours_1 >= 0 and hours_1 < 10):
            string_hours_1 = '0' + str(hours_1)
        else:
            string_hours_1 = str(hours_1)

        if (minutes_1 >= 0 and minutes_1 < 10):
            string_minutes_1 = '0' + str(minutes_1)
        else:
            string_minutes_1 = str(minutes_1)

        if (seconds_1 >= 0 and seconds_1 < 10):
            string_seconds_1 = '0' + str(seconds_1)
        else:
            string_seconds_1 = str(seconds_1)

        label2 = self.ids['set_time_display_1']
        label2.text = string_hours_1 + ":" + string_minutes_1 + ":" + string_seconds_1
        hours_2 = int(math.floor(time_2 / 3600))
        minutes_2 = int(math.floor((time_2 - hours_2 * 3600) / 60))
        seconds_2 = int(time_2 - hours_2 * 3600 - minutes_2 * 60)

        if (hours_2 >= 0 and hours_2 < 10):
            string_hours_2 = '0' + str(hours_2)
        else:
            string_hours_2 = str(hours_2)

        if (minutes_2 >= 0 and minutes_2 < 10):
            string_minutes_2 = '0' + str(minutes_2)
        else:
            string_minutes_2 = str(minutes)

        if (seconds_2 >= 0 and seconds_2 < 10):
            string_seconds_2 = '0' + str(seconds_2)
        else:
            string_seconds_2 = str(seconds_2)

        label3 = self.ids['set_time_display_2']
        label3.text = string_hours_2 + ":" + string_minutes_2 + ":" + string_seconds_2

    def check_times(self,*args):

        global time_1
        global time_2

        b_set_time_2 = self.ids['button_set_time_2']
        if (time_1 > 3):
            b_set_time_2.disabled = False
        else:
            b_set_time_2.disabled = True


class RunMode(Screen):
    def __init__(self, **kwargs):
        super(RunMode, self).__init__(**kwargs)
        Clock.schedule_interval(self.main_handling, 0.1)
        Clock.schedule_interval(self.read_module, 0.01)

    def display_time(self):

        global string_hours_1
        global string_minutes_1
        global string_seconds_1
        global string_hours_2
        global string_minutes_2
        global string_seconds_2
        global time_1
        global time_2
        global remaining_time
        global which_time

        label30 = self.ids['remaining_time']
        label3 = self.ids['run_mode_current_time']

        if (which_time == 1):
            label3.text = string_hours_1 + ":" + string_minutes_1 + ":" + string_seconds_1
            if (remaining_time == time_1):
                label30.text = '00:00:00'
        if (which_time == 2):
            label3.text = string_hours_2 + ":" + string_minutes_2 + ":" + string_seconds_2
            if (remaining_time == time_2):
                label30.text = '00:00:00'


    def main_handling(self, *args):

        global counter
        global remaining_time
        global start
        global string_remaining_hours
        global string_remaining_minutes
        global string_remaining_seconds
        global remaining_hours
        global remaining_minutes
        global remaining_seconds
        global which_time
        global string_hours_2
        global string_minutes_2
        global string_seconds_2

        label8 = self.ids['status_label']
        label5 = self.ids['remaining_time']
        label33 = self.ids['run_mode_current_time']

        if start > 1:
            counter = counter + 1

        if counter > 9 and start > 1:
            counter = 0
            if remaining_time > 0:
                remaining_time = remaining_time - 1

                remaining_hours = int(math.floor(remaining_time / 3600))
                remaining_minutes = int(math.floor((remaining_time - remaining_hours * 3600) / 60))
                remaining_seconds = int(remaining_time - remaining_hours * 3600 - remaining_minutes * 60)

                if (remaining_hours >= 0 and remaining_hours < 10):
                    string_remaining_hours = '0' + str(remaining_hours)
                else:
                    string_remaining_hours = str(set_hours)

                if (remaining_minutes >= 0 and remaining_minutes < 10):
                    string_remaining_minutes = '0' + str(remaining_minutes)
                else:
                    string_remaining_minutes = str(remaining_minutes)

                if (remaining_seconds >= 0 and remaining_seconds < 10):
                    string_remaining_seconds = '0' + str(remaining_seconds)
                else:
                    string_remaining_seconds = str(remaining_seconds)
                label5.text = string_remaining_hours + ":" + string_remaining_minutes + ":" + string_remaining_seconds
            else:
                counter = 0
                if (which_time == 1):
                    which_time = 2
                else:
                    which_time = 1
                if (which_time == 1):
                    remaining_time = time_1
                    label33.text = string_hours_1 + ":" + string_minutes_1 + ":" + string_seconds_1
                if (which_time == 2):
                    remaining_time = time_2
                    label33.text = string_hours_2 + ":" + string_minutes_2 + ":" + string_seconds_2
                start = 1
                label8.text = 'PRESSING FINISH'
                label8.color = (.15, .83, .15, .85)
                uC.set_relay_down()

    def module_init(self):

        global readMode
        global time_1
        global time_2
        global remaining_time
        global set_time
        global which_time

        label6 = self.ids['status_label']
        label15 = self.ids['connect/reset']
        label16 = self.ids['remaining_time']

        if (readMode == 2 and start != 2):
            label15.text = 'RESET TIME'
            label16.text = '00:00:00'
#            time_1 = set_time

        if (time_1 > 3):
            while (readMode != 2):
                uC.serial_write('AC2E')
                delay.sleep(0.02)
                myData = uC.serial_read()
                readMode = int(myData[2:3])
                if (readMode == 2):
                    label6.text = 'CONNECTED'
                    label15.text = 'RESET TIME'
                    label6.color = (.15, .83, .15, .85)
        else:
            label6.text = 'SET TIME MORON !'
            label6.color = (.15, .15, .15, .85)

    def module_sleep(self):

        global readMode
        label8 = self.ids['status_label']

        while (readMode != 1):
            uC.serial_write('AC1E')
            delay.sleep(0.02)
            myData = uC.serial_read()
            readMode = int(myData[2:3])
            if (readMode == 1):
                label8.text = 'DISCONNECTED'
                label8.color = (.83, .15, .15, .85)

    def read_module(self, *args):

        global readValue
        global readMode
        global start
        global readRelay
        global which_time

        label7 = self.ids['status_label']

        if (readMode == 2):
            if (MasterModule.inWaiting() < 1):
                uC.serial_write('AC3E')
            myData = uC.serial_read()
            if (str(myData[0:1].decode("utf-8")) == 'B'):
                try:
                    readValue = int(int(myData[2:3]) * 10 + int(myData[3:4]))
                except:
                    readValue = 0
            if (readValue == 1):
                start = 2
                label7.text = 'PRESSING'
                label7.color = (.15, .15, .83, .85)
                if (readValue == 1 and readRelay != 1):
                    uC.set_relay_up()

    def hold_counting(self):

        global start

        start = 1

    def change_ConnectReset_label(self):

        label17 = self.ids['connect/reset']
        label17.text = 'CONNECT'


class ManualMode(Screen):
    def change(self):

        sm.current = 'main'

    def module_init(self):

        global readMode
        global time_1

        label9 = self.ids['manual_status_label']

        while (readMode != 2):
            uC.serial_write('AC2E')
            delay.sleep(0.02)
            myData = uC.serial_read()
            readMode = int(myData[2:3])
            if (readMode == 2):
                label9.text = 'CONNECTED'
                label9.color = (.15, .83, .15, .85)

    def module_sleep(self):

        global readMode
        label12 = self.ids['manual_status_label']

        while (readMode != 1):
            uC.serial_write('AC1E')
            delay.sleep(0.02)
            myData = uC.serial_read()
            readMode = int(myData[2:3])
            if (readMode == 1):
                label12.text = 'DISCONNECTED'
                label12.color = (.83, .15, .15, .85)

    def read_module(self, *args):

        global readValue
        global readMode
        global start
        global readRelay

        label7 = self.ids['status_label']

        if (readMode == 2):
            if (MasterModule.inWaiting() < 1):
                uC.serial_write('AC3E')
            myData = uC.serial_read()
            if (str(myData[0:1].decode("utf-8")) == 'B'):
                try:
                    readValue = int(int(myData[2:3]) * 10 + int(myData[3:4]))
                except:
                    readValue = 0
            if (readValue == 1):
                start = 2
                label7.text = 'PRESSING'
                label7.color = (.15, .15, .83, .85)
                if (readValue == 1 and readRelay != 1):
                    uC.set_relay_up()

    def up(self):
        global readRelay
        label10 = self.ids['manual_status_label']

        if (readRelay == 1):
            label10.text = 'ITS UP U FAGGOT'

        while (readRelay != 1):
            uC.serial_clear()
            uC.serial_write('AF1E')
            myData = uC.serial_read()
            readRelay = int(myData[2:3])
            if (readRelay == 1):
                label10.text = 'UP'
                label10.color = (.83, .15, .15, .85)

    def down(self):
        global readRelay
        global remaining_time
        global time_1
        global time_2
        global which_time

        label11 = self.ids['manual_status_label']

        if (readRelay == 2):
            label11.text = 'ITS DOWN U FAGGOT'

        while (readRelay != 2):
            uC.serial_clear()
            uC.serial_write('AF2E')
            myData = uC.serial_read()
            readRelay = int(myData[2:3])
            if (readRelay == 2):
                if (remaining_time > 0):
                    if (which_time == 1):
                        remaining_time = time_1
                    if (which_time == 2):
                        remaining_time = time_2
                label11.text = 'DOWN'
                label11.color = (.15, .83, .15, .85)

    def zero(self):
        global readRelay

        while (readRelay != 3):
            uC.serial_clear()
            uC.serial_write('AF3E')
            myData = uC.serial_read()
            readRelay = int(myData[2:3])


class InfoMode(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainMenu(name='main'))
sm.add_widget(SetMode(name='set'))
sm.add_widget(RunMode(name='run'))
sm.add_widget(ManualMode(name='manual'))
sm.add_widget(InfoMode(name='info'))


class SubApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    SubApp().run()
