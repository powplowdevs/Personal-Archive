from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

# change 'ip:port' with your proxy's ip and port
proxy_ip_port = '192.168.1.155:8080'

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
#proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

# replace 'your_absolute_path' with your chrome binary absolute path
driver = webdriver.Chrome('G:\My Drive\Programing\Personal scripts\Py_networking\chromedriver.exe', desired_capabilities=capabilities)

driver.get('https://www.myip.com/')

time.sleep(80)

driver.quit()