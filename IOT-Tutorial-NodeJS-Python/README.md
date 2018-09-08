# IOT-Workshop

This readme basically tell us what dependencies required.

```bash
apt install openssh-server mysql-server python-pip npm nodejs
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
apt update
apt-get install -y mongodb-org
```

how to change IP and port bind for mongodb
```bash
vim /etc/mongod.conf
```
```text
 21 # network interfaces
 22 net:
 23   port: 7005
 24   bindIp: 0.0.0.0
```
```bash
service mongodb restart
```

how to change IP and port bind for mysql
```bash
vim /etc/mysql/mysql.conf.d/mysqld.cnf
```
```text
34 port            = 3306
43 bind-address    = 127.0.0.1
```
```bash
service mysql restart
```

install Python packages
```bash
pip install socketIO-client-nexus pymongo MySQL-python pyserial
```

install Nodejs packages
```bash
npm install express socket.io pm2 nodemon mysql
```

how to access our amazon EC2
```bash
chmod 400 ourkey.pem
ssh -i "iot-class.pem" ubuntu@ec2-13-229-100-118.ap-southeast-1.compute.amazonaws.com
ssh -i "dh-crawler-4.pem" ubuntu@ec2-13-228-79-252.ap-southeast-1.compute.amazonaws.com
```
