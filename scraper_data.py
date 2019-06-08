from selenium import webdriver
import time
from yattag import Doc
driver = webdriver.Chrome("C:\\Users\\Gabriel Hidalgo\\PycharmProjects\\email\\chromedriver.exe")

#div Location on Website
number= 1
mar=3.5

#Monocle
driver.get('https://monocle.com/radio/shows/the-urbanist/')
title = driver.find_element_by_xpath('//*[@id="content"]/div/section[1]/div/div/div[1]/section[2]/div/p[1]')
describe = driver.find_element_by_xpath('//*[@id="content"]/div/section[1]/div/div/div[1]/section[2]/div/p[2]')
monocle_d = describe.text
monocle_t = title.text
driver.find_element_by_xpath('//*[@id="content"]/div/section[1]/div/div/div[1]/div/div/div[1]/a').click()
monocle_url = driver.current_url

#govtech
driver.get('https://www.govtech.com/fs/')
time.sleep(15)
driver.find_element_by_xpath('/html/body/section/div[1]/div/div/div[2]/div['+str(number)+']').click()

time.sleep(5)
title = driver.find_element_by_xpath('//*[@id="article_header"]/h1')
gov_t = title.text
describe = driver.find_element_by_xpath('//*[@id="article_header"]/p')
gov_d = describe.text
gov_url = driver.current_url

#City Lab

driver.get('https://www.citylab.com/transportation/')
time.sleep(4)
driver.find_element_by_xpath('//*[@id="qcCmpButtons"]/button[1]').click()
driver.find_element_by_xpath('//*[@id="main-content"]/section[2]/div/h1/a').click()
driver.implicitly_wait(4)
describe = driver.find_element_by_xpath('//*[@id="main-content"]/article/div[2]/h1')
title = driver.find_element_by_xpath('//*[@id="article-section-1"]/p[1]')
city_d = describe.text
city_t = title.text
city_url = driver.current_url

#Planetizen
driver.get('https://www.planetizen.com/news')
describe = driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[5]/div')
title = driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[3]')
planet_d = describe.text
planet_t = title.text
driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/a/picture/img').click()
planet_url = driver.current_url

#qz
driver.get('https://qz.com/on/the-future-of-cities/')
driver.execute_script("window.scrollTo(0.5, document.body.scrollHeight);")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="site-content"]/div/div/div[2]/div[1]/div/article['+str(number)+']/div/a').click()
time.sleep(3)
#//*[@id="site-content"]/article/header/div/h1
title = driver.find_element_by_xpath('//*[@id="site-content"]/article/header/div/h1')
qz_t = title.text
driver.execute_script("window.scrollTo(0, 1000)")
time.sleep(2)
describe = driver.find_element_by_xpath('//*[@id="article-content"]/p[1]')
qz_d = describe.text
qz_url = driver.current_url


#Side Walk Labs
driver.get('https://www.sidewalklabs.com/blog/?')
driver.find_element_by_xpath('/html/body/main/section/div/div/div/div/div[2]/div/a['+str(number+12)+']/article').click()
describe = driver.find_element_by_xpath('/html/body/main/section/article/div[2]/div[2]/div/div[2]/div/h4/p')
title = driver.find_element_by_xpath('/html/body/main/section/article/div[1]/div/div/div[1]/h1')
side_d = describe.text
side_t = title.text
side_url = driver.current_url

#Carto
driver.get('https://carto.com/blog')
time.sleep(2)
title = driver.find_element_by_xpath('/html/body/div[1]/div/ul/li['+str(number)+']/div/div[2]/h2')
carto_t = title.text
driver.find_element_by_xpath('/html/body/div[1]/div/ul/li['+str(number)+']/div/div[2]/h2/a').click()
time.sleep(2)
describe = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/p[1]')
carto_d = describe.text
carto_url = driver.current_url


