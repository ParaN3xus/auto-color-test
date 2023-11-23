from selenium import webdriver
from selenium.webdriver.common.by import By
import re

driver = webdriver.Edge()
driver.get("https://www.webhek.com/post/color-test/")

driver.find_element(By.ID, "overlay99").click()
driver.find_element(By.XPATH, '//*[@id="index"]/div[2]/button').click()

pattern = re.compile(r"rgb\([0-9]*,\s[0-9]*,\s[0-9]*\)")


while True:
    src = driver.page_source
    colorsstr = ""
    for i in src.splitlines():
        if i.find('<div id="box" class="lv') != -1:
            colorsstr = i
            break

    colors = pattern.findall(colorsstr)

    colorsdict = {}
    keylist = []

    count = 1
    for i in colors:
        if colorsdict.get(i) == None:
            colorsdict[i] = []
        colorsdict[i].append(count)

        count += 1

        if len(colorsdict) == 2:
            keylist = list(colorsdict.keys())
            if len(colorsdict[keylist[0]]) != 1 and len(colorsdict[keylist[1]]) != 1:
                break


    if(len(keylist) >= 2):
        if len(colorsdict[keylist[0]]) < len(colorsdict[keylist[1]]):
            index = 0
        else:
            index = 1
            
        try:
            driver.find_element(By.XPATH, "//*[@id=\"box\"]/span[" + str(colorsdict[keylist[index]][0]) +"]").click()
        except:
            break

input()
driver.close()
