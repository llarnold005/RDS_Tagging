from urllib import response
import boto3



def tag_dbs(response_iterator):
    db_arn = []
    for db in response_iterator:
        db_instances = db['DBInstances']
        for db_info in db_instances:
            db_arn.append(db_info['DBInstanceArn'])
    return(db_arn)
    
def add_tags_to_resource(db_arn, client):
    try:
        for arn in db_arn:
            client.add_tags_to_resource(
        ResourceName = arn,
        Tags = [
            {
                'Key': 'Test',
                'Value': 'Test'
            },
        ])
        
        return True 
    except Exception as e:
        return(e)
        
        

def main():
    client = boto3.client('rds')
    paginator = client.get_paginator('describe_db_instances')
    response_iterator = paginator.paginate()  
    var = tag_dbs(response_iterator)
    results = add_tags_to_resource(var, client)
    print(results)
main()
