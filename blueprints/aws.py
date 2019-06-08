import boto3

ec2 = boto3.resource('ec2', 'us-east-2a')

#config = {
#    'GroupŃame': 'GrupoScript',
#    'Description': 'Criado por Script'
#}
#security_group = ec2.create_security_group(**config)

security_groups = ec2.security_groups.all()
for group in security_groups:
    print(group.group_name, group.group_id)

instances = ec2.instances.all()
for instance in instances:
    print(instance.instance_id)
    print(instance.instance_type)


new_instance = ec2.create_instances(
    ImageId='ami'
)