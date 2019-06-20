import boto3


iam = boto3.resource('iam')
iam_keys = boto3.client('iam')
group_list = boto3.client('iam')
attach_group = boto3.client('iam')
grp = boto3.client("iam")
device = boto3.client("iam")
#arn = boto3.client("iam")
#auth1 = boto3.client("iam")
#auth2 = boto3.client("iam")

######################################################################
user = raw_input("Please enter your e-user address: ")
response = iam.create_user(UserName=user)

print("MFA is compulsory in this account, please complete the following steps.")

verify = raw_input("Please enter your email address again:")
if verify != user:
        print("Email addresses do not match, exiting")
        exit()
elif verify == user:
        verify == verify#rep = device.enable_mfa_device(UserName=verify)

serial = raw_input("Please enter your exact device ARN serial number (arn:aws:iam::accntno:user/emailadd) ")
#reps = arn.enable_mfa_device(SerialNumber=serial)

code1 = raw_input("Please enter the first code: ")
#repso = auth1.enable_mfa_device(AuthenticationCode1=code1)

code2 = raw_input("Please enter the second code: ")
#repson = auth2 .enable_mfa_device(AuthenticationCode2=code2)

response = device.enable_mfa_device(UserName=verify, SerialNumber=serial, AuthenticationCode1=code1, AuthenticationCode2=code2)