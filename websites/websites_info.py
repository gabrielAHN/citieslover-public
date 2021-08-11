from scrapers.newsletter_scrapers import (
    rss_parser, apple_parser, allthingsurban,
    govtech, transitcenter, streetsblog, umc,
    parking_mobility, axios, spur
)
from scrapers.jobs_scrapers import (
    planetizen_jobs, allthingsurban_jobs,
    apany_jobs, nextcity_jobs, govlove_jobs
)


website_info = {
    'citymapper': {
        'name': 'Citymapper',
        'type': ['job'],
        'image_size':   '60px',
        'image': 'https://logovectorseek.com/wp-content/uploads/2020/11/citymapper-logo-vector.png',
        'feature_post': True        
     },
    'planetizen': {
        'name': 'Planetizen',
        'type': ['news'],
        'image_size':   '60px',
        'image': 'https://simplycareer.com/wp-content/uploads/2015/05/planetizen-425x215.png',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'https://www.planetizen.com/frontpage/feed',
        },
        'jobs': {
            'scrape_function': planetizen_jobs,
            'website': 'https://www.planetizen.com/jobs',
        }        
     },
    'thecityfix': {
        'name': 'TheCityFix',
        'type': ['article'],
        'image_size':   '35px',
        'image': 'https://thecityfixlearn.org/sites/default/files/18_Logo_TheCityFix_Learn.png',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'https://feeds.feedburner.com/thecityfix/posts'
        }
     },
    'allthingsurban': {
        'name': 'All Things Urban',
        'type': ['blog'],
        'image_size':   '35px',
        'image': 'https://all-things-urban.storage.googleapis.com/static/images/social.jpg',
        'newsletter': {
            'scrape_function': allthingsurban,
            'website': 'https://www.allthingsurban.net/blog'
        },
        'jobs': {
            'scrape_function': allthingsurban_jobs,
            'website': 'https://www.allthingsurban.net/career'
        }
     },
    'monocle': {
        'name': 'Monocle',
        'type': ['podcast'],
        'image_size': '70px',
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmKMTL7s8pHWi3lGcPnbXw5_bP4VXZIP2PgdXV5wr-u7tlTtgf',
        'newsletter': {
                'scrape_function': rss_parser,
                'website': 'https://www.omnycontent.com/d/playlist/e6127ab7-b81e-456b-893c-a8d600215365/7903d81a-7481-40dd-85ff'
                           '-a8db009e611f/ff59014c-a954-4271-8920-a8db009e612d/podcast.rss '
        } 
    },
    'smartcities': {
        'name': 'Smartcities',
        'type': ['news'],
        'image': 'https://leadingcities2014.files.wordpress.com/2019/09/smartcities_logo_black.png',
        'image_size':   '18px',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'https://www.smartcitiesdive.com/feeds/news/'
        }
    },
    'datasmart': {
        'name': 'Datasmart',
        'type': ['article'],
        'image': 'https://pbs.twimg.com/profile_images/877596367555874817/EsB6Sxl4.jpg',
        'image_size':   '70px',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'https://datasmart.ash.harvard.edu/feeds'
        }
    },
    'strongtowns': {
        'name': 'Strongtowns',
        'type': ['podcast'],
        'image': 'https://pbcdn1.podbean.com/imglogo/image-logo/2312128/Blue_Stripe_Square_edit.png',
        'image_size':   '70px',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'https://feed.podbean.com/podcast.strongtowns.org/feed.xml'
        }
    },
    "itetalk": {
        'name': 'Itetalk',
        'type': ['podcast'],
        'image': 'https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/d933ad68df9d533175abe3a002d22ede.jpg',
        'image_size':   '70px',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'https://www.spreaker.com/show/1744465/episodes/feed'
        }
    },
    "metromag": {
        'name': 'Metro Mag',
        'type': ['news'],
        'image': 'https://fleetimages.bobitstudios.com/upload/metro-magazine/met-og-__-1200x630-s.png',
        'image_size':   '55px',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'https://www.metro-magazine.com/rss'
        }
    },
    "talkingheadways": {
        'name': 'Talking Headways',
        'type': ['podcast'],
        'image': 'https://ssl-static.libsyn.com/p/assets/3/3/e/8/33e8d0ffe911533c/talking_headways_v7.png',
        'image_size':   '60px',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'https://streetsblog.libsyn.com/rss'
        }
    },
    "secondave": {
        'name': 'Second Ave Sagas',
        'type': ['blog'],
        'image': 'http://bkabak.wpengine.com/wp-content/uploads/2019/10/saslogo960x200.jpg',
        'image_size':   '20px',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'http://feeds.feedburner.com/SecondAveSagas'
        }
    },
    "cityjournal": {
        'name': 'City Journal',
        'type': ['news'],
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/48/City_Journal_logo.png',
        'image_size':   '70px',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'http://feeds.feedburner.com/city-journal'
        }
    },
    "bikeleague": {
        'name': 'Bike League',
        'type': ['blog'],
        'image': 'https://www.bikeleague.org/sites/all/themes/lab/images/league-logo.png',
        'image_size':   '60px',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'https://www.bikeleague.org/blog/feed'
        }
    },
    "govlove": {
        'name': 'GovLove',
        'type': ['podcast'],
        'image': 'https://storage.googleapis.com/proudcity/elglor/uploads/2018/02/cropped-elgl-icon-blue.png',
        'image_size':   '40px',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'https://govlove.libsyn.com/rss'
        },
        'jobs': {
            'scrape_function': govlove_jobs,
            'website': 'https://elgljobs.com/jobs/?categories[]=Data%20%26%20Analysis&categories[]=Innovation&categories[]=Planning'
        }
    },
    "nextcity": {
        'name': 'Next City',
        'type': ['news'],
        'image': 'https://nextcity.org/images/events/Next_City_Orange_Logo.png',
        'image_size':   '60px',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'https://nextcity.org/feeds/daily'
        },
        'jobs': {
            'scrape_function': nextcity_jobs,
            'website': 'https://jobs.nextcity.org/'
        }
    },
    "apany": {
        'name': 'NY APA',
        'type': ['jobs'],
        'image': 'https://planning-org-uploaded-media.s3.amazonaws.com/uploads/PROFILE_PHOTOS/7816568a-17ef-47c6-8291-2cda62b13910.png',
        'image_size':   '40px',
        'jobs': {
            'scrape_function': apany_jobs,
            'website': 'https://www.nyplanning.org/career-development/jobs/'
        }
    },
    "govtech": {
        'name': 'Govtech',
        'type': ['news'],
        'image': 'https://assets.website-files.com/59dfccba14d0c50001317351/5a625dd96f429200014442c3_gt.jpg',
        'image_size':   '70px',
        'newsletter': {
            'scrape_function': govtech,
            'website': 'https://www.govtech.com/transportation/'
        }
    },
    "transitcenter": {
        'name': 'Transitcenter',
        'type': ['blog'],
        'image': 'https://d3n8a8pro7vhmx.cloudfront.net/circulatesd/pages/1101/attachments/original/1553274530/transit-center-logo.png?1553274530',
        'image_size':   '30px',
        'newsletter': {
            'scrape_function': transitcenter,
            'website': 'https://transitcenter.org/blog/'
        }
    },
    "streetsblog": {
        'name': 'Streetsblog',
        'type': ['blog'],
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQm06X4'
              '-kgmtexgJpGSv8RLLBu86D7KkMISeaSVNP1vNtn7nggAIg&s',
        'image_size':   '70px',
        'newsletter': {
            'scrape_function': streetsblog,
            'website': 'https://nyc.streetsblog.org/category/issues-campaigns/transit/'
        }
    },
    "intelligenttransport": {
        'name': 'Intelligent Transport',
        'type': ['news'],
        'image': 'https://www.intelligenttransport.com/wp-content/themes/it19/images/IT-Logo@2x.png',
        'image_size':   '40px',
        'newsletter': {
            'scrape_function': rss_parser,
            'website': 'https://feeds.feedburner.com/IntelligentTransport'
        }
    },
    "urbanmobilitycompany": {
        'name': 'Urban Mobility Company',
        'type': ['blog'],
        'image': 'https://www.autonomy.paris/wp-content/uploads/2021/03/Screenshot_2021-03-18-Urban-Mobilty-Daily-Urban-Mobility-Company.png',
        'image_size':   '40px',
        "newsletter": {
            'scrape_function': umc,
            'website': 'https://urbanmobilitycompany.com/content/daily'
        }
    },
    "parkingmobility": {
        'name': 'Parking Mobility',
        'type': ['article'],
        'image': 'https://www.parking-mobility.org/wp-content/themes/ipi/images/IPMI_LOGO-R_RGB_220x96.png',
        'image_size':   '30px',
        "newsletter": {
            'scrape_function': parking_mobility,
            'website': 'https://www.parking-mobility.org/news-publications/ipmi-blog/'
        } 
    },
    "humantransit": {
        'name': 'Human Transit',
        'type': ['blog'],
        'image': 'https://humantransit.org/wp-content/uploads/HT-favicon@16x.png',
        'image_size':  '40px',
        "newsletter": {
            'scrape_function': rss_parser,
            'website': 'https://feeds.feedburner.com/humantransit/TCwW'
        }
    },
    "metrospectives": {
        'name': 'METROspectives',
        'type': ['podcast'],
        'image': 'https://fleetimages.bobitstudios.com/upload/podcasts/metrospectives'
                '/metrospectives-cover-__-315x315-r.png',
        'image_size':  '40px',
        "newsletter": {
            'scrape_function': rss_parser,
            'website': 'https://anchor.fm/s/18836658/podcast/rss'
        }
    },
    "Axios": {
        'name': 'Axios',
        'type': ['news'],
        'image': 'https://assets.axios.com/203e9f932cc97836ac2ff4c6c982676c.png',
        'image_size':   '50px',
        "newsletter": {
            'scrape_function': axios,
            'website': 'https://www.axios.com/economy-business/transportation/?page=1'
        }
    },
    "spur": {
        'name': 'Spur',
        'type': ['article'],
        'image': 'https://pbs.twimg.com/profile_images/1283457372699017216/v0M0jO2G_400x400.jpg',
        'image_size':   '60px',
        "newsletter": {
            'scrape_function': spur,
            'website': 'https://www.spur.org/news'
        }
    },
    "thetransitauthority": {
        'name': 'The Transit Authority',
        'type': ['podcast'],
        'image': 'https://media.glassdoor.com/sqll/264289/american-public-transportation-association-squarelogo.png',
        'image_size':   '40px',
        "newsletter": {
            'scrape_function': apple_parser,
            'website': 'https://podcasts.apple.com/us/podcast/the-transit-authority/id1512818062'
        }
    },
    "themobilitypodcast": {
        'name': 'The Mobility Podcast',
        'type': ['podcast'],
        'image': 'https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/74/07/46/7407463c-0bef-b30a-edb7-68915c5ade7c'
                '/mza_6209235826687352097.jpg/1200x1200bb.jpg',
        'image_size':   '40px',
        "newsletter": {
            'scrape_function': apple_parser,
            'website': 'https://podcasts.apple.com/us/podcast/the-mobility-podcast/id1301517009'
        }
    }
}