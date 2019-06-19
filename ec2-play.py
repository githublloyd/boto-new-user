import boto3


iam = boto3.resource('iam')
iam_keys = boto3.resource('iam')
group_list = boto3.client('iam')
attach_group = boto3.client('iam')



mail = raw_input("Please enter your e-mail address: ")
response = iam.create_user(UserName=mail)


prog = raw_input("Do you require programmatic access?(y/n): ") 
if prog == "y":
        iam_keys.create_access_key(UserName=mail)
        print("Make sure awscli is installed on your machine")
elif prog == "n":
        print("Console access only")


list = group_list.list_groups()
groups = list['Groups']
print(groups)
index = 1

for group in groups:
        print("%d: %s" % (index, group["GroupName"]))
        index +=1

option = int(input("Please pick a Group number: "))
arn = groups[option-1]["Arn"]
print("You selected option %d: %s" % (option, arn))