from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os

# =========================
# SETUP
# =========================

os.makedirs("9gag_memes", exist_ok=True)

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(180)

driver.get("https://9gag.com/funny")

time.sleep(10)

# =========================
# STORAGE
# =========================

downloaded = set()
count = 0
target = 1000

# =========================
# SCRAP LOOP
# =========================

while count < target:

    # scroll to load more memes
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

    images = driver.find_elements(By.TAG_NAME, "img")

    for img in images:
        src = img.get_attribute("src")

        # only real meme CDN images
        if src and "img-9gag-fun.9cache.com" in src:

            if src in downloaded:
                continue

            try:
                img_data = requests.get(src, timeout=10).content

                with open(f"9gag_memes/meme_{count}.jpg", "wb") as f:
                    f.write(img_data)

                downloaded.add(src)

                print(f"Downloaded {count}")

                count += 1

                if count >= target:
                    break

            except:
                pass

print("Done! Total images:", count)

driver.quit()