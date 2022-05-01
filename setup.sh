pip install flask
sudo apt install python3-flask
sudo apt install default-libmysqlclient-dev
sudo apt install mariadb-server
pip install flask-mysqldb
sudo systemctl start mariadb
sudo mysql -u root < createBDD.sql
