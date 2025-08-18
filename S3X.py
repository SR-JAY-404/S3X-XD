import os, platform, time, sys
os.system("pip uninstall urllib3 requests chardet idna certifi -y");os.system("pip install urllib3 requests chardet idna certifi")
os.system("pip install requests && pip install rich")
def S1(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.02)
os.system("git pull")
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            from s3x import s3x
            welcome()
        elif bit == '32bit':
            from s3x import s3x
            welcome()
        else:
            exit('\033[1;31m[●] Connection & Network Error ❌')
Run()
