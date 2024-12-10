import requests
from bs4 import BeautifulSoup
from telegram import Bot
from telegram.error import TelegramError

# Configurações do Telegram
TELEGRAM_API_TOKEN = '7866607840:AAFRdr1e7LwuUnUZ2mFXG1XWSXxCPV62rnQ'
CHAT_ID = '1725903374'
bot = Bot(token=TELEGRAM_API_TOKEN)

# URL da Facebook Ad Library com o filtro de "Bet"
url = "https://web.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&is_targeted_country=false&media_type=all&q=Bet&search_type=keyword_unordered"

# Função para fazer o scraping da página
def get_ads_from_facebook():
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Erro ao acessar a página")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    ads = []
    ad_elements = soup.find_all('div', class_='some_class_name')  # Ajuste conforme o HTML real
    
    for ad in ad_elements:
        ad_text = ad.get_text()
        ads.append(ad_text)
    
    return ads

# Função para enviar os anúncios para o Telegram
def send_ads_to_telegram(ads):
    for ad in ads:
        try:
            bot.send_message(chat_id=CHAT_ID, text=ad)
        except TelegramError as e:
            print(f"Erro ao enviar mensagem para o Telegram: {e}")

# Executar o scraping e enviar os anúncios
ads = get_ads_from_facebook()
if ads:
    send_ads_to_telegram(ads)
else:
    print("Nenhum anúncio encontrado.")
