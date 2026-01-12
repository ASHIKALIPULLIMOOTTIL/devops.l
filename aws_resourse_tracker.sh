#!/bin/bash

#ashk ali
#27-2-25
#aws resourse usage
#aws s3
#aws ec2
#aws lambda

#list s3 buckets
aws s3 ls

#list ec2 instances
aws ec2 describe-instances | jq '.Reservations[].Instances[].InstanceId'

#list lambda
aws lambda list-functions

#list iam user
aws iam list-users 

