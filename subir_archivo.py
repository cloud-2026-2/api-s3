import boto3
import json

def lambda_handler(event, context):
    # Entrada dinámica total
    body = json.loads(event.get('body', '{}')) if isinstance(event.get('body'), str) else event.get('body', {})
    nombre_bucket = body.get('bucket')
    nombre_carpeta = body.get('directorio')
    nombre_archivo = body.get('archivo')      # Ej: "nota.txt"
    contenido = body.get('contenido', '')      # El texto que irá dentro del archivo
    
    if not nombre_bucket or not nombre_carpeta or not nombre_archivo:
        return {
            'statusCode': 400,
            'message': 'Error: Debes proporcionar "bucket", "directorio" y "archivo".'
        }
    
    # Formamos la ruta completa (Key) dentro de S3
    if not nombre_carpeta.endswith('/'):
        nombre_carpeta += '/'
    ruta_final_s3 = f"{nombre_carpeta}{nombre_archivo}"
        
    # Proceso
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=nombre_bucket, Key=ruta_final_s3, Body=contenido)
        return {
            'statusCode': 200,
            'bucket': nombre_bucket,
            'ruta': ruta_final_s3,
            'message': 'Archivo subido exitosamente.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'error': str(e)
        }
