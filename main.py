import PySimpleGUI as sg
from pynput import keyboard
import asyncio
import pyautogui


i = 0
charlist = ["",""]
def kisayol(key):
    try:
        print('{0} '.format(key.char))
        charlist[0] = charlist[1]
        charlist[1] = format(key.char)
    except AttributeError:
        print('{0}'.format(key))
        charlist[0] = charlist[1]
        charlist[1] = format(key)
    print(charlist)
    if str(format(key)) == "Key.home":
        with pyautogui.hold('ctrlleft'):
            pyautogui.press('t') 
    if charlist[0] == 'Key.ctrl_l' and charlist[1] == 'Key.shift':
        with pyautogui.hold('ctrlleft'):
            pyautogui.press('t') 
    if i == 0:
        
        return False


        
#**********GUI****************  



layout = [[sg.Text("Kısayol programını Aç/Kapa")], [sg.Button("Aç")], [sg.Button("Kapa")]]


window = sg.Window("Kısayolcu", layout, margins=(75, 50))

while True:
    
    event, values = window.read()
    
    if event == "Aç" or event == sg.WIN_CLOSED:
        i = 1
            

        
        listener = keyboard.Listener(on_release=kisayol)
        listener.start()
    if event == "Kapa" or event == sg.WIN_CLOSED:
        i = 0
        window.close()
        break

    print(i)
    




