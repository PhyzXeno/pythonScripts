#python printf.py  -require python27

from ctypes import *

msvcrt = cdll.msvcrt
haha = "Hello\n"
msvcrt.printf("My: %s", haha)
