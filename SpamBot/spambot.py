import pyautogui, time
import webbrowser as wb


wb.open('https://web.whatsapp.com/')

f = open("spamText.txt", 'r')
time.sleep(10)
for i in f:
    pyautogui.typewrite(i)
    pyautogui.press('enter')