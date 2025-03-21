import os
from functions import VkBot
from time import sleep


if __name__ == '__main__':

    session = VkBot(access_token=os.getenv('VKTOKEN'))

    search_result = session.search_users(age=22, sex=1, city='Новосибирск')

    for profile in search_result:
        print(profile['id'])
        print(f'{profile["first_name"]} {profile["last_name"]}')
        print(f'https://vk.com/id{profile["id"]}')
        print(session.get_photo_links(user_id=profile['id']))
        sleep(0.1)