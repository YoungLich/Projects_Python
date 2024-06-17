import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Caminho absoluto para o arquivo login.txt
file_path = r'c:\\Users\User\OneDrive\Área de Trabalho\Login\login.txt'

if not os.path.exists(file_path):
    raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado.")

# Lê o arquivo com os dados de login
with open(file_path, 'r') as file:
    lines = file.readlines()
    username = lines[0].strip()
    password = lines[1].strip()

# Caminho para o ChromeDriver
driver_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe' 

# Verifique se o ChromeDriver existe no caminho fornecido
if not os.path.exists(driver_path):
    raise FileNotFoundError(f"O ChromeDriver não foi encontrado no caminho: {driver_path}")

# Configura o serviço do ChromeDriver
service = Service(driver_path)

# Opções do Chrome
chrome_options = Options()
chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'  # Caminho para o Chrome, se necessário

# Verifique se o navegador Chrome existe no caminho fornecido
if not os.path.exists(chrome_options.binary_location):
    raise FileNotFoundError(f"O navegador Chrome não foi encontrado no caminho: {chrome_options.binary_location}")

# Inicializa o navegador Chrome
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Acessa a página de login
    login_url = 'https://pje1g-sp.tse.jus.br/pje/login.seam?loginComCertificado=false&cid=7819' 
    driver.get(login_url)

    # Encontra e preenche os campos de login
    username_field = driver.find_element(By.NAME, 'username')  # Substitua 'username' pelo nome correto do campo
    password_field = driver.find_element(By.NAME, 'password')  # Substitua 'password' pelo nome correto do campo

    username_field.send_keys(username)
    password_field.send_keys(password)

    # Envia o formulário
    password_field.send_keys(Keys.RETURN)

    # Aguarda a página carregar
    time.sleep(5)

    # Verifica se o login foi bem-sucedido
    if "Welcome" in driver.page_source:  # Ajuste a verificação conforme o conteúdo da página pós-login
        print("Login bem-sucedido!")
        # A partir daqui, você pode interagir com outras páginas autenticadas
        # driver.get('https://example.com/protected-page')
    else:
        print("Falha no login.")
finally:
    # Fecha o navegador
    driver.quit()