import time


# 进度条  现在进度  总进度  提示信息  宽度
def progress_bar(now, end, text=" loding...", width=25):
    # 当前进度
    progress = int(now / end * 100)
    # 进度条宽度
    _x = int(progress / int(100/width))
    _y = width - _x
    ans = "\r[{:>3d}%]".format(progress) + "：" + "█"*_x + " "*_y + "|{}".format(text)
    print(ans, end='')


if __name__ == '__main__':

    for i in range(1, 101):
        time.sleep(0.1)
        progress_bar(i, 100)