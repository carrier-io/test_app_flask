Simple backed with registration.

Installation Locally (dev-mode)
============
####Preconditions:
1. Installed MySQL
2. Started MySQL server and service
for Mac:
```bash
service mysqld start
mysql.server start
```
2. Installed Python 3+ version

### Deployment steps
1. Open console and run next:
```bash
$ python3 -m venv ./venv 
$ source venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=main.py
$ export FLASK_DEBUG=1
$ flask run
$ open http://127.0.0.1:5000/

(venv) user@rodman backend-flask % flask run
 * Serving Flask app 'main.py' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Debugger is active!
 * Debugger PIN: 903-827-600
127.0.0.1 - - [24/Jun/2022 12:27:11] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [24/Jun/2022 12:27:11] "GET /swaggerui/swagger-ui-bundle.js HTTP/1.1" 200 -
127.0.0.1 - - [24/Jun/2022 12:27:11] "GET /swaggerui/swagger-ui.css HTTP/1.1" 200 -
127.0.0.1 - - [24/Jun/2022 12:27:11] "GET /swaggerui/swagger-ui-standalone-preset.js HTTP/1.1" 200 -
127.0.0.1 - - [24/Jun/2022 12:27:11] "GET /swaggerui/droid-sans.css HTTP/1.1" 200 -
127.0.0.1 - - [24/Jun/2022 12:27:11] "GET /swagger.json HTTP/1.1" 200 -
```
Deployment to PythonAnywhere
============
####Preconditions:
1. Register `Beginner `free account by the link https://www.pythonanywhere.com/registration/register/beginner/

## DB setup
1. Login and navigate to `Databases`
2. Create new DB `MySQL`: https://www.pythonanywhere.com/user/{your_username}/databases/
3. Create a database with name `pythonlogin`
4. Open mysql console by clicking on created databases (console name will be in the `{username}$pythonlogin`)
5. Create `accounts` table:
```sql
CREATE TABLE IF NOT EXISTS `accounts`(
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `username` varchar(50) NOT NULL,
    `password` varchar(255) NOT NULL,
    `email` varchar(100) NOT NULL,
    PRIMARY KEY(`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
```
6. Validate that DB created
7. Run 
```sql
show tables; 
```
you should see
```bash
+-------------------------------+
| accounts                      |
+-------------------------------+
1 row in set (0.00 sec)
```
## App setup
1. Open `Consoles` tab
2. Click on `Bash`
3. Clone repo:
```bash
$ git clone https://github.com/carrier-io/test_app_flask.git
```
4. Switch to the main Dashboard: https://www.pythonanywhere.com/user/{username}/
5. Click on `Web`
6. Click on `Add a new web app`
7. Select `Flask`
8. Select latest python
9. Typy `/home/{username}/backend-flask/main.py`
10. Click next 
11. Validate msg on screen:
```html
All done! Your web app is now set up. Details below.
```
12. Open `Consoles`
13. Click on existing bash console
14. Run next:
```bash
$ cd backend-flask/
$ git status
$ git checkout main.py
$ pip install -r requirements.txt
$ sed -i sed -e "s/yourdomainname.pythonanywhere.com/{username}.pythonanywhere.com/g" ~/backend-flask/model/tasks.py
```  
where `{username}` is  the username you use to log in to PythonAnywhere
for example:
```bash
$ sed -i sed -e "s/yourdomainname.pythonanywhere.com/test.pythonanywhere.com/g" ~/backend-flask/model/tasks.py
$ cat ~/backend-flask/model/tasks.py
```
you should find in output script next line:
```bash
 domain='test.pythonanywhere.com'
```
15. Update DB config in `main.py` and save changes using next cmd: `nano main.py`
```bash
# Enter your database connection details below
app.config['MYSQL_HOST'] = '{username}.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = '{username}'
app.config['MYSQL_PASSWORD'] = '{password}'
app.config['MYSQL_DB'] = '{username}$pythonlogin' #is the full name of your database, which comprises your username, then a dollar sign, then the name you gave it.
```
16. Navigate to `Web` tab
17. Click reload web app
18. Open registration page in web browser: 
```commandline
open https://{username}.pythonanywhere.com/login/register
```
19. Test register and login