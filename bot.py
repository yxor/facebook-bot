from account import Account
import time, random


class Bot:
    def __init__(self, email, password):
        self.account = Account()
        self.account.authenticate(email, password)

        self.groups = self.account.get_groups()
        self.emails = [ email for email in open("data/emails.txt") ]
        self.group_posts = []
        self.profile_posts = []
        
        
    def post_loop(self):
        temp_post = "hey guys i got a collection of e-books about few programming languages that i want to share, drop your email if you want to get it https://imgur.com/a/f0ALN7O/"
        ## posting the temp_post once and every group and pushing the infos of the posts in
        ## self.group_posts
        for k in range(len(self.groups)):
            uid = self.account.post_group(self.groups[k], temp_post)
            self.group_posts.append({"key":k, "groupid":self.groups[k], "id": uid})
            self.wait(0.5)
        self.save_posts()

    def collect_loop(self):
        self.load_posts()
        ## goes through every post in self.group_posts and gets all comments and look for emails
        ## and if found it stores them in the emails.txt
        for k in range(len(self.group_posts)):
            comments = self.account.get_comments_from_group_post(self.group_posts[k]["groupid"], self.group_posts[k]["id"])
            self.emails += self.get_emails_from_comments(comments)
            self.wait(0.2)
        self.save_emails()

    def save_emails(self):
        with open("data/emails.txt", "w") as f:
            f.write("\n".join(self.emails))

    def save_posts(self):
        with open("data/posts.txt", "w") as f:
            text = "\n".join([ f'{post["key"]} {post["groupid"]} {post["id"]}' for post in self.group_posts])
            f.write(text)

    def load_posts(self):
        with open("data/posts.txt", "r") as f:
            text = f.read()
            self.group_posts += [{"key":line.split()[0], "groupid":line.split()[1], "id":line.split()[2]} \
                            for line in text.split("\n")]

    @staticmethod
    def wait(mins):
        time.sleep(60 * mins)
	
    @staticmethod
    def get_emails_from_comments(comments):
        emails = []		
        for comment in comments:
            words = comment.split()
            for word in words:
                if '@' in word:
                    emails.append(word)	
        return emails	