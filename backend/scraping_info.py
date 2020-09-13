from backend.scraping_sites import moncole, cityfix, \
    planetizen, govtech, streetsblog, smartcities, datasmart, \
    strongtowns, transitcenter, masstransit, \
    itetalk, metro_mag


scarping_dict = [
    {'source': 'monocle',
     'type': 'podcast',
     'scraped_function': moncole,
     'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmKMTL7s8pHWi3lGcPnbXw5_bP4VXZIP2PgdXV5wr-u7tlTtgf',
     'website': 'https://www.omnycontent.com/d/playlist/e6127ab7-b81e-456b-893c-a8d600215365/7903d81a-7481-40dd-85ff'
                '-a8db009e611f/ff59014c-a954-4271-8920-a8db009e612d/podcast.rss '
     },
    {'source': 'thecityfix',
     'type': 'article',
     'scraped_function': cityfix,
     'image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAATYAAACjCAMAAAA3vsLfAAAA0lBMVEX////9sBb//v/8///9qwD/1AH'
              '///3+58L9qgD+/vv8rQD8sBj//v7936n92Z39rQD9xGf+/PX9u0j/+Oj8wlj9pwD+8tz+rxn97ND90IT905H9uj/9tSn'
              '/+PD9xWP9syX91gD+4W3+3VH7wlT97tP9ynX86sf+9N/93q77vED4rwD8vEz92qH+zwD9ynD98sb97sv8z3/72JP95bb80Yv3xVr'
              '+2qT86Zz931n97rD+77z8u0/92Tj7ujf9+eX'
              '+99n6y2v85Ij82kD84Xb0sxL966CKyaTJAAARWUlEQVR4nO1biXbbtrYFAQgmQNo0TUnQaLuxRtpWokjXSZo6ae/1'
              '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',
     'website': 'https://feeds.feedburner.com/thecityfix/posts'
     },
    {'source': 'planetizen',
     'type': 'news',
     'scraped_function': planetizen,
     'image': 'https://www.planetizen.com/sites/all/themes/custom/plnz3/logo.svg',
     'website': 'https://www.planetizen.com/frontpage/feed'
     },
    {'source': 'govtech',
     'type': 'news',
     'scraped_function': govtech,
     'image': 'https://assets.website-files.com/59dfccba14d0c50001317351/5a625dd96f429200014442c3_gt.jpg',
     'website': 'https://www.govtech.com/transportation/'
     },
    {'source': 'streetblog',
     'type': 'blog',
     'scraped_function': streetsblog,
     'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQm06X4'
              '-kgmtexgJpGSv8RLLBu86D7KkMISeaSVNP1vNtn7nggAIg&s',
     'website': 'https://nyc.streetsblog.org/category/issues-campaigns/transit/'
     },
    {'source': 'smartcities',
     'type': 'news',
     'scraped_function': smartcities,
     'image': 'https://leadingcities2014.files.wordpress.com/2019/09/smartcities_logo_black.png',
     'website': 'https://www.smartcitiesdive.com/feeds/news/'
     },
    {'source': 'datasmart',
     'type': 'article',
     'scraped_function': datasmart,
     'image': 'data:image/png;base64,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',
     'website': 'https://datasmart.ash.harvard.edu/feeds'
     },
    {'source': 'strongtowns',
     'type': 'podcast',
     'scraped_function': strongtowns,
     'image': 'https://pbcdn1.podbean.com/imglogo/image-logo/2312128/Blue_Stripe_Square_edit.png',
     'website': 'https://feed.podbean.com/podcast.strongtowns.org/feed.xml'
     },
    {'source': 'transitcenter',
     'type': 'blog',
     'scraped_function': transitcenter,
     'image': 'https://d3n8a8pro7vhmx.cloudfront.net/circulatesd/pages/1101/attachments/original/1553274530/transit-center-logo.png?1553274530',
     'website': 'https://transitcenter.org/blog/'
     },
    {'source': 'masstransit',
     'type': 'news',
     'scraped_function': masstransit,
     'image': 'https://www.greenpowerbus.com/wp-content/uploads/2017/03/mass-transit350-300.jpg',
     'website': 'https://www.masstransitmag.com/'
     },
    {'source': 'itetalk',
     'type': 'podcast',
     'scraped_function': itetalk,
     'image': 'https://d3wo5wojvuv7l.cloudfront.net/t_square_limited_320/images.spreaker.com/original/d933ad68df9d533175abe3a002d22ede.jpg',
     'website': 'https://www.spreaker.com/show/1744465/episodes/feed'
     },
    {'source': 'metro_mag',
     'type': 'news',
     'scraped_function': metro_mag,
     'image': 'https://sc.bobitstudios.com/logos/met.svg',
     'website': 'https://www.metro-magazine.com/rss'
     },
]
