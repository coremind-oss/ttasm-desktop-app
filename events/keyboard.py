import enum
from threading import Thread
import types

from pynput import keyboard


class KeyboardEvents():
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if not isinstance(value, types.FunctionType):
                raise Exception('expected a callback function, found {}'.format(type(value)))
            else:
                setattr(self, key, value)

    def on_press(self, key = None):

        print('\n------->|{0}|<-- pressed, start function pressing button f12'.format(key))
        if isinstance(key, enum.Enum):
            print(type(key))
            
        if key == keyboard.Key.f12:
            print('\n------->We press regular button to trigger a function present_timestamp_form() from tray.py')

            

    def on_release(self, key):
        try:
            print('-------> {0} released'.format(key))
            if key == keyboard.Key.esc:
                # Stop listener
                return False
            
        except AttributeError:
            print('------->special key {0} pressed'.format(
                key))
    
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
        
    
    