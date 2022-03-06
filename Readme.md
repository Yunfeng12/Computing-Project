# Final Year Project/PC Scanner
To test PC Scanner that need three parts
1. To set up two Linux
2. Installing Nginx
3. Installing PC Scanner and Nmap
4. Running Nmap
5.	Running PCscanner



## To set up two Linux
First, prepare your Linux server* with a fresh install of CentOS, Ubuntu or Redhat, depends what you like.
In this case, I choose AWS [https://aws.amazon.com/] as my server. and then the few tings have to do 
1. IPv4 Firewall. I suggest open all ports from 0 to 65334
<img width="555" alt="image" src="https://user-images.githubusercontent.com/92934877/156922076-4afd09bc-b422-4148-96ad-4564276274f5.png">

2. Start an editor, vi or whatever, and load the sshd config. Allow root login and password authentication by commenting/uncommenting: 
   > sudo vi /etc/ssh/sshd_config.    PermitRootLogin yes  PasswordAuthentication yes

## Installing Nginx
look at picture there are 6 Nignxs, we need to install it

<img width="522" alt="image" src="https://user-images.githubusercontent.com/92934877/156922243-fbeecb03-2206-4ffa-96de-470836cd0094.png">

### Number 1
1. Firstly, download the Nginx file from path Building-Nginx/nginx-1.16.1-1.el7.ngx.x86_64.rpm, or download from the official nginx website
2. Secondly, upload file to the linux via SCP or SSH
3. and then type command to install it
   > rpm -ivh  nginx-1.16.1-1.el7.ngx.x86_64.rpm
4. running nginx by typing the command
   > systemctl nginx start
5. checking the nginx status
   > systemctl nginx status
6. checking the webpage of nginx via browser in personal computer
   > http://IP:80
the picture showing below meaning that nginx was successfully installed 
<img width="390" alt="image" src="https://user-images.githubusercontent.com/92934877/156925052-c23cca42-8c65-403c-9055-53e857ad7471.png">

  




### Number 2

### Number 3

### Number 4

### Number 5

### Number 6
## Installing PC Scanner and Nmap


## Running Nmap

## Running PCscanner


  

