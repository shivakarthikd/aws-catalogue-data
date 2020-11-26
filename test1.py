
import boto3
import urllib3
import json


def lambda_handler(event, context):
    # TODO implement

    http = urllib3.PoolManager()
    response = http.request('GET', 'https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json')
    j_res = json.loads(response.data.decode('utf-8'))
    for j in j_res['offers'].keys():
        ser_api = j_res['offers'][j]['currentVersionUrl']
        ser_response = http.request('GET', 'https://pricing.us-east-1.amazonaws.com' + ser_api)

        ser_info = json.loads(ser_response.data.decode('utf-8'))
        rds_catalouge = dict(rds_info['products'])
        tmp_file_path = "/tmp/+"+j+"servicecat.txt"
        f = open(tmp_file_path, 'w')
        for i in rds_catalouge.keys():
            rds_p = rds_info['terms']['OnDemand'][i][list(rds_info['terms']['OnDemand'][i].keys())[0]]['priceDimensions'][
                list(rds_info['terms']['OnDemand'][i][list(rds_info['terms']['OnDemand'][i].keys())[0]][
                         'priceDimensions'].keys())[0]]
            rds_cat = dict(rds_catalouge[str(i)]['attributes'])
            if 'storageClass' in rds_cat.keys() and rds_cat['storageClass'] != 'Tags':
                l1 = str(rds_cat['location']) + str(rds_cat['storageClass']) + str(rds_cat['volumeType']) + str(
                    rds_p['pricePerUnit'])

            # file.write(l1+'\n')
                f.write(l1 + '\n')
        f.close()
        s3 = boto3.resource('s3')
    # response = s3_client.upload_file(tmp_file_path, servicecatelouge, obj1)
        s3.Bucket('servicecatelouge').upload_file(tmp_file_path, 'servicecat.txt')


