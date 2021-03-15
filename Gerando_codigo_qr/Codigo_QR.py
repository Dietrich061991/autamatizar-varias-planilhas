import pyqrcode
# usando o link do meu perfil  do lunkdin para gerar o codigo
my_url = pyqrcode.create('https://www.linkedin.com/in/dietrich-montcho-b13672121/')
# gerando o codigo QR
my_url.svg('my_linkedin.svg', scale=1)
#vizualisando no terminal
print(my_url.terminal (quiet_zone=1))