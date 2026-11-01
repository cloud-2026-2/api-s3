import boto3
import json

def lambda_handler(event, context):
    # Entrada dinámica: ¿En qué bucket y qué nombre de carpeta?
    body = json.loads(event.get('body', '{}')) if isinstance(event.get('body'), str) else event.get('body', {})
    nombre_bucket = body.get('bucket')
    nombre_carpeta = body.get('directorio')
    
    if not nombre_bucket or not nombre_carpeta:
        return {
            'statusCode': 400,
            'message': 'Error: Debes proporcionar "bucket" y "directorio" en el body.'
        }
    
    # Nos aseguramos de que el nombre de la carpeta termine en "/"
    if not nombre_carpeta.endswith('/'):
        nombre_carpeta += '/'
        
    # Proceso
    s3 = boto3.client('s3')
    try:
        # put_object con Body vacíocrea la carpeta simulada
        s3.put_object(Bucket=nombre_bucket, Key=nombre_carpeta, Body='')
        return {
            'statusCode': 200,
            'bucket': nombre_bucket,
            'message': f'Directorio "{nombre_carpeta}" creado exitosamente.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }

