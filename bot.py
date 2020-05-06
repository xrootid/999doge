import cloudscraper, json, sys, importlib, random, string, decimal, time, os
from getpass import getpass
from warna import *
from config import *
def trialuser():
		ch = random.randint(chance1, chance2)
		low = int(1000000) - (ch) * int(10000)
		num_for = "{:.0f}".format
		if base_bet > 0:
			bid = (0 + base_bet) * float(100000000)
		else:
			bid = (0 + base_bet) / float(100000000)
		headers = {
		"user-agent": "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.93 Mobile Safari/537.36",
		"content-type": "application/x-www-form-urlencoded",
		"accept": "*/*",
		"x-requested-with": "com.reland.relandicebot",
		"sec-fetch-site": "cross-site",
		"sec-fetch-mode": "cors",
		"accept-encoding": "gzip, deflate",
		"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
		"cookie": "lang=id"
		}
		url_login = 'https://www.999doge.com/api/web.aspx'
		dlogin = 'a=Login&Key=258aed99b1924356909fd825d695a9ac&Username='+Username+'&Password='+Password+'&Totp='
		dseed = 'a=GetServerSeedHash&s=4b0e122438114b6aa8550df1d4ace992'
		total_profit = int(0)
		scr = cloudscraper.create_scraper()
		login = scr.post(url_login, data=dlogin, headers=headers).text
		logbal = json.loads(login)
		doge = logbal['Doge']
		dogbal = doge['Balance']
		limit = int(50000000000)
		if dogbal > limit:
			print("Silakan membeli premium user")
			print("Limit Trial 500 DOGE")
		else:
			ses = json.loads(login)
			dbet = {
			"a":"PlaceBet",
			"s": ses["SessionCookie"],
			"PayIn": int(bid),
			"Low": low,
			"High":"999999",
			"ClientSeed":"5664556",
			"Currency":"doge",
			"ProtocolVersion":"2"
			}
			ws = 0
			ls = 0
			total = 0
			numws = 0
			numls = 0
			play = scr.post(url_login, data=dbet, headers=headers).json()
			num_format = "{:.8f}".format
			while total < target_profit:
				time.sleep(interval)
				ch = random.randrange(chance1, chance2)
				low = int(1000000) - (ch) * int(10000)
				profit = (play['PayOut'] - bid) / float(100000000)
				bidshow = (0 + bid) / 100000000
				total += profit
				if play['PayOut'] > 0:
					numws += 1
					numls = 0
					balance = (play['StartingBalance'] + play['PayOut']) / float(100000000)
					if numws > ws:
						ws +=1
					print(hijau+"[W]",putih+"["+str(ch)+"]"+hijau,"My Bet Profit: "+num_format(profit)+putih+" ",kuning,"Bet : "+num_format(bidshow),putih)
					if base_bet > 0:
						bid = (0 + base_bet) * float(100000000)
					else:
						bid = (0 + base_bet) / float(100000000)
					bid = int(bid)
					print(biru+"Total "+num_format(total)+putih,kuning+num_format(balance)+putih,hijau+"WS:"+str(ws)+"["+str(numws)+"]",merah+"LS:"+str(ls)+"["+str(numls)+"]"+putih, end="\r") 
					play = scr.post(url_login, data={"a":"PlaceBet","s":ses['SessionCookie'],"PayIn": bid,"Low": low,"High":"999999","ClientSeed":"5664556","Currency":"doge","ProtocolVersion":"2"}, headers=headers).json()
				else:
					numws = 0
					numls += 1
					balance = (play['StartingBalance'] - base_bet) / float(100000000)
					if numls > ls:
						ls += 1
					print(merah+"[L]",putih+"["+str(ch)+"]"+ merah,"My Bet Profit: "+num_format(profit)+putih,kuning,"Bet : "+num_format(bidshow),putih)
					bid = int(bid) * int(if_lose)
					print(biru+"Total "+num_format(total)+putih,kuning+num_format(balance)+putih,hijau+"WS:"+str(ws)+"["+str(numws)+"]",merah+"LS:"+str(ls)+"["+str(numls)+"]"+putih, end="\r") 
					play = scr.post(url_login, data={"a":"PlaceBet","s":ses['SessionCookie'],"PayIn": bid,"Low": low,"High":"999999","ClientSeed":"5664556","Currency":"doge","ProtocolVersion":"2"}, headers=headers).json()
			else:
				print(kuning,"Yay sudah mencapai target profit : ",num_format(total))
