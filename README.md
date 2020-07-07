# Credify

User management API

## Getting Started
These instructions below will get you a copied version of the project up and running on your local machine for development and testing purposes. Please see [Deployment](#deployment) for detailed notes on how to deploy the project on a concrete system.

### Prerequisites
```
- docker
- docker-compose
- python3
- virtualenv + pip
- Oracle SDK (7 or above) - for build only
```

### Installing

1. Being ensured that **docker** daemon and **docker-compose** tool are already installed in your working environment with recommended version as below
- docker 19.03.5, build 633a0ea or later
- docker-compose 1.24.1, build 4667896b or later

```bash
# check docker daemon status
$ sudo service docker status

# check docker daemon version
$ sudo docker --version

# check docker-compose tool version
$ sudo docker-compose --version
```

_Note_: in the case you are using Windows or Macbook for development, you can download and install [Docker Desktop](https://www.docker.com/products/docker-desktop) tool. It will help you installed both of **docker** daemon and **docker-compose** tool from package installer and easily managing their state (started/stopped) from system tray icon.

2. Being ensured that **python3** and required environment packages (**virtualenv**, **pip**) also are installed and configured properly in your working environment:
- python 3.7.3 or above
- virtualenv 16.5.0 or above
- pip 19.0.3 or above

```bash
# check python version
$ sudo python --version

# check virtualenv version
$ sudo virtualenv --version

# check pip version
$ sudo pip --version
```
### Local Development

#### Activate virtualenv and install required python packages
Being ensured that current working folder is root directory of "credify" repository.
```bash
cd user_management
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Export required system variables
``` bash
export FLASK_APP=app.py
export APP_SETTINGS=local
export DATABASE_URL="postgresql+psycopg2://postgres:postgres@localhost:5432/user_mgr"
export FLASK_ENV=development
export GOOGLE_APPLICATION_CREDENTIALS=$(pwd)/firebase.json
```

OR

``` bash
source setenv
```

#### Create tables structure and import demo data

```bash
rm -Rf migrations
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
#### Drop tables structure and remove demo data
```bash
python manage.py db downgrade
```

#### Create ERD picture with [ERAlchemy](https://pypi.org/project/ERAlchemy/)
#### Activate virtualenv and install required ERAlchemy PyPi packages
Being ensured that current working folder is root directory of "neurobase_back_end" repository.
```bash
source venv/bin/activate
cd user_management
sudo apt install graphviz
pip install eralchemy
```
### Create ER diagram from MySQL database
```bash
eralchemy -i postgresql+psycopg2://postgres:postgres@localhost:5432/user_mgr -o erd_user_mgmt.png --exclude-tables alembic_version

```

### Development environment setup
A step by step series of instructions that tell you how to get a development environment running.

Being ensured that **git** CLI tool is installed in your working environment before proceeding next step.

1. Create project working directory and check out source code from Github project _credify_ repository:

```bash
# create working folder
$ mkdir -p projects/demo
$ cd projects/demo

# clone source code from github repository
$ git clone https://github.com/vietnamz/credify.git

.
├── README.md
├── deployment.sh
├── docker-compose.yml
├── gateway
├── migrate.sh
├── user_management
├── venv
└── vuefireabse.html

3 directories, 5 files
```

2. Build docker images of backend micro-services by using `deployment_reset.sh` script. It will help to build all required docker images from latest checked-out source code, installing and marking them as **latest** version in local docker repository, and finally bring them up as system daemons.

```bash
$ sudo cd projects/demo/credify
$ ./deployment.sh
```

_Note_: instead of using `deployment.sh` script (strongly recommended), you would like to rebuild and startup **specific micro-service docker container independently** (example `user_management`) by using **docker-compose** command, please follow those instructions below.

```bash
$ sudo cd projects/demo/credify

# Rebuild and restart specific user-mgmt-service container
$ sudo docker-compose build user-mgmt-service
$ sudo docker-compose up -d user-mgmt-service
```

List of current micro-services (which are defined in `docker-compose.yml` file):

| Service Name | Binding Information | Docs API | Description |
| ------ | ------ | ------ | ------ |
| postgres-db | 0.0.0.0:5432->5432/tcp | N/A | Postgres database docker container |
| api-gateway | 0.0.0.0:5000->5000/tcp | N/A | Proxy gateway for all provided micro-service |
| user-mgmt-service | 0.0.0.0:5001->5001/tcp | http://`<server IP address>`:5000/users/docs | User management micro-service|

3. Being ensured that all required docker containers have been built and started up successfully with `docker ps` command like below

```bash
$ sudo docker ps
CONTAINER ID        IMAGE                   COMMAND                   CREATED             STATUS              PORTS                    NAMES
d4415023f19e        neurobase/api-gateway   "/bin/sh -c 'echo \"T…"   11 minutes ago      Up 11 minutes       0.0.0.0:5000->5000/tcp   credify_api-gateway_1
3ac4051b7b3c        user-mgmt-service       "/bin/bash wait_to_s…"    12 minutes ago      Up 12 minutes       0.0.0.0:5001->5001/tcp   credify_user-mgmt-service_1
8a0c7a335eef        postgres                "docker-entrypoint.s…"    12 minutes ago      Up 12 minutes       0.0.0.0:5432->5432/tcp   dev_postgres
```

4. Clean up un-used or redundant docker images from local docker repository for saving storage space purpose (not strictly required)

```bash
$ sudo docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
```

5. Remove un-used/exited docker containers.

```bash
$ sudo docker rm $(sudo docker ps -aq -f status=exited)
```

6. Check availability of running services by browsing to its API documentation site in web browser, example
`http://<your server IP address>:5000/users/docs`

## Frontend Test application

1. In order to do verify phone OTP, I decided to come with firebase. Please checkout vuefireabse.html for detail.

2. It's required to install a http server to run vuefireabse.html rather than open it manually.

3. Install nodejs http server by command below:
```bash 
sudo npm install -g http-server
```

4. At the top of credify repo. Run the below command to open web browser.

```bash 
http-server
```

5. Finally, follow the instruction to do phone verification with firebase.


## Test firebase users.

Test

|  Identifier | User UID |
| ------ | ------ | 
| +84939717135 | 68BQeiGHEUgklhQsuSZagrdfeU72 |

## Contributing

`To be updated!`

## Authors

`To be updated!`

## License

`To be updated!`
