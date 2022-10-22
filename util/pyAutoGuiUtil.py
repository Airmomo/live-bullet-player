import pyautogui
import time


def tap(button_key_name, duration=0.25):
    """
        点击一次按键指令
        :param button_key_name: 按键名称
        :param duration: 持续时间
        :return:
    """
    if button_key_name is not None:
        button_key_name = button_key_name.lower()
        pyautogui.keyDown(button_key_name)
        time.sleep(duration)
        pyautogui.keyUp(button_key_name)


def mouseMoveRelLeft(duration=0.25):
    """
        鼠标向左移动一定距离
        :param duration: 持续时间
    """
    pyautogui.moveRel(-50, 0, duration=duration)


def mouseMoveRelRight(duration=0.25):
    """
        鼠标向右移动一定距离
        :param duration: 持续时间
    """
    pyautogui.moveRel(50, 0, duration=duration)


def mouseMoveRelUp(duration=0.25):
    """
        鼠标向上移动一定距离
        :param duration: 持续时间
    """
    pyautogui.moveRel(0, -50, duration=duration)


def mouseMoveRelDown(duration=0.25):
    """
        鼠标向下移动一定距离
        :param duration: 持续时间
    """
    pyautogui.moveRel(0, 50, duration=duration)


def mouseLeftClick(duration=0.5):
    """
        点击鼠标左键
    """
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()


def mouseRightClick(duration=0.5):
    """
        点击鼠标左键
    """
    pyautogui.mouseDown(button='right')
    time.sleep(duration)
    pyautogui.mouseUp(button='right')
