from secret import LOGIN, PASSWORD
import vk_api
import requests

session = vk_api.VkApi(login=LOGIN, password=PASSWORD, auth_handler=lambda: (input(), True))
session.auth()

upload = vk_api.VkUpload(session)
photo = upload.photo(photos=['static/img/lady.png', ],
                     album_id=88005553535)
vk_photo_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"

vk = session.get_api()
