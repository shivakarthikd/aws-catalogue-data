
import requests
response = requests.get('https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json', auth=('user', 'pass'))
j_res=response.json()
ser_api=j_res['offers']['AmazonRDS']['currentVersionUrl']
ser_response=requests.get('https://pricing.us-east-1.amazonaws.com'+ser_api)
#['AmazonRds']
ser_info=ser_response.json()


ser_catalouge=ser_info['products']
# for i in rds_catalouge.keys():
#     rds_cat=rds_catalouge[str(i)]['attributes']
#    # print(rds_cat.keys())
#     if 'instanceType' in rds_cat.keys() :
#         print(rds_cat['instanceType'],rds_cat['vcpu'],rds_cat['memory'],rds_cat['databaseEngine'])


######### pricing #####

pkeys=ser_info['terms']['OnDemand'].keys()

for i in pkeys:

     ser_p=ser_info['terms']['OnDemand'][i][ser_info['terms']['OnDemand'][i].keys()[0]]['priceDimensions'][ser_info['terms']['OnDemand'][i][ser_info['terms']['OnDemand'][i].keys()[0]]['priceDimensions'].keys()[0]]
     ser_cat = ser_catalouge[str(i)]['attributes']
     if 'instanceType' in ser_cat.keys() :
          print(ser_cat['instanceType'],ser_cat['vcpu'],ser_cat['memory'],ser_cat['databaseEngine'],ser_p['pricePerUnit'])
     #print(rds_p)
