from playwright.sync_api import sync_playwright
from time import sleep,time

session = sync_playwright().start()
browser = session.chromium.launch(headless=False)
page = browser.new_page(java_script_enabled=True)
page.goto("https://monkeytype.com",wait_until="load")
page.locator("button.active.acceptAll").click()
page.locator("p.fc-button-label").nth(0).click()
page.keyboard.press("A")
start = time()
while time()-start < 30:
    text = ""
    wordlist = page.locator("div.word:not(.typed)")
    for i in range(wordlist.count()):
        text += wordlist.nth(i).inner_text() + " "
    print(text)
    page.keyboard.type(text)

#100 sec's sleep to see your wpm
sleep(100.0)

page.close()
browser.close()
session.stop()
