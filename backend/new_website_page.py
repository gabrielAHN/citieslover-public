
color_dict = {
    'podcast': '#F7931E',
    'article': '#E4ECF0',
    'blog': '#DB5367',
    'news': '#0f75bc'
}


def create_updated_website(articles):
    html = ""
    html += get_top_html()
    html += get_article_html(articles)
    html += get_bottom_html(articles)
    return html


def get_icon_dict(articles):
    icon_dict = {
        'podcast_icon': [],
        'news_icon': [],
        'article_icon': [],
        'blog_icon': []
    }
    for icon in icon_dict:
        [
            icon_dict[icon].append(article.source)
            for article in articles
            if article.article_type in icon
        ]
    return str(icon_dict)


def get_top_html():
    html = """<!DOCTYPE html>
    {% extends "topics/base.html" %}
    {% block nav_item_work %}active{% endblock nav_item_work %}
        {% block body_block %}
        {% load static %}
        <center>
        <img width="30%" src="https://ci4.googleusercontent.com/proxy/Dk8FOl4cdxiKMIoY55xoZL9gyRGvccQTifuPlt1Xj_0Tvs25REnBGsmMtJr4oPcYzhC3tEszp1gnlDB0gscjT9GLLIgztt2pyKCDUEPXR7PNew=s0-d-e1-ft#https://www.gabrielhn.com/static/images/Newsletter/cover.png" alt="">
        <h1 style="width:15cm;font-family: 'Dosis', sans-serif;"><b>Welcome</b></h1>
        <p style="width:15cm;font-family: 'Dosis', sans-serif;"><b>CityLover</b> is where I can get the most recent city topics and news from my favorite website sources. I created this for myself to help spend more time reading content instead of searching for it.</p>
        <p style="width:15cm;font-family: 'Dosis', sans-serif;"><b> Now I am offering this tool to any fellow Citylovers out there!</b></p>
        <h3>
        </h3>
        <div id='sign_up_div' style="font-size:15px;font-family: 'Dosis', sans-serif;border: 7px solid #FCE25F;padding:4px;border-radius: 15px;width:9cm;display: block;" onclick="drop_down('sign_up')" onmouseover="signup_opacity('sign_up_div', 'sign_up', '0.5')" onmouseleave="signup_opacity('sign_up_div', 'sign_up', '1')">
                <h1 style="font-size:20px;font-family: 'Dosis', sans-serif;">Newsletter Sign-Up 📫</h1>
                {% for message in messages %}
                    {% if "signup" in message.tags %}
                    {% endif %}
                    {{ message }}
                    {% endfor %}
            <div id="sign_up" style="display: none;">
                <p>For those that want to consistenly be in the know you can sign up for the newsletter instead of having to visit this webpage all the time. It will give that day's most recent article for each source.</p>
                <form method="POST">
                    {% csrf_token %}
                    <p>First name: <input type="text" name="first_name" required id="id_first_name"></p>
                    <p>Email: <input type="email" name="email" required id="id_email"></p>
                    <p>Send Newsletters every:</p>
                        <label>Monday</label>
                        <input type="checkbox" name="newsletter_day" value="mon" id="id_newsletter_day_0">
                        <label>Tuesday</label>
                        <input type="checkbox" name="newsletter_day" value=tue id="id_newsletter_day_1">
                        <label>Wednesday</label>
                        <input type="checkbox" name="newsletter_day" value="wed" id="id_newsletter_day_2">
                        <label>Thursday</label>
                        <input type="checkbox" name="newsletter_day" value="thu" id="id_newsletter_day_3">
                        <label>Friday</label>
                        <input type="checkbox" name="newsletter_day" value=fri id="id_newsletter_day_4">
                        <label>Saturday</label>
                        <input type="checkbox" name="newsletter_day" value="sat" id="id_newsletter_day_5"/>
                        <label>Sunday</label>
                        <input type="checkbox" name="newsletter_day" value="sun" id="id_newsletter_day_6"/>
                    <input type="hidden" name="botcatcher" id="id_botcatcher" />
                    <br>
                    <br>
                    <input type="submit" value="Sign-Up" class="btn btn-light" style='font-weight:bold'>
                    <input type="submit" name="Send Sample Email" value="Send Sample Email" class="btn btn-light" style='font-weight:bold'>
                </form>
            </div>
        </div>
                <a class='pink' style="font-size:15px;color:black;font-family: 'Dosis', sans-serif;" href='https://github.com/gh15hidalgo/citylover'> Citylover repo</a>
        <div class="container" style="margin-top:1cm;margin-bottom:2cm;font-family: 'Dosis', sans-serif;">
            <center><h2><b>Explore Cities</b></h2></center>
        <div style="display: flex;justify-content: center;flex-shrink: 2;">
            <div id="all" onclick="filter_articles('all')" onmouseover="icon_colour('all', '#FCE25F')" onmouseleave="icon_colour('all', 'white')"  style="border: 5px solid white;padding:10px;border-radius:15px;">
                <h1 style="font-family: 'Dosis', sans-serif;font-size:15px">All</h1>
                <img src="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/openmoji/272/cityscape_1f3d9-fe0f.png" style="width:0.95cm;" />
            </div>
            <div id="podcast_icon" onclick="filter_articles('podcast_icon')" onmouseover="icon_colour('podcast_icon', '#F7931E')" onmouseleave="icon_colour('podcast_icon', 'white')" style="border: 5px solid white;padding:10px;border-radius:15px;">
                <h1 style="font-family: 'Dosis', sans-serif;font-size:15px">Podcast</h1>
                <img src="{% static "images/Newsletter/headphones.png" %}" style="width:0.95cm;" />
            </div>
            <div id="article_icon" onclick="filter_articles('article_icon')" onmouseover="icon_colour('article_icon' ,'#E4ECF0')" onmouseleave="icon_colour('article_icon', 'white')" style="border: 5px solid white;padding:10px;border-radius:15px;">
                <h1 style="font-family: 'Dosis', sans-serif;font-size:15px">Articles</h1>
                <img src="{% static "images/Newsletter/articles.png" %}" style="width:0.95cm;" />
            </div>
            <div id="blog_icon" onclick="filter_articles('blog_icon')" onmouseover="icon_colour('blog_icon' ,'#DB5367')" onmouseleave="icon_colour('blog_icon', 'white')" style="border: 5px solid white;padding:10px;border-radius:15px;">
                <h1 style="font-family: 'Dosis', sans-serif;font-size:15px">Blog</h1>
                <img src="{% static "images/Newsletter/blog.png" %}" style="width:0.90cm;" />
            </div>
            <div  id="news_icon" onclick="filter_articles('news_icon')" onmouseover="icon_colour('news_icon' ,'#0f75bc')" onmouseleave="icon_colour('news_icon', 'white')" style="border: 5px solid white;padding:10px;border-radius:15px;">
                <h1 style="font-family: 'Dosis', sans-serif;font-size:15px">News</h1>
                <img src="{% static "images/Newsletter/news.png" %}" style="width:0.80cm;" />
            </div>
        </div>"""
    return html


