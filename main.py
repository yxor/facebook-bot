from bot import Account
import time
import random


email = "ava.miller83581293@protonmail.com"
password = "bigthot"

msgs = [
	"hi"
]


if __name__ == "__main__":
	account = Account("C:\\Users\\Ahmed Tounsi\\chromedriver.exe")
	account.authenticate(email, password)
	time.sleep(3)
	time.sleep(3)
	while True:
		account.accept_all_friends()
		pajeets = account.get_most_recent_conversations(0)
		print(pajeets)
		time.sleep(3)
		for pajeet in pajeets:
			account.send_message(pajeet, random.choice(msgs))
			time.sleep(5)


