import random
from yattag import Doc
from backend.new_website import create_new_website


html_dict = {
    'podcast': ['#F7931E', '1.2cm', 'https://www.gabrielhn.com/static/images/Newsletter/headphones.png'],
    'article': ['#E4ECF0', '1cm', 'https://www.gabrielhn.com/static/images/Newsletter/articles.png'],
    'blog': ['#DB5367', '0.75cm', 'https://www.gabrielhn.com/static/images/Newsletter/blog.png'],
    'news': ['#0f75bc', '0.75cm', 'https://www.gabrielhn.com/static/images/Newsletter/news.png'],
}


def email_html(user, websites):
    intro, end = email_content(user)
    table = scraping_content(websites)
    icons = icons_info()
    html = intro + icons+ table + end
    return html


def website_html(websites):
    table = scraping_content(websites)
    icons = icons_info()
    html = create_new_website(table, icons)
    return html


def email_content(user):
    doc, tag, text = Doc().tagtext()
    doc.asis('<!DOCTYPE html>')
    with tag('html', lang="en"):
        with tag('head'):
            doc.asis('<meta charset="utf-8">')
        with tag('center'):
            with tag('div'):
                with tag('img', src='https://www.gabrielhn.com/static/images/Newsletter/cover.png',
                         style="width:35%"):
                    doc.stag('br')
                    with tag('h1', style="font-family: 'Dosis', sans-serif;font-size:40px"):
                        text('Hello ' + user)
                with tag('p', style="font-family: 'Dosis', sans-serif;"):
                    text(
                        'Here are this weeks articles and podcasts from the most interesting sources for cities out '
                        'there all filtered out just for you.')
        intro = doc.getvalue()
        doc, tag, text = Doc().tagtext()
        with tag('center'):
            with tag('a', style="font-family: 'Dosis', sans-serif;font-size:25px", href='https://www.gabrielhn.com/topics/city/',
                     target="_blank"):
                text('Click here if you have not signed up')
        doc.stag('br')
        with doc.tag('h3', style="font-family: 'Dosis', sans-serif;font-size:10px"):
            text('I do not own any of this material just sharing it along to those interested')
        end = doc.getvalue()
    return intro, end


def icons_info():
    doc, tag, text = Doc().tagtext()
    with tag('center'):
        with tag('h3', style="font-family:font-family: 'Dosis', sans-serif;"):
            text('Click on the icons to check them out')
        with tag('div', style='display: flex;width: 50%;'):
            for i in html_dict:
                with tag('div', style="border: 0px solid {};padding:5px;border-radius: "
                                      "30px;width:1cm;margin-left: auto;margin-right: auto;".format(html_dict[i][0])):
                    doc.stag('img',
                             src=html_dict[i][2],
                             style="width:{};".format(html_dict[i][1]))
                    with tag('h1', style="font-family: 'Dosis', sans-serif;font-size:15px"):
                        text(i)
    icons = doc.getvalue()
    return icons


def scraping_content(websites):
    random.shuffle(websites)
    doc, tag, text = Doc().tagtext()
    with tag('center'):
        count = 0
        while count <= len(websites):
            index_list = list(range(count, count+4))
            count += 4
            index_list = [x for x in index_list if x < len(websites)]
            with tag('div', style='display: flex;width: 70%;'):
                for i in index_list:
                    with tag('div',
                             style='border: 5px solid {};padding:10px;border-radius:15px;width:4cm;margin-left: '
                                   'auto;margin-right: auto;margin-bottom:10px'.format(html_dict[websites[i]['type']][0])):
                        doc.stag('img',
                                 src=websites[i]['image'],
                                 style="width:100px;")
                        doc.stag('br')
                        with doc.tag('h4', style="font-family: 'Dosis', sans-serif;font-size:10px"):
                            text(websites[i]['title'])
                            doc.stag('br')
                        with tag('p', style="font-family: 'Dosis', sans-serif;font-size:10px"):
                            text(websites[i]['description'])
                        with tag('a', style="font-family: 'Dosis', sans-serif;", href=websites[i]['link'], target="_blank"):
                            doc.stag('img', src=html_dict[websites[i]['type']][2],
                                     style="width:{};".format(html_dict[websites[i]['type']][1]))

    table = doc.getvalue()
    return table
