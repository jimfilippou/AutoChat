# Author : FrozenVortex

from fabric.api import local
import time

run = True

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def get_window_id(current, name):
    if current:
        return int(local("xdotool getactivewindow", True))
    else:
        return int(local("xdotool search --name \"%s\"" %name, True))


def get_sent(index):
    with open('sentences.txt') as f:
        sequence = f.read().splitlines()
        return sequence[index]


def handle_message(identity, sent):
    # Needs To Be Minimized
    local("xdotool windowfocus --sync %s" % identity)
    local("xdotool type --delay 250 \"%s\"" % sent)
    local("xdotool key KP_Enter")


def main():
    for s in range(file_len("sentences.txt")):
        identity = get_window_id(False, "Mozilla Firefox")
        sent = get_sent(s)
        handle_message(identity, sent)
        time.sleep(15)


if __name__ == "__main__":
    print("Wating 10 seconds...")
    time.sleep(10)
    main()
