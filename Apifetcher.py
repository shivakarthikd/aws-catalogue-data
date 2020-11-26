import boto3
import json
#import awspricing
#
client=boto3.client('ec2')
client2 = boto3.client('pricing')

response = client.describe_instance_types(
    Filters = [
        {
            'Name' : 'instance-type',
            'Values':[ 't3.large' ]
        }
    ]
)
price=[]
typelist=[]
for i in response['InstanceTypes']:
    typelist.append(i['InstanceType'])

for i in typelist:
    response2 = client2.get_products(
        ServiceCode='AmazonEc2',
        Filters=[
            {
                'Type': 'TERM_MATCH',
                'Field': 'InstanceType',
                'Value': i
            },

        ],
    )
    if len(response2['PriceList'])!=0:
        res=response2['PriceList'][3]
        val=json.loads(res)
        price.append(val['terms']['OnDemand'][val['terms']['OnDemand'].keys()[0]]['priceDimensions'][val['terms']['OnDemand'][val['terms']['OnDemand'].keys()[0]]['priceDimensions'].keys()[0]]['pricePerUnit']['USD'])
    else:
        price.append('0.0000')

o=0
info=response['InstanceTypes']
print(' InstanceType ',' memory ','  VCpus  ','  PricePerUnit ')
for i in info:
    if i['MemoryInfo']['SizeInMiB'] > 1024:
        mem=i['MemoryInfo']['SizeInMiB']/1024
    else:
        mem=i['MemoryInfo']['SizeInMiB']


    print(i['InstanceType'],mem,i['VCpuInfo']['DefaultVCpus'],str(price[o]))
    o=o+1
