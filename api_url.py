import requests
import logging

'''To get the reponse from the AWS URL'''
try:
    response = requests.get('https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json')
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("SUCCESS " + str(response.status_code))
    '''Convert the respose to JSON format'''
    j_res=response.json()
except requests.exceptions as e :
    logging.exception("Error at URL or END Point Declaration" + e )