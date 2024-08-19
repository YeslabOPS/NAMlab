import paramiko

local_file = "ops_demo.py"
remote_file = "auto_del_startup.py"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname="10.1.1.221",
            port=22,
            username="huaweiuser",
            password="Huawei123@")

sftp = ssh.open_sftp()
sftp.put(local_file, remote_file)

ssh.close()