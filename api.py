import requests
import base64


class API:
    def __init__(self):
        self.session = requests.Session()

    def get_image_as_base64(self, url):
        try:
            response = requests.get(url)
        except Exception as error:
            raise Exception("Unable to make GET request {}".format(error))

        return base64.b64encode(response.content)

