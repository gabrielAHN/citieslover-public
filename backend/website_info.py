from backend.website_scrape import (
        rss_parser, govtech, streetsblog, transitcenter,
        the_city, int_transport, spur, parking_mobility,
        axios, umc
    )



website_dict = [
    {
        'source': 'Monocle',
        'type': 'podcast',
        'scraped_function': rss_parser,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmKMTL7s8pHWi3lGcPnbXw5_bP4VXZIP2PgdXV5wr-u7tlTtgf',
        'image_size': '70px',
        'website': 'https://www.omnycontent.com/d/playlist/e6127ab7-b81e-456b-893c-a8d600215365/7903d81a-7481-40dd-85ff'
                '-a8db009e611f/ff59014c-a954-4271-8920-a8db009e612d/podcast.rss '
     },
    {
        'source': 'TheCityFix',
        'type': 'article',
        'scraped_function': rss_parser,
        'image_size':   '35px',
        'image': 'https://thecityfixlearn.org/sites/default/files/18_Logo_TheCityFix_Learn.png',
        'website': 'https://feeds.feedburner.com/thecityfix/posts'
     },
    {
        'source': 'Planetizen',
        'type': 'news',
        'scraped_function': rss_parser,
        'image_size':   '60px',
        'image': 'https://simplycareer.com/wp-content/uploads/2015/05/planetizen-425x215.png',
        'website': 'https://www.planetizen.com/frontpage/feed'
     },
    {
        'source': 'Govtech',
        'type': 'news',
        'scraped_function': govtech,
        'image': 'https://assets.website-files.com/59dfccba14d0c50001317351/5a625dd96f429200014442c3_gt.jpg',
        'image_size':   '70px',
        'website': 'https://www.govtech.com/transportation/'
     },
    {
        'source': 'Streetsblog',
        'type': 'blog',
        'scraped_function': streetsblog,
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQm06X4'
              '-kgmtexgJpGSv8RLLBu86D7KkMISeaSVNP1vNtn7nggAIg&s',
        'image_size':   '70px',
        'website': 'https://nyc.streetsblog.org/category/issues-campaigns/transit/'
     },
    {   
        'source': 'Smartcities',
        'type': 'news',
        'scraped_function': rss_parser,
        'image': 'https://leadingcities2014.files.wordpress.com/2019/09/smartcities_logo_black.png',
        'image_size':   '18px',
        'website': 'https://www.smartcitiesdive.com/feeds/news/'
     },
    {
        'source': 'Datasmart',
        'type': 'article',
        'scraped_function': rss_parser,
        'image': 'https://pbs.twimg.com/profile_images/877596367555874817/EsB6Sxl4.jpg',
        'image_size':   '70px',
        'website': 'https://datasmart.ash.harvard.edu/feeds'
     },
    {
        'source': 'Strongtowns',
        'type': 'podcast',
        'scraped_function': rss_parser,
        'image': 'https://pbcdn1.podbean.com/imglogo/image-logo/2312128/Blue_Stripe_Square_edit.png',
        'image_size':   '70px',
        'website': 'https://feed.podbean.com/podcast.strongtowns.org/feed.xml'
     },
    {
        'source': 'Transitcenter',
        'type': 'blog',
        'scraped_function': transitcenter,
        'image': 'https://d3n8a8pro7vhmx.cloudfront.net/circulatesd/pages/1101/attachments/original/1553274530/transit-center-logo.png?1553274530',
        'image_size':   '30px',
        'website': 'https://transitcenter.org/blog/'
     },
    {
        'source': 'Itetalk',
        'type': 'podcast',
        'scraped_function': rss_parser,
        'image': 'https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/d933ad68df9d533175abe3a002d22ede.jpg',
        'image_size':   '70px',
        'website': 'https://www.spreaker.com/show/1744465/episodes/feed'
     },
    {
        'source': 'Metro Mag',
        'type': 'news',
        'scraped_function': rss_parser,
        'image': 'https://fleetimages.bobitstudios.com/upload/metro-magazine/met-og-__-1200x630-s.png',
        'image_size':   '55px',
        'website': 'https://www.metro-magazine.com/rss'
     },
    {
        'source': 'Talking Headways',
        'type': 'podcast',
        'scraped_function': rss_parser,
        'image': 'https://ssl-static.libsyn.com/p/assets/3/3/e/8/33e8d0ffe911533c/talking_headways_v7.png',
        'image_size':   '60px',
        'website': 'https://streetsblog.libsyn.com/rss'
     },
    {
        'source': 'Second Ave Sagas',
        'type': 'blog',
        'scraped_function': rss_parser,
        'image': 'http://bkabak.wpengine.com/wp-content/uploads/2019/10/saslogo960x200.jpg',
        'image_size':   '20px',
        'website': 'http://feeds.feedburner.com/SecondAveSagas'
     },
    {
        'source': 'City Journal',
        'type': 'news',
        'scraped_function': rss_parser,
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/48/City_Journal_logo.png',
        'image_size':   '70px',
        'website': 'http://feeds.feedburner.com/city-journal'
     },
    {
        'source': 'The City',
        'type': 'news',
        'scraped_function': the_city,
        'image': 'https://cdn.vox-cdn.com/uploads/chorus_asset/file/19799246/city-logo-png8-smaller.0.png',
        'image_size':   '40px',
        'website': 'https://www.thecity.nyc/rss/index.xml'
     },
    {
        'source': 'GovLove',
        'type': 'podcast',
        'scraped_function': rss_parser,
        'image': 'https://storage.googleapis.com/proudcity/elglor/uploads/2018/02/cropped-elgl-icon-blue.png',
        'image_size':   '40px',
        'website': 'https://govlove.libsyn.com/rss'
     },
    {
        'source': 'Arup',
        'type': 'article',
        'scraped_function': rss_parser,
        'image': 'https://www.pexip.com/hubfs/ARUP%20logo-1.jpg',
        'image_size':   '60px',
        'website': 'https://www.arup.com/news-and-events/rss/news'
     },
    {
        'source': 'Next City',
        'type': 'news',
        'scraped_function': rss_parser,
        'image': 'https://inn.org/wp-content/uploads/2017/11/Next-City.png',
        'image_size':   '60px',
        'website': 'https://nextcity.org/feeds/daily'
     },
    {
        'source': 'Intelligent Transport',
        'type': 'news',
        'scraped_function': int_transport,
        'image': 'https://www.intelligenttransport.com/wp-content/themes/it19/images/IT-Logo@2x.png',
        'image_size':   '40px',
        'website': 'https://www.intelligenttransport.com/transport-news/'
     },
    {
        'source': 'Bike League',
        'type': 'blog',
        'scraped_function': rss_parser,
        'image': 'https://www.bikeleague.org/sites/all/themes/lab/images/league-logo.png',
        'image_size':   '60px',
        'website': 'https://www.bikeleague.org/blog/feed'
     },
    {
        'source': 'Spur',
        'type': 'article',
        'scraped_function': spur,
        'image': 'https://pbs.twimg.com/profile_images/1283457372699017216/v0M0jO2G_400x400.jpg',
        'image_size':   '60px',
        'website': 'https://www.spur.org/news'
     },
    {
        'source': 'Parking Mobility',
        'type': 'article',
        'scraped_function': parking_mobility,
        'image': 'https://www.parking-mobility.org/wp-content/themes/ipi/images/IPMI_LOGO-R_RGB_220x96.png',
        'image_size':   '30px',
        'website': 'https://www.parking-mobility.org/news-publications/ipmi-blog/'
     },
    {
        'source': 'Axios',
        'type': 'news',
        'scraped_function': axios,
        'image': 'https://assets.axios.com/203e9f932cc97836ac2ff4c6c982676c.png',
        'image_size':   '50px',
        'website': 'https://www.axios.com/economy-business/transportation/?page=1'
     },
    {
        'source': 'Urban Mobility Company',
        'type': 'blog',
        'scraped_function': umc,
        'image': 'https://urbanmobilitydaily.com/wp-content/uploads/2020/12/top-ten-urban-mobility-daily-articles-of-2020-image.png',
        'image_size':   '40px',
        'website': 'https://urbanmobilitycompany.com/content/daily'
     },
    {
        'source': 'Human Transit',
        'type': 'blog',
        'scraped_function': rss_parser,
        'image': 'https://humantransit.org/wp-content/uploads/HT-favicon@16x.png',
        'image_size':   '40px',
        'website': 'https://feeds.feedburner.com/humantransit/TCwW'
     },
]
