import logging
import boto3
from botocore.exceptions import ClientError
from urllib.parse import urlparse
import pandas as pd

def get_url(url, sep):
    url=urlparse(url)
    if url.scheme=="s3":
        client = boto3.client('s3')
        obj = client.get_object(Bucket=url.netloc, Key=url.path[1:])
        return pd.read_csv(obj['Body'],sep=sep)
    else:
        return pd.read_csv(url,sep=sep)

if __name__=="__main__":
    df=get_url("s3://apexon-model-registry/winequality-red.csv", sep=";")
    print(df.describe)