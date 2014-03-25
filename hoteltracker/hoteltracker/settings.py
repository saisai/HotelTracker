# Scrapy settings for hoteltracker project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'hoteltracker'

SPIDER_MODULES = ['hoteltracker.spiders']
NEWSPIDER_MODULE = 'hoteltracker.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hoteltracker (+http://www.yourdomain.com)'