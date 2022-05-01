pip install flask
pip install flask-mysqldb
sudo apt install default-libmysqlclient-dev
sudo apt install mariadb-server
sudo systemctl start mariadb
sudo mysql -u root < createBDD.sql
