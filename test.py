
from api_url import j_res
import requests
import logging
from uploadtodb import uploadtodb
# f = open('us-east-1-file.txt', 'wb')
s_code='AmazonEC2'
for s_code in j_res['offers'].keys():
    ser_api=j_res['offers'][s_code]['currentRegionIndexUrl']

    '''  fetches the list of endpoints of all  API's region wise'''
    ser_response = requests.get('https://pricing.us-east-1.amazonaws.com'+ser_api)

    ser_info=ser_response.json()
    ser_catalouge = ser_info['regions']
    ser_catalouge_reg = {}
    ser_info_reg = {}
    if 'us-east-1' in ser_catalouge.keys():
        ser_reg_api = ser_catalouge['us-east-1']['currentVersionUrl']
        '''API end point to fetch region wise services list '''
        ser_response_region = requests.get('https://pricing.us-east-1.amazonaws.com' + ser_reg_api)

        ser_info_reg = ser_response_region.json()
        ser_catalouge_reg = ser_info_reg['products']
    if 'terms' not in ser_info_reg.keys():
        logging.exception('service Pricing not exists: '+s_code)
    else:
        new_cat={}
        for i in ser_info_reg['terms']['OnDemand'].keys():

             ser_p = ser_info_reg['terms']['OnDemand'][i][ser_info_reg['terms']['OnDemand'][i].keys()[0]]['priceDimensions'][ser_info_reg['terms']['OnDemand'][i][ser_info_reg['terms']['OnDemand'][i].keys()[0]]['priceDimensions'].keys()[0]]

             ser_cat = ser_catalouge_reg[str(i)]['attributes']
             diffKeys = set(ser_cat.keys()) - set(new_cat.keys())
             #uploadtodb(ser_cat,s_code,diffKeys)
             new_cat=ser_cat
             print new_cat

             # logging.makeLogRecord('success')
             # if 'storageClass' in rds_cat.keys() and rds_cat['storageClass']!='Tags' :
             #     print(rds_cat['location'],rds_cat['storageClass'],rds_cat['volumeType'],rds_p['pricePerUnit'])


        #      rds_p=rds_info['terms']['OnDemand'][i][rds_info['terms']['OnDemand'][i].keys()[0]]['priceDimensions'][rds_info['terms']['OnDemand'][i][rds_info['terms']['OnDemand'][i].keys()[0]]['priceDimensions'].keys()[0]]
#
#              f.write(str(rds_cat)+str(rds_p['pricePerUnit'])+'\n')
# f.write(s_code+'\n')
# f.close()
