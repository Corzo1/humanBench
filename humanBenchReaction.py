import pyautogui
import win32api
import win32con
import time

def click(x,y):
    win32api.SetCursorPos(x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

while True:
    r = pyautogui.pixel(1464, 416)[0]
    if r == 75:
        click()
        print("Clicked")
        # Remove the second click() call if not needed


