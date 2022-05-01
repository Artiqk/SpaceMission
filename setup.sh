pip install flask
sudo apt install default-libmysqlclient-dev
sudo apt install mariadb-server
sudo systemctl start mariadb
sudo mysql -u root < createBDD.sql
export FLASK_APP=server
