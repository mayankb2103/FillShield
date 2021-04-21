from shield import Browser
import logging


logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)
m_Browser= Browser(18784179,"Samsung@123")
m_Browser.OpenDriver(True)
m_Browser.OpenShield()
m_Browser.SignIn()
m_Browser.FillQuiz()
m_Browser.AcceptDisclosure()
m_Browser.FillQuestionarie()
del m_Browser
