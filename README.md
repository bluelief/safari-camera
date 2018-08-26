# Using camera in safari with python api server


## What is?

This program using camera in safari. Then check barcode or QR code with python api server.  


## Setup


Install nodejs.  

```sh
node -v
v8.11.2

npm -v
5.6.0
```


Clone this project in your directory. Just run npm installer.    


```sh
git clone https://github.com/bluelief/safari-camera.git
cd safari-camera
npm install --production
```


## Setup nginx

Self-signed certificate

```bash
sudo openssl req -new -x509 -sha256 -newkey rsa:2048 -days 365 -nodes \
-out /etc/nginx/ssl/nginx.pem -keyout /etc/nginx/ssl/nginx.key
sudo chmod 400 ./*
```

Edit /etc/nginx/conf.d/*.conf

[https://github.com/bluelief/safari-camera/tree/master/nginx/conf.d](https://github.com/bluelief/safari-camera/tree/master/nginx/conf.d)


## Setup python

```bash
pip3 install -r requirements.txt
```


## Usage

Check the Makefile for command meaning.  

```bash
make nginx_start
make start
```


## License

Copyright (c) 2018 bluelief.  
Licensed under the MIT License.  
