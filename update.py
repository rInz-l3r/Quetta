import os
import time
import sys

def main():
    time.sleep(10)
    os.system("git pull")
    time.sleep(60)
    os.system("python3 run_quetta.py std")

if __name__ == "__main__":
    main()
