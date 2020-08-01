import requests
import os

class NotifyBot(object):
    """ Python client for LINE Notify API
    Args:
        token (str): LINE Notify API token which can be obtained from https://notify-bot.line.me/ .
                     If nothing is given, it will load the token used last time.
    """
    API_URL = "https://notify-api.line.me/api/notify"
    def __init__(self, token=None):
        PATH = os.path.dirname(os.path.abspath(__file__))
        if token is None:
            try:
                with open(f"{PATH}/token", "r") as f:
                    self._token = f.readlines()[-1].rstrip("\n")
            except:
                raise Exception("[*] Not token specified.")
        else:
            self._token = token
        if not os.path.exists(f"{PATH}/token"):
            with open(f"{PATH}/token", "w") as f:
                f.write(self._token+"\n")
        else:
            with open(f"{PATH}/token", "r") as f:
                if self._token+"\n" not in f.readlines():
                    with open(f"{PATH}/token", "a") as f:
                        f.write(self._token+"\n")
        self._header = {'Authorization': 'Bearer ' + self._token}

    def send_message(self, message):
        """
        Args:
            message (str): The message to send. Maximum length is 1000.
        """
        r = requests.post(
            NotifyBot.API_URL, 
            headers=self._header, 
            params={'message': str(message)},
            )
        if not r.ok:
            raise Exception("[*] Could not send message.")

    def send_image(self, caption, image):
        """
        Args:
            caption (str): Non-empty caption to send
            image (str): path to the image        
        """
        with open(image, 'rb') as f:
            r = requests.post(
                NotifyBot.API_URL, 
                headers=self._header, 
                params={'message': str(caption)}, 
                files={'imageFile': f},
                )
        if not r.ok:
            raise Exception("[*] Failed to send image")

    def send_sticker(self, message, page_id, sticker_id):
        """Send a sticker
        Args:
            message (str): Non-empty message to send. Maximum length is 1000.
            page_id (int): ID of sticker package. Refer to https://devdocs.line.me/files/sticker_list.pdf
            sticker_id (int): ID of sticker. Refer to https://devdocs.line.me/files/sticker_list.pdf
        """
        assert isinstance(page_id, int) and isinstance(sticker_id, int)
        r = requests.post(
            NotifyBot.API_URL, 
            headers=self._header, 
            params={
                'message': str(message),
                'stickerPackageId': page_id,
                'stickerId': sticker_id,
                },
            )
        if not r.ok:
            raise Exception("[*] Could not send stiker.")

if __name__ == '__main__':
    token = "YOUR API TOKEN"
    bot = NotifyBot(token)

    bot.send_message("test")