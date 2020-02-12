import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.65.205.31", username="cisco",password="Lilies09", look_for_keys=False)
connection = ssh.invoke_shell()
connection.send("enable\n")
connection.send("Ansi_4GY\n")
connection.send("sh version\n\n")
time.sleep(1)
#print(stdout.readlines())
#print(stderr.readlines())
#list1 = stdout.readlines()
#output = [line.rstrip() for line in list1]
print(connection.recv(9999))
connection.close()
