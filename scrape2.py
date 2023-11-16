import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

link_lst = []
"""
isv-r PNCib ViTmJb BUooTd - div tag
isv-r PNCib ViTmJb BUooTd
rg_i - a tag
jlTjKd - a tag after click first a tag
sFlh5c pT0Scc iPVvYb - img tag
sFlh5c pT0Scc iPVvYb
"""
def get_image_links(keyword, repeat):
    global link_lst
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(f"https://www.google.com/search?q={keyword}&tbm=isch")
    time.sleep(2)
    for i in range(repeat):
        driver.find_elements(By.CLASS_NAME, "rg_i")[i].click()
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        a_tag = soup.find_all("a", class_="jlTjKd")
        #.find("img", class_="sFlh5c")
        #if "https" in link:
        link_lst.append(a_tag[i].find("img", class_="sFlh5c")['src'])
        time.sleep(1)
    driver.quit()
    return link_lst

def main():
    keyword = "장원영"
    repeat = 2
    lst = get_image_links(keyword, repeat)
    print(lst)

if __name__ == "__main__":
    main()