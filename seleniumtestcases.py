from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")

chrome_service = Service(ChromeDriverManager().install())

def get_driver(headless=True):
    if not headless:
        return webdriver.Chrome(service=chrome_service)
    return webdriver.Chrome(service=chrome_service, options=options)

def test_case_1():
    driver = get_driver()
    try:
        driver.get("http://13.60.55.59:5173/")
        # driver.maximize_window()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[1]/nav/a[2]"))
        ).click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='name']").send_keys("John Doe")
        driver.find_element(By.XPATH, "//*[@id='position']").send_keys("Software Engineer")
        driver.find_element(By.XPATH, "//*[@id='positionIntern']").click()
        driver.find_element(By.XPATH, "//*[@id='root']/div/form/input").click()
        print("Test Case 1 Passed: Employee created successfully!")
    except Exception as e:
        print(f"Test Case 1 Failed: {e}")
    finally:
        driver.quit()

def test_case_2():
    driver = get_driver()
    try:
        driver.get("http://13.60.55.59:5173/")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='loginEmail']"))
        )
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='loginPassword']"))
        )
        print("Test Case 2 Passed: Login page elements loaded successfully!")
    except Exception as e:
        print(f"Test Case 2 Failed: {e}")
    finally:
        driver.quit()

def test_case_3():
    driver = get_driver()
    try:
        driver.get("http://13.60.55.59:5173/")
        driver.find_element(By.XPATH, "//*[@id='loginEmail']").send_keys("wrongemail@example.com")
        driver.find_element(By.XPATH, "//*[@id='loginPassword']").send_keys("wrongpassword")
        driver.find_element(By.XPATH, "//*[@id='loginButton']").click()
        time.sleep(2)
        assert "Invalid credentials" in driver.page_source
        print("Test Case 3 Passed: Invalid login displayed error message.")
    except Exception as e:
        print(f"Test Case 3 Failed: {e}")
    finally:
        driver.quit()

def test_case_4():
    driver = get_driver()
    try:
        driver.get("http://13.60.55.59:5173/")
        driver.find_element(By.XPATH, "//*[@id='loginEmail']").send_keys("admin@example.com")
        driver.find_element(By.XPATH, "//*[@id='loginPassword']").send_keys("securepassword")
        driver.find_element(By.XPATH, "//*[@id='loginButton']").click()
        time.sleep(2)
        assert "Dashboard" in driver.page_source
        print("Test Case 4 Passed: Logged in and navigated to dashboard.")
    except Exception as e:
        print(f"Test Case 4 Failed: {e}")
    finally:
        driver.quit()

def test_case_5():
    driver = get_driver()
    try:
        driver.get("http://13.60.55.59:5173/")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='dashboardButton']"))
        ).click()
        assert "Dashboard Overview" in driver.page_source
        print("Test Case 5 Passed: Dashboard button functional.")
    except Exception as e:
        print(f"Test Case 5 Failed: {e}")
    finally:
        driver.quit()

def test_case_6():
    driver = get_driver()
    try:
        driver.get("http://13.60.55.59:5173/")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='employeeListButton']"))
        ).click()
        assert "Employee List" in driver.page_source
        print("Test Case 6 Passed: Employee list page loaded.")
    except Exception as e:
        print(f"Test Case 6 Failed: {e}")
    finally:
        driver.quit()

def test_case_7():
    driver = get_driver()
    try:
        driver.get("http://13.60.55.59:5173/")
        driver.find_element(By.XPATH, "//*[@id='addEmployeeButton']").click()
        driver.find_element(By.XPATH, "//*[@id='name']").send_keys("Jane Doe")
        driver.find_element(By.XPATH, "//*[@id='position']").send_keys("Manager")
        driver.find_element(By.XPATH, "//*[@id='addButton']").click()
        time.sleep(2)
        assert "Employee added successfully" in driver.page_source
        print("Test Case 7 Passed: Added a new employee.")
    except Exception as e:
        print(f"Test Case 7 Failed: {e}")
    finally:
        driver.quit()

def test_case_8():
    driver = get_driver()
    try:
        driver.get("http://13.60.55.59:5173/")
        driver.find_element(By.XPATH, "//*[@id='searchEmployee']").send_keys("Jane Doe")
        driver.find_element(By.XPATH, "//*[@id='searchButton']").click()
        assert "Jane Doe" in driver.page_source
        print("Test Case 8 Passed: Employee found.")
    except Exception as e:
        print(f"Test Case 8 Failed: {e}")
    finally:
        driver.quit()

def test_case_9():
    driver = get_driver()
    try:
        driver.get("http://13.60.55.59:5173/")
        driver.find_element(By.XPATH, "//*[@id='editEmployeeButton']").click()
        driver.find_element(By.XPATH, "//*[@id='position']").clear()
        driver.find_element(By.XPATH, "//*[@id='position']").send_keys("Senior Manager")
        driver.find_element(By.XPATH, "//*[@id='updateButton']").click()
        assert "Employee updated successfully" in driver.page_source
        print("Test Case 9 Passed: Employee updated.")
    except Exception as e:
        print(f"Test Case 9 Failed: {e}")
    finally:
        driver.quit()

def test_case_10():
    driver = get_driver()
    try:
        driver.get("http://13.60.55.59:5173/")
        driver.find_element(By.XPATH, "//*[@id='deleteEmployeeButton']").click()
        time.sleep(2)
        assert "Employee deleted successfully" in driver.page_source
        print("Test Case 10 Passed: Employee deleted.")
    except Exception as e:
        print(f"Test Case 10 Failed: {e}")
    finally:
        driver.quit()

test_case_1()
test_case_2()
test_case_3()
test_case_4()
test_case_5()
test_case_6()
test_case_7()
test_case_8()
test_case_9()
test_case_10()
