# Scrapy
## Web Crawler using `Scrapy` package on python 3.x

### How to install package ?
`python3 -m pip install Scrapy`

### How to create project from `Scrapy` ?
- Move to folder

  `cd FolderName`
- Create `Scrapy` project

  `scrapy startproject yourprojectname`
- After inputting, some documents and settings will be created automatically. The data structure is as follows :
	(yourprojectname)
	│ scrapy.cfg
	│
	└─yourprojectname
			│ items.py
			│ middlewares.py
			│ pipelines.py
			│ settings.py
			│ __init__.py
			│
			├─spiders
			│ │ yourprojectname.py
			│ │ __init__.py
			│ │
			│ └─__pycache__
			│ __init__.cpython-36.pyc
			│
			└─__pycache__
							settings.cpython-36.pyc
							__init__.cpython-36.pyc
							items.cpython-36.pyc
