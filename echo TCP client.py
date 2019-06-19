__author__ = 'heiyanbin'

def status():
    return 0, 0

def throttle(x):
    pass
maxStep = 100
def control(speed):
    l, r = 0, maxStep
    while l < r:
        m = l + (r - l) / 2
        last_v = 0
        throttle(m)
        while True:
            v = status()[1]
            if v == last_v:
                break
            last_v = v
        if last_v < speed:
            l = m + 1
        elif last_v > speed:
            r = m - 1
        return m
