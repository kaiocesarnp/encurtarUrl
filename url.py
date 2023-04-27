import pyshorteners

s = pyshorteners.Shortener()

# Define o URL que será encurtado
url = 'https://kaiocesarnp.github.io/portfolio/'

# Encurta o URL usando o serviço TinyURL
short_url = s.tinyurl.short(url)

print(short_url)

# Explicação de cada linha do código:

# import pyshorteners - importa a biblioteca pyshorteners para o código.

# s = pyshorteners.Shortener() - cria um objeto da classe Shortener da biblioteca pyshorteners e atribui a variável "s".

# url = 'https://kaiocesarnp.github.io/portfolio/' - define uma URL que será encurtada e a atribui à variável "url".

# short_url = s.tinyurl.short(url) - chama o método "short" da classe Shortener com o argumento "url" e atribui o resultado a variável "short_url". O método "short" encurta a URL usando o serviço "tinyurl".
    # o método "short" é chamado para o serviço "TinyURL" através da propriedade "tinyurl" do objeto
    #  "Shortener" criado anteriormente. Esse método recebe como argumento a URL que deve ser 
    # encurtada (que é a variável "url" definida anteriormente) e retorna a URL encurtada 
    # pelo serviço "TinyURL". O valor de retorno é atribuído à variável "short_url".

# print(short_url) - imprime a URL encurtada na saída padrão.




# A classe "Shortener" da biblioteca "pyshorteners" é a classe principal que fornece uma interface 
    # para encurtar URLs usando diferentes serviços de encurtamento. Quando um objeto desta 
    # classe é criado, ele possui métodos que podem ser usados para encurtar URLs usando 
    # diferentes serviços de encurtamento, como "TinyURL", "Bitly", "AdFly", entre outros.

# Os métodos fornecidos pela classe "Shortener" geralmente têm um formato comum, onde um método é 
    # usado para selecionar o serviço de encurtamento e, em seguida, o método "short" é chamado 
    # para encurtar a URL. Por exemplo, na linha short_url = s.tinyurl.short(url) do código 
    # fornecido, o método "tinyurl" é usado para selecionar o serviço de encurtamento "TinyURL", 
    # e em seguida, o método "short" é chamado para encurtar a URL definida na variável "url".




