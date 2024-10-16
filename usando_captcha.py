import pyautogui as py
from resolver_captcha import quebrar_capctcha

texto = quebrar_capctcha()

py.PAUSE = 0.4
py.press("win")
py.write("Chrome")
py.press("enter")
py.write(texto)

print(f"O texto do captcha foi: {texto}")
