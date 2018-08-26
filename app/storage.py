from app import cloud_storage_client

def upload_to_bucket(source_filename, destination_filename, bucket_name=None):
	if not bucket_name:
		bucket_name = list(cloud_storage_client.list_buckets())[0].__dict__['name']

	bucket = cloud_storage_client.get_bucket(bucket_name)
	blob = bucket.blob(destination_filename)

	blob.upload_from_filename(source_filename)

def download_from_bucket(source_filename, destination_filename, bucket_name=None):
	if not bucket_name:
		bucket_name = list(cloud_storage_client.list_buckets())[0].__dict__['name']

	bucket = cloud_storage_client.get_bucket(bucket_name)
	blob = bucket.blob(source_filename)

	blob.download_to_filename(destination_filename)