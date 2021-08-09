# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:02:10 2021

@author: Deniz Rumet FIRAT
"""

from selenium import webdriver
import time
import xlsxwriter

# Setup excel work files
workbook = xlsxwriter.Workbook('freq.xlsx')
worksheet = workbook.add_worksheet('freqTable')

PATH=''

# Maximize window to get the complete data
driver = webdriver.Chrome(PATH)
driver.get('')
driver.maximize_window()

# Wait for fully load
time.sleep(3)


# Take the hertz value every 10 second for 30 times
for q in range(3):
    freq = driver.find_element_by_class_name('')
    freqs = freq.text.split()[0]
    print(freqs)
    k = freqs
    worksheet.write(q,1,k)
    date = time.ctime()
    worksheet.write(q,0,date)
    time.sleep(10)

workbook.close()
driver.quit()

        