#City solutions
a=number
driver.get('https://datasmart.ash.harvard.edu/')
title = driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div/div/div/div/div/div/div['+str(a)+']/div/div[2]/h2/a')
cs_t = title.text
describe = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/div/div/div/div/div/div['+str(a)+']/div/div[2]/p')
cs_d = describe.text
driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div/div/div/div/div/div['+str(a)+']/div/div[2]/h2/a').click()
cs_url = driver.current_url


#Verge
driver.get('https://www.theverge.com/transportation')
time.sleep(6)
title = driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[1]/div/div['+str(number+1)+']/div/div/h2/a')
v_t = title.text
driver.execute_script("window.scrollTo(0, 1000)")
driver.find_element_by_xpath('/html/body/div[2]/div[5]/div/div/div[1]/div/div['+str(number+1)+']/div/div/h2/a').click()
time.sleep(4)
describe = driver.find_element_by_xpath('/html/body/div[2]/section/section/div[1]/div[1]/p')
v_d = describe.text
v_url = driver.current_url

#Places

driver.get('https://placesjournal.org/explore-places/urbanism')
driver.implicitly_wait(4)
driver.find_element_by_xpath('/html/body/div[4]/div/a[2]').click()
driver.find_element_by_xpath('//*[@id="ajax-load-more"]/ul[1]/div/li['+str(number)+']/a').click()
title = driver.find_element_by_xpath('/html/body/div[3]/section/div/section/article/header/h1')
describe = driver.find_element_by_xpath('/html/body/div[3]/section/div/section/article/header/p')
places_d = describe.text
places_t = title.text
places_url = driver.current_url

#SmartCities
#driver.get('https://www.smartcitiesdive.com/')
# driver.implicitly_wait(7)
# title = driver.find_element_by_xpath('//*[@id="main-content"]/section/ul/li[3]/div[2]/h3')
# smart_t = title.text
# describe = driver.find_element_by_xpath('//*[@id="main-content"]/section/ul/li[3]/div[2]/p')
# smart_d = describe.text
# driver.find_element_by_xpath('//*[@id="main-content"]/section/ul/li[3]/div[2]/a').click()
# smart_url = driver.current_url

#NYMAG
driver.get('http://nymag.com/tags/cityscape/')
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[7]/div[2]/section[1]/div[3]/button[1]/p').click()
driver.find_element_by_xpath('/html/body/main/div/div[1]/section/ol/li['+str(number)+']/div/div[3]/a').click()
title = driver.find_element_by_xpath('/html/body/section[6]/section[1]/article/header/div/div/div[2]/h1')
mag_t = title.text
describe = driver.find_element_by_xpath('/html/body/section[6]/section[1]/article/header/div[1]/div[1]/div[2]/h2')
mag_d = describe.text
mag_url = driver.current_url

driver.close()

