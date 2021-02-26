import sys
from selenium import webdriver
from os import mkdir
options = webdriver.ChromeOptions()
# adding this line, and options = options in webdriver.Chrome() gives full screenshot functionality to below code.
# without this, it gives viewport only
options.headless = True #(if we want no UI to be displayed)

PATH = "./chromedriver.exe"
driver = webdriver.Chrome(PATH,options=options)
problemset = sys.argv[1]
driver.get("https://codeforces.com/contest/" + problemset)
problemtable = driver.find_element_by_class_name("problems")
rows = problemtable.find_elements_by_tag_name("tr")
questions = []

for row in rows[1:]:
    toQues = row.find_element_by_tag_name("a")
    qNo = str(toQues.text)
    questions.append(qNo)

mkdir(problemset)
for qNo in questions:
    pathDir = problemset + '/' + qNo
    mkdir(pathDir)
    urlQues = 'https://codeforces.com/problemset/problem/' + problemset + '/' + qNo
    driver.get(urlQues)
    
    samples = driver.find_element_by_class_name('sample-test')
    inputs = samples.find_elements_by_class_name('input')
    outputs = samples.find_elements_by_class_name('output')
    count = 0
    for input in inputs:
        count+=1
        path = pathDir + '/input' + str(count) + '.txt'
        f = open(path, "at")
        data = input.find_element_by_tag_name("pre")
        f.write(data.text)
    count = 0
    for output in outputs:
        count+=1
        path = pathDir + '/output' + str(count) + '.txt'
        f = open(path, "at")
        data = input.find_element_by_tag_name("pre")
        f.write(data.text)        
    
    path = pathDir + "/problem.png"
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment (copied comment, don't know what it means)
    driver.find_element_by_tag_name('body').screenshot(path)
    # why can't use driver.close() here? gives invalid session id
    # driver.save_screenshot(path) gives incomplete screenshot

