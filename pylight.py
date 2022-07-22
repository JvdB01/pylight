import re
import brightness
import PySimpleGUI as sg
from screeninfo import get_monitors as gm

resolution = str(gm()[0])
width  = re.search("(?<=width=).*?(?=,)", resolution)[0]
height = re.search("(?<=height=).*?(?=,)", resolution)[0]
sg.theme('SystemDefault')
old = brightness.view()
brightness.set(255)
sg.Window(title="PyLight", layout=[[]], margins=(width,height)).read()
brightness.set(old)
