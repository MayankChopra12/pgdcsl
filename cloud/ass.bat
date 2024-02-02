set /p FileName=Enter the name of the file to upload:
set /p BucketName=Enter the name of the S3 bucket:

aws s3 cp "%FileName%" "s3://%BucketName%/"

set /p CopyDestination=Enter the destination path to copy the file to:

aws s3 cp "s3://%BucketName%/%FileName%" "s3://%CopyDestination%/"