# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AquariusItem(scrapy.Item):
    # 平台id
    platformId = scrapy.Field()
    # 平台名称
    platformName = scrapy.Field()
    # 成交量 0
    tradeVolume = scrapy.Field()
    # 投资人数 1
    investmentNumber = scrapy.Field()
    # 借款人数 2
    borrowNumber = scrapy.Field()
    # 平均利率 3
    averageInterestRate = scrapy.Field()
    # 平均借款期限 4
    averateBorrowTerm = scrapy.Field()
    # 借款标数 5
    bidNumber = scrapy.Field()
    # 注册资金 6
    registeredCapital = scrapy.Field()
    # 满标用时 7
    finishBidTime = scrapy.Field()
    # 累计待还金额 8
    unreturnedAmount = scrapy.Field()
    # 近30日资金净流入 9
    monthNetInflows = scrapy.Field()
    # 时间加权成交量 10
    timeWeightedVolume = scrapy.Field()
    # 未来60日待还 11
    returnInSixtyDays = scrapy.Field()
    # 前十大土豪待收金额占比 12
    topTenUncollectedRatio = scrapy.Field()
    # 人均投资金额 13
    averageInvestmentAmount = scrapy.Field()
    # 前十大借款人待还金额占比 14
    topTenUnreturnRatio = scrapy.Field()
    # 人均借款金额 15
    averageBorrowAmount = scrapy.Field()
    # 资金杠杆 16
    leverageFund = scrapy.Field()
    # 运营时间 17
    operationTime = scrapy.Field()
    # 时间
    datetime = scrapy.Field()

