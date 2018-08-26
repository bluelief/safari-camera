# Copyright (c) 2018 Bluelief.
# This source code is licensed under the MIT license.

.PHONY : clean
clean:
	rm -rf node_modules/
	rm -rf package-lock.json


.PHONY : install
install:
	npm install --production


.PHONY : build
build:
	npm run webpack


.PHONY : start
start:
	@echo '[*] Start python web service.' 
	@python3 webserv.py


.PHONY : stop
stop:
	-@pkill -f webserv.py | true
	@echo '[*] Stop service program.'


.PHONY : nginx_start
nginx_start:
	@sudo /etc/init.d/nginx start


.PHONY : nginx_stop
nginx_stop:
	@sudo /etc/init.d/nginx stop
