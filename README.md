# Scrapy
  Web Crawler using `Scrapy` package on python 3.x

### How to install package ?
  `python3 -m pip install Scrapy`

### How to create project ?
_run on terminal or CMD or powershell_
- Move to folder 

  `cd FolderName`
- Create `Scrapy` project

  `scrapy startproject yourprojectname`
- After inputting, some documents and settings will be created automatically. The data structure is as follows :

  * scrapy.cfg
  * items.py
  * middlewares.py
  * pipelines.py
  * settings.py
  * spiders / yourprojectname.py

### How to work on python ?
- Setting parameters in `Items.py`
- Writing crawler code in `spiders / yourprojectname.py`
- Setting database infomation in `settings.py` and `pipelines.py`

### How to run ?
_run on terminal or CMD or powershell_
- Run the py

  `scrapy crawl yourprojectname`
- Run and output

  `scrapy crawl yourprojectname -o output.json` _Output json_
  
  `scrapy crawl yourprojectname -o output.csv` _Output csv_
  
### Reference
_https://www.maxlist.xyz/2018/08/25/python_scrapy_ptt/_
