from account import Account
import time
import random

email = ""
password = ""


msgs = [line for line in open("msgs.txt", encoding="utf-8")]

def save(filename, listu):
	with open(filename, "a", encoding="utf-8") as f:
		f.write("\n".join(listu))


def send_people_things():
	account.authenticate(email, password)
	time.sleep(3)
	pajeets = account.get_most_recent_conversations(5)
	for pajeet in pajeets:
		chat = account.get_chatlog(pajeet, 5)
		for msg in chat:
				try:
					if msg["author"] == pajeet and not msg["content"] in msgs:
						msgs.append(msg["content"])
						print(msg["content"])
				except:
					pass
		time.sleep(3)
	save("msgs.txt", msgs)
	while True:
		pajeets = account.get_most_recent_conversations(0)
		for pajeet in pajeets:
			chat = account.get_chatlog(pajeet, 0)
			for msg in chat:
				try:
					if msg["author"] == pajeet and not msg["content"] in msgs:
						msgs.append(msg["content"])
						print(msg["content"])
				except:
					pass
			for _ in range(random.randint(1,4)):
				account.send_message(pajeet, random.choice(msgs))
				time.sleep(5)
			time.sleep(10)
		time.sleep(10)
		save("msgs.txt", msgs)

def scrape_groups():
	account.authenticate(email, password)
	time.sleep(6)
	groups = account.get_groups()
	time.sleep(6)
	for group in groups:
		post_ids = account.get_post_IDs_from_group(group, 4)
		time.sleep(10)
		for post in post_ids:
			comments = account.get_comments_from_group_post(group, post)
			time.sleep(6)
			print(comments)

			
		

if __name__ == "__main__":
	account = Account("C:\\Users\\Ahmed Tounsi\\chromedriver.exe", headless=False)
	try:
		send_people_things()
	except:
		account.exit()