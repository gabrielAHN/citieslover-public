def create_new_website(table, icons):
	top = """
	<!DOCTYPE html>
	<center>
	<img width="30%" src="https://ci4.googleusercontent.com/proxy/Dk8FOl4cdxiKMIoY55xoZL9gyRGvccQTifuPlt1Xj_0Tvs25REnBGsmMtJr4oPcYzhC3tEszp1gnlDB0gscjT9GLLIgztt2pyKCDUEPXR7PNew=s0-d-e1-ft#https://www.gabrielhn.com/static/images/Newsletter/cover.png" alt="">
	<h1 style="width:15cm;font-family: 'Dosis', sans-serif;"><b>Welcome</b></h1>
	<p style="width:15cm;font-family: 'Dosis', sans-serif;"><b>City Lover</b> is a newsletter that filters through all of the recent city topics and news from my favorite website sources. I created this for myself to help spend more time reading content instead of searching for it.</p>
	<p style="width:15cm;font-family: 'Dosis', sans-serif;"><b> Now I am offering this tool to any fellow City Lovers out there!</b></p>
	<div class="row" style="font-size:15px;font-family: 'Dosis', sans-serif;;border: 7px solid #FCE25F;padding:4px;border-radius: 15px;width:7cm;">
	<center>
	<a href="https://www.gabrielhn.com/topics/city/" style="font-size:15px;font-family: 'Dosis'"> Check out the real website here</a>
	</div>
	<br style="clear: both">
	<div class="container" style="margin-top:1cm;margin-bottom:2cm;font-family: 'Dosis', sans-serif;">
	<center><h2><b>This Week's Newsletter</b></h2></center>
		"""

	bottom = """</div>"""
	html = top + icons + table + bottom
	return html
