
import paramiko

key = paramiko.RSAKey.from_private_key_file('/home/developer/python-521.pem')

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname='13.58.34.110', username='ubuntu', pkey=key)

commands = [

    'sudo apt-get update -y',
    'sudo apt-get install python3-pip -y',

    'git clone https://github.com/magalbr/dashboard.git',

    'pip3 install -r dashboard/requirements.txt',
    'sudo python3 dashboard/app.py',

]

for command in commands:
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode(), stderr.read().decode())