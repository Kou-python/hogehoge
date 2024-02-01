from selenium import webdriver
from selenium.webdriver.common.by import By
import time

## パラメータ
URL = "https://business.form-mailer.jp/fms/d610957048169"
photo = "/content/Screenshot_20240201-071649.png"

# 個人情報
name = "XXXX"
ruby = "XXXXXXXX"
phone = ["XXX", "XXXX", "XXXX"]
stu_name = "XXXX"


## ドライバー設定
options = webdriver.ChromeOptions()
# options.add_argument("--headless") # GUIを使わない
# options.add_argument("--disable-dev-shm-usage") # メモリ不足のエラー回避
options.add_argument("--no-sandbox")  # パフォーマンス向上
options.add_experimental_option("detach", True)  # ブラウザを閉じない

driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()


## Webアクセス開始
driver.get(URL)
# まず、テスト
print(driver.title)
# 教師名
driver.find_element(By.XPATH, "//input[@class='form-control form-name-sei']").send_keys(
    name[:2]
)
driver.find_element(By.XPATH, "//input[@class='form-control form-name-mei']").send_keys(
    name[2:]
)
# 教師名フリガナ
driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/form/div[2]/div/div/div/div[1]/input",
).send_keys(ruby[:4])
driver.find_element(
    By.XPATH,
    "//html/body/div[1]/div/form/div[2]/div/div/div/div[2]/input",
).send_keys(ruby[4:])

# 電話番号
driver.find_element(By.XPATH, "//input[@id='field_804370_1']").send_keys(phone[0])
driver.find_element(By.XPATH, "//input[@id='field_804370_2']").send_keys(phone[1])
driver.find_element(By.XPATH, "//input[@id='field_804370_3']").send_keys(phone[2])
# 生徒名
driver.find_element(
    By.XPATH,
    "//html/body/div[1]/div/form/div[4]/div/div/div/div[1]/input",
).send_keys(stu_name[:2])
driver.find_element(
    By.XPATH,
    "/html/body/div[1]/div/form/div[4]/div/div/div/div[2]/input",
).send_keys(stu_name[2:])
