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

with open("/home/venus/Git_repo/Site_Web/index.html", "w") as text_file:
	print("""<!DOCTYPE html>\n
<html lang="en-US">\n
  	<head>\n
		<meta name="description" content="Welcome to the pzim.fr website! Consult the 'words of the day' most used on Twitter in France and around the world.">\n
		<meta name="keywords" content="Words of the day, words of today, word of the day, words of the day, twitter, Twitter, most common, most common words on Twitter, GitHub pages, pzim.fr, pzim, pzim-devdata, Wordcloud, wordcloud, mot de jour, mots d'aujourd'hui, mot du jour sur twitter, news, actualité, quel est le mot le plus utilisé sur Twitter, mot le plus utilise sur Twitter">\n
		<meta http-equiv="refresh" content="600">\n
		<meta name="author" content="Pzim">\n
		<meta name="viewport" content="width=device-width, initial-scale=1.0">\n
		\n
    		<meta charset="utf-8" >\n
    		<link rel="stylesheet" href="style.css"/>\n
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">\n
\n		
		<link rel="icon" type="image/gif" href="images/favicon/animated_favicon1.gif">\n
		<link rel="shortcut icon" href="images/favicon/favicon.ico">\n
		<link rel="apple-touch-icon" href="images/favicon/apple-touch-icon.png">\n
		<link rel="apple-touch-icon" sizes="57x57" href="images/favicon/apple-icon-57x57.png">\n
		<link rel="apple-touch-icon" sizes="60x60" href="images/favicon/apple-icon-60x60.png">\n
		<link rel="apple-touch-icon" sizes="72x72" href="images/favicon/apple-icon-72x72.png">\n
		<link rel="apple-touch-icon" sizes="76x76" href="images/favicon/apple-icon-76x76.png">\n
		<link rel="apple-touch-icon" sizes="114x114" href="images/favicon/apple-icon-114x114.png">\n
		<link rel="apple-touch-icon" sizes="120x120" href="images/favicon/apple-icon-120x120.png">\n
		<link rel="apple-touch-icon" sizes="144x144" href="images/favicon/apple-icon-144x144.png">\n
		<link rel="apple-touch-icon" sizes="152x152" href="images/favicon/apple-icon-152x152.png">\n
		<link rel="apple-touch-icon" sizes="180x180" href="images/favicon/apple-icon-180x180.png">\n
		<link rel="icon" type="image/png" sizes="192x192"  href="images/favicon/android-icon-192x192.png">\n
		<link rel="icon" type="image/png" sizes="32x32" href="images/favicon/favicon-32x32.png">\n
		<link rel="icon" type="image/png" sizes="96x96" href="images/favicon/favicon-96x96.png">\n
		<link rel="icon" type="image/png" sizes="16x16" href="images/favicon/favicon-16x16.png">\n
		<link rel="manifest" href="/images/favicon/manifest.json">\n
		<meta name="msapplication-TileColor" content="#ffffff">\n
		<meta name="msapplication-TileImage" content="/images/favicon/ms-icon-144x144.png">\n
		<meta name="theme-color" content="#ffffff">\n
		\n
		<title>Welcome to my Github website</title>\n
		<script type="application/ld+json">\n
		\n
    {\n
      "@context": "https://schema.org",\n
      "@type": "Organization",\n
      "url": "http://pzim.fr/",\n
      "logo": "https://github.com/pzim-devdata/pzim-devdata.github.io/raw/master/images/favicon/apple-icon-180x180.png"},\n
      "member": {\n
    "@type": "Person",\n
    "image": "https://raw.githubusercontent.com/pzim-devdata/pzim-devdata.github.io/master/images/mon_profil.webp",\n
    "disambiguatingDescription": "I am a passionate person  about coding and new technologies",\n
    "jobTitle" : "DATA Developer",\n
    "name": "Pzim",\n
    "sameAs": "http://www.pzim.fr/",\n
    "address": {\n
  "@type": "PostalAddress",\n
  "addressLocality": "Rueil-Malmaison",\n
  "postalCode": "92500"},\n
      "email": "mailto:contact@pzim.fr"}\n
   	        </script>\n
		\n
		\n
	        <script>\n
	            function myFunction() {\n
	      	    var x = document.lastModified;\n
	      	    document.getElementById("demo").innerHTML = x;\n
	   	    }\n
	        </script>\n
\n
  	</head>\n
	\n
	\n
	<body onload="myFunction()", style="background-color:snow;">\n
		\n
		<a href="javascript:" id="return-to-top"><i class="icon-chevron-up"></i></a>\n
		<!-- ICON NEEDS FONT AWESOME FOR CHEVRON UP ICON -->\n
		<link href="//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css" rel="stylesheet">\n
		\n
		<header>\n
			\n
			<ul>\n
  				<li id="head"><a id="alink" href="https://pzim-devdata.github.io/">Home</a>&nbsp;&nbsp;&nbsp;</li>\n
  				<li id="head"><a id="alink" href="https://github.com/pzim-devdata/Tools-for-Linux">Linux</a>&nbsp;&nbsp;&nbsp;</li>\n
				<li id="head"><a id="alink" href="https://github.com/pzim-devdata/Skills-and-training-certificates">Skills</a>&nbsp;&nbsp;&nbsp;</li>\n
				<li id="head"><a id="alink" href="https://github.com/pzim-devdata/DATA-developer">Projects</a>&nbsp;&nbsp;&nbsp;</li>\n
  				<li id="head"><a id="alink" href="mailto:contact@pzim.fr?Subject=Contact%20from%20Git">Contact</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>\n
				<li id="right"><a id="alink" href="https://github.com/pzim-devdata"><picture>\n
												  			<source srcset="\n
			images/gitwhite.webp 600w,\n
			images/gitwhite.webp 1200w" type="image/webp">\n
												  			<source srcset="\n
			images/gitwhite.jpg 600w, \n
			images/gitwhite.jpg 1200w" type="image/jpeg">\n
										   			<img alt="GitHub" src="images/gitwhite.jpg " >\n
			</picture></a></li>\n
			</ul>\n
			\n
		</header>\n
		\n
		\n
		<section>\n
		<div id="arriere">\n
			<picture >\n
			  <source srcset="\n
			    images/Banniere.webp 1x,\n
			    images/Banniere.webp 2x" type="image/webp">\n
			  <source srcset="\n
			    images/Banniere.jpg 1x, \n
			    images/Banniere.jpg 2x" type="image/jpeg">\n
			   <img id="arriere" src="images/Banniere.jpg">\n
			</picture>\n
			\n
		</div>\n
		<div id="devant">\n
			<p id="devant">Welcome to my Github website !</p>\n
		</div>\n
		</section>\n
		<section>\n
			<div id="google_translate_element" style="position: relative; text-align: left; left: 3.5vw; top: 0.5vw;"></div>\n

			<script type="text/javascript">\n
			function googleTranslateElementInit() {\n
			  new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element');\n
			}\n
			</script>\n
\n
			<script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>\n
\n
			<h1 id="h1">These are the words of the day on Twitter : <br><br>		</h1>\n
			<p>Last update on : <span id="demo"></span> GMT<br><br></p>\n
									\n
			<div>\n
			    \n
				<picture>\n
				  <source srcset="\n
				    https://raw.githubusercontent.com/pzim-devdata/Git_repo/master/words_of_the_day.webp 1x,\n
				    https://raw.githubusercontent.com/pzim-devdata/Git_repo/master/words_of_the_day.webp 2x" type="image/webp">\n
				  <source srcset="\n
				    https://raw.githubusercontent.com/pzim-devdata/Git_repo/master/words_of_the_day.png 1x, \n
				    https://raw.githubusercontent.com/pzim-devdata/Git_repo/master/words_of_the_day.png 2x" type="image/png">\n
				   <img id="arriere_2" alt="Words of the day on Twitter" src="https://raw.githubusercontent.com/pzim-devdata/Git_repo/master/words_of_the_day.png">\n
				</picture>\n
			</div>\n
			<div>\n
			    <br>\n
				<picture>\n
				  <source srcset="\n
				    https://raw.githubusercontent.com/pzim-devdata/Git_repo/master/mots_du_jour.webp 1x,\n
				    https://raw.githubusercontent.com/pzim-devdata/Git_repo/master/mots_du_jour.webp 2x" type="image/webp">\n
				  <source srcset="\n
				    https://raw.githubusercontent.com/pzim-devdata/Git_repo/master/mots_du_jour.png 1x, \n
				    https://raw.githubusercontent.com/pzim-devdata/Git_repo/master/mots_du_jour.png 2x" type="image/png">\n
				   <img id="arriere_2" alt="Mots du jour sur Twitter" src="https://raw.githubusercontent.com/pzim-devdata/Git_repo/master/mots_du_jour.png">\n
				</picture>\n
			</div>\n
			<p><br>These images are from a program running on a server<br>that automatically checks the most used words on Twitter. <br><br>It's created by myself. <br><br>You can check the Python code of these images on the <a id="link_in_p" href="https://github.com/pzim-devdata/Git_repo/blob/master/Wordcloud_actu_france_demo.py">pzim-devdata GitHub page</a> !\n
			</p>\n
			<p><br>Feel free to 
<a id="link_in_p" href="mailto:contact@pzim.fr?Subject=Contact%20from%20Git" target="_top">contact</a>
 me !<br><br>\n
			</p>\n
		</section>\n
		<section style="background-color:OldLace;">\n
			<p><br><br></p>\n
			<h1 id="h1">This is a real-time analysis of the CAC40 stock market index :<br><br><br>		</h1>\n
			\n
			<div>\n
				<p>\n
On the """ + aujourdhui.Date_string.min() +", the value of the CAC40 is " + str(aujourdhui.iloc[-1,0]) + " points at "+ aujourdhui.Heure_string.max()+". <br><br>The CAC40 increased by +" + str(-round(100-aujourdhui.iloc[-1,0]*100/ minimum5ans.Low.min(),2))+"% from its lowest point on " +minimum5ans.Date_string.min()+". <br><br>The CAC40 has varied by "+str(round(100-maximum5ans.High.max()*100/aujourdhui.iloc[-1,0] ,2)) +"% since its highest point in the last 5 years from "+maximum5ans.Date_string.max()+".<br><br>Since the year 2000, the value of the CAC40 has dropped to "+str(minimum2000.Low.min())+" points on "+ minimum2000.Date_string.min() +". <br><br>Over the past 15 years, the value of the CAC40 has fallen to "+str(minimum15ans.Low.min())+" points on "+ minimum15ans.Date_string.min() +". <br><br>Over the past 10 years, the value of the CAC40 has fallen to "+str(minimum10ans.Low.min())+" points on "+ minimum10ans.Date_string.min() +". <br><br>In the past 5 years, the value of the CAC40 has fallen to "+str(minimum5ans.Low.min())+" points on "+ minimum5ans.Date_string.min() +""". \n
			
				</p>\n
			</div>\n
			<p><br>This text comes from a program running on a <br> server which automatically checks the CAC40 share price. <br> <br> It was created by myself. <br> <br> You can check the Python code of this self-generated text on the <a id = "link_in_p" href = "https://github.com/pzim-devdata/Git_repo/blob/master/yfinanc.py" > GitHub page of pzim-devdata</a> !\n
			</p>\n
			<p><br>Feel free to 
<a id="link_in_p" href="mailto:contact@pzim.fr?Subject=Contact%20from%20Git" target="_top">contact</a>
 me !<br><br>\n
			</p>\n
			<p>\n
				MIT <a id = "link_in_p" href = "https://github.com/pzim-devdata/Git_repo/blob/master/LICENSE" >licence</a><br>\n
Copyright (c) 2020 pzim-devdata\n
			</p>\n
			\n
			<audio controls preload="metadata" autoplay loop >\n
				<source src ="https://github.com/pzim-devdata/Git_repo/raw/master/aa.mp3" type="audio/mpeg">\n
				<source src ="https://github.com/pzim-devdata/Git_repo/raw/master/aa.mp3" type="audio/ogg; codecs=vorbis">\n
				Your browser can't read audio file
			</audio>\n
		
			<script \n
			  type="text/JavaScript" \n
			  language="JavaScript">\n
			\n
			function date_ddmmmyy(date)\n
			{\n
			  var d = date.getDate();\n
			  var m = date.getMonth() + 1;\n
			  var y = date.getYear();\n
\n
			  if(y >= 2000)\n
			  {\n
			    y -= 2000;\n
			  }\n
			  if(y >= 100)\n
			  {\n
			    y -= 100;\n
			  }\n
\n
			  var mmm = \n
			    ( 1==m)?'Jan':( 2==m)?'Feb':(3==m)?'Mar':\n
			    ( 4==m)?'Apr':( 5==m)?'May':(6==m)?'Jun':\n
			    ( 7==m)?'Jul':( 8==m)?'Aug':(9==m)?'Sep':\n
			    (10==m)?'Oct':(11==m)?'Nov':'Dec';\n
\n
			  return "" +\n
			    (d<10?"0"+d:d) + "-" +\n
			    mmm + "-" +\n
			    (y<10?"0"+y:y);\n
			}\n
\n
			function date_lastmodified()\n
			{\n
			  var lmd = document.lastModified;\n
			  var s   = "Unknown";\n
			  var d1;\n
\n
			  if(0 != (d1=Date.parse(lmd)))\n
			  {\n
			    s = "" + date_ddmmmyy(new Date(d1));\n
			  }\n
\n
			  return s;\n
			}\n
\n
			document.write( \n
			  "<br>This page was updated on " + \n
			  date_lastmodified() + "<br><br>");\n
\n
			</script>\n
			\n
			<script src="//code.jquery.com/jquery-3.4.1.min.js"></script>\n
			<script>\n
			// ===== Scroll to Top ==== \n
			$(window).scroll(function() {\n
			    if ($(this).scrollTop() >= 50) {        // If page is scrolled more than 50px\n
				$('#return-to-top').fadeIn(200);    // Fade in the arrow\n
			    } else {\n
				$('#return-to-top').fadeOut(200);   // Else fade out the arrow\n
			    }\n
			});\n
			$('#return-to-top').click(function() {      // When arrow is clicked\n
			    $('body,html').animate({\n
				scrollTop : 0                       // Scroll to top of body\n
			    }, 500);\n
			});\n
\n
			</script> \n
		</section>\n
		\n
	    <footer>\n
			<ul>\n
  				<li id="head">footer1 </li>\n
  				<li id="head">footer2</li>\n
  				<li id="head">footer3</li>\n
  				<li id="head">footer4</li>\n
			</ul>\n
	    </footer>\n
	\n
	</body>\n
	\n
	\n
\n
</html>\n""", file=text_file)
	text_file.close()

