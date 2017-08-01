from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(
        key))
  
def on_release(self, key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False
   
   
with Listener(
       on_press=on_press,
       on_release=on_release) as listener:
    listener.join()


# from pynput import keyboard
# 
# def on_press(key):
#     try: k = key.char # single-char keys
#     except: k = key.name # other keys
#     if key == keyboard.Key.esc: return False # stop listener
#     if k in ['1', '2', 'left', 'right']: # keys interested
#         # self.keys.append(k) # store it in global-like variable
#         print('Key pressed: ' + k)
#         return False # remove this if want more keys
# 
# lis = keyboard.Listener(on_press=on_press)
# lis.start() # start to listen on a separate thread
# lis.join() # no this if main thread is polling self.key