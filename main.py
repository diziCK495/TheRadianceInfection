# hotkey_demo.py
import keyboard
import time
import pyperclip
import win32clipboard

from config import *

def cut_all_and_get_text() -> str:
    global oriClip
    """
    模拟 Ctrl+A / Ctrl+X 剪切全部文本，并返回剪切得到的内容。
    delay: 每步之间的延时（秒），默认0.1秒。
    """
    # 清空剪贴板，防止读到旧数据
    pyperclip.copy("")

    # 发送 Ctrl+A 和 Ctrl+X
    keyboard.send(SELECT_ALL_HOTKEY)
    keyboard.send(CUT_HOTKEY)
    time.sleep(DELAY)

    # 获取剪切后的内容
    new_clip = pyperclip.paste()

    return new_clip

def combine(oriStr,insChr=' '):
    return insChr.join(oriStr)+insChr

def Start():
    print("Start generate...")
    text=cut_all_and_get_text()
    if text == "":
        print("no text")
        return
    print("Get Text:",text)
    if USE_DREAM_NAIL:
        combinedText = '……'+combine(text,insChr = SEPARATOR)+'……'
    else:
        combinedText = combine(text,insChr = SEPARATOR)
    print("Combine Text:",combinedText)
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, combinedText)
    win32clipboard.CloseClipboard()

    if AUTO_PASTE_TEXT:
        keyboard.send(PASTE_HOTKEY)
        time.sleep(DELAY)
        if AUTO_SEND_TEXT:
            keyboard.send(SEND_HOTKEY)

# 绑定 Ctrl+Alt+H 作为全局热键
ok=keyboard.add_hotkey(HOTKEY, Start, suppress=BLOCK_HOTKEY or HOTKEY==SEND_HOTKEY)

print("Starting...")
print("Hot key bind: "+str(bool(ok)))
print("Press "+HOTKEY+" to trans")
# 保持程序运行
keyboard.wait()
