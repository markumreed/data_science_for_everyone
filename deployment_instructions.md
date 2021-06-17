# Deploying Bokeh apps to DigitalOcean


## Setting up the server account
- Create account on DigitalOcean with Credit Card or PayPal
- Create $5 monthly droplet and check email for droplet credentials
- Login to the server with ssh on Linux/Mac and putty on Windows passing the IP and port 22
- Enter root for username and the password received via email
- The server will ask to change the password. Do so.
- You should be logged in now.


## Installing software
- Go to the server root directory with "cd /"
- Install required software with "apt-get install python-virtualenv nginx gunicorn supervisor python-pip"
- Create a new directory for the virtual environment with "mkdir /opt/envs"
- Create a virtual environment with virtualenv "virtualenv /opt/envs/virtual"
- Activate the virtual environment ". /opt/envs/virtual/bin/activate"
- Install Python dependencies "pip install bokeh" "pip install flask" "pip install gunicorn"
- Create a new directory inside the nginx server "mkdir /var/log/nginx/flask"
- Create a new directory for uploading app files "mkdir /opt/webapps" "mkdir /opt/webapps/bokehflask"


## Create configuration files
- Make sure you have your configuration files ready which are bokeh_serve.conf, flask.conf and default.


## Upload your local app files
- Download the Filezilla software
- Enter your server IP in Host, root in Username, the droplet password in Password, leave the Port empty, and press Quickconnect
- Locate your local project directory on the left panel and select your Python files and the templates directory or any other associated local directory, but not configuration files
- Locate and select the server /opt/webapps/bokehflask directory on the right panel
- Right click over your left pannel local selected files and click Upload
- Upload the file named default to /etc/nginx/sites-available using the same procedure
- Upload files bokeh_serve.conf and flask.conf to /etc/supervisor/conf.d using the same procedure


## Adjusting your uploaded files in the server
- Open the app.py file with  "nano /opt/webapps/bokehflask/app.py"
- Add "from werkzeug.contrib.fixers import ProxyFix" to the remote app.py file.
- Modify the index function as follows: 
def index():
    url="http://104.236.40.212:5006"
    session=pull_session(url=url,app_path="/random_generator")
    bokeh_script=autoload_server(None,app_path="/random_generator",session_id=session.id, url=url)
    return render_template("index.html", bokeh_script=bokeh_script)
- Add "app.wsgi_app = ProxyFix(app.wsgi_app)" to the remote app.py file after the index function.
- Save the file by pressing Control-X, then type y and then hit Enter.
- Open the bokeh_serve.conf file with "nano /etc/supervisor/conf.d/bokeh_serve.conf" and put your IP for --allow-websocket-origin and your IP and port 5006 for --host 


## Starting the services
- Start the nginx webserver with "service nginx restart"
- Start supervisor with "service supervisor restart"
- Start flask with "supervisorctl restart flask"
- Start bokeh server with "supervisorctl restart bokeh_serve"
- Visit your app in the browswer at http://104.236.40.212 (put your own IP)
