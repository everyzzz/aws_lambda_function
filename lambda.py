import json
import os
import mercadopago

def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])   
    payment_data = {
        "token": event["token"],
        "installments": int(event["installments"]),
        "payment_method_id": event["payment_method_id"],
        "transaction_amount": int(event["transaction_amount"]),
        "payer": {
            "email": event["payer"]["email"],
            "identification": {
                "type": event["payer"]["identification"]["type"], 
                "number": event["payer"]["identification"]["number"]
            }
        }
    }

    payment_response = sdk.payment().create(payment_data)
    payment = payment_response["response"]
    return{
        "statusCode": 201,
        "body": payment,
        
    }