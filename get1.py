import boto3
def get_csv_from_s3(bucket_name,s3_key,file_name):
	s3=boto3.client('s3')
	try:
		s3.download_file(bucket_name,s3_key,file_name)
		print("File Downloaded Successfully From S3")
	except Exception as e:
		print(f"An Error Occurred:{str(e)}")

bucket_name='revision11' 
file_name='prem.py'
s3_key='ProjectRev.py'

get_csv_from_s3(bucket_name,s3_key,file_name)