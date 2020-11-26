
from api_url import j_res
import requests

f = open('us-east-1-file.txt', 'wb')
for i in j_res['offers'].keys():
    ser_api=j_res['offers']['AmazonEC2']['currentRegionIndexUrl']

    '''  fetches the list of endpoints of all services from all regions seperately '''
    ser_response=requests.get('https://pricing.us-east-1.amazonaws.com'+ser_api)

    ser_info=ser_response.json()
    ser_catalouge=ser_info['regions']
    ser_catalouge_reg={}
    ser_info_reg={}
    if 'us-east-1' in ser_catalouge.keys():
        ser_reg_api=ser_catalouge['us-east-1']['currentVersionUrl']
        ser_response_region = requests.get('https://pricing.us-east-1.amazonaws.com' + ser_reg_api)
       # print(rds_response_region.json())
        ser_info_reg = ser_response_region.json()
        ser_catalouge_reg = ser_info_reg['products']
        print ser_catalouge_reg
    for i in ser_info_reg['terms'].keys():

         ser_p=ser_info_reg['terms']['OnDemand'][i][ser_info_reg['terms']['OnDemand'][i].keys()[0]]['priceDimensions'][ser_info_reg['terms']['OnDemand'][i][ser_info_reg['terms']['OnDemand'][i].keys()[0]]['priceDimensions'].keys()[0]]

         ser_cat=ser_catalouge_reg[str(i)]['attributes']
     # if 'storageClass' in rds_cat.keys() and rds_cat['storageClass']!='Tags' :
     #     print(rds_cat['location'],rds_cat['storageClass'],rds_cat['volumeType'],rds_p['pricePerUnit'])
         #print(rds_cat,rds_p['pricePerUnit'])

#      rds_p=rds_info['terms']['OnDemand'][i][rds_info['terms']['OnDemand'][i].keys()[0]]['priceDimensions'][rds_info['terms']['OnDemand'][i][rds_info['terms']['OnDemand'][i].keys()[0]]['priceDimensions'].keys()[0]]

         f.write(str(ser_cat)+str(ser_p['pricePerUnit'])+'\n')

f.close()