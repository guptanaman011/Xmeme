sudo apt-get update

sudo apt-get install -y python3.8 

sudo apt-get install -y python3-pip

pip3 install Django

## Install Mysql
echo y | sudo apt-get install -y mysql-server
​
## Install zip
echo y | sudo apt-get -y install unzip

sudo apt-get update

sudo apt-get install -y python-djangorestframework

pip instal -y django-rest-swagger==2.2.0


## Create Mysql USER AND PASSWORD
​
sudo mysql -u root -e "DROP USER 'xmeme'@'localhost'";
​
sudo mysql -u root -e "CREATE USER 'root'@'localhost' IDENTIFIED BY 'hideandseek';
GRANT ALL PRIVILEGES ON * . * TO 'xmeme'@'localhost';
FLUSH PRIVILEGES;"
​
## Drop and Create Database Xmeme in Mysql
sudo mysql -u xmeme -pxmememysql -e "DROP DATABASE xmeme;"
​
sudo mysql -u xmeme -pxmememysql -e  "CREATE DATABASE xmeme_imagedata DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;use xmeme;"


pip instal django-rest-swagger-ui