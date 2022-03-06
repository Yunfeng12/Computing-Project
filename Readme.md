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
   > http://52.221.235.236:80

the picture showing below meaning that nginx was successfully installed 

<img width="390" alt="image" src="https://user-images.githubusercontent.com/92934877/156925052-c23cca42-8c65-403c-9055-53e857ad7471.png">

### Number 2
1. Firstly, download the Nginx file from path Building-Nginx/nginx-portable-11.zip
2. Secondly, upload file to the linux via SCP or SSH
3. extract it 
  > unzip  nginx-portable-11.zip
4. change the default port from 80 to 100 and runing it
  >cd nginx/conf
  >vi nginx.conf
  >
<img width="278" alt="image" src="https://user-images.githubusercontent.com/92934877/156927028-e628afec-3cd1-47e4-adcd-ffeee873ffad.png">
  >cd nginx/sbin
  >./nginx
5. checking the webpage of nginx via browser in personal computer
   >http://52.221.235.236:100/

### Number 3
1. Firstly, download the Nginx file from path Building-Nginx/nginx-1.16.1.tar.gz, or download from the official nginx website
2. Secondly, upload file to the linux via SCP or SSH
3. extract it 
   > tar  -zxvf   nginx-1.16.1.tar.gz
4. Install compilation tools and library files, and PCRE
   >yum -y install make wget zlib zlib-devel gcc-c++ libtool  openssl openssl-devel
   >wget http://downloads.sourceforge.net/project/pcre/pcre/8.35/pcre-8.35.tar.gz
   >tar zxvf pcre-8.35.tar.gz
   > cd pcre-8.35
   >  ./configure
   >  make && make install
5. and then intall nginx and config it
   > cd nginx-1.16.1
   > ./configure --prefix=/usr/local/nginx-port-103
   > make && make install
6. from now, nginx 3 have be installed, and then need change the default listen port from 80 to 101
   >cd /usr/local/nginx-port-101/conf
   >vi nginx.conf
 
   <img width="307" alt="image" src="https://user-images.githubusercontent.com/92934877/156926404-ef9b244b-b2c7-4063-a795-4c47add4d6b3.png">
7. checking the webpage of nginx via browser in personal computer
   >http://52.221.235.236:101/


 





### Number 4

### Number 5

### Number 6
## Installing PC Scanner and Nmap


## Running Nmap

## Running PCscanner


  

