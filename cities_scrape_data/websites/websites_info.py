from ..scrapers.newsletter_scrapers import *
from ..scrapers.jobs_scrapers import *
from ..util.requests_types import (
    get_response, get_response_header, get_post_response
)

website_info = [
    {
        'id': 'planetizen',
        'name': 'Planetizen',
        'image': 'https://simplycareer.com/wp-content/uploads/2015/05/planetizen-425x215.png',
        'scrapers': [
            {
                'scrape_function': rss_parser,
                'requests': {
                    "request_type": get_response
                },
                'website': 'https://www.planetizen.com/frontpage/feed',
                'type': 'news'
            },
            {
                'scrape_function': planetizen_jobs,
                'requests': {
                    "request_type": get_response
                },
                'website': 'https://www.planetizen.com/jobs',
                'type': 'jobs'
            }
        ]
    },
    {
        'id': 'allthingsurban',
        'name': 'All Things Urban',
        'image': 'https://all-things-urban.storage.googleapis.com/static/images/social.jpg',
        'scrapers': [
            {
                'scrape_function': allthingsurban,
                'requests': {
                    "request_type": get_response
                },
                'website': 'https://www.allthingsurban.net/blog',
                'type': 'blog'
            },
            {
                'scrape_function': allthingsurban_jobs,
                'requests': {
                    "request_type": get_response
                },
                'website': 'https://www.allthingsurban.net/career',
                'type': 'jobs'
            }
        ]
    },
    {
        'id': 'monocle',
        'name': 'Monocle',
        'image': 'https://img.monocle.com/radio/shows/defaults/the-urbanist_tile-6564b4a0c56d9.jpg',
        'scrapers': [
            {
                'scrape_function': apple_parser,
                'requests': {
                    "request_type": get_response
                },
                'website': 'https://podcasts.apple.com/us/podcast/the-urbanist/id474763572',
                'type': 'podcast'
            }
        ]
    },
    {
        'id': 'smartcities',
        'name': 'Smartcities',
        'image': 'https://leadingcities2014.files.wordpress.com/2019/09/smartcities_logo_black.png',
        'scrapers': [
            {
                'scrape_function': rss_parser,
                'requests': {
                    "request_type": get_response
                },
                'website': 'https://www.smartcitiesdive.com/feeds/news/',
                'type': 'news'
            }
        ]
    },
    {
        'id': 'strongtowns',
        'name': 'Strongtowns',
        'image': 'https://pbcdn1.podbean.com/imglogo/image-logo/2312128/Blue_Stripe_Square_edit.png',
        'scrapers': [
            {
                'scrape_function': rss_parser,
                'requests': {
                    "request_type": get_response
                },
                'website': 'https://feed.podbean.com/podcast.strongtowns.org/feed.xml',
                'type': 'podcast'
            }
        ]
    },
    {
        'id': 'itetalk',
        'name': 'Itetalk',
        'image': 'https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/d933ad68df9d533175abe3a002d22ede.jpg',
        'scrapers': [
            {
                'scrape_function': rss_parser,
                'requests': {
                    "request_type": get_response
                },
                'website': 'https://www.spreaker.com/show/1744465/episodes/feed',
                'type': 'podcast'
            }
        ]
    },
    {
        'id': 'metromag',
        'name': 'Metro Mag',
        'image': 'https://fleetimages.bobitstudios.com/upload/metro-magazine/met-og-__-1200x630-s.png',
        'scrapers': [
            {
                'scrape_function': rss_parser,
                'requests': {
                    "request_type": get_response
                },
                'website': 'https://www.metro-magazine.com/rss',
                'type': 'news'
            }
        ]
    },
    {
        'id': 'talkingheadways',
        'name': 'Talking Headways',
        'image': 'https://ssl-static.libsyn.com/p/assets/3/3/e/8/33e8d0ffe911533c/talking_headways_v7.png',
        'scrapers': [
            {
                'scrape_function': rss_parser,
                'requests': {
                    "request_type": get_response
                },
                'website': 'https://streetsblog.libsyn.com/rss',
                'type': 'podcast'
            }
        ]
    },
    {
        'id': 'govlove',
        'name': 'GovLove',
        'image': 'https://storage.googleapis.com/proudcity/elglor/uploads/2018/02/cropped-elgl-icon-blue.png',
        'scrapers': [
            {
                'scrape_function': rss_parser,
                'requests': {
                    "request_type": get_response
                },
                'website': 'https://govlove.libsyn.com/rss',
                'type': 'podcast'
            },
            {
                'scrape_function': govlove_jobs,
                'requests': {
                    "request_type": get_response
                },
                'website': 'https://elgljobs.com/jobs/?categories[]=Data%20%26%20Analysis&categories[]=Innovation&categories[]=Planning',
                'type': 'jobs'
            }
        ]
    },
    {
        'id': 'govtech',
        'name': 'Govtech',
        'image': 'https://assets.website-files.com/59dfccba14d0c50001317351/5a625dd96f429200014442c3_gt.jpg',
        'scrapers': [
                {
                    'scrape_function': govtech,
                    'requests': {
                        "request_type": get_response_header
                    },
                    'website': 'https://www.govtech.com/transportation/',
                    'type': 'news'
                }
        ]
    },
    {
        'id': 'transitcenter',
        'name': 'Transitcenter',
        'image': 'https://d3n8a8pro7vhmx.cloudfront.net/circulatesd/pages/1101/attachments/original/1553274530/transit-center-logo.png?1553274530',
        'scrapers': [
                {
                    'scrape_function': transitcenter,
                    'requests': {
                        "request_type": get_response_header
                    },
                    'website': 'https://transitcenter.org/blog/',
                    'type': 'blog'
                },
            {
                    'scrape_function': transitcenter_job,
                    'requests': {
                        "request_type": get_response_header
                    },
                    'website': 'https://transitcenter.org/careersattransitcenter/',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'streetsblog',
        'name': 'Streetsblog',
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQm06X4-kgmtexgJpGSv8RLLBu86D7KkMISeaSVNP1vNtn7nggAIg&s',
        'scrapers': [
                {
                    'scrape_function': streetsblog,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://nyc.streetsblog.org/category/issues-campaigns/transit/',
                    'type': 'blog'
                }
        ]
    },
    {
        'id': 'intelligenttransport',
        'name': 'Intelligent Transport',
        'image': 'https://www.intelligenttransport.com/wp-content/themes/it19/images/IT-Logo@2x.png',
        'scrapers': [
                {
                    'scrape_function': rss_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://feeds.feedburner.com/GlobalRailwayReview',
                    'type': 'news'
                }
        ]
    },
    {
        'id': 'parkingmobility',
        'name': 'Parking Mobility',
        'image': 'https://www.parking-mobility.org/wp-content/themes/ipi/images/IPMI_LOGO-R_RGB_220x96.png',
        'scrapers': [
                {
                    'scrape_function': parking_mobility,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://www.parking-mobility.org/news-publications/ipmi-blog/',
                    'type': 'articles'
                }
        ]
    },
    {
        'id': 'metrospectives',
        'name': 'METROspectives',
        'image': 'https://fleetimages.bobitstudios.com/upload/podcasts/metrospectives/metrospectives-cover-__-315x315-r.png',
        'scrapers': [
                {
                    'scrape_function': rss_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://anchor.fm/s/18836658/podcast/rss',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'Axios',
        'name': 'Axios',
        'image': 'https://assets.axios.com/203e9f932cc97836ac2ff4c6c982676c.png',
        'scrapers': [
                {
                    'scrape_function': axios,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://www.axios.com/economy-business/transportation/?page=1',
                    'type': 'news'
                }
        ]
    },
    {
        'id': 'spur',
        'name': 'Spur',
        'image': 'https://www.aaonetwork.org/sites/default/files/orgs_images/SPUR-only-Logo_black.gif',
        'scrapers': [
                {
                    'scrape_function': spur,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://www.spur.org/news',
                    'type': 'articles'
                }
        ]
    },
    {
        'id': 'thetransitauthority',
        'name': 'The Transit Authority',
        'image': 'https://media.glassdoor.com/sqll/264289/american-public-transportation-association-squarelogo.png',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/the-transit-authority/id1512818062',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'themobilitypodcast',
        'name': 'The Mobility Podcast',
        'image': 'https://is3-ssl.mzstatic.com/image/thumb/Podcasts113/v4/74/07/46/7407463c-0bef-b30a-edb7-68915c5ade7c/mza_6209235826687352097.jpg/1200x1200bb.jpg',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/the-mobility-podcast/id1301517009',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'micromobilitypodcast',
        'name': 'The Micromobility Podcast',
        'image': 'https://cdn.substack.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb50394d7-f3de-45b5-9087-542005d1cef0_256x256.png',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/ride-ai/id1434457337',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'zag',
        'name': 'Zag',
        'image': 'https://zagdaily.com/wp-content/uploads/2021/10/Zag-Daily.jpg',
        'scrapers': [
                {
                    'scrape_function': zag,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://zagdaily.com/category/trends/',
                    'type': 'news'
                }
        ]
    },
    {
        'id': 'nyc_plannning',
        'name': 'NYC Planning',
        'image': 'https://planning-org-uploaded-media.s3.amazonaws.com/uploads/PROFILE_PHOTOS/95ba7dce-738f-465b-917a-e457760cb7b1.png',
        'scrapers': [
                {
                    'scrape_function': nyc_planning_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://www.nyc.gov/assets/planning/libs/JSON/Careers/careers.json',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'transloc',
        'name': 'transloc',
        'image': 'https://biz.prlog.org/transloc/logo.png',
        'scrapers': [
                {
                    'scrape_function': transloc,
                    'requests': {
                        "request_type": get_response_header
                    },
                    'website': 'https://transloc.com/the-movement-podcast/',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'commutifi',
        'name': 'Commutifi',
        'image': 'https://uploads-ssl.webflow.com/6006f47f5b6ed87abfdb7d41/6006f67241d3345f61b36142_logo-teal%402x.png',
        'scrapers': [
                {
                    'scrape_function': commutifi,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://www.commutifi.com/category/podcast',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'carto',
        'name': 'Carto',
        'image': 'https://mma.prnewswire.com/media/695160/CARTO_Logo.jpg',
        'scrapers': [
                {
                    'scrape_function': lever_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://jobs.lever.co/cartodb',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'cityage_podcast',
        'name': 'The CityAge Podcast',
        'image': 'https://m.media-amazon.com/images/I/51-1+SKPvCL._SL500_.jpg',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/ca/podcast/the-cityage-podcast/id1621156635',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'uber',
        'name': 'Uber',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Uber_logo_2018.png/640px-Uber_logo_2018.png',
        'scrapers': [
                {
                    'scrape_function': uber_jobs,
                    'requests': {
                        "request_type": get_post_response,
                        'header': {
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 '
                            'Safari/537.36',
                            'x-csrf-token': 'x',
                            'content-type': 'application/json',
                        },
                        'payload': {
                            "params": {
                                "location": [
                                    {
                                        "country": "USA",
                                    },
                                    {
                                        "country": "GBR",
                                    },
                                    {
                                        "country": "HKG",
                                    },
                                    {
                                        "country": "JPN",
                                    },
                                    {
                                        "country": "ESP",
                                    },
                                    {
                                        "country": "CAN",
                                    },
                                    {
                                        "country": "BRA",
                                    }
                                ],
                                "department": [
                                    "Public Policy",
                                    "Data Science",
                                    "Engineering",
                                    "Product"
                                ]
                            }
                        }
                    },
                    'website': 'https://www.uber.com/api/loadSearchJobsResults?localeCode=en',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'via',
        'name': 'Via',
        'image': 'https://assets-global.website-files.com/609196881a69bf7486cbfd01/60919d5d15b7324b8aa8d9d8_via-logo.svg',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/modeshift/id1644748349',
                    'type': 'podcast'
                },
            {
                    'scrape_function': greenhouse_older_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://boards.greenhouse.io/via',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'modernmobility',
        'name': 'Modern Mobility Podcast',
        'image': 'https://deow9bq0xqvbj.cloudfront.net/image-logo/11422003/ModMob_Podcast_Cover_Art-headphones-resized.jpg',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/the-modern-mobility-podcast/id1559679341',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'mobilitydata',
        'name': 'Mobility Data',
        'image': 'https://mobilitydata.org/app/uploads/2021/04/cropped-flaticon_logo-18.png',
        'scrapers': [
                {
                    'scrape_function': mobilitydata_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://careers.mobilitydata.org',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'goswift',
        'name': 'Swiftly',
        'image': 'https://store.lmknowledgehub.com/storage/swift/G1lc1nfABW8ZhO2Kdu0WP2o0TqbqN8CVnjoquQn8.png',
        'scrapers': [
                {
                    'scrape_function': lever_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://jobs.lever.co/goswift',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'smartgrowthamerica',
        'name': 'Smart Growth America',
        'image': 'https://smartgrowthamerica.org/wp-content/uploads/2021/08/SGA_logo_card.png',
        'scrapers': [
                {
                    'scrape_function': smartgrowamerica_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://smartgrowthamerica.org/about-us/careers/',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'nlc',
        'name': 'National League of Cities',
        'image': 'https://upload.wikimedia.org/wikipedia/en/0/00/National_League_of_Cities_logo.png',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/citiesspeak-with-clarence-anthony/id1635203625',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'electronomous',
        'name': 'Electronomous',
        'image': 'https://www.showsbee.com/newmaker/www/u/2022/20225/com_img/Electronomous-logo.png',
        'scrapers': [
                {
                    'scrape_function': electronomous,
                    'requests': {
                        "request_type": get_response_header
                    },
                    'website': 'https://www.electronomous.com/news/',
                    'type': 'news'
                }
        ]
    },
    {
        'id': 'revel',
        'name': 'Revel',
        'image': 'https://s4-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/075/500/resized/revel_greenhouse.png',
        'scrapers': [
                {
                    'scrape_function': greenhouse_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://boards.greenhouse.io/revel',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'streetlightdata',
        'name': 'Street Light Data',
        'image': 'https://lever-client-logos.s3.amazonaws.com/0046318a-573c-41a8-8de0-52fda3259340-1546914822777.png',
        'scrapers': [
                {
                    'scrape_function': lever_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://jobs.lever.co/streetlightdata',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'lime',
        'name': 'Lime',
        'image': 'https://lever-client-logos.s3.amazonaws.com/04d69456-1062-431c-bf70-177b55749515-1571247003987.png',
        'scrapers': [
                {
                    'scrape_function': lever_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://jobs.lever.co/lime',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'urbanfootprint',
        'name': 'Urban Footprint',
        'image': 'https://urbanfootprint.com/wp-content/uploads/2022/06/UrbanFootprint_Logo@2x.png',
        'scrapers': [
                {
                    'scrape_function': urbanfootprint_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://boards.greenhouse.io/urbanfootprint',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'mbta',
        'name': 'MBTA',
        'image': 'https://lever-client-logos.s3-us-west-2.amazonaws.com/753da791-a783-4cb5-b37d-ce85a22dc7bd-1596468426966.png',
        'scrapers': [
                {
                    'scrape_function': lever_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://jobs.lever.co/mbta/',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'optibus',
        'name': 'Optibus',
        'image': 'https://www.optibus.com/wp-content/uploads/2021/12/optibus-dark-logo.svg',
        'scrapers': [
                {
                    'scrape_function': optibus_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://www.optibus.com/company/careers/jobs/',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'itoworld',
        'name': 'Ito World',
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqX4ny_KpkEgtdPbWqcBzeETqJ0IB7utegAg&s',
        'scrapers': [
                {
                    'scrape_function': ito_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://itoworld.bamboohr.com/careers/list',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'voi',
        'name': 'Voi',
        'image': 'https://pbs.twimg.com/profile_images/1293203903610105861/Kh_w4N69_400x400.jpg',
        'scrapers': [
                {
                    'scrape_function': voi_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://careers.voi.com/jobs?department=Research+%26+Development&query=',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'tier',
        'name': 'Tier',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/TIER_Mobility_Logo_%28blau%2C_2021%29.svg/1200px-TIER_Mobility_Logo_%28blau%2C_2021%29.svg.png',
        'scrapers': [
                {
                    'scrape_function': greenhouse_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://boards.greenhouse.io/tiermobility',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'veo',
        'name': 'Veo',
        'image': 'https://s4-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/297/800/resized/veo_logo_black.png?1622840779',
        'scrapers': [
                {
                    'scrape_function': greenhouse_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://job-boards.greenhouse.io/veocorporatecareers',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'populus',
        'name': 'Populus',
        'image': 'https://images.squarespace-cdn.com/content/v1/5fc6dab681da8a590dace76d/1608170071061-NYJKZQQBQHK4IHASGYNR/Populus_SecondaryLogo_Dark.png',
        'scrapers': [
                {
                    'scrape_function': greenhouse_older_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://boards.greenhouse.io/populus',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'blablacar',
        'name': 'Blablacar',
        'image': 'https://lever-client-logos.s3.us-west-2.amazonaws.com/e3520345-0a28-449b-8485-23082ade0c1f-1623869719522.png',
        'scrapers': [
                {
                    'scrape_function': lever_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://jobs.lever.co/blablacar',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'dott',
        'name': 'Dott',
        'image': 'https://lever-client-logos.s3.us-west-2.amazonaws.com/f11eb4df-5f0d-4027-8616-f0ae67765b48-1607421366657.png',
        'scrapers': [
                {
                    'scrape_function': lever_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://jobs.lever.co/dott',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'digitalbluefoam',
        'name': 'Digital Blue Foam',
        'image': 'https://assets-global.website-files.com/64c79ac5be374c3df952fa71/64e6109eb0e64d7926970b5b_dbf.svg',
        'scrapers': [
                {
                    'scrape_function': dbf_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://www.digitalbluefoam.com/company/career',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'transitunplugged',
        'name': 'Transit Unplugged',
        'image': 'https://pbs.twimg.com/profile_images/1456617608023773192/BATZcuGt_400x400.jpg',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/transit-unplugged/id1308238228',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'waroncars',
        'name': 'The War on Cars',
        'image': 'https://pbs.twimg.com/profile_images/1049045594755538944/0QCcdgNi_400x400.jpg',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/the-war-on-cars/id1437755068',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'smartcitieschronicles',
        'name': 'Smart Cities Chronicles',
        'image': 'https://is1-ssl.mzstatic.com/image/thumb/Podcasts125/v4/88/2c/cd/882ccd3c-7246-aa82-9992-cf6eb13d34a2/mza_3654834813016531476.png/626x0w.webp',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/smart-cities-chronicles/id1448411504',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'trafi',
        'name': 'Trafi',
        'image': 'https://workable-application-form.s3.amazonaws.com/advanced/production/6076d2e3756dfc2c9f97167c/1dba3256-e0d4-44c1-9e86-85abaa003048',
        'scrapers': [
                {
                    'scrape_function': workable_jobs,
                    'requests': {
                        "request_type": get_post_response,
                        'header': {
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 '
                            'Safari/537.36',
                            'content-type': 'application/json',
                        },
                        'payload': {
                            "query": "", "location": [], "department": [
                            ], "worktype": [], "remote": [], "workplace": []
                        }
                    },
                    'website': 'https://apply.workable.com/api/v3/accounts/trafi/jobs',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'replica',
        'name': 'Replica',
        'image': 'https://mms.businesswire.com/media/20211004005009/en/910899/22/replica_logo.jpg',
        'scrapers': [
                {
                    'scrape_function': replica_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://replicainc.applytojob.com/apply/jobs/',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'lastminute',
        'name': 'lastminute',
        'image': 'https://corporate.lastminute.com/wp-content/uploads/2023/11/brands-lastminutecom.svg',
        'scrapers': [
                {
                    'scrape_function': lastminute_jobs,
                    'requests': {
                        "request_type": get_response,
                    },
                    'website': 'https://corporate.lastminute.com/wp-admin/admin-ajax.php?action=lm_careers_search',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'lametro',
        'name': 'LA Metro',
        'image': 'https://www.publicissapient.com/content/dam/ps-rebrand/work/la-metros-boundary-less-fare-cards/Promo_GOV_LA-Metro-Tap.jpg',
        'scrapers': [
                {
                    'scrape_function': la_metro_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://jobs.metro.net/jobsearch.aspx',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'rpa',
        'name': 'Regional Plan Association',
        'image': 'https://upload.wikimedia.org/wikipedia/en/0/05/Regional_Plan_Association_logo.png',
        'scrapers': [
                {
                    'scrape_function': rpa_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://rpa.org/latest',
                    'type': 'articles'
                },
            {
                    'scrape_function': rpa_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://rpa.org/about/join',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'lyft',
        'name': 'Lyft',
        'image': 'https://image.careerpuck.com/_TnoAqcr/_TnoAqcr.300.png',
        'scrapers': [
                {
                    'scrape_function': lyft_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://api.careerpuck.com/v1/public/job-boards/lyft',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'curbed',
        'name': 'Curbed',
        'image': 'https://cdn.vox-cdn.com/thumbor/hqUmDteDLbeE75fhl2onrLwpWPc=/0x0:5290x3549/1200x800/filters:focal(2222x1352:3068x2198)/cdn.vox-cdn.com/uploads/chorus_image/image/67624042/Edit_Letter_Lede_V1.0.jpg',
        'scrapers': [
                {
                    'scrape_function': curbed_scraper,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://www.curbed.com/cityscape/',
                    'type': 'news'
                }
        ]
    },
    {
        'id': 'transitapp',
        'name': 'Transit App',
        'image': 'https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Transit_App_icon.png/300px-Transit_App_icon.png',
        'scrapers': [
                {
                    'scrape_function': transit_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://manifesto.transitapp.com/jobs',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'spare',
        'name': 'Spare',
        'image': 'https://app.pinpointhq.com/rails/active_storage/representations/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBL1RjSnc9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--5d0af3b2ab4d0240ffa1d59a987009d6d3ef5f93/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCam9MY21WemFYcGxTU0lRTkRRd0xqQjRNVEF3TGpBR09nWkZWQT09IiwiZXhwIjpudWxsLCJwdXIiOiJ2YXJpYXRpb24ifX0=--5fd990b5737f041b8b006e0f6f8b9bd3043c9631/spare-logo.png',
        'scrapers': [
                {
                    'scrape_function': spare_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://sparelabs.pinpointhq.com/en/postings.json',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'thenewurbanorder',
        'name': 'The New Urban Order',
        'image': 'https://substackcdn.com/image/fetch/w_1360,c_limit,f_webp,q_auto:best,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fe10dd1-1613-4f0c-a8b6-b36a210d2022_629x629.png',
        'scrapers': [
                {
                    'scrape_function': rss_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://thenewurbanorder.substack.com/feed',
                    'type': 'blog'
                }
        ]
    },
    {
        'id': 'chartercitiesinstitute_podcast',
        'name': 'Charter Cities Institute Podcast',
        'image': 'https://cdn.movemeback.com/media/organisation/logo/charter-cities-institute-organisation-logo-20200213-14483469.png',
        'scrapers': [
                {
                    'scrape_function': chartercitiesinstitute_podcast_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://chartercitiesinstitute.org/category/podcast/',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'chartercitiesinstitute_blog',
        'name': 'Charter Cities Institute Blog',
        'image': 'https://cdn.movemeback.com/media/organisation/logo/charter-cities-institute-organisation-logo-20200213-14483469.png',
        'scrapers': [
                {
                    'scrape_function': chartercitiesinstitute_blog_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://chartercitiesinstitute.org/blog/',
                    'type': 'blog'
                }
        ]
    },
    {
        'id': 'the-mobility-house',
        'name': 'The Mobility House',
        'image': 'https://cdn.theorg.com/cd0c0e7e-3df6-4f96-96e6-4421e9d887fc_medium.jpg',
        'scrapers': [
                {
                    'scrape_function': workable_jobs,
                    'requests': {
                        "request_type": get_post_response,
                        'header': {
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 '
                            'Safari/537.36',
                            'content-type': 'application/json',
                        },
                        'payload': {
                            "query": "", "location": [], "department": [
                            ], "worktype": [], "remote": [], "workplace": []
                        }
                    },
                    'website': 'https://apply.workable.com/api/v3/accounts/the-mobility-house/jobs',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'alongfortherid',
        'name': 'Along for the Ride',
        'image': 'https://substackcdn.com/image/fetch/w_1360,c_limit,f_webp,q_auto:best,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37b19261-f7a6-48fe-bb9d-43d244a7fb7e_1280x242.png',
        'scrapers': [
                {
                    'scrape_function': rss_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://alongfortheride.substack.com/feed',
                    'type': 'blog'
                }
        ]
    },
    {
        'id': 'trufiassociation',
        'name': 'Trufi Association',
        'image': 'https://www.trufi-association.org/wp-content/uploads/2021/12/TrufiAssociation_Logo-BlackText-retina-603%C3%97140px.png',
        'scrapers': [
                {
                    'scrape_function': rss_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://www.trufi-association.org/feed/',
                    'type': 'blog'
                }
        ]
    },
    {
        'id': 'eurocities',
        'name': 'Euro Cities',
        'image': 'https://eurocities.eu/wp-content/themes/eurocities/images/logo.svg',
        'scrapers': [
                {
                    'scrape_function': eurocities_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://eurocities.eu/latest/',
                    'type': 'news'
                }
        ]
    },
    {
        'id': 'activecities',
        'name': 'Active Cities',
        'image': 'https://walk21.com/wp-content/uploads/2023/02/Active_Cities_Interreg_square-1536x1536.png',
        'scrapers': [
                {
                    'scrape_function': activecities_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://www.interregnorthsea.eu/active-cities/news',
                    'type': 'news'
                }
        ]
    },
    {
        'id': 'gvshp',
        'name': 'NYC Village Preservation',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/4/4d/Village_Preservation_Logo.png',
        'scrapers': [
                {
                    'scrape_function': gvshp_parser,
                    'requests': {
                        "request_type": get_response_header
                    },
                    'website': 'https://www.villagepreservation.org/blog/',
                    'type': 'blog'
                },
            {
                    'scrape_function': gvshp_jobs,
                    'requests': {
                        "request_type": get_response_header
                    },
                    'website': 'https://www.villagepreservation.org/employment-internships/',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'itdpTransportMatters',
        'name': 'ITDP: Transport Matters',
        'image': 'https://gallery.mailchimp.com/0b5e10eda9e3afdb7eceb76f6/images/1ebf09b3-ebeb-4bbb-af99-396df5e5450f.jpg',
        'scrapers': [
                {
                    'scrape_function': itdpTransportMatters_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://itdp.org/transport-matters-blog/',
                    'type': 'news'
                }
        ]
    },
    {
        'id': 'nextstoptransittech',
        'name': 'Next Stop: Transit Tech',
        'image': 'https://d3t3ozftmdmh3i.cloudfront.net/production/podcast_uploaded_nologo/12515454/12515454-1613071096981-0ad3b212986b3.jpg',
        'scrapers': [
                {
                    'scrape_function': rss_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://feeds.simplecast.com/ciqd74e4',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'urbandesignforum',
        'name': 'Urban Design Forum',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Urbandesingforumlogo.jpg/440px-Urbandesingforumlogo.jpg',
        'scrapers': [
                {
                    'scrape_function': urbandesignforum_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://urbandesignforum.org/join/opportunities/',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'themasterplan',
        'name': 'The Masterplan',
        'image': 'https://is1-ssl.mzstatic.com/image/thumb/Podcasts126/v4/dd/18/94/dd18947c-8879-28fc-d7a6-5f430523b3cf/mza_7786262743904593528.jpg/626x0w.webp',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/the-masterplan/id1701440562',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'urbanroots',
        'name': 'Urban Roots',
        'image': 'https://is1-ssl.mzstatic.com/image/thumb/Podcasts122/v4/a5/ee/98/a5ee98a0-1f2b-61ea-79f2-fadcf4fb6e52/mza_179906692931538217.jpg/626x0w.webp',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/urban-roots/id1531965989',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'humankindnewsletter',
        'name': 'Humankind’s Newsletter',
        'image': 'https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25139679-8355-42d3-b743-df2059020b61_600x600.png',
        'scrapers': [
                {
                    'scrape_function': rss_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://humankindcity.substack.com/feed',
                    'type': 'blog'
                }
        ]
    },
    {
        'id': 'futuremobility',
        'name': 'Future Mobility',
        'image': 'https://substackcdn.com/image/fetch/w_96,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25139679-8355-42d3-b743-df2059020b61_600x600.png',
        'scrapers': [
                {
                    'scrape_function': futuremobility_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://futuremobility.lindholmen.se/en/news',
                    'type': 'blog'
                }
        ]
    },
    {
        'id': 'powerofcommunity',
        'name': 'Power of Community by City Destinations Alliance',
        'image': 'https://s3-us-west-2.amazonaws.com/anchor-generated-image-bank/production/podcast_uploaded_nologo400/16424521/16424521-1655287794780-5727f4a57098b.jpg',
        'scrapers': [
                {
                    'scrape_function': rss_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://anchor.fm/s/627e6b04/podcast/rss',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'zencity',
        'name': 'Zencity',
        'image': 'https://pbs.twimg.com/profile_images/1704493064499191808/hdEuPhlV_400x400.png',
        'scrapers': [
                {
                    'scrape_function': zencity_jobs,
                    'requests': {
                        "request_type": get_response_header
                    },
                    'website': 'https://zencity.io/careers/',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'nava',
        'name': 'Nava',
        'image': 'https://www.navapbc.com/favicon.svg',
        'scrapers': [
                {
                    'scrape_function': lever_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://jobs.lever.co/nava/',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'urbanomnibus',
        'name': 'Urban Omnibus',
        'image': 'https://urbanomnibus.net/wp-content/themes/uo/assets/img/uo-logo-white.svg',
        'scrapers': [
                {
                    'scrape_function': urbanomnibus_parser,
                    'requests': {
                        "request_type": get_response_header
                    },
                    'website': 'https://urbanomnibus.net/browse/',
                    'type': 'news'
                }
        ]
    },
    {
        'id': 'enotransportation',
        'name': 'Eno Transporation Weekly',
        'image': 'https://enotrans.org/wp-content/uploads/2022/12/Eno-Logo-2-1030x258.png',
        'scrapers': [
                {
                    'scrape_function': enotransportation_parser,
                    'requests': {
                        "request_type": get_response_header
                    },
                    'website': 'https://enotrans.org/eno-transportation-weekly/',
                    'type': 'news'
                }
        ]
    },
    {
        'id': 'nusurbananalytics',
        'name': 'NUS Urban Analytics',
        'image': 'https://ual.sg/media/logo_hudf6568bba15e1da205f5ca71c5f20891_42193_0x70_resize_lanczos_3.png',
        'scrapers': [
                {
                    'scrape_function': nusurbananalytics_parser,
                    'requests': {
                        "request_type": get_response_header
                    },
                    'website': 'https://ual.sg/post/',
                    'type': 'articles'
                }
        ]
    },
    {
        'id': 'movingpeople',
        'name': '#MovingPeople',
        'image': 'https://media.beehiiv.com/cdn-cgi/image/fit=scale-down,format=auto,onerror=redirect,quality=80/uploads/publication/logo/4654d93c-147e-4cf2-94cc-56703237268c/green_man_light.jpg',
        'scrapers': [
                {
                    'scrape_function': rss_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://rss.beehiiv.com/feeds/iCkeaq5DWm.xml',
                    'type': 'blog'
                }
        ]
    },
    {
        'id': 'electricera',
        'name': 'Electric Era',
        'image': 'https://pbs.twimg.com/profile_images/1863655693972291584/lnUdeakc_400x400.jpg',
        'scrapers': [
                {
                    'scrape_function': electricera_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://electriceratechnologies.com/careers',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'parkmobile',
        'name': 'Park Mobile',
        'image': 'https://www.parking.net/Upload/Industry/00-New-HD-Logos/parkmobile-company-logo-480px_main.jpg',
        'scrapers': [
                {
                    'scrape_function': parkmobile_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://careers.parkmobile.io/jobs',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'inspirationMobility',
        'name': 'Inspiration Mobility',
        'image': 'https://lever-client-logos.s3.us-west-2.amazonaws.com/f446fc6e-6ae0-456d-a9c2-f847132abef2-1640978230903.png',
        'scrapers': [
                {
                    'scrape_function': lever_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://jobs.lever.co/inspiration-mobility',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'fleet',
        'name': 'Fleet',
        'image': 'https://cdn.prod.website-files.com/60c7f12862eab431c781bc24/669a82ea31e72031ec334bdf_Group%2010122572.avif',
        'scrapers': [
                {
                    'scrape_function': fleet_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://www.movewithfleet.com/about-us',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'vivacitylabs',
        'name': 'Vivacity Labs',
        'image': 'https://lever-client-logos.s3.us-west-2.amazonaws.com/e0200f8d-63da-4b74-b3d6-f9fe20007388-1656683474532.png',
        'scrapers': [
                {
                    'scrape_function': lever_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://jobs.lever.co/vivacitylabs/',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'nplan',
        'name': 'nPlan',
        'image': 'https://gallery-cdn.breezy.hr/e99e7f5f-8b57-4a28-b172-2ef7f1d58ff2/nPlan_logo_blue.png',
        'scrapers': [
                {
                    'scrape_function': nplan_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://nplan.breezy.hr/',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'bloomworks',
        'name': 'Bloomworks',
        'image': 'https://s7-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/165/600/resized/bw-green.png?1686168632',
        'scrapers': [
                {
                    'scrape_function': greenhouse_older_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://boards.greenhouse.io/bloomworks',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'arcadis',
        'name': 'Arcadis',
        'image': 'https://c.smartrecruiters.com/sr-company-logo-prod-aws-dc5/57e9b7bbe4b0b6fa1a859b8d/huge?r=s3-eu-central-1&_1702069078823',
        'scrapers': [
                {
                    'scrape_function': arcadis_jobs,
                    'requests': {
                        "request_type": get_multi_responses,
                        "end_points": [
                            'page=1', 'page=2', 'page=3', 'page=4',
                            'page=5', 'page=6', 'page=7'
                        ]
                    },
                    'website': 'https://careers.smartrecruiters.com/IBIGroup/api/groups?',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'metropolis',
        'name': 'Metropolis',
        'image': 'https://s3-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/053/300/original/mark.png?1578956035',
        'scrapers': [
                {
                    'scrape_function': greenhouse_jobs,
                    'requests': {
                        "request_type": get_response,
                    },
                    'website': 'https://job-boards.greenhouse.io/metropolis',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'gridwise',
        'name': 'Gridwise',
        'image': 'https://gridwise.io/wp-content/uploads/2021/09/logo.svg',
        'scrapers': [
                {
                    'scrape_function': gridwise_jobs,
                    'requests': {
                        "request_type": get_response,
                    },
                    'website': 'https://jobs.ashbyhq.com/gridwise?embed=js',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'papayadash',
        'name': 'Papaya Dash',
        'image': 'https://workable-application-form.s3.amazonaws.com/advanced/production/628ced9a7d26824e5742d0d5/9a161780-a02c-9947-ac23-563a862f1016',
        'scrapers': [
                {
                    'scrape_function': workable_jobs,
                    'requests': {
                        "request_type": get_post_response,
                        'header': {
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 '
                            'Safari/537.36',
                            'content-type': 'application/json',
                        },
                        'payload': {
                            "query": "", "location": [], "department": [
                            ], "worktype": [], "remote": [], "workplace": []
                        }
                    },
                    'website': 'https://apply.workable.com/api/v3/accounts/papayadash/jobs',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'foursquareItp',
        'name': 'Foursquare ITP',
        'image': 'https://s3.amazonaws.com/resumator/customer_20200514151826_0OI7MI4QLNBYFWYO/logos/20230831160450_Full_Color_CMYK.jpg',
        'scrapers': [
                {
                    'scrape_function': foursquareitp_jobs,
                    'requests': {
                        "request_type": get_response,
                    },
                    'website': 'https://foursquareitp.applytojob.com/',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'inrix',
        'name': 'Inrix',
        'image': 'https://mma.prnewswire.com/media/2446738/INRIX_Logo.jpg',
        'scrapers': [
                {
                    'scrape_function': inrix_jobs,
                    'requests': {
                        "request_type": get_response,
                    },
                    'website': 'https://jobs.jobvite.com/careers/inrix/jobs?__jvst=Job%20Board&__jvsd=Career_Site',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'freewheelingpodcast',
        'name': 'The Freewheeling Podcast',
        'image': 'https://is1-ssl.mzstatic.com/image/thumb/Podcasts115/v4/c7/a2/1f/c7a21fdd-ef81-b534-1c6c-e876e31f618a/mza_5534370612162334114.jpg/600x600bb.webp',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response,
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/the-freewheeling-podcast/id1549884606',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'urbcast',
        'name': 'Urbcast',
        'image': 'https://is1-ssl.mzstatic.com/image/thumb/Podcasts112/v4/d9/87/f1/d987f1d9-6939-9d99-8029-aedb635eb98d/mza_13540068321417830341.jpg/600x600bb.webp',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response,
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/urbcast-a-podcast-about-cities-podcast-o-miastach/id1515146767',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'journal_buildingscities',
        'name': 'Buildings & Cities Journal',
        'image': 'https://storage.googleapis.com/jnl-up-j-bc-public/journals/1/pageHeaderLogoImage_en_US.png',
        'scrapers': [
                {
                    'scrape_function': journal_buildingscities_parser,
                    'requests': {
                        "request_type": get_response,
                    },
                    'website': 'https://journal-buildingscities.org/',
                    'type': 'articles'
                }
        ]
    },
    {
        'id': 'rebel',
        'name': 'Rebel',
        'image': 'https://www.stichtingfresh.nl/wp-content/uploads/2020/02/rebel.png',
        'scrapers': [
                {
                    'scrape_function': rebel_job_parser,
                    'requests': {
                        "request_type": get_response,
                    },
                    'website': 'https://rebelgroup.com/en/career/',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'haydenai',
        'name': 'HaydenAI',
        'image': 'https://logowik.com/content/uploads/images/haydenai8139.logowik.com.webp',
        'scrapers': [
                {
                    "scrape_function": haydenai_parser,
                    "requests": {
                        "request_type": get_post_response,
                        "header": {
                            "content-type": "application/json",
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)"
                        },
                        "payload": {
                            "operationName": "ApiJobBoardWithTeams",
                            "variables": {
                                "organizationHostedJobsPageName": "haydenai"
                            },
                            "query": "query ApiJobBoardWithTeams($organizationHostedJobsPageName: String!) {\n  jobBoard: jobBoardWithTeams(\n    organizationHostedJobsPageName: $organizationHostedJobsPageName\n  ) {\n    teams {\n      id\n      name\n      parentTeamId\n      __typename\n    }\n    jobPostings {\n      id\n      title\n      teamId\n      locationId\n      locationName\n      employmentType\n      secondaryLocations {\n        ...JobPostingSecondaryLocationParts\n        __typename\n      }\n      compensationTierSummary\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment JobPostingSecondaryLocationParts on JobPostingSecondaryLocation {\n  locationId\n  locationName\n  __typename\n}"
                        }
                    },
                    "website": "https://jobs.ashbyhq.com/api/non-user-graphql?op=ApiJobBoardWithTeams",
                    "type": "jobs"
                }
        ]
    },
    {
        "id": "masabi",
        "name": "Masabi",
        "image": "https://careers.masabi.com/wp-content/uploads/2023/01/06-red-black-1024x576.png",
        "scrapers": [
            {
                "scrape_function": masabi_job_parser,
                "requests": {
                    "request_type": get_post_response,
                    "header": {
                        "content-type": "application/json",
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)"
                    },
                    "payload": {
                        "operationName": "ApiJobBoardWithTeams",
                        "variables": {
                            "organizationHostedJobsPageName": "masabi"
                        },
                        "query": "query ApiJobBoardWithTeams($organizationHostedJobsPageName: String!) {\n  jobBoard: jobBoardWithTeams(\n    organizationHostedJobsPageName: $organizationHostedJobsPageName\n  ) {\n    teams {\n      id\n      name\n      parentTeamId\n      __typename\n    }\n    jobPostings {\n      id\n      title\n      teamId\n      locationId\n      locationName\n      employmentType\n      secondaryLocations {\n        ...JobPostingSecondaryLocationParts\n        __typename\n      }\n      compensationTierSummary\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment JobPostingSecondaryLocationParts on JobPostingSecondaryLocation {\n  locationId\n  locationName\n  __typename\n}\n"
                    }
                },
                "website": "https://jobs.ashbyhq.com/api/non-user-graphql?op=ApiJobBoardWithTeams",
                "type": "jobs"
            }
        ]
    },
    {
        'id': 'roadie',
        'name': 'Roadie',
        'image': 'https://s2-recruiting.cdn.greenhouse.io/external_greenhouse_job_boards/logos/400/587/300/original/Roadie_UPS_Logo_Stack_BROWN.png?1648056516',
        'scrapers': [
                {
                    'scrape_function': greenhouse_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://job-boards.greenhouse.io/roadie',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'goodtraffic',
        'name': 'Good Traffic',
        'image': 'https://is1-ssl.mzstatic.com/image/thumb/Podcasts211/v4/b8/56/4b/b8564ba8-f066-7a26-c7ca-3db49914ffe7/mza_4128940626188746453.jpg/600x600bb.webp',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/good-traffic/id1707603110',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'cabify',
        'name': 'Cabify',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Cabify-Logo-Moradul-RGB.png/440px-Cabify-Logo-Moradul-RGB.png',
        'scrapers': [
                {
                    'scrape_function': cabify_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://cabify.careers/en/jobs?search=&office=&department=',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'autofleet',
        'name': 'Autofleet',
        'image': 'https://workablehr.s3.amazonaws.com/uploads/account/logo/445657/logo',
        'scrapers': [
                {
                    'scrape_function': workable_jobs,
                    'requests': {
                        "request_type": get_post_response,
                        'header': {
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 '
                            'Safari/537.36',
                            'content-type': 'application/json',
                        },
                        'payload': {
                            "query": "", "location": [], "department": [
                            ], "worktype": [], "remote": [], "workplace": []
                        }
                    },
                    'website': 'https://apply.workable.com/api/v3/accounts/autofleet/jobs',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'spacespodcast',
        'name': 'Spaces Podcast',
        'image': 'https://is1-ssl.mzstatic.com/image/thumb/Podcasts221/v4/db/30/54/db305462-8eb8-b6d5-eab3-abd1935751e1/mza_2839107751596279306.png/600x600bb.webp',
        'scrapers': [
                {
                    'scrape_function': apple_parser,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://podcasts.apple.com/us/podcast/spaces-podcast/id1326670085',
                    'type': 'podcast'
                }
        ]
    },
    {
        'id': 'cyvlai',
        'name': 'Cyvl Ai',
        'image': 'https://lever-client-logos.s3.us-west-2.amazonaws.com/50c872b0-4a13-4b4b-964f-d211908916c5-1719259337206.png',
        'scrapers': [
                {
                    'scrape_function': lever_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://jobs.lever.co/cyvl-ai',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'procureai',
        'name': 'Procure Ai',
        'image': 'https://workable-application-form.s3.amazonaws.com/advanced/production/602fa2bc3e0ec0b348d61f16/6a4ba8ba-9859-9635-8e15-d4a8a13dd8e5',
        'scrapers': [
            {
                'scrape_function': workable_jobs,
                'requests': {
                    "request_type": get_post_response,
                    'header': {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 '
                        'Safari/537.36',
                        'content-type': 'application/json',
                    },
                    'payload': {
                        "query": "", "location": [], "department": [
                        ], "worktype": [], "remote": [], "workplace": []
                    }
                },
                'website': 'https://apply.workable.com/api/v3/accounts/procureai/jobs',
                'type': 'jobs'
            }
        ]
    },
    {
        'id': 'podaris',
        'name': 'Podaris',
        'image': 'https://cdn.prod.website-files.com/627130c0c6ca7661fa206333/627130c0c6ca76825e2064d1_podaris_logo.svg',
        'scrapers': [
                {
                    'scrape_function': podaris_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://embed.homerun.co/nqcgqjpfb0xkutoxamvm/widget-en.html?t=1734964836330',
                    'type': 'jobs'
                }
        ]
    },
    {
        'id': 'coforma',
        'name': 'Coforma',
        'image': 'https://lever-client-logos.s3.us-west-2.amazonaws.com/d469341d-d7d9-43b5-9b93-e82d5792eae7-1602006045141.png',
        'scrapers': [
                {
                    'scrape_function': lever_jobs,
                    'requests': {
                        "request_type": get_response
                    },
                    'website': 'https://jobs.lever.co/coforma',
                    'type': 'jobs'
                }
        ]
    }
]
