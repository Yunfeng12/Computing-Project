import nmap
import sys
import paramiko
import pandas as pd
import re



#targeting_host that provide to Nmap to detect expored ports.
#the port is for ssh port of targeting host
#username is Linux account
#the password of root is for login via the ssh

targeting_host = input('Please typing the targeting host IP that you want to scan:')
#host = '52.221.235.236'
port = 22
username = "root"
#password = "Test@test4321"
password = input('Please typing the password of root account of the targeting host:')


#the nmap_scan that will scan the targetiing host and discover active ports exposed to oudside. and then produce a dic of port.
def nmap_scan(host):
    nm = nmap.PortScanner()
    nm.scan(host, '80-300') 
    port_list = list(nm[host]['tcp'].keys()) #will draw all TCP port that exposed to outside
    
    if port_list:
       print('the {0} exposed those ports {1} to outside'.format(host,port_list))
       return port_list
    else:
       print('the targeting_host is inactiving or no any port exposed to outside and quit the program')
     #break        if the targeting host is closed or no any exposed port, and then quit the program
     # sys.exit()


#sshclient_execmd is for remote ssh and running command
def sshclient_execmd(execmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)   #log in the host via ssh
    stdin, stdout, stderr = ssh.exec_command(execmd)
    command_result = stdout.read().decode('utf-8')
#   print(command_result)
    return command_result

#sshclent_execmd_stderr is for remote ssh and running command, compare with sshclient-execmd, the difference is that 
#we need the value from stdour, not stdout
def sshclient_execmd_stderr(execmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)   #log in the host via ssh
    stdin,stdout, stderr = ssh.exec_command(execmd)
    command_result = stderr.read().decode('utf-8')
#   print(command_result)
    return command_result

#command() function is to query port in the remote server, and get server_name and server_version
def command(): 
    df = pd.DataFrame(columns=['Host','Port','Server','Version'])
    port_list = nmap_scan(host)
#   print(port_list)

    i = 0 
    for i in range(len(port_list)):
        port = port_list[i]
        #command_1 is to query port and get process of server
        command_1 = "netstat -lntup|grep 0.0.0.0:%d|grep tcp | awk '{print $7}'| grep   -o  ^[0-9]*"%(port)
        process = sshclient_execmd(command_1)
        process = int(process)
 
        #command_2 is for getting directory of server depends on process of server
        command_2 = "ls -l /proc/%d/exe | awk '{print $11}'"%(process)
        index_server = sshclient_execmd(command_2)
        index_server = ''.join(index_server)

        #command_3 is for getting server name and version by typing command '**server_directory**   -v'
        index_server = index_server + "-v"
        command_3 = re.sub('\s+'," ",index_server)
        #print(command_3)
        result = sshclient_execmd_stderr(command_3)
        
        #default_server_list is kind of server name database. the particulary port will be labeled server_name
        # if result match one of default_server_list
        default_server_list = ['nginx', 'mysql', 'tomcat', 'apache']
        s = 0
        server_name = "Unknow"
        server_version = "Unknow"
        for server in default_server_list:
            n = re.search(server,result)
            if n:
                server_name = server
                #print(server_name)
                server_version = re.search(r'[0-9]\.[0-9]*\.[0-9]*',result)
                if server_version:
                   server_version = server_version.group(0)
        df = df.append({'Host': host,'Port':port,'Server':server_name,'Version': server_version},ignore_index=True)
    return df
    

def data():
       df = command()
       print(df)
       df.to_csv('nginx.csv', index=False)     
       print("Finished scanning completely, please view the file nginx.csv")


if __name__ == '__main__':
    data()

