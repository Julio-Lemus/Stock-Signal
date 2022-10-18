import requests
import smtplib
from password_file import password, api_key

prices = requests.get(f"https://financialmodelingprep.com/api/v3/quote/DAR?apikey={api_key}").json()
stock_price = prices[0]['price']
email_host = ''

print(stock_price)

def send_email(password):
	server = smtplib.SMTP('smtp.' + '{email_host}', 587)
	server.ehlo()
	server.starttls()
	server.login({email}, password)
	subject = '{stock} is a go!'
	body = 'ER tomorrow!'
	msg = f'subject: {subject} {body}'

	server.sendmail(
		{email},
		{email},
		msg
		)

	print('email is sent')
	server.quit()

target_price = 0
if stock_price >= {target_price}:
	#send an email using smpt
	send_email(password)
