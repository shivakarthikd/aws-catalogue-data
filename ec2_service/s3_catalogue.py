from api_url import j_res
import requests
import logging
from upload_to_mysql import uploadtodb
#set your log level
logging.basicConfig(level=logging.ERROR)

service_name='AmazonS3'
service_list = j_res['offers'].keys()
curr_region_endpoint = j_res['offers'][service_name]['currentRegionIndexUrl']
regionwise_url_list_response = requests.get('https://pricing.us-east-1.amazonaws.com'+curr_region_endpoint)
''' List Of all the Regions'''
#region_list = ser_response.json()['regions'].keys()
region_list = ['us-east-1']
regionwise_url_list_response=regionwise_url_list_response.json()
#print(regionwise_url_list_response)
for region in region_list:
    curr_version_endpoint=regionwise_url_list_response['regions'][region]['currentVersionUrl']
    print(curr_version_endpoint)
    service_res=requests.get('https://pricing.us-east-1.amazonaws.com'+curr_version_endpoint)
    service_res=service_res.json()


######### pricing #####
    pkeys=service_res['products'].keys()
    new_cat = {}
    ser_cat={}
    for i in pkeys:
         if i in service_res['terms']['OnDemand'].keys():
            ser_p=service_res['terms']['OnDemand'][i][service_res['terms']['OnDemand'][i].keys()[0]]['priceDimensions'][service_res['terms']['OnDemand'][i][service_res['terms']['OnDemand'][i].keys()[0]]['priceDimensions'].keys()[0]]
            if float(ser_p['pricePerUnit']['USD']) > float('0.00'):
                ser_cat= service_res['products'][i]['attributes']
                # ser_cat['storageClass'] = service_res['products'][i]['attributes']['storageClass']
                # ser_cat['volumeType'] =service_res['products'][i]['attributes']['volumeType']
                # ser_cat['pricePerunit'] = ser_p['pricePerUnit']['USD']

                print(ser_cat)
                diffKeys = set(ser_cat.keys()) - set(new_cat.keys())
                uploadtodb(ser_cat,service_name.lower(),diffKeys)
                new_cat=ser_cat
             # print(ser_cat['instanceType'],ser_cat['vcpu'],ser_cat['memory'],ser_cat['databaseEngine'],ser_p['pricePerUnit'])
         #print(rds_p)