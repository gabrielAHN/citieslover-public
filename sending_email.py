import smtplib
from yattag import Doc
import config
import Scraped_Data
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

users = pd.read_csv('emails.csv')
emails = users['email']
names = users['first_name']


for user,email in zip(names,emails):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "City Lover Weekly"
        msg['From'] = config.EMAIL_ADDRESS

        msg['To'] = email

        doc, tag, text = Doc().tagtext()
        doc.asis('<!DOCTYPE html>')
        with tag('html', lang="en"):
            with tag('head'):
                doc.asis('<meta charset="utf-8">')
            with tag('center'):
                with tag('center'):
                    with tag('div'):
                        with tag('img', src='https://www.gabrielhn.com/static/images/Newsletter/cover.png',
                                 style="width:35%"):
                            doc.stag('br')
                            with tag('h1', style="font-family:Gadugi;font-size:40px"):
                                text('Hello ' + user)
                        with tag('p', style="font-family:Gadugi;"):
                            text(
                                'Here are this weeks articles and podcasts from the most interesting sources for cities out there all filtered out just for you.')
                        with tag('h3', style="font-family:Gadugi;"):
                            text('Click on the icons to check them out')
            doc.stag('br', style="clear:both")
            with tag('center'):
                with tag('div',
                         style='margin-left: 12cm; display: flex;flex-wrap: wrap;flex-direction: row;flex-flow: row wrap;;align-items: center;align-content: flex-end;'):
                    with tag('div', style="margin-left:10cm;1px;margin:1px"):
                        doc.stag('img',
                                 src='https://www.gabrielhn.com/static/images/Newsletter/headphones.png',
                                 style="width:1cm;")
                        with tag('h1', style="font-family:Gadugi;font-size:15px"):
                            text('Podcast')
                    with tag('div', style="margin:1px"):
                        doc.stag('img',
                                 src='https://www.gabrielhn.com/static/images/Newsletter/articles.png',
                                 style="width:1cm")
                        with tag('h1', style="font-family:Gadugi;font-size:15px"):
                            text('Article')
                    with tag('div', style="margin:1px"):
                        doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/blog.png',
                                 style="width:0.75cm")
                        with tag('h1', style="font-family:Gadugi;font-size:15px"):
                            text('Blog')
                    with tag('div', style="margin:1px"):
                        doc.stag('img', src='https://www.gabrielhn.com/static/images/Newsletter/news.png',
                                 style="width:0.65cm")
                        with tag('h1', style="font-family:Gadugi;font-size:15px"):
                            text('News')

            doc.stag('br', style="clear:both")
        html_1 = doc.getvalue()

        doc, tag, text = Doc().tagtext()
        with tag('center'):
            with tag('a', style="font-family:Gadugi;font-size:25px", href='https://www.gabrielhn.com/topics/city/',
                     target="_blank"):
                text('Click here if you have not signed up')
            doc.stag('br')
            with doc.tag('h3', style="font-family:Gadugi;font-size:10px"):
                text('I do not own any of this material just sharing it along to those interested')
        html_2 = doc.getvalue()

        html_3 = html_1 + Scraped_Data.doc.getvalue() + html_2
        part2 = MIMEText(html_3, 'html')
        msg.attach(part2)
#print(msg.as_string())
        server.sendmail(config.EMAIL_ADDRESS,email,msg.as_string())
        print(user,email,'success')
    except:
        print(user,email,'Failed')
