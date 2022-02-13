# Final Year Project/PC Scanner
To test PC Scanner that need three parts
1. To set up two Linux
2. Installing Nginx
3. Installing PC Scanner


## To set up two Linux
First, prepare your Linux server* with a fresh install of CentOS, Ubuntu or Redhat, depends what you like.
In this case, I choose AWS [https://aws.amazon.com/] as my server. and then the few tings have to do 
1. IPv4 Firewall. I suggest open all ports from 0 to 65334
2. Start an editor, vi or whatever, and load the sshd config. Allow root login and password authentication by commenting/uncommenting: 
   > sudo vi /etc/ssh/sshd_config.    PermitRootLogin yes  PasswordAuthentication yes

## Installing Nginx


  

