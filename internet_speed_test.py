import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from average_calc import average_calc

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver_instance = webdriver.Chrome(options=chrome_options)


def speed_check(driver):
    tally = 5
    errors = 0
    successes = 0
    speeds = []

    for i in range(tally):
        try:
            driver.get("https://www.speedtest.net")

            #wait for page to load some content
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "start-text")))

            # reject cookie popup
            try:
                reject_btn = driver.find_element(By.ID, "onetrust-reject-all-handler")
                reject_btn.click()
            except NoSuchElementException as e:
                print(print(e))


            go_button = driver.find_element(By.CLASS_NAME, "start-text")
            go_button.click()

            time.sleep(50)

            #retrieve download and upload speeds
            download_speed = driver.find_element(By.CSS_SELECTOR, ".download-speed").text
            upload_speed = driver.find_element(By.CSS_SELECTOR, ".upload-speed").text

            #append speeds to dictionary
            speeds.append({f"download_{i+1}": download_speed,
                           f"upload_{i+1}": upload_speed})
            print(f"Download: {download_speed} Mbps, Upload: {upload_speed} Mbps")
            successes += 1

        except (WebDriverException, TimeoutException, NoSuchElementException) as e:
            print(f"Error occurred: {e}")
            errors += 1

        driver.quit()
        print(speeds)
        print(f"Successes: {successes}, Errors: {errors}")

        return print(average_calc(speeds))


speed_check(driver_instance)