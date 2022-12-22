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
    process = subprocess.run(
        ["cat", "/proc/sys/net/ipv4/icmp_echo_ignore_all"],
        capture_output=True,
        text=True
    )
    if process.stdout == 1:
        raise "icmp is disabled"

    host = argv[1]
    l = 1
    r = 2000

    while r - l > 1:
        mtu = (l + r) // 2
        checker = check_mtu(host, str(mtu))
        if checker.returncode == 0:
            l = mtu
        elif checker.returncode == 1:
            r = mtu
        else:
            raise checker.stderr

    print(f"MTU is {l + 28}")


if __name__ == '__main__':
    main(sys.argv)
