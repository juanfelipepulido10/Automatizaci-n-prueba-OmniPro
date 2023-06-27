import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import cv2
import time

class Assessment_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Busqueda_navegador(self):
        driver = self.driver
        driver.implicitly_wait(5)
        self.driver.maximize_window()
        driver.get('https://www.mercadolibre.com.co/')
        self.assertIn('Mercado Libre',driver.title)
        Barra_busqueda = driver.find_element(By.XPATH,'//*[@id="cb1-edit"]')
        time.sleep(2)
        Barra_busqueda.send_keys("BMW serie 3")
        Barra_busqueda.send_keys(Keys.RETURN)
        time.sleep(5)
        assert 'El titulo ingresado no corresponde' not in driver.page_source

    def test_filtro(self):
        driver = self.driver
        driver.implicitly_wait(5)
        self.driver.maximize_window()
        driver.get('https://www.mercadolibre.com.co/')
        Barra_busqueda = driver.find_element(By.XPATH,'//*[@id="cb1-edit"]')
        time.sleep(3)
        Barra_busqueda.send_keys("BMW serie 3")
        Barra_busqueda.send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        Filtro_ciudad = driver.find_element(By.XPATH,'//*[@id="root-app"]/div/div[2]/aside/section[2]/div[5]/ul/li[1]/a/span[1]')
        driver.execute_script("arguments[0].click();", Filtro_ciudad)
        driver.implicitly_wait(10)
        Filtro_modelo = driver.find_element(By.XPATH,'//*[@id="root-app"]/div/div[2]/aside/section[2]/div[3]/ul/li[1]/a/span[1]')
        driver.execute_script("arguments[0].click();", Filtro_modelo)
        driver.implicitly_wait(10)
        Ordenar = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/div[2]/div[2]/div/div/div[2]/div/div/button/span')
        driver.execute_script("arguments[0].click();", Ordenar)
        driver.implicitly_wait(10)
        Ordenar_menor_valor = driver.find_element(By.XPATH, '//*[@id="andes-dropdown-más-relevantes-list-option-price_asc"]/div/div/span')
        driver.execute_script("arguments[0].click();", Ordenar_menor_valor)
        driver.implicitly_wait(10)
        Filtro_financiamiento = driver.find_element(By.XPATH,'//*[@id="is_financeable_highlighted"]')
        driver.execute_script("arguments[0].click();", Filtro_financiamiento)
        time.sleep(5)

    def test_formulario (self):
        driver = self.driver
        driver.implicitly_wait(5)
        self.driver.maximize_window()
        driver.get('https://www.mercadolibre.com.co/')
        Search = driver.find_element(By.XPATH, '//*[@id="cb1-edit"]')
        Search.send_keys("bmw serie 3 318i e90 lci")
        Search.send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        Filtro_categoria = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/aside/section/div[4]/ul/li[1]/a/span[1]')
        driver.execute_script("arguments[0].click();", Filtro_categoria)
        driver.implicitly_wait(10)
        Ordenar = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/div[2]/div[2]/div/div/div[2]/div/div/button/span')
        driver.execute_script("arguments[0].click();", Ordenar)
        driver.implicitly_wait(10)
        Menor_precio = driver.find_element(By.XPATH, '//*[@id="andes-dropdown-más-relevantes-list-option-price_asc"]/div/div/span')
        driver.execute_script("arguments[0].click();", Menor_precio)
        driver.implicitly_wait(10)
        Select_car = driver.find_element(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/ol[1]/li[1]/div/div/div[2]/div/div[3]/a')
        driver.execute_script("arguments[0].click();", Select_car)
        driver.implicitly_wait(10)
        driver.switch_to.window(driver.window_handles[1])
        Barra_name = driver.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[2]/div[2]/div[4]/form/div[1]/div[1]/label/div/input')
        time.sleep(2)
        Barra_name.send_keys("Juan")
        Barra_Last_name = driver.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[2]/div[2]/div[4]/form/div[1]/div[2]/label/div/input')
        time.sleep(1)
        Barra_Last_name.send_keys("Pulido")
        time.sleep(1)
        Barra_email = driver.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[2]/div[2]/div[4]/form/div[1]/div[3]/label/div/input')
        time.sleep(1)
        Barra_email.send_keys("juanfelipepulido10@gmail.com")
        time.sleep(1)
        Barra_tel = driver.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[2]/div[2]/div[4]/form/div[1]/div[4]/label/div/input')
        time.sleep(1)
        Barra_tel.send_keys("3005453503")
        time.sleep(1)
        Barra_comentario = driver.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[2]/div[2]/div[4]/form/div[1]/div[5]/label/div/textarea')
        time.sleep(1)
        Barra_comentario.send_keys("Estoy interesado en el vehículo, ¿Aún se encuentra disponible?")
        time.sleep(1)
        Checkbox_terminos = driver.find_element(By.XPATH, '//*[@id="ui-pdp-main-container"]/div[2]/div[2]/div[4]/form/div[2]/label/input')
        time.sleep(1)
        driver.execute_script("arguments[0].click();", Checkbox_terminos)
        driver.implicitly_wait(10)
        Preguntar_boton = driver.find_element(By.XPATH,'//*[@id="ui-pdp-main-container"]/div[2]/div[2]/div[4]/form/div[3]/button/span')
        print(Preguntar_boton.is_displayed())
        print(Preguntar_boton.is_enabled())
        time.sleep(5)

    def test_documentacion(self):
        driver=self.driver

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()





