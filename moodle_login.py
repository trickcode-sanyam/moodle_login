from selenium import webdriver


PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")

uid = input("Please enter Kerberos ID: ")
password = input("Please enter your password: ")

id_box = driver.find_element_by_id("username")
id_box.send_keys(uid)

pass_box = driver.find_element_by_id("password")
pass_box.send_keys(password)

form = driver.find_element_by_id("login")
formText = form.text.split("\n")
captchaPrompt = formText[3].split(" ")
if captchaPrompt[1] == 'subtract':
    captcha = round(int(captchaPrompt[2])) - round(int(captchaPrompt[4]))
elif captchaPrompt[1] == 'add':
    captcha = round(int(captchaPrompt[2])) + round(int(captchaPrompt[4]))
elif captchaPrompt[2] == 'first':
    captcha = round(int(captchaPrompt[4]))
else:
    captcha = round(int(captchaPrompt[6]))

captcha_box = driver.find_element_by_id("valuepkg3")
captcha_box.send_keys(captcha)

loginbtn = driver.find_element_by_id("loginbtn")
loginbtn.click()


