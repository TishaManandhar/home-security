import threading
import time
import motion
import buzzer

def looper():
    while True:
        time.sleep(2)
        is_motion = motion.motion_detect()
        if is_motion:
            print("motion detected")
            buzzer.alert()
        else:
            print("motion not detected")


if __name__ == "__main__":
    t = threading.Thread(target=looper)
    t.start()
    print("running main thread")