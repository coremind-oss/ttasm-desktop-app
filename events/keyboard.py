from pynput import keyboard
from threading import Thread


class KeyboardEvents():
    


    def on_press(self, key = None):

        print('\n------->{0} pressed, start function pressing button f12'.format(key))
        if key == keyboard.Key.f12:
            
########### how to call here present_timestamp_form() ?
            
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
         
    def show_message_window(self):
        self.listener.on_press()
    
    def listener(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as self.listener:
            self.listener.join()
        
    
    