def premiumuser():
		ch = random.randint(chance1, chance2)
		low = int(1000000) - (ch) * int(10000)
		num_for = "{:.0f}".format
		if base_bet > 0:
			bid = (0 + base_bet) * float(100000000)
		else:
			bid = (0 + base_bet) / float(100000000)
		headers = {
		"user-agent": "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.93 Mobile Safari/537.36",
		"content-type": "application/x-www-form-urlencoded",
		"accept": "*/*",
		"x-requested-with": "com.reland.relandicebot",
		"sec-fetch-site": "cross-site",
		"sec-fetch-mode": "cors",
		"accept-encoding": "gzip, deflate",
		"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
		"cookie": "lang=id"
		}
		url_login = 'https://www.999doge.com/api/web.aspx'
		dlogin = 'a=Login&Key=258aed99b1924356909fd825d695a9ac&Username='+Username+'&Password='+Password+'&Totp='
		dseed = 'a=GetServerSeedHash&s=4b0e122438114b6aa8550df1d4ace992'
		total_profit = int(0)
		scr = cloudscraper.create_scraper()
		login = scr.post(url_login, data=dlogin, headers=headers)
		ses = json.loads(login.text)
		dbet = {
		"a":"PlaceBet",
		"s": ses["SessionCookie"],
		"PayIn": int(bid),
		"Low": low,
		"High":"999999",
		"ClientSeed":"5664556",
		"Currency":"doge",
		"ProtocolVersion":"2"
		}
		ws = 0
		ls = 0
		total = 0
		numws = 0
		numls = 0
		play = scr.post(url_login, data=dbet, headers=headers).json()
		num_format = "{:.8f}".format
		while total < target_profit:
			time.sleep(interval)
			ch = random.randrange(chance1, chance2)
			low = int(1000000) - (ch) * int(10000)
			profit = (play['PayOut'] - bid) / float(100000000)
			bidshow = (0 + bid) / 100000000
			total += profit
			if play['PayOut'] > 0:
				numws += 1
				numls = 0
				balance = (play['StartingBalance'] + play['PayOut']) / float(100000000)
				if numws > ws:
					ws +=1
				print(hijau+"[W]",putih+"["+str(ch)+"]"+hijau,"My Bet Profit: "+num_format(profit)+putih+" ",kuning,"Bet : "+num_format(bidshow),putih)
				if base_bet > 0:
					bid = (0 + base_bet) * float(100000000)
				else:
					bid = (0 + base_bet) / float(100000000)
				bid = int(bid)
				print(biru+"Total "+num_format(total)+putih,kuning+num_format(balance)+putih,hijau+"WS:"+str(ws)+"["+str(numws)+"]",merah+"LS:"+str(ls)+"["+str(numls)+"]"+putih, end="\r") 
				play = scr.post(url_login, data={"a":"PlaceBet","s":ses['SessionCookie'],"PayIn": bid,"Low": low,"High":"999999","ClientSeed":"5664556","Currency":"doge","ProtocolVersion":"2"}, headers=headers).json()
			else:
				numws = 0
				numls += 1
				balance = (play['StartingBalance'] - base_bet) / float(100000000)
				if numls > ls:
					ls += 1
				print(merah+"[L]",putih+"["+str(ch)+"]"+ merah,"My Bet Profit: "+num_format(profit)+putih,kuning,"Bet : "+num_format(bidshow),putih)
				bid = int(bid) * int(if_lose)
				print(biru+"Total "+num_format(total)+putih,kuning+num_format(balance)+putih,hijau+"WS:"+str(ws)+"["+str(numws)+"]",merah+"LS:"+str(ls)+"["+str(numls)+"]"+putih, end="\r") 
				play = scr.post(url_login, data={"a":"PlaceBet","s":ses['SessionCookie'],"PayIn": bid,"Low": low,"High":"999999","ClientSeed":"5664556","Currency":"doge","ProtocolVersion":"2"}, headers=headers).json()
		else:
			print(kuning,"Yay sudah mencapai target profit : ",num_format(total))
scr = cloudscraper.create_scraper()
url = "https://mastercoinmaru.000webhostapp.com/user.php"
premium = input('Premium Member? Y/N : ')
if premium == 'Y':
	username = input("Username :")
	password = getpass("Password :")
	authcode = scr.post(url, data={"username":username, "password":password}).text
	if authcode == "LOGIN BERHASIL":
		os.system('clear')
		print("\033[1;31m====================================================\033[0m")
		print("\033[1;32m[+]\033[0m             \033[0;36mDO WITH YOUR OWN RISK \033[0m           \033[1;32m[+]\033[0m")
		print("\033[1;32m[+]\033[0m \033[1;33mCreator : Layscape\033[0m                           \033[1;32m[+]\033[0m")
		print("\033[1;32m[+]\033[0m \033[1;33mPremium Script Member\033[0m                        \033[1;32m[+]\033[0m")
		print("\033[1;31m====================================================\033[0m")
		print("Disclaimer : \nScript tidak jalan jangan salahkan author. \nHarap baca petunjuk dengan baik.")
		print("---------------------------")
		premiumuser()
	else:
		print("LOGIN FAILED CHECK USERNAME OR PASSWORD")
