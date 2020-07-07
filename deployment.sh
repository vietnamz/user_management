#!/bin/bash

build_user() 
{
	docker-compose -f docker-compose.yml build user-mgmt-service
	docker-compose -f docker-compose.yml up -d user-mgmt-service
}

build_gateway() 
{
	pushd gateway
	./gradlew build docker
	popd

	docker-compose -f docker-compose.yml build api-gateway
	docker-compose -f docker-compose.yml up -d api-gateway
}


build_sql() 
{
	docker-compose -f docker-compose.yml rm -s -v -f postgres_db
	docker-compose -f docker-compose.yml build postgres_db
	docker-compose -f docker-compose.yml up -d --force-recreate postgres_db
}

create_env () {
	if [ -d venv ]; then
	    rm -fr venv
	    echo "Remove existed virtual environment"
	fi
	python3 -m venv venv
	echo "Create new virtual environment"
    source ./venv/bin/activate
    echo "Active new virtual environment"
    pip install -r requirements.txt
}



migrate_db()
{
	# source ./venv/bin/activate
	create_env;

	# user management
	pushd user_management
	/bin/bash migrate.sh
	popd
}

reset_all_volume()
{
	docker-compose -f docker-compose.yml down -v
}

if [ "$1" = "help" ]; then
	echo "sudo ./deployment_new.sh         -- build all service without reset database: gateway | user "
	echo "sudo ./deployment_new.sh user    -- build service user without reset database"
	echo "sudo ./deployment_new.sh reset   -- build all service and reset database"
fi

if [ "$1" = "reset" ]; then
	if [[ "$2" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    	reset_all_volume;
    	build_sql;
    else
    	read -r -p "WARNIG!!! It's will be reset all your database. Are you sure? [y/N] " response
		if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
		    reset_all_volume;
			build_sql;
		else
			exit 1;
		fi
	fi
fi

if [ "$1" = "user" ] || [ "$1" = "" ] || [ "$1" = "reset" ]; then
	build_user;
fi

if [ "$1" = "gateway" ] || [ "$1" = "" ] || [ "$1" = "reset" ]; then
	build_gateway;
fi

if [ "$1" = "reset" ]; then
    migrate_db;
fi
