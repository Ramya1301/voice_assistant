import pyautogui as spam
import time

limit = input("Enter your limit:")
msg = input("Enter your message:")
i = 0
time.sleep(10)

# using while loop for this project

while i < int(limit):
    spam.typewrite(msg)
    spam.press('Enter')
    i += 1