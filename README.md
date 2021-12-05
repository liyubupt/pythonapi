

```bash
pip install -r requirements
```

Windows:

```powershell
$Env:FLASK_ENV="development"
$Env:SQLAZURECONNSTR_WWIF="<your-connection-string>"
```

Your connection string is something like:

```
DRIVER={ODBC Driver 17 for SQL Server};SERVER=<your-server-name>.database.windows.net;DATABASE=<your-database-name>;UID=PythonWebApp;PWD=PLACEHOLDER
```

To run and test the Python REST API local, just run

```bash
python -m flask run
```

Python will start the HTTP server and when everything is up and running you'll see something like

```text
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Get a customer

```bash
curl -s -X GET http://localhost:5000/customer/123
```