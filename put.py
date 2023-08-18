import boto3
def upload_csv_to_s3(bucket_name,s3_key,file_name):
    s3=boto3.client('s3')
    try:
        s3.upload_file(file_name,bucket_name,s3_key)
        print("File uploaded Successfully From S3")
    except FileNotFoundError:
        print("The File Was Not Found")
    except Exception as e:
        print(f"An Error Occurred:{str(e)}")

bucket_name='revision11' 
file_name='prem.py'
s3_key='Put.py'

upload_csv_to_s3(bucket_name,s3_key,file_name)