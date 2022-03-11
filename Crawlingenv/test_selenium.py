from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome("C:/Users/aquus/Desktop/Py_study/Crawlingenv/chromedriver.exe")
driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl") #구글 이미지 주소
elem = driver.find_element_by_name("q") # 구글 검색창
elem.send_keys("코딩") # 검색할 내용
elem.send_keys(Keys.RETURN) # 엔터

SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight") # 스크롤 높이 저장
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #브라우저 끝까지 스크롤 내림
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight") # 브라우저 높이 비교
    if new_height == last_height:
        try: # 시도했을 때
            driver.find_element_by_css_selector(".mye4qd").click() # 결과 더 보기 버튼 선택
        except: # 없으면 여기로
            break
    last_height = new_height
# 검색 후 나오는 이미지들
count = 1
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
for image in images:
    try:
        image.click() #첫 번째 요소 클릭
        time.sleep(2) #이미지가 완전히 뜨기까지 기다리기
        img_url = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src") #이미지 주소
        urllib.request.urlretrieve(img_url, str(count)+"jpg") # (이미지 주소, 저장 이름)
        count += 1
    except: # 오류 발생시 넘기기
        pass

driver.close() # 브라우저 닫기

#클래스 네임의 경우 조심 웹사이트 개발자 도구에서 xPath 복사 권장