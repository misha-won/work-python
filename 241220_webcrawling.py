from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time

# ChromeDriver 경로 설정
chrome_driver_path = r"C:\Workspace\work-python\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)

# Selenium WebDriver 옵션 설정
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": r"C:\Workspace\work-python\Downloads"}  # 파일 다운로드 경로 설정
options.add_experimental_option("prefs", prefs)

# WebDriver 초기화
driver = webdriver.Chrome(service=service, options=options)

# URL 패턴 설정 (시작 ID와 끝 ID)
start_id = 486839
end_id = 489781
base_url = "https://www.chuncheon.go.kr/mayor/now/photo/?bbsId=BBSMSTR_000000000333&nttId={}&flag=view"

try:
    for ntt_id in range(0, end_id - start_id + 1):
        try:
            # 각 페이지 열기
            url = base_url.format(end_id - ntt_id)
            driver.get(url)
            time.sleep(0.2)  # 페이지 로딩 대기

            # 다운로드 버튼 찾기 및 클릭
            buttons = driver.find_elements(By.XPATH, "//a[contains(@href, 'javascript:fn_egov_downFile')]")
            if buttons:
                for button in buttons:
                    button.click()
                    time.sleep(0.2)  # 파일 다운로드 대기
            else:
                print(f"[INFO] No download button found on page {url}. Skipping...")

        except WebDriverException as e:
            print(f"[WARNING] Could not load page {url}. Skipping... Error: {e}")
            continue

finally:
    # 작업 완료 후 드라이버 종료
    driver.quit()