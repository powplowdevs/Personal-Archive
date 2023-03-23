# import pyppeteer
# import asyncio
# import pyautogui as pa
# import pyperclip 
# import time

# from bs4 import BeautifulSoup
# from selenium import webdriver

# import requests

# async def main():
#     # launches a chromium browser, can use chrome instead of chromium as well.
#     browser = await pyppeteer.launch(headless=False)
#     # creates a blank page
#     page = await browser.newPage()
#     # follows to the requested page and runs the dynamic code on the site.
#     await page.goto('https://crypto.com/nft/')
#     time.sleep(5)
    
#     #use inspect to get html
#     #hit root not the body
#     pa.keyDown("ctrl")
#     pa.keyDown("shift")
#     pa.keyDown("i")
#     time.sleep(2)
#     pa.keyUp("ctrl")
#     pa.keyUp("shift")
#     pa.keyUp("i")
#     time.sleep(0.3)
#     pa.moveTo(527,270)
#     time.sleep(0.3)
#     pa.click(button="left")
#     time.sleep(0.3)
#     pa.moveTo(540,320)
#     time.sleep(0.3)
#     pa.click(button="left")
#     time.sleep(0.3)
#     pa.moveTo(550,330)
#     time.sleep(0.3)
#     pa.click(button="left")
#     time.sleep(0.3)
#     pa.moveTo(560,330)
#     time.sleep(0.3)
#     pa.click(button="left")
#     time.sleep(0.3)
#     pa.keyDown("down")
#     time.sleep(0.3)
#     pa.keyDown("down")
#     time.sleep(0.3)
#     pa.keyDown("down")
#     time.sleep(0.3)
#     pa.keyDown("down")
#     time.sleep(0.3)
#     pa.moveTo(565,275)
#     time.sleep(0.3)
#     pa.click(button="left")
#     time.sleep(0.3)
#     pa.moveTo(580,295)
#     time.sleep(0.3)
#     pa.click(button="left")
#     pa.moveTo(580,305)
#     time.sleep(0.3)
#     pa.click(button="left")
#     time.sleep(0.3)
#     pa.keyDown("down")
#     time.sleep(0.3)
#     pa.keyDown("down")
#     time.sleep(0.3)
#     pa.moveTo(590,340)
#     time.sleep(0.3)
#     pa.click(button="right")    
#     pa.moveTo(620,450)
#     time.sleep(0.3)
#     pa.click(button="left")
#     time.sleep(0.3)
#     pa.moveTo(850,530)
#     time.sleep(0.3)
#     pa.click(button="left")

    
#     # pa.click(button="left")
#     # time.sleep(0.3)
#     # pa.click(button="left")
#     # time.sleep(0.3)
#     # pa.keyDown("ctrl")
#     # pa.keyDown("a")
#     # time.sleep(0.3)
#     # pa.keyUp("ctrl")
#     # pa.keyUp("a")   
#     # time.sleep(0.3)
#     # pa.keyDown("ctrl")
#     # pa.keyDown("c")
#     # time.sleep(0.3)
#     # pa.keyUp("ctrl")
#     # pa.keyUp("c") 
#     # time.sleep(0.3)
#     cont = pyperclip.paste()
#     time.sleep(1)

#     return cont

# # prints the html code of the user profiel: tupac
# #print(asyncio.get_event_loop().run_until_complete(main()))

# # url = "https://crypto.com/nft"

# # r = requests.get(url, timeout=(35, 27))
# # soup = BeautifulSoup(r.text, 'html.parser') 
# # print(soup)

# # browser = webdriver.PhantomJS('G:\My Drive\Programing\Personal scripts\py_trolling\phantomjs.exe')
# # browser.get(url)
# # html = browser.page_source
# # soup = BeautifulSoup(html, 'lxml')
# # a = soup.find('section', 'wrapper')
# # print(soup)


# # from requests_html import HTMLSession
# # s = HTMLSession()
# # response = s.get(url)
# # response.html.render()
# # print(response)

# from bs4 import BeautifulSoup
# from selenium import webdriver    

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# # executable_path param is not needed if you updated PATH
# browser = webdriver.Chrome(options=options, executable_path='G:\My Drive\Programing\Personal scripts\py_trolling\chromedriver.exe')
# browser.get("https://crypto.com/nft")
# time.sleep(5)
# html = browser.page_source
# soup = BeautifulSoup(html, features="html.parser")
# print(soup)
# browser.quit()




