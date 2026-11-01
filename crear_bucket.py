import boto3
import json

def lambda_handler(event, context):
    # Entrada: Recibimos el nombre del nuevo bucket desde el body
    # Nota: Usamos json.loads porque API Gateway envía el body como un string de texto
    body = json.loads(event.get('body', '{}')) if isinstance(event.get('body'), str) else event.get('body', {})
    nombre_bucket = body.get('bucket')
    
    if not nombre_bucket:
        return {
            'statusCode': 400,
            'message': 'Error: Debes proporcionar el parámetro "bucket" en el body.'
        }
        
    # Proceso
    s3 = boto3.client('s3')
    try:
        s3.create_bucket(Bucket=nombre_bucket)
        return {
            'statusCode': 200,
            'message': f'Bucket "{nombre_bucket}" creado exitosamente.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }

