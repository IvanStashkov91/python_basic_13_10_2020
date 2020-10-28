import json
import requests
import homeworks

url = 'https://5ka.ru/api/v2/special_offers/?store=&records_per_page=12&page=1&categories=&ordering=&price_promo__gte=&price_promo__lte=&search='

response = requests.get(url)

data = json.loads(response.text)

print(1)

#
# url = 'https://d2xzmw6cctk25h.cloudfront.net/geekbrains/public/ckeditor_assets/pictures/9898/retina-c02461738f9570b643224f572f9b15d7.png'
#
# response = requests.get(url)

# file = open('gb_blog_image.png', 'wb')
# try:
#     file.write(response.content)
# except IOError:
#     pass
# finally:
#     file.close()
# print(1)
#
# with open("gb_blog_image.png", 'rb') as file:
#     lines = file.read(4)
#     print(1)
