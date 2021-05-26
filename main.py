from shield import Browser
import logging


logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
m_Browser= Browser(18784179,"Samsung@123")
m_Browser.OpenDriver(True)
m_Browser.OpenShield()
m_Browser.SignIn()
m_Browser.FillQuiz()
m_Browser.AcceptDisclosure()
m_Browser.FillQuestionarie(reason="Work From Home outside NCR")
del m_Browser
