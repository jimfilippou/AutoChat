from fabric.api import local
import os, time

run = True


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def GetWindowID(current=False, name="Mozilla Firefox"):
    if current:
        return int(local("xdotool getactivewindow", True))
    else:
        return int(local("xdotool search --name \"%s\"" %name, True))


def GetSent(index):
    with open('sentences.txt') as f:
        sequence = f.read().splitlines()
        return sequence[index]


def main():
    for s in range(file_len("sentences.txt")):
        identity = GetWindowID()
        sent = GetSent(s)
        # Needs To Be Minimized
        os.system("xdotool windowfocus --sync %s" % identity)
        os.system("xdotool type --delay 250 \"%s\"" % sent)
        os.system("xdotool key KP_Enter")
        time.sleep(5)


if __name__ == "__main__":
    print("Wating 10 seconds...")
    time.sleep(10)
    main()
