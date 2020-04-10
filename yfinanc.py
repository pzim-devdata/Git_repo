import yfinance as yf

CAC40 = yf.Ticker("^FCHI")

hist_an_2000 = CAC40.history(start="2000-01-01",interval = "1d")
hist_15_ans = CAC40.history(period="15y",interval = "1d")
hist_10_ans = CAC40.history(period="10y",interval = "1d")
hist_5_ans = CAC40.history(period="5y",interval = "1d")
aujourdhui = CAC40.history(period="1d",interval = "1m")

def ajout_colonne_date(hist) :
	Date=[]
	Date_string=[]
	Heure_string=[]
	for x in hist.index:
		Date.append(x)
	for x in hist.index:
		Date_string.append(x.strftime("%A %d %b %Y"))
	for x in hist.index:
		Heure_string.append(x.strftime("%Hh%M GMT +1"))
	hist['Date']=Date
	hist['Date_string']=Date_string
	hist['Heure_string']=Heure_string

ajout_colonne_date(hist_an_2000)
ajout_colonne_date(hist_15_ans) 
ajout_colonne_date(hist_10_ans)
ajout_colonne_date(hist_5_ans)
ajout_colonne_date(aujourdhui)


minimum2000 = hist_an_2000[hist_an_2000.Low == hist_an_2000.Low.min()]
minimum15ans = hist_15_ans[hist_15_ans.Low == hist_15_ans.Low.min()]
minimum10ans = hist_10_ans[hist_10_ans.Low == hist_10_ans.Low.min()]
minimum5ans = hist_5_ans[hist_5_ans.Low == hist_5_ans.Low.min()]

maximum2000 = hist_an_2000[hist_an_2000.High == hist_an_2000.High.max()]
maximum15ans = hist_15_ans[hist_15_ans.High == hist_15_ans.High.max()]
maximum10ans = hist_10_ans[hist_10_ans.High == hist_10_ans.High.max()]
maximum5ans = hist_5_ans[hist_5_ans.High == hist_5_ans.High.max()]

with open("CAC40.txt", "w") as text_file:
	print(f"Depuis l'an 2000, le cours du CAC40 est tombé à "+str(minimum2000.Low.min())+" points, le "+ minimum2000.Date_string.min() +". \n\nAu cours des 15 dernières années, le cours du CAC40 est tombé à "+str(minimum15ans.Low.min())+" points, le "+ minimum15ans.Date_string.min() +". \n\nAu cours des 10 dernières années, le cours du CAC40 est tombé à "+str(minimum10ans.Low.min())+" points, le "+ minimum10ans.Date_string.min() +". \n\nAu cours des 5 dernières années, le cours du CAC40 est tombé à "+str(minimum5ans.Low.min())+" points, le "+ minimum5ans.Date_string.min() +". \n\nAujourd'hui, le " + aujourdhui.Date_string.min() +", le CAC40 vaut " + str(aujourdhui.iloc[-1,0]) + " points à "+ aujourdhui.Heure_string.max()+". \n\nLe CAC40 a varié de " + str(round(aujourdhui.iloc[-1,0]*100/ minimum5ans.Low.min(),2))+" %, depuis son point le plus bas du " +minimum5ans.Date_string.min()+". \n\nLe CAC40 a varié de "+str(round(100-maximum5ans.High.max()*100/aujourdhui.iloc[-1,0] ,2)) +" % depuis son point le plus haut de ces 5 dernières années du "+maximum5ans.Date_string.max(), file=text_file) 
	text_file.close()

with open("/home/venus/Git_repo/Site_Web/CAC40.html", "w") as text_file:
	print("""<!DOCTYPE html><html><head><meta name="description" content="Welcome to the pzim.fr website! Consult the 'words of the day' most used on Twitter in France and around the world."><meta name="keywords" content="Words of the day, words of today, word of the day, words of the day, twitter, Twitter, most common, most common words on Twitter, GitHub pages, pzim.fr, pzim, pzim-devdata, Wordcloud, wordcloud, mot de jour, mots d'aujourd'hui, mot du jour sur twitter, news, actualité, quel est le mot le plus utilisé sur Twitter, mot le plus utilise sur Twitter"><meta http-equiv="refresh" content="600"><meta name="author" content="Pzim"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="utf-8" ><link rel="stylesheet" href="style.css"/><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"></head><body style="background-color:OldLace;font-size: 2vw;"><section>Today, """ + aujourdhui.Date_string.min() +", the value of the CAC40 is " + str(aujourdhui.iloc[-1,0]) + " points at "+ aujourdhui.Heure_string.max()+". <br><br>The CAC40 increased by +" + str(-round(100-aujourdhui.iloc[-1,0]*100/ minimum5ans.Low.min(),2))+"% from its lowest point on " +minimum5ans.Date_string.min()+". <br><br>The CAC40 has varied by "+str(round(100-maximum5ans.High.max()*100/aujourdhui.iloc[-1,0] ,2)) +"% since its highest point in the last 5 years from "+maximum5ans.Date_string.max()+".<br><br>Since the year 2000, the value of the CAC40 has dropped to "+str(minimum2000.Low.min())+" points on "+ minimum2000.Date_string.min() +". <br><br>Over the past 15 years, the value of the CAC40 has fallen to "+str(minimum15ans.Low.min())+" points on "+ minimum15ans.Date_string.min() +". <br><br>Over the past 10 years, the value of the CAC40 has fallen to "+str(minimum10ans.Low.min())+" points on "+ minimum10ans.Date_string.min() +". <br><br>In the past 5 years, the value of the CAC40 has fallen to "+str(minimum5ans.Low.min())+" points on "+ minimum5ans.Date_string.min() +""". </section></body></html>""", file=text_file) 
	text_file.close()

