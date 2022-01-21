from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import re


def launchBrowser(email_path, username, password, exp_username):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    driver.get('https://twitter.com/i/flow/login')
    driver.implicitly_wait(10)

    action = ActionChains(driver)
    driver.find_element_by_name('text').click()
    action.send_keys(email_path)
    action.perform()

    driver.implicitly_wait(10)
    next_btn = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div'
    driver.find_element(By.XPATH,next_btn).click()
    driver.implicitly_wait(10)

    user_path = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input' 
    driver.find_element_by_name('text')
    action.send_keys(username)
    action.perform()

    driver.implicitly_wait(10)
    next_btn = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div'
    driver.find_element(By.XPATH,next_btn).click()
    driver.implicitly_wait(10)

    driver.find_element_by_name('password').click()
    action.send_keys(password)
    action.perform()

    login_path = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div'
    driver.find_element(By.XPATH,login_path).click()
    driver.implicitly_wait(10)

    explore_path = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div'
    
    driver.find_element(By.XPATH,explore_path).click()
    driver.implicitly_wait(10)

    print()
    print()

    print('You have succesfuly loged in ...')
    print('Hurry Up...')

    search_path = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/label/div[2]/div/input'
    driver.find_element(By.XPATH,search_path).click()
    action.send_keys(exp_username)
    driver.implicitly_wait(10)
    action.send_keys(u'\ue007')
    action.perform()
    profile_path = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[3]/div/div/div'
    driver.find_element(By.XPATH, profile_path).click()

    path_Folowing = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/div[1]'
    following = driver.find_element_by_xpath(path_Folowing)
    driver.implicitly_wait(10)

    time.sleep(2)
    try:
        path_for_Follower = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[5]/div[2]'
        
        follower = driver.find_element_by_xpath(path_for_Follower)
        driver.implicitly_wait(10)

        path_biography = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div'
        biography = driver.find_element_by_xpath(path_biography)
        driver.implicitly_wait(10)

        path_option = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div[1]'
        user_id = driver.find_element_by_xpath(path_option).click()
        driver.implicitly_wait(10)

        report_url = '//*[@id="layers"]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[4]'
        driver.find_element(By.XPATH, report_url).click()
        get_url = driver.current_url
        user_id = int(re.search(r'\d+', get_url).group())
        print()
        print()
        print('===================== here Is Your Details ==========================')
        print('Followers ===> ',following.text)
        print('Followers ===> ',follower.text)
        print('Biography ===> ', biography.text)
        print('User Id ===> ', user_id)
    
        return driver

    except:
        print('Try again Some went wrong ...')
        print('Enter Correct User name In currect format ...')


driver = launchBrowser('vikask99588@gmail.com', '@vikas_kumar995', 'Vikas@123', 'PMO india')
