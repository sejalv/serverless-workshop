import json, os
import stripe
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['STRIPE_CHARGE_TABLE'])
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

def handler(event, context):
	print('createCharge');
	print(event);
	requestBody = json.loads(event['body'])
	#requestBody = event['body']
	print(requestBody);
	
	token = requestBody['token']['id'];
	amount = requestBody['charge']['amount'];
	currency = requestBody['charge']['currency'];
	
	charge = stripe.Charge.create(
		amount=amount,
		currency=currency,
		description="Serverless Stripe Test charge",
		source=token
	)
	
	timestamp = str(datetime.utcnow().timestamp())

	'''
	charge = stripe.Charge.create(
	  amount=2000,
	  currency="eur",
	  source="tok_mastercard",
	  description="Charge for jenny.rosen@example.com",
	)
	'''

	if charge:
		response = {
		        "statusCode": 200,	# success
		        "headers": {
		          "Access-Control-Allow-Origin": "*",
		          #"Content-Type": "application/json",
		        },
		        "body": json.dumps({
		          "message": "Charge processed succesfully!",
		          "charge": charge,
		        })
		    }
		    
		S = {
		    'amount': amount,
		    'currency': currency,
		    'createdAt': timestamp,
		    'updatedAt': timestamp,
		}
	        
		item = {
	        'id': token,
	        'S': S,
		}

		# write the todo to the database
		table.put_item(Item=item)

		return response

	else:
		response = {
		        "statusCode": 500,	# failure

		        headers: {
		          "Access-Control-Allow-Origin": "*",
		          #"Content-Type": "application/json",
		        },
		        "body": json.dumps({
		          error: err.message,
		        })
		    }
		return response