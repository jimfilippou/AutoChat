from fabric.api import local
import os,time

run = True

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def GetWindowID(current=False):
    if current:
        return int(local("xdotool getactivewindow", True))
    else:
        return int(local("xdotool search --name \"Mozilla Firefox\"", True))

def GetSent(index):
    with open('sentences.txt') as f:
        sequence = f.read().splitlines()
        return sequence[index]

def main():
    while run:
        for s in range(file_len("sentences.txt")):
            id = GetWindowID()
            sent = GetSent(s)
            # Needs To Be Minimized
            os.system("xdotool windowfocus --sync %s" %(id))
            os.system("xdotool type %s" %(sent))
            os.system("xdotool key KP_Enter")
            time.sleep(5)



if __name__== "__main__":
    main()
