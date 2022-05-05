# SpaceMission

## How to setup the project

### You first need to start the database service (It is recommended to use MariaDB)
```
sudo service mariadb start
```

### Then give setup the execution permissions and execute it 
```
chmod +x setup.sh
./setup.sh
```

### You also need to define the Python file as an environment variable
```
export FLASK_APP=server
```

### Finally you can start the server
```
flask run
```
