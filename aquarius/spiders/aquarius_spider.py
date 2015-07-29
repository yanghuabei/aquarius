import scrapy
import re
import datetime as date
import urlparse

from aquarius.items import AquariusItem

class AquariusSpider(scrapy.Spider):
    name = "aquarius"
    start_urls = []
    urlPrefix = 'http://shuju.wangdaizhijia.com/indexs-0-0-0-0-0-0.html'
    startTime = date.date(2013, 11, 8)
    endTime = date.date(2014, 11, 7)

    def __init__(self):
        currentTime = self.startTime
        timeDelta = date.timedelta(days=1)
        while(currentTime <= self.endTime):
            strTime = currentTime.strftime('%Y-%m-%d')
            urlStr = self.urlPrefix + '?startTime=' + strTime + '&endTime=' + strTime
            self.start_urls.append(urlStr)
            currentTime += timeDelta

        print self.start_urls



    def parse(self, response):
        items = []
        # get all rows
        rows = response.xpath('//table[@class="ph_tab ph_tab1"]/tr')

        # iterate all row
        for i, row in enumerate(rows):
            # drop title
            if i == 0:
                continue

            # start to extract data
            item = self.extractRowData(row)
            # add datetime
            datetime = self.getURLDateTime(response.url)
            item['datetime'] = datetime
            items.append(item)

        return items

    def extractRowData(self, row):
        item = AquariusItem()
        cells = row.xpath('td')
        # get platformId
        linkHref = cells[1].css('a::attr(href)').extract()[0]
        item['platformId'] = self.getInt(linkHref)
        # get platformName
        item['platformName'] = cells[1].css('a::text').extract()[0]
        # get tradeVolume
        cellContent = row.css('td.td0::text').extract()[0]
        tradeVolume = self.getFloat(cellContent)
        tradeVolume = tradeVolume * 10000
        item['tradeVolume'] = tradeVolume
        # get investmentNumber
        cellContent = row.css('td.td1::text').extract()[0]
        item['investmentNumber'] = self.getInt(cellContent)
        # get borrowNumber
        cellContent = row.css('td.td2::text').extract()[0]
        item['borrowNumber'] = self.getInt(cellContent)
        # get averageInterestRate
        cellContent = row.css('td.td3::text').extract()[0]
        item['averageInterestRate'] = self.getFloat(cellContent) * 0.01
        # get averateBorrowTerm
        cellContent = row.css('td.td4::text').extract()[0]
        item['averateBorrowTerm'] = self.getFloat(cellContent)
        # get bidNumber
        cellContent = row.css('td.td5::text').extract()[0]
        item['bidNumber'] = self.getInt(cellContent)
        # get registeredCapital
        cellContent = row.css('td.td6::text').extract()[0]
        item['registeredCapital'] = self.getFloat(cellContent) * 10000

        # get finishBidTime
        cellContent = row.css('td.td7::text').extract()[0]
        item['finishBidTime'] = self.getFloat(cellContent)

        # get unreturnedAmount
        cellContent = row.css('td.td8::text').extract()[0]
        item['unreturnedAmount'] = self.getFloat(cellContent) * 10000

        # get monthNetInflows
        cellContent = row.css('td.td9::text').extract()[0]
        item['monthNetInflows'] = self.getFloat(cellContent) * 10000

        # get timeWeightedVolume
        cellContent = row.css('td.td10::text').extract()[0]
        item['timeWeightedVolume'] = self.getFloat(cellContent) * 10000

        # get returnInSixtyDays
        cellContent = row.css('td.td11::text').extract()[0]
        item['returnInSixtyDays'] = self.getFloat(cellContent) * 10000

        # get topTenUncollectedRatio
        cellContent = row.css('td.td12::text').extract()[0]
        item['topTenUncollectedRatio'] = self.getFloat(cellContent) * 0.01

        # get averageInvestmentAmount
        cellContent = row.css('td.td13::text').extract()[0]
        item['averageInvestmentAmount'] = self.getFloat(cellContent) * 10000

        # get topTenUnreturnRatio
        cellContent = row.css('td.td14::text').extract()[0]
        item['topTenUnreturnRatio'] = self.getFloat(cellContent) * 0.01

        # get averageBorrowAmount
        cellContent = row.css('td.td15::text').extract()[0]
        item['averageBorrowAmount'] = self.getFloat(cellContent) * 10000

        # get leverageFund
        cellContent = row.css('td.td16::text').extract()[0]
        item['leverageFund'] = self.getFloat(cellContent)

        # get operationTime
        cellContent = row.css('td.td17::text').extract()[0]
        item['operationTime'] = self.getOperationTime(cellContent)
        # print item

        return item

    def getInt(self, str):
        str = str.replace(',', '')
        intPattern = re.compile(r'\d+')
        match = intPattern.search(str)
        if match:
            return int(match.group())
        else:
            return 0

    def getFloat(self, str):
        str = str.replace(',', '')
        floatPattern = re.compile(r'\d+\.\d*')
        match = floatPattern.search(str)
        if match:
            return float(match.group())
        else:
            return 0

    def getOperationTime(self, str):
        year = 0
        month = 0

        numberPattern = re.compile(r'\d+')
        numbers = numberPattern.findall(str)
        if len(numbers) > 1:
            year = int(numbers[0])
            month = int(numbers[1])
        elif len(numbers) > 0:
            month = int(numbers[0])
        return year * 12 + month

    def getURLDateTime(self, url):
        query = urlparse.urlparse(url)[4]
        querys = query.split('&')
        startTime = date.datetime.strptime(querys[0].split('=')[1], '%Y-%m-%d')
        return startTime



