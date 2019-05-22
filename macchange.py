import tkinter as tk
from threading import Timer

import time
import os
import csv
import win32api
import win32con
import random

from selenium import webdriver
from tkinter.filedialog import askopenfilename
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


root = tk.Tk()
root.title("Welcome to You!")
root.geometry('340x320')


v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("One Minute"),
    ("Two Minutes"),
    ("Three Minutes"),
    ("Five Minutes"),
    ("Ten Minutes"),
    ("Fifteen Minutes"),
    ("No Minutes"),
]

def ShowChoice():
    print(v.get())

def rand_mac():
 return "%02x%02x%02x%02x%02x%02x" % (
  random.randint(0, 255),
  random.randint(0, 255),
  random.randint(0, 255),
  random.randint(0, 255),
  random.randint(0, 255),
  random.randint(0, 255)
 )

def eth():
    filename = askopenfilename()
    global selection
    selection = v.get()
    glCount = 0

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        # line_countdef = 0
        for row in csv_reader:
            if glCount == 0:
                print(f'Column names are {", ".join(row)}')
                glCount += 1
            else:
                print(f'\t{row[1]}, works in the {row[2]} department, and was born in {row[3]}.')

                # os.system('macshift.exe -i "Ethernet"')

                # strmac = rand_mac().upper()
                # os.system('macshift.exe -i "Ethernet" ' + strmac)
                # print (strmac)
                time.sleep(5)
                try:
                    driver = webdriver.Chrome("chromedriver.exe")
                    driver.set_page_load_timeout(20)
                    # driver.get("http://localhost/scrappy/")
                    # driver.get("http://wibox.net/")
                    driver.get("http://localhost/mymac10")
                except TimeoutException:
                    driver.quit()
                    continue

                timeout = 20
                try:
                    element_present = EC.presence_of_element_located((By.ID, 'nome'))
                    WebDriverWait(driver, timeout).until(element_present)
                except TimeoutException:
                    # print ("Timed out waiting for page to load")
                    # win32api.MessageBox(0, 'The page could not be loaded.', 'Warning',
                    # win32con.MB_OK | win32con.MB_ICONINFORMATION)

                    driver.quit()
                    continue
                time.sleep(15)
                # driver.find_element_by_id("nome").clear()
                # time.sleep(5)

                # driver.find_element_by_id("telefone").send_keys(row[2])
                driver.find_element_by_id("btcon").click()
                try:
                    time.sleep(2)
                    driver.find_element_by_name("termos").click()
                    driver.find_element_by_id("btFinal").click()
                    time.sleep(10)
                    # driver.execute_script("window.open('https://www.google.com')")
                    # driver.execute_script("window.open('https://www.uol.com.br')")
                    # driver.execute_script("window.open('https://www.youtube.com')")

                except:
                    try:
                        time.sleep(2)
                        driver.find_element_by_name("termos").click()
                        driver.find_element_by_id("btFinal").click()

                        time.sleep(5)
                        # driver.execute_script("window.open('https://www.google.com')")
                        # driver.execute_script("window.open('https://www.uol.com.br')")
                        # driver.execute_script("window.open('https://www.youtube.com')")
                    except:
                        # os.system('macshift.exe -i "Ethernet"')
                        time.sleep(10)
                        driver.quit()
                        continue
                if selection == 3:
                    time.sleep(60 * (selection + 2))
                if selection == 4:
                    time.sleep(60 * (selection + 6))
                if selection == 5:
                    time.sleep(60 * (selection + 10))
                if selection == 6:
                    time.sleep(1)
                else:
                    time.sleep(60 * (selection + 1))
                glCount += 1
                # os.system('macshift.exe -i "Ethernet"')
                # time.sleep(5)
                driver.quit()
                # while True:
                # print(selection)
                # os.system('macshift.exe -i "Ethernet0"')


def wifi():
    filename = askopenfilename()
    global selection
    selection = v.get()
    glCount = 0

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        # line_countdef = 0
        for row in csv_reader:
            if glCount == 0:
                print(f'Column names are {", ".join(row)}')
                glCount += 1
            else:
                print(f'\t{row[1]}, works in the {row[2]} department, and was born in {row[3]}.')

                # os.system('macshift.exe -i "Ethernet"')

                # strmac = rand_mac().upper()
                # os.system('macshift.exe -i "Ethernet" ' + strmac)
                # print (strmac)
                time.sleep(5)
                try:
                    driver = webdriver.Chrome("chromedriver.exe")
                    driver.set_page_load_timeout(20)
                    # driver.get("http://localhost/scrappy/")
                    # driver.get("http://wibox.net/")
                    driver.get("http://localhost/mymac10")
                except TimeoutException:
                    driver.quit()
                    continue

                timeout = 20
                try:
                    element_present = EC.presence_of_element_located((By.ID, 'nome'))
                    WebDriverWait(driver, timeout).until(element_present)
                except TimeoutException:
                    # print ("Timed out waiting for page to load")
                    # win32api.MessageBox(0, 'The page could not be loaded.', 'Warning',
                    # win32con.MB_OK | win32con.MB_ICONINFORMATION)

                    driver.quit()
                    continue
                time.sleep(15)
                # driver.find_element_by_id("nome").clear()
                # time.sleep(5)

                # driver.find_element_by_id("telefone").send_keys(row[2])
                driver.find_element_by_id("btcon").click()
                try:
                    time.sleep(2)
                    driver.find_element_by_name("termos").click()
                    driver.find_element_by_id("btFinal").click()
                    time.sleep(10)
                    # driver.execute_script("window.open('https://www.google.com')")
                    # driver.execute_script("window.open('https://www.uol.com.br')")
                    # driver.execute_script("window.open('https://www.youtube.com')")

                except:
                    try:
                        time.sleep(2)
                        driver.find_element_by_name("termos").click()
                        driver.find_element_by_id("btFinal").click()

                        time.sleep(5)
                        # driver.execute_script("window.open('https://www.google.com')")
                        # driver.execute_script("window.open('https://www.uol.com.br')")
                        # driver.execute_script("window.open('https://www.youtube.com')")
                    except:
                        # os.system('macshift.exe -i "Ethernet"')
                        time.sleep(10)
                        driver.quit()
                        continue
                if selection == 3:
                    time.sleep(60 * (selection + 2))
                if selection == 4:
                    time.sleep(60 * (selection + 6))
                if selection == 5:
                    time.sleep(60 * (selection + 10))
                if selection == 6:
                    time.sleep(1)
                else:
                    time.sleep(60 * (selection + 1))
                glCount += 1
                # os.system('macshift.exe -i "Ethernet"')
                # time.sleep(5)
                driver.quit()
                # while True:
                # print(selection)
                # os.system('macshift.exe -i "Ethernet0"')


tk.Label(root,
         text="""Please Choose the time!""",
         justify = tk.CENTER,
         font=("Arial Bold", 16),
         padx = 20,pady=20).pack()

for val, language in enumerate(languages):
    tk.Radiobutton(root,
                  text=language,
                  padx = 30,
                  variable=v,
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)

slogan = tk.Button(root,
                width=20,
                text="Ethernet",
                command=eth)
slogan.pack()




wifi = tk.Button(root,
                width=20,
                text="Wi-Fi",
                command=wifi)

wifi.pack()




root.mainloop()