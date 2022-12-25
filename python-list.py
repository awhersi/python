#create empty list
aws_list = []

#insert items into list
aws_list.append("Amazon EC2")
aws_list.append("Amazon RDS")
aws_list.append("Amazon S3")
aws_list.append("Amazon IAM")
aws_list.append("Amazon EBS")
aws_list.append("Amazon Lambda")
aws_list.append("Amazon EFS")
aws_list.append("Amazon CloudFront")
aws_list.append("Amazon SNS")
aws_list.append("Amazon VPC")

#print list and length of list
print(aws_list)
print(f"There are {len(aws_list)} items in this list")

#delete items from list
del aws_list[3]
aws_list.remove("Amazon SNS")

#print updated list and length of list
print(aws_list)
print(f"There are {len(aws_list)} items in this list")


