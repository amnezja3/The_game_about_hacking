import pyautogui

latLoc = pyautogui.locateOnScreen('img/latitude2.png')

pyautogui.click(latLoc)
pyautogui.move(-32, 0)
pyautogui.mouseDown()
pyautogui.move(125, 10)
pyautogui.mouseUp()
pyautogui.move(-32, 0)

pyautogui.hotkey('ctrl', 'c')
pyautogui.click(button='right')
pyautogui.move(15, 15)
pyautogui.click()

latLocins = pyautogui.locateOnScreen('img/nslat.png')
pyautogui.click(latLocins)
pyautogui.move(25, 5)
pyautogui.tripleClick()
pyautogui.hotkey('ctrl', 'v')
pyautogui.move(0, 50)
pyautogui.click()
