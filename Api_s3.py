
import requests
response = requests.get('https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json', auth=('user', 'pass'))
j_res=response.json()
ser_api=j_res['offers']['AmazonS3']['currentVersionUrl']
ser_response=requests.get('https://pricing.us-east-1.amazonaws.com'+ser_api)
#['AmazonRds']
ser_info=ser_response.json()
ser_catalouge=ser_info['products']
#print(rds_catalouge)
for i in ser_catalouge.keys():
     ser_p=ser_info['terms']['OnDemand'][i][ser_info['terms']['OnDemand'][i].keys()[0]]['priceDimensions'][ser_info['terms']['OnDemand'][i][ser_info['terms']['OnDemand'][i].keys()[0]]['priceDimensions'].keys()[0]]

     ser_cat=ser_catalouge[str(i)]['attributes']
     if 'storageClass' in ser_cat.keys() and ser_cat['storageClass']!='Tags' :
         print ser_cat
         # print(ser_cat['location'],ser_cat['storageClass'],ser_cat['volumeType'],ser_p['pricePerUnit'])

#      rds_p=rds_info['terms']['OnDemand'][i][rds_info['terms']['OnDemand'][i].keys()[0]]['priceDimensions'][rds_info['terms']['OnDemand'][i][rds_info['terms']['OnDemand'][i].keys()[0]]['priceDimensions'].keys()[0]]
