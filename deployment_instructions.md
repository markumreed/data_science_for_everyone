# Deploying Bokeh apps to DigitalOcean


## Setting up the server account
- Create account on DigitalOcean with Credit Card or PayPal
- Create $5 monthly droplet and check email for droplet credentials
- Login to the server with ssh on Linux/Mac and putty on Windows passing the IP and port 22
- Enter root for username and the password received via email
- The server will ask to change the password. Do so.
- You should be logged in now.

## Connect to DigitalOcean using ssh

```
ssh <username>@<remote>
```

## Installing software
- Go to the server root directory with 
```bash
cd /
```
- Install required software and packages
```bash
sudo apt-get update
sudo apt-get install python3-pip
pip3 install bokeh virtualenv
```
- Create a new directory for the virtual environment
```bash
mkdir /opt/envs
```
- Create a virtual environment with virtualenv 
```bash
virtualenv /opt/envs/virtual
```
- Activate the virtual environment
```bash
. /opt/envs/virtual/bin/activate
```


## Upload your local app files
- Connect to the remote system using sftp
```bash
sftp <username>@<remote>
```
- Transferring Local Files to the Remote System
```bash
sftp> put localFile
```


## Starting the services
- Start bokeh server 
```bash
bokeh serve --show bokeh_streaming_example.py --allow-websocket-origin="*"
```
