from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurações do navegador
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # Iniciar maximizado
options.add_argument('--disable-infobars')  # Desabilitar infobars
options.add_argument('--disable-extensions')  # Desabilitar extensões

# Inicializa o serviço do ChromeDriver automaticamente usando o webdriver_manager
service = Service(ChromeDriverManager().install())

# Inicializa o navegador com o serviço e opções configuradas
driver = webdriver.Chrome(service=service, options=options)

try:
    # Navega até a página de login
    driver.get('https://pje1g.trf3.jus.br/pje/authenticateSSO.seam')  # URL da página de login

    # Aguarda alguns segundos para garantir que a página foi carregada
    time.sleep(3)

    # Encontra o campo de usuário pelo seu nome e digita o nome de usuário
    campo_usuario = driver.find_element(By.NAME, 'username')  # Substitua 'username' pelo nome correto do campo
    campo_usuario.send_keys('39918397845')  # Substitua 'seu_usuario' pelo seu nome de usuário

    # Encontra o campo de senha pelo seu nome e digita a senha
    campo_senha = driver.find_element(By.NAME, 'password')  # Substitua 'password' pelo nome correto do campo
    campo_senha.send_keys('103Jhms@')  # Substitua 'sua_senha' pela sua senha

    # Submete o formulário de login
    campo_senha.send_keys(Keys.RETURN)

    # Aguarda até que a URL da segunda página seja carregada completamente
    WebDriverWait(driver, 10).until(EC.url_matches('https://pje1g.trf3.jus.br/pje/Push/listView.seam'))

    # Espera alguns segundos adicionais para garantir que a página esteja completamente carregada (opcional)
    time.sleep(5)

finally:
    # Feche o navegador
    driver.quit()