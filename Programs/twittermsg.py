import urllib.request

password="mahesh@2012"





def twitter():
	password_manager=urllib.request.HTTPPasswordMgr()
	password_manager.add_password("Twitter API", "http://twitter.com/statuses","Mssaboo1",password)
	http_handler=urllib.request.HTTPBasicAuthHandler(password_manager)
	page_opener=urllib.request.build_opener(http_handler)
	urllib.request.install_opener(page_opener)
	params=urllib.parse.urlencode({'status':'HI'})
	resp=urllib.request.urlopen("http://twitter.com/statuses/update.json",params)
	resp.read()


twitter()
