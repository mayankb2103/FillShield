from shield_work import Browser
import logging


logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
k_Browser= Browser(18784179,"Samsung@123")
k_Browser.OpenDriver(True)
del k_Browser
m_Browser= Browser(18784179,"Samsung@123")
m_Browser.OpenDriver(False)
m_Browser.OpenShield()
m_Browser.SignIn()
m_Browser.FillQuiz()
m_Browser.AcceptDisclosure()
m_Browser.FillQuestionarie()
#:w
del m_Browser
