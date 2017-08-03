from threading import Thread
import types

from pynput import keyboard

import tray


class KeyboardEvents():
        
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if type(value) not in [types.FunctionType, types.MethodType, tray.Signal]:
                raise Exception('expected a callback function, found {}'.format(type(value)))
            else:
                setattr(self, key, value)

    def on_press(self, key = None):
        if key == keyboard.Key.f12:
            if hasattr(self, 'f12'): self.f12.send()

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False
    
    def start_listening(self):
        t = Thread(target=self.listener)
        t.start()
        
    def stop_listener(self):
        self.listener.on_release(keyboard.Key.esc)
    
    def listener(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as self.listener:
            self.listener.join()
        
    
    