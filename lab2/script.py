import subprocess
import sys
import time


def check_mtu(host, mtu):
    request = ['ping', host, '-M', 'do', '-s', mtu, '-c', '1']
    result = subprocess.run(request, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result


def main(argv):
    if len(argv) < 2:
        raise "too many args"

    host = argv[1]
    l = 1
    r = 2000

    while r - l > 1:
        mtu = (l + r) // 2
        if check_mtu(host, str(mtu)):
            l = mtu
        else:
            r = mtu
        time.sleep(1)

    print(f"MTU is {l}")


if __name__ == '__main__':
    main(sys.argv)
