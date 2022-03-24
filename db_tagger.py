from urllib import response
import boto3


def tag_dbs(response_iterator):
    databases = []
    for db in response_iterator:
        db_instances = db["DBInstances"]
        for db_info in db_instances:
            databases.append(
                {
                    "db_arn": db_info["DBInstanceArn"],
                    "db_name": db_info["DBInstanceIdentifier"],
                }
            )
    return databases


def add_tags_to_resource(databases, client):
    try:
        for database in databases:
            client.add_tags_to_resource(
                ResourceName=database["db_arn"],
                Tags=[
                    {"Key": "Name", "Value": database["db_name"]},
                ],
            )

        return True
    except Exception as e:
        return e


def main():
    client = boto3.client("rds")
    paginator = client.get_paginator("describe_db_instances")
    response_iterator = paginator.paginate()
    var = tag_dbs(response_iterator)
    results = add_tags_to_resource(var, client)
    print(results)


main()
