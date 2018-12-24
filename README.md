# Facebook Handler

A python library made with selenium to control a facebook account
without the use of the offical API

## Getting Started

 __You need the language of the account you're using to be English(US), otherwise the program will not run.__

### Prerequisites

You need to have the selenium library and the chromewebdriver on your computer:
```
pip install selenium
```

You can get the chromewebdriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). 



### Installing

Clone the library or download it to your machine.

## Running the program

### Authenticating to a facebook account

```python
from account import Account

# run as headless if you want to to see the chrome gui
acc = Account("PATH/TO/CHROMEWEBDRIVE/BINARY.exe", headless=False) 

acc.authenticate("account@email.com", "password1")

# make sure to call the exit method when youre done with the account
# or the process will keep running in the background
acc.exit()
```
### Currently you can use the program to

* Make a Facebook post
* Send a Friend request
* Accept friend requests
* Scrape comments from a facebook profile post
* Get the ids of all the groups the account has joined
* Make a group post
* Get the ids of posts of a certain group
* Get comments from a group post
* Get the ids of people the account has recently talked to
* Get the chatlog of the conversation between the account and other users
* Send a message to another user (or a group chat) 

## Built With

* [selenium](https://selenium-python.readthedocs.io/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
