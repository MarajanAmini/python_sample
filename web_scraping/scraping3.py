import requests
from bs4 import BeautifulSoup
import os

def get_data(res_one):
	img = res_one.find("img")
	img_link = img["src"]
	img_title = img["alt"]
	return img_title, img_link

def download_img (img_link):
	respons = requests.get(img_link)
	if respons.status_code == 200:
		return respons.content
	return False


def save_img(result,img_title):
	path_img1 = os.path.join(folder,img_title,img_title + ".jpg")
	print(path_img1)
	with open(path_img1,"wb") as f:
		f.write(result)
		
url = "https://www.zaban.shop/product/list/10_383_30/%D8%A7%D9%85%D8%B1%DB%8C%DA%A9%D9%86-%D9%87%D8%AF%D9%88%DB%8C-american-headway"
respons = requests.get(url)
print(respons.status_code)
soup = BeautifulSoup(respons.text,"html.parser")
folder ="/home/amini/Desktop/images"
res = soup.find_all("div",class_= "product-item")
for res_one in res:
	img_title,img_link = get_data(res_one)
	print(img_title,img_link)
	img_title = img_title.replace("/","")

	os.makedirs(os.path.join(folder,img_title),exist_ok = True )
	result = download_img(img_link)
	if result:
		save_img(result,img_title)
