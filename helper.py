import base64


class Helper:

    def encode_file_as_base64(self, file_path):
        with open(file_path, "rb") as img_file:
            return base64.b64encode(img_file.read())
