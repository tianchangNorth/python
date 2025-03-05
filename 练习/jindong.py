from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options  # 新增配置导入

# 修改浏览器配置
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument('--ignore-certificate-errors')  # 忽略证书错误
driver = webdriver.Chrome(options=options)  # 应用配置

driver.get('https://search.jd.com/Search?keyword=手机')

try:
    driver.maximize_window()
    
    # 优化等待条件为元素可点击
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".gl-item"))
    )
    
    # 分段滚动加载
    for i in range(3):
        driver.execute_script(f"window.scrollTo(0, {i*500})")
        time.sleep(1.5)  # 增加滚动间隔
    
    # 更新价格选择器路径
    prices = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".gl-item .J_price"))
    )
    
    for p in prices[:5]:
        # 使用text_to_be_present_in_element等待价格加载
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "strong"), "¥")
        )
        print(p.text.strip())

finally:
    driver.quit()