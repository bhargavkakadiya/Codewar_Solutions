#6kyu
def bouncingBall(h, bounce, window):
    if window >= h or bounce >= 1 or bounce <= 0 or h <= 0:
        return -1
    bh = h * bounce
    viewed = 1
    while bh > window:
        viewed += 2
        bh = bh * bounce
    return viewed

bouncingBall(30, 0.66 , 1.5)