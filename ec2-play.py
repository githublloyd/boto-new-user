import boto3


iam = boto3.resource('iam')
iam_keys = boto3.client('iam')
group_list = boto3.client('iam')
attach_group = boto3.client('iam')
grp = boto3.client("iam")
device = boto.client("iam")
arn = boto.client("iam")
auth1 = boto.client("iam")
auth2 = boto.client("iam")

######################################################################
user = raw_input("Please enter your e-user address: ")
response = iam.create_user(UserName=user)
######################################################################

######################################################################
access = raw_input("Do you require programmatic access?(y/n): ") 
if access == "y":
        iam_keys.create_access_key(UserName=user)
        print("Make sure AWSCLI is installed on your machine")
elif access == "n":
        print("Console access only")
######################################################################

######################################################################
list = group_list.list_groups()
groups = list['Groups']
index = 1

for group in groups:
        print("%d: %s" % (index, group["GroupName"]))
        index +=1

option = int(input("Please pick a Group number: "))
#arn = groups[option-1]["Arn"]
#print("You selected option %d: %s" % (option, arn))

group_name = groups[option-1]["GroupName"]

final = grp.add_user_to_group(GroupName=group_name, UserName=user)

print("User has been added to Group %s" % (group_name))
######################################################################

######################################################################
