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
    
    def send(self, message, image=None, package_id=None, sticker_id=None):
        """
        Args:
            message (str): The message to send. Maximum length is 1000.
            image (str): path to the image (optional)
            package_id (int): ID of sticker package (optional). Refer to https://devdocs.line.me/files/sticker_list.pdf
            sticker_id (int): ID of sticker (optional). Refer to https://devdocs.line.me/files/sticker_list.pdf
        """
        params = {'message': str(message)}
        if package_id is not None and sticker_id is not None:
            params.update({
                'stickerPackageId': int(package_id),
                'stickerId': int(sticker_id),
                })
        if image is None:
            r = requests.post(
                NotifyBot.API_URL, 
                headers=self._header, 
                params=params
                )
        else:
            with open(image, 'rb') as f:
                r = requests.post(
                    NotifyBot.API_URL, 
                    headers=self._header, 
                    params=params, 
                    files={'imageFile': f},
                    )
        if not r.ok:
            raise Exception("[*] Could not send message.")

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

    def send_sticker(self, message, package_id, sticker_id):
        """Send a sticker
        Args:
            message (str): Non-empty message to send. Maximum length is 1000.
            package_id (int): ID of sticker package. Refer to https://devdocs.line.me/files/sticker_list.pdf
            sticker_id (int): ID of sticker. Refer to https://devdocs.line.me/files/sticker_list.pdf
        """
        assert isinstance(package_id, int) and isinstance(sticker_id, int)
        r = requests.post(
            NotifyBot.API_URL, 
            headers=self._header, 
            params={
                'message': str(message),
                'stickerPackageId': package_id,
                'stickerId': sticker_id,
                },
            )
        if not r.ok:
            raise Exception("[*] Could not send stiker.")

def register_token():
    import argparse
    parser = argparse.ArgumentParser(
        description='Register LINE Notify API token',
        epilog='end',
        add_help=True,
        )
    parser.add_argument(
        'accesstoken',
        help='access token',
        action='store',
        )
    args = parser.parse_args()
    NotifyBot(args.accesstoken)

def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Register LINE Notify API token',
        epilog='end',
        add_help=True,
        )
    parser.add_argument(
        'message',
        help='The message to send. Maximum length is 1000.',
        action='store',
        )
    parser.add_argument(
        '-i', '--image',
        help='image to be sent',
        action='store',
        required=False,
        default=None,
        )
    parser.add_argument(
        '-sp', '--stickerpackage',
        help='sticker package ID',
        type=int,
        action='store',
        required=False,
        default=None,
        )
    parser.add_argument(
        '-s', '--sticker',
        help='sticker ID',
        type=int,
        action='store',
        required=False,
        default=None,
        )
    args = parser.parse_args()
    bot = NotifyBot()
    bot.send(args.message, args.image, args.stickerpackage, args.sticker)