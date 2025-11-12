import sys
import time

def spinner():
    """
    Simple animation for when the video conversion process happens
    """
    rotations = [
        "\\",
        "|",
        "/",
        "-",
    ]

    for spoke in rotations:
        print(f"{spoke}\r", end="")
        time.sleep(0.5)

spinner()