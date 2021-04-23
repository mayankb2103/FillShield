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
loggershield.setLevel(logging.INFO)


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

    def OpenDriver(self, head_less=True):
        loggershield.info("Opening Driver")
        opts = Options()
        


        opts.headless=head_less
        #opts.add_argument('--no-sandbox')
        #opts.add_argument("--disable-dev-shm-usage") #overcome limited resource problems

        #opts.add_argument('--disable-gpu')

        #opts.add_argument('--single-process')
        #opts.add_argument('--ignore-certificate-errors')
        #opts.add_argument("--ignore-ssl-errors=true")
        #opts.add_argument("--ssl-protocol=any")
        





        self.driver = webdriver.Chrome(options=opts)
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

        for NoButton in NoButtons[:5]:
             NoButton.click()
             time.sleep(2)

        NoneAboveXpath="//*[@name='checkbox-5-sub-5']/./.."
        NoneAbove=self.driver.find_element_by_xpath(NoneAboveXpath)
        NoneAbove.click()
        time.sleep(2)
        
        for NoButton in NoButtons[5:6]:
            NoButton.click()
            time.sleep(2)

        ## Food Details
        FoodArrowXpath="//*[@class='mat-select-arrow']"
        FoodArrow=self.driver.find_element_by_xpath(FoodArrowXpath)
        FoodArrow.click()
        time.sleep(2)

        NBNLXpath="//span[text()=' Neither Breakfast Nor Lunch ']"
        NBNL=self.driver.find_element_by_xpath(NBNLXpath)
        NBNL.click()
        time.sleep(2)
        
        for NoButton in NoButtons[6:]:
             NoButton.click()
             time.sleep(2)


        strtofile("/tmp/htmls/Qfillbefore.html",self.driver.page_source)   
        UpdateButtonXpath="//*[@type='submit']"
        UpdateButton= self.driver.find_element_by_xpath(UpdateButtonXpath)
        UpdateButton.click()
        
        
        self.waitloader("//span[text()='OK']", mode="Questionarie Fill")
        strtofile("/tmp/htmls/QFill.html",self.driver.page_source)
        
        
        
        time.sleep(2)
        # loggershield.info(self.driver.page_source)
        strtofile("/tmp/htmls/QFill.html",self.driver.page_source)   
        OKButtonXpath='//*[@id="mat-dialog-2"]/app-com-dailog/div[2]/button[2]/span'
        OKButton= self.driver.find_element_by_xpath(OKButtonXpath)
        OKButton.click()
        time.sleep(3)
        strtofile("/tmp/htmls/OKClick.html",self.driver.page_source)   






        
        self.waitloader("//*[@class='barcode']", mode="Shield Fill")
        strtofile("/tmp/htmls/afterfill.html",self.driver.page_source)   

        # strtofile("Shield-status.html",self.driver.page_source)




    def getstatus():
        pass
        

    def __del__(self):
        if(self.driver!=None):
            self.driver.quit()






