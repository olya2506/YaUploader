import requests as requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_upload_link(self, file_path: str):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Authorization': self.token}
        params = {'path': file_path}
        response = requests.get(upload_url, params=params, headers=headers)
        pprint(response.json())
        return response.json()


    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_upload_link(file_path).get('href')
        response = requests.put(href, data=open(file_path, 'rb'))
        if response.status_code == 201:
            print('Файл загружен')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

