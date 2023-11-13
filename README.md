flask_template
=

Setup
--
```
- Run `python main.py` directly to set up the application (Flask)
- For test: http://127.0.0.1:5000/api/info/v1/test
```


Folder
--
```
flask_template/
|
├── env/ → Virtual environment
|
├── lib/
|   └── config.py
|
├── models/  → Main code section
|   ├── __init__.py
|   └── test_get.py
|
├── view/  → API
|   ├── __init__.py
|   └── test_api.py → test API
|
└── main.py → Run it!
```