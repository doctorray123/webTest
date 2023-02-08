import webTest
import test_data
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
url=test_data.url['url']
username=test_data.login_data['username']
password=test_data.login_data['password']
s_key=test_data.s_key['s_key']

result=webTest.search_key(url,driver,username,password,s_key)
print(result)
if s_key in result:
    print("search pass!")
else:
    print("search failed!")
