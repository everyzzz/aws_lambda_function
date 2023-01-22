import json
import os
import mercadopago

def lambda_handler(event, context):
    #initialize sdk
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN_PRO"])
    #bodyGet = json.loads(event["body"])
    
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
    

    if payment["status"] == 400:
        return {
            "ok": "false",
            "body": payment
        }
    else:
        if payment["status"] == "approved":
            return{
                "ok": "true",
                "statusCode": 201,
                "body": payment,
                "id": payment["id"],
                "status": payment["status"],
                "status_detail": payment["status_detail"]  
            }
        else:
            return{
                "ok": "false",
                "body": payment,
                "status": payment["status"]
            }