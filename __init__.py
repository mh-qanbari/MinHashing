from FlajoletMartin import FlajoletMartin
from HW3ExcelManager import ExcelManager
from AlonMatiasSzegedy import AMS

if __name__ == '__main__':
    excel_mgr = ExcelManager("Data.xlsx")

    # """
    print "[PART1] : First part of exercise"
    # seller_names = set()
    fm = FlajoletMartin(L=32, hashes_count=50, hash_group_count=20)
    for seller in excel_mgr.getSellers():
        seller_ = seller.lower()
        # seller_names.add(seller_)
        fm.run(seller_)
    # print "Real value :", len(seller_names)
    print "Flajolet-Martin estimated value :", fm.getResult()
    print "[PART1]; ................................................. "
    # """

    # """
    print "[PART2] : Second part of exercise"
    ams = AMS(20, 5000)
    for goods, region in excel_mgr.getRegionsGoods():
        goods_ = goods.lower()
        region_ = region.lower()
        ams.run(goods_, region_)
    for region, moment2 in ams.getResult():
        print "Region :", region, "\tSecond moments :", moment2
    print "[PART2]; ................................................. "
    # """

    # """
    print "[PART3] : Third part of exercise"
    ams = AMS(20, 5000)
    for month, region, goods in excel_mgr.getRegionsGoodsbyMonth():
        goods_ = goods.lower()
        region_month = '-'.join([region.lower(), month])
        ams.run(goods_, region_month)
    region_month_moment2 = dict()
    for region_month, moment2 in ams.getResult():
        region, month = region_month.split('-')
        # if region not in region_month_moment2:
        #     if month not in region_month_moment2[region]:
        if region not in region_month_moment2:
            month_moment2 = {month: moment2}
            region_month_moment2[region] = month_moment2
        else:
            region_month_moment2[region][month] = moment2
    for region, month_moment2 in region_month_moment2.iteritems():
        print "Region :", region
        for month, moment2 in month_moment2.iteritems():
            print "\tMonth :", month, "\tSecondMoment :", moment2
    print "[PART3]; ................................................. "
    # """
