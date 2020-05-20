# async, will return immediately and won't wait crawl finished
import inspect

from flask import json
from scrapy.commands import settings
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from spiders.review_spi import ReviewSpiSpider

from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)
lnk = ''

@app.route('/hg')
def crawl(self):

    crawlSettings = {}

    configure_logging()

    s = get_project_settings()
    for a in inspect.getmembers(settings):
        if not a[0].startswith('_'):
            # Ignores methods
            if not inspect.ismethod(a[1]):
                s.update({a[0]: a[1]})

    # if you want to use CrawlerRunner, when you want to integrate Scrapy to existing Twisted Application
    runner = CrawlerRunner(s)
    d = runner.crawl(ReviewSpiSpider, crawlSettings)
    d.addCallback(return_spider_output)
    return d
def return_spider_output(output):
    return json.dumps([list(item) for item in output])


