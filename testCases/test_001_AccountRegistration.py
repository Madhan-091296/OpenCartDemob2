import os
import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.randomString import random_string_generator

class Test_001_AccountReg:
    # baseURL = "https://demo.opencart.com/"
    # baseURL = "https://tutorialsninja.com/demo/"
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("test_001_Account Registration Started")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.logger.info("Providing customer details for registration")
        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email = random_string_generator()+"@gmail.com"
        # self.email = ReadConfig.getUseremail()
        self.regpage.setEmail(self.email)
        self.password = ReadConfig.getPassword()
        self.regpage.setTelephone("65656565")
        self.regpage.setPassword(self.password)
        self.regpage.setConfirmPassword(self.password)
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        if self.confmsg == "Your Account Has Been Created!":
            self.logger.info("Account registration is passed..")
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.getcwd())+"\\screenshots\\"+"test+account_reg.png")
            self.logger.error("Account registration is failed.")
            assert False
        self.driver.quit()
        self.logger.info("**** test_001_AccountRegistration finished *** ")


