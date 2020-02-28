import yl_os
import yl_json
import yl_requests


def test_yl_os():
    pass


def test_yl_json():
    pass


def test_yl_requests():
    print(yl_requests.getUserAgent())


if __name__ == '__main__':
    print("yl_os".center(50, "-"))
    test_yl_os()
    print("yl_json".center(50, "-"))
    test_yl_json()
    print("yl_requests".center(50, "-"))
    test_yl_requests()