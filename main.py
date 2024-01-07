import threading
import time

def looper():
    while True:
        time.sleep(2)
        print("Hello")

if __name__ == "__main__":
    t = threading.Thread(target=looper)
    print("running main thread")