doc, tag, text = Doc().tagtext()
with tag('center'):
    with tag('div',style='margin-left:' + str(mar) + 'cm;display: flex;flex-wrap: wrap;flex-direction: row;flex-flow: row wrap;;align-items: center;align-content: flex-end;'):
        #Smart Cities
        # with tag('div',
        #          style='border: 5px solid #0f75bc;padding:10px;border-radius: 15px;width:4cm;margin:5px;'):
        #     doc.stag('img', src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDvAsd3k9bUVKJ6CXlJufDF_tVi6kyYq5_BDOZy2i9ehsfWBOs6Q",
        #              style="width:150px;")
        #     doc.stag('br')
        #     with doc.tag('h4', style="font-family:Gadugi;font-size:10px"):
        #         text(smart_t)
        #         doc.stag('br')
        #     with tag('p', style="font-family:sans-serif;font-size:10px"):
        #         text(smart_d)
        #     with tag('a', style="font-family:sans-serif;", href=smart_url, target="_blank"):
        #         doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/news.png', style="width:1cm")

        # City Lab
        with tag('div', style='border: 5px solid #0f75bc;padding:10px;border-radius: 15px;width:4cm;margin:5px;'):
            doc.stag('img', src="https://cdn.citylab.com/static/b/citylab/img/logos/logo_social_1200x630.png",
                     style="width:150px;")
            doc.stag('br')
            with doc.tag('h4', style="font-family:Gadugi;font-size:10px"):
                text(city_d)
                doc.stag('br')
            with tag('p', style="font-family:sans-serif;font-size:10px"):
                text(city_t)
            with tag('a', style="font-family:sans-serif;", href=city_url, target="_blank"):
                doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/news.png', style="width:1cm")

        #Places
        with tag('div',style='border: 5px solid #E4ECF0;padding:10px;border-radius: 15px;width:4cm;margin:5px;'):
            doc.stag('img', src="https://placesjournal.org/wp-content/themes/places/img/fallback-logo.png",style="width:150px;")
            doc.stag('br')
            with doc.tag('h4', style="font-family:Gadugi;font-size:10px"):
                text(places_t)
                doc.stag('br')
            with tag('p', style="font-family:sans-serif;font-size:10px"):
                text(places_d)
            with tag('a', style="font-family:sans-serif;", href=places_url, target="_blank"):
                doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/articles.png',
                         style="width:1cm")

        #Planetizen
        with tag('div', style='border: 5px solid #E4ECF0;padding:10px;border-radius: 15px;width:4cm;margin:5px;'):
            doc.stag('img', src= "https://www.planetizen.com/sites/all/themes/custom/plnz3/logo.png" , style="width:150px;")
            doc.stag('br')
            with doc.tag('h4',style="font-family:Gadugi;font-size:10px"):
                text(planet_t)
                doc.stag('br')
            with tag('p',style="font-family:sans-serif;font-size:10px"):
                text(planet_d)
            with tag('a',style="font-family:sans-serif;", href=planet_url, target="_blank"):
                doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/articles.png', style="width:1cm")

        # NYMAG
        with tag('div',
                 style='border: 5px solid #E4ECF0;padding:10px;border-radius: 15px;width:4cm;margin:5px'):
            doc.stag('img',
                     src="https://assets.nymag.com/media/sites/nymag/icon.1500x1500.png",
                     style="width:100px;")
            doc.stag('br')
            with doc.tag('h4', style="font-family:Gadugi;font-size:10px"):
                text(mag_t)
                doc.stag('br')
            with tag('p', style="font-family:Gadugi;font-size:10px"):
                text(mag_d)
            with tag('a', style="font-family:Gadugi;", href=mag_url, target="_blank"):
                doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/articles.png',
                         style="width:1cm")
