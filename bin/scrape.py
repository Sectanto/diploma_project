def scrapeData(filename='', savedirectory='datasets/'):

    import os
    import scrapy
    from scrapy.crawler import CrawlerProcess
    import re

    class QuotesSpider(scrapy.Spider):
        name = "quotes"

        def start_requests(self):
            urls = [
                'file:///' + filename,
                # 'http://quotes.toscrape.com/page/1/',
                # 'http://quotes.toscrape.com/page/2/',
            ]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)


        def parse(self, response):

            yield { 'h1': response.css('div.article-content').css('h1::text').get() }
            # yield { 'h1': response.css('div.article-content').css('address').get() }

            authors = response.css('div.article-content')
            copy = []
            for author in authors.css('address').css('a::text').getall():
                if(not author in copy):
                    copy.append(author)
                    yield { 'authors':  author }

            timestamp = response.css('time.article-timestamp::text').get()
            yield { 'date': timestamp }
            
            for div in response.css('div.middle-column'):
                
                
                for plaintexts in div.css('p').getall():    
                    p = re.compile(r'<.*?>').sub('', plaintexts)
                    p = re.sub(r'[\W_]+', ' ', p)

                    yield {
                        'p': p,
                        # 'p': plaintexts
                    }
            # for quote in response.css('div'):
            #     yield {
            #         'div': quote.css('div.middle-column').get(),
            #         'author': quote.css('small.author::text').get(),
            #         'tags': quote.css('div.tags a.tag::text').getall(),
            #     }


   

    savefilename = os.path.splitext(filename)[0]
    ext = '.json'
    savefilename += ext

    savefilename = savefilename.split('\\')[-1]
    savefilename = savedirectory + savefilename
    
    process = CrawlerProcess(settings={
        "FEEDS": {
            savefilename: {"format": "json"},
        },
    })
    os.remove(savefilename)
    
    process.crawl(QuotesSpider)
    process.start() 

    

scrapeData("C:\\Users\\zssva\\Desktop\\thesis_cake\\build\\entry.html")
# scrapeData("C:\\Users\\zssva\\Desktop\\thesis_cake\\build\\entry2.html")