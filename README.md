# NotifyBot
Python client for LINE Notify API. API document: [Here](https://notify-bot.line.me/doc/en/) 

## Installation 
1) Clone this repository
```bash
$ git clone https://github.com/Kashu7100/NotifyBot.git
$ cd NotifyBot
```
2) Install NotifyBot
```bash
$ python setup.py install
```

## Usage
Once NotifyBot is installed, you can use following commands:

```
$ register_notify_token -h
usage: register_notify_token [-h] accesstoken

Register LINE Notify API token

positional arguments:
  accesstoken  access token

optional arguments:
  -h, --help   show this help message and exit

end
```

```
$ send_notify -h
usage: send_notify [-h] [-i IMAGE] [-sp STICKERPACKAGE] [-s STICKER] message

Send LINE Notify message

positional arguments:
  message               The message to send. Maximum length is 1000.

optional arguments:
  -h, --help            show this help message and exit
  -i IMAGE, --image IMAGE
                        image to be sent
  -sp STICKERPACKAGE, --stickerpackage STICKERPACKAGE
                        sticker package ID
  -s STICKER, --sticker STICKER
                        sticker ID

end
```
