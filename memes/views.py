from django.shortcuts import render

#imports related to apis and data
import requests
import json


#create a header that acts like a firefox browser (to avoid 429 error)
headers={
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"en-US,en;q=0.5",
"Connection":"keep-alive",
"DNT":"1",
"Host":"www.reddit.com",
"TE":"Trailers",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
}

#functions to extract memes from subreddits

def get_r_memes():

	#making response
	memes_response = requests.get("https://www.reddit.com/r/memes.json",headers=headers,params={'limit':'100'})

	#Validating the response
	if memes_response.status_code == 200:
		memes_json = json.loads(memes_response.text)
	elif memes_response.status_code == 429:
		print("!!!! Sending too many requests..... Reddit refused the connection, please try after a while !!!!")
		return None
	else:
		print(f"!!!! Error in connecting --- error code {memes_response.status_code} --- Please check your connection !!!!")
		return None

	#going through all the posts in /r/memes homepage and checking for images

	image_list=[]
	for child in memes_json['data']['children']:
		try:
			if child['data']['post_hint'] == 'image':
				image_list.append(child['data']['url'])
		except:
			pass

	return image_list


def get_r_CricketShitpost():

	#making response
	memes_response = requests.get("https://www.reddit.com/r/CricketShitpost.json",headers=headers,params={'limit':'100'})

	#Validating the response
	if memes_response.status_code == 200:
		memes_json = json.loads(memes_response.text)
	elif memes_response.status_code == 429:
		print("!!!! Sending too many requests..... Reddit refused the connection, please try after a while !!!!")
		return None
	else:
		print(f"!!!! Error in connecting --- error code {memes_response.status_code} --- Please check your connection !!!!")
		return None

	#going through all the posts in /r/memes homepage and checking for images

	image_list=[]
	for child in memes_json['data']['children']:
		try:
			if child['data']['post_hint'] == 'image':
				image_list.append(child['data']['url'])
		except:
			pass

	return image_list



def get_r_DankEngineeringMemes():

	#making response
	memes_response = requests.get("https://www.reddit.com/r/DankEngineeringMemes.json",headers=headers,params={'limit':'100'})

	#Validating the response
	if memes_response.status_code == 200:
		memes_json = json.loads(memes_response.text)
	elif memes_response.status_code == 429:
		print("!!!! Sending too many requests..... Reddit refused the connection, please try after a while !!!!")
		return None
	else:
		print(f"!!!! Error in connecting --- error code {memes_response.status_code} --- Please check your connection !!!!")
		return None

	#going through all the posts in /r/memes homepage and checking for images

	image_list=[]
	for child in memes_json['data']['children']:
		try:
			if child['data']['post_hint'] == 'image':
				image_list.append(child['data']['url'])
		except:
			pass

	return image_list





# Create your views here.

def home_view(request):
	memes = get_r_memes()

	if memes:
		context ={'memes':memes,}
	else:
		print("-------------------error-------------------------------")
	

	return render(request,'homepage.html',context)


def cricket_view(request):
	memes = get_r_CricketShitpost()

	if memes:
		context ={'memes':memes,}
	else:
		print("-------------------error-------------------------------")
	

	return render(request,'cricket.html',context)

def engineering_view(request):
	memes = get_r_DankEngineeringMemes()

	if memes:
		context ={'memes':memes,}
	else:
		print("-------------------error-------------------------------")
	

	return render(request,'engineering.html',context)