doc.stag('br', style="clear:both")
with tag('center'):
    with tag('div', style='margin-left:' + str(mar) + 'cm;display: flex;flex-wrap: wrap;flex-direction: row;flex-flow: row wrap;;align-items: center;align-content: flex-end;'):

        #Side Walk Labs
        with tag('div', style='border: 5px solid #DB5367;padding:10px;border-radius: 15px;width:4cm;margin:5px;'):
            doc.stag('img', src= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhMjNWMQR17AuHThWZI8m5iaZrIFLeeKtR8oB0VfREPVTXky330Q" , style="width:150px;")
            doc.stag('br')
            with doc.tag('h4',style="font-family:Gadugi;font-size:10px"):
                text(side_t)
                doc.stag('br')
            with tag('p',style="font-family:sans-serif;font-size:10px"):
                text(side_d)
            with tag('a',style="font-family:sans-serif;", href=side_url, target="_blank"):
                doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/blog.png', style="width:1cm")

        #City Solutions
        with tag('div',style='border: 5px solid #E4ECF0;padding:10px;border-radius: 15px;width:4cm;margin:5px'):
            doc.stag('img',src="https://pbs.twimg.com/profile_images/877596367555874817/EsB6Sxl4_400x400.jpg", style="width:100px;")
            doc.stag('br')
            with doc.tag('h4', style="font-family:Gadugi;font-size:10px"):
                text(cs_t)
                doc.stag('br')
            with tag('p', style="font-family:Gadugi;font-size:10px"):
                text(cs_d)
            with tag('a', style="font-family:Gadugi;", href=cs_url, target="_blank"):
                doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/articles.png',style="width:1cm")

        #qz
        with tag('div',style='border: 5px solid #E4ECF0;padding:10px;border-radius: 15px;width:4cm;margin:5px;'):
            doc.stag('img', src="https://pmcvariety.files.wordpress.com/2018/07/quartz-logo.png?w=960",style="width:150px;")
            doc.stag('br')
            with doc.tag('h4', style="font-family:Gadugi;font-size:10px"):
                text(qz_t)
                doc.stag('br')
            with tag('p', style="font-family:sans-serif;font-size:10px"):
                text(qz_d)
            with tag('a', style="font-family:sans-serif;", href=qz_url, target="_blank"):
                doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/articles.png',
                         style="width:1cm")

        #Carto
        with tag('div', style='border: 5px solid #DB5367;padding:10px;border-radius: 15px;width:4cm;margin:5px;'):
            doc.stag('img', src= "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/CARTO-logo.svg/1200px-CARTO-logo.svg.png" , style="width:150px;")
            doc.stag('br')
            with doc.tag('h4',style="font-family:Gadugi;font-size:10px"):
                text(carto_t)
                doc.stag('br')
            with tag('p',style="font-family:sans-serif;font-size:10px"):
                text(carto_d)
            with tag('a',style="font-family:sans-serif;", href=carto_url, target="_blank"):
                doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/blog.png', style="width:1cm")

with tag('center'):
    with tag('div', style='margin-left:' + str(mar) + 'cm;display:flex;'):
        #Verge
        with tag('div', style='border: 5px solid #0f75bc;padding:10px;border-radius: 15px;width:4cm;margin:5px;'):
            doc.stag('img', src= "https://cdn.vox-cdn.com/uploads/chorus_asset/file/9672633/VergeOG.0_1200x627.0.png" , style="width:150px;")
            doc.stag('br')
            with doc.tag('h4',style="font-family:Gadugi;font-size:10px"):
                text(v_t)
                doc.stag('br')
            with tag('p',style="font-family:sans-serif;font-size:10px"):
                text(v_d)
            with tag('a',style="font-family:sans-serif;", href=v_url, target="_blank"):
                doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/news.png', style="width:1cm")
        #Monocle
        with tag('div',
                 style='border: 5px solid #F7931E;padding:10px;border-radius: 15px;width:4cm;margin:5px'):
            doc.stag('img',
                     src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmKMTL7s8pHWi3lGcPnbXw5_bP4VXZIP2PgdXV5wr-u7tlTtgf",
                     style="width:100px;border-radius:50%;")
            doc.stag('br')
            with doc.tag('h4', style="font-family:Gadugi;font-size:10px"):
                text(monocle_t)
                doc.stag('br')
            with tag('p', style="font-family:Gadugi;font-size:10px"):
                text(monocle_d)
            with tag('a', style="font-family:Gadugi;", href=monocle_url, target="_blank"):
                doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/headphones.png',
                         style="width:1cm")
        #Gov Tech
        with tag('div',
                 style='border: 5px solid #0f75bc;padding:10px;border-radius: 15px;width:4cm;margin:5px'):
            doc.stag('img',
                     src="https://assets.website-files.com/59dfccba14d0c50001317351/5a625dd96f429200014442c3_gt.jpg",
                     style="width:100px;")
            doc.stag('br')
            with doc.tag('h4', style="font-family:Gadugi;font-size:10px"):
                text(gov_t)
                doc.stag('br')
            with tag('p', style="font-family:Gadugi;font-size:10px"):
                text(gov_d)
            with tag('a', style="font-family:Gadugi;", href=gov_url, target="_blank"):
                doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/news.png',
                         style="width:1cm")


html = doc.getvalue()
