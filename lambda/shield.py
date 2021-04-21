import logging



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import os
import subprocess
import time
import random
loggershield = logging.getLogger()
loggershield.setLevel(logging.DEBUG)


def strtofile(fname, strg):
    with open(fname,"w") as fle:
        fle.write(strg)

class Browser:
    def __init__(self, emp_id, pass_wd):
        loggershield.info("Init The BROSWER")
        self.driver = None
        self.employee_id= emp_id
        self.password= pass_wd
        

    def waitloader(self, xpathformat, timeout=20, mode="Page Load",isdump=False):
        try:
            element_present = EC.presence_of_element_located((By.XPATH, xpathformat))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            loggershield.error("Timed out waiting for page to load")
        finally:
            loggershield.info("{} Done".format(mode))
        if(isdump):
            finaldump=self.driver.page_source
            loggershield.info(finaldump)

    def OpenDriver(self, head_less=True):
        loggershield.info("Opening Driver")
        opts = Options()
        tt=os.listdir("/opt")
        loggershield.info(tt)
        


        opts.binary_location = '/home/mayankb2103/Downloads/robert/git-hub/chrome-binary-robert/headless-chromium_latest'
        # opts.headless=head_less
        opts.add_argument('--no-sandbox')
        opts.add_argument("--disable-dev-shm-usage") #overcome limited resource problems

        opts.add_argument('--headless')
        opts.add_argument('--disable-gpu')

        opts.add_argument('--window-size=1280x1696')
        opts.add_argument('--user-data-dir=/tmp/user-data')
        opts.add_argument('--hide-scrollbars')
        opts.add_argument('--enable-logging')
        opts.add_argument('--log-level=0')
        opts.add_argument('--v=99')
        opts.add_argument('--single-process')
        opts.add_argument('--disable-dev-shm-usage')
        opts.add_argument('-disable-extensions')
        opts.add_argument('--ignore-certificate-errors')
        opts.add_argument("--ignore-ssl-errors=true")
        opts.add_argument("--ssl-protocol=any")
        opts.add_argument('--homedir=/tmp') 
        opts.add_argument('--disk-cache-dir=/tmp/cache-dir')
        opts.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.3163.100 Safari/537.36')
        loggershield.info(opts)
        





        self.driver = webdriver.Chrome(executable_path="/home/mayankb2103/Downloads/robert/git-hub/chrome-binary-robert/chromedriver", options=opts)
        loggershield.info("Opening Driver, Done")

    def OpenShield(self):
        loggershield.info("Opening Shield HomePage")
        self.driver.get("https://sbsdbindia.samsungcloud.tv/webapp/srid")
        

    def SignIn(self):
        loggershield.info("SignIn Start")
        time.sleep(3)
        signindump=self.driver.page_source
        strtofile("signin.html",signindump)
        empid= self.driver.find_element_by_xpath("//*[@formcontrolname='empId']")
        passwd= self.driver.find_element_by_xpath("//*[@formcontrolname='password']")
        submitbut= self.driver.find_element_by_xpath("//*[@type='submit']")

        time.sleep(2)
        empid.send_keys(self.employee_id)
        time.sleep(2)
        passwd.send_keys(self.password)
        time.sleep(2)
        submitbut.click()        
    
        self.waitloader("//span[text()='Logout']", mode="SignIn")
        time.sleep(2)
        # strtofile("quiz.html",self.driver.page_source)

        

    def FillQuiz(self):
        loggershield.info("Quiz Filling start")
        RadioButtonXpath="//*[@id='mat-radio-{}']".format(random.randint(2,5))
        RadioButton= self.driver.find_element_by_xpath(RadioButtonXpath)
        RadioButton.click()
        time.sleep(1)

        CheckAnswerXpath="//span[text()='Check Answer']"
        CheckAnswer= self.driver.find_element_by_xpath(CheckAnswerXpath)
        CheckAnswer.click()
        time.sleep(1)

        CloseXpath="//span[text()='Close']"
        Close= self.driver.find_element_by_xpath(CloseXpath)
        Close.click()
        
        self.waitloader("//span[text()='AGREE']", mode="Quiz Filling")
        time.sleep(1)
        # strtofile("Disclosure.html",self.driver.page_source)

    def AcceptDisclosure(self):
        loggershield.info("Accepting Disclosure")
        AgreeXPath="//span[text()='AGREE']"
        Agree= self.driver.find_element_by_xpath(AgreeXPath)
        Agree.click()
        self.waitloader("//h2[text()='Please answer below questions:']", mode="Disclosure Acceptance")
        time.sleep(1)
        # strtofile("questionarie.html",self.driver.page_source)

    def FillQuestionarie(self):
        loggershield.info("Filling Questionarie")
        NoButtonXpath="//div[contains(@class, 'mat-radio-label-content') and text()='No']"
        NoButtons= self.driver.find_elements_by_xpath(NoButtonXpath)

        # for NoButton in NoButtons:
        #     NoButton.click()
        #     time.sleep(1)

        NoneAboveXpath="//*[@name='checkbox-5-sub-5']/./.."
        NoneAbove=self.driver.find_element_by_xpath(NoneAboveXpath)
        NoneAbove.click()
        time.sleep(2)

        ## Food Details
        FoodArrowXpath="//*[@class='mat-select-arrow']"
        FoodArrow=self.driver.find_element_by_xpath(FoodArrowXpath)
        FoodArrow.click()
        time.sleep(1)

        NBNLXpath="//span[text()=' Neither Breakfast Nor Lunch ']"
        NBNL=self.driver.find_element_by_xpath(NBNLXpath)
        NBNL.click()
        


        UpdateButtonXpath="//*[@type='submit']"
        UpdateButton= self.driver.find_element_by_xpath(UpdateButtonXpath)
        UpdateButton.click()

        self.waitloader("//*[@class='barcode']", mode="Quiz Filling", isdump=True)


        strtofile("Shield-status.html",self.driver.page_source)


    def getstatus():
        pass
        

    def __del__(self):
        if(self.driver!=None):
            self.driver.close()






