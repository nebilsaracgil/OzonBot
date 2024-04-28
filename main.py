import undetected_chromedriver as uc 
import time 

def import_js_as_string(file_path):
    with open(file_path, 'r') as file:
        js_code = file.read()
    return js_code
 
options = uc.ChromeOptions() 
options.headless = False  

driver = uc.Chrome(use_subprocess=True, options=options) 
driver.get('https://www.ozon.ru/product/kofe-molotyy-carte-noire-original-230-g-138218832/?avtc=1&avte=1&avts=1714216658')



time.sleep(4)
result = driver.execute_script(import_js_as_string('./script.js'))
print(result)

driver.quit()