def get_article_html(articles):
    html = '<div style="display: flex;flex-wrap: wrap;width: 65%;">'
    for i in range(0, len(articles)):
        html += """
                <div id="{0}" onclick="get_articles('{0}','{0}_articles')" onmouseover="change_opacity('{0}', '{0}_articles', '0.5')"
                    onmouseleave="change_opacity('{0}', '{0}_articles', '1')" style="border: 5px solid {1};padding:10px;
                    border-radius:15px;width:4cm;margin-left: auto;margin-right: auto;margin-top:10px;
                    height: 120px";display: block;>
                    <img src="{2}" style="height: {3};vertical-align: middle;display:block;margin:auto;">
                    <p style="font-family: 'Dosis', sans-serif;">{0}<p>
                    <div id="{0}_articles" style="display: none;">
                        {4}
                    </div>
                </div>""".format(articles[i].source, color_dict[articles[i].article_type], articles[i].image, articles[i].image_size, get_article_list(articles[i].articles))
    return html


def get_article_list(articles):
    html = ""
    for article in articles:
        html += """     <a style="font-family: 'Dosis', sans-serif;" href="{}" target="_blank">
                            <h4 style="font-family: 'Dosis', sans-serif;font-size:10px">{}</h4>
                        </a>
                """.format(article.url, article.title)
    return html


def get_bottom_html(articles):
    html = """</div>
    <script type='text/javascript'>
        function drop_down(source){
            var element = document.getElementById(source)
            element.style.display = "block";
        }
        function signup_opacity(source, source_2, opacity){
            var element = document.getElementById(source)
            var element_2 = document.getElementById(source_2)
            if (element_2.style.display === "none") {
                element.style.opacity = opacity;
            } else {
                element.style.opacity = "1.0";
            }
        }
        function icon_colour(icon, color){
            document.getElementById(icon).style.borderColor = color ;
        }
        function change_opacity(source, source_articles, opacity){
            var element = document.getElementById(source)
            var element_2 = document.getElementById(source_articles)
            if (element_2.style.display === "none") {
                element.style.opacity = opacity;
            } else {
                element.style.opacity = "1.0";
            }
        }
        function get_articles(source, source_articles){
            var element = document.getElementById(source_articles)
            var element_2 = document.getElementById(source)
            if (element.style.display === "block") {
                element.style.display = "none";
                element_2.style.height = "120px"
            } else {
                element.style.display = "block";
                element_2.style.height = "100%"
            }
        }
        var filter_dict =
                """
    html += get_icon_dict(articles)
    html += """
        function filter_articles(div_id, colour){
            for (var key in filter_dict) {
                for (var i = 0; i < filter_dict[key].length; i++) {
                    if (div_id == "all") {
                        console.log(filter_dict[key][i])
                        document.getElementById(filter_dict[key][i]).style.display = "block";
                    } else if (key != div_id) {
                        document.getElementById(filter_dict[key][i]).style.display = "none";
                    } if (key == div_id) {
                        document.getElementById(filter_dict[div_id][i]).style.display = "block";
                    }
                }
            }
        }
    </script>
    {% endblock %}"""
    return html
