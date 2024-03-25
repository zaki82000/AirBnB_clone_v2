#!/usr/bin/env bash
# sets your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

printf "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html 1> /dev/null

sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

conf="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"

sudo sed -i "/server_name _;/ a \\${conf}" /etc/nginx/sites-available/default 

sudo service nginx restart
