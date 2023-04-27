import pyshorteners

s = pyshorteners.Shortener()

# Define o URL que será encurtado
url = 'https://kaiocesarnp.github.io/portfolio/'

# Encurta o URL usando o serviço TinyURL
short_url = s.tinyurl.short(url)

print(short_url)