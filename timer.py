import PySimpleGUI as sg
import time
from playsound import playsound


def timer1(timerr):
    sg.change_look_and_feel('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Timer')],
              [sg.Text('t', key='--timer--'), ],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Timer', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=100)
        if event =='Cancel':  # if user closes window or clicks cancel
            break

        print(timerr)
        while timerr >= 0:
            time.sleep(1)
            timerr = timerr - 1
            window['--timer--'].update(timerr)
            window.refresh()
        window.refresh()
        window['--timer--'].update('Time up')

        playsound('C:/Users/USER/Downloads/Telegram Desktop/SVATI/ios_notification.mp3')
        break
    window.close()


