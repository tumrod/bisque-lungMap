# bisque-lungMap
##### bisque-lungMap repository has 2 parts to it: 
- Bio-Image Semantic Query User Environment aka [Bisque](http://bioimage.ucsb.edu/bisque), a tool we used to store the lung images and their tags/annotations. 
- [lungMAP](http://lungmap.net/) is an on-going comprehensive lung development web-based atlas project. This repository is a part of data and metadata management process to create a molecular atlas of the mammalian lung.

We are using [Bisque's](http://bisque.iplantcollaborative.org) iPlantcollaborative version, instead of the original [Bisque](http://bioimage.ucsb.edu/bisque) from ucsb because we would like to utilize other platforms and tools from [iPlantCollaborative](iplantcollaborative.org) as well as Bisque. In addition, we utilize [TACC's](http://tacc.utexas.edu) technology to facilitate with large dataset we have.

## Why using it?
Bisque's web application works greats for small dataset (like 100-300 images). However, it can take awhile to add annotations/tags to each image by hand. In addition, storing the metadata in a spreadsheet can be helpful.

### Features:
- bq_annotation.py: import annotations/tags from a spreadsheet (tab-delimited txt file) to the images
- bq_tags.py: export annotations/tags into a spreadsheet format
- bq_dataset.py: create a dataset from images' name list
- bq_query.py: get a list of requested returned value (filename, uri,etc) of the images/dataset query by tags

## Getting started
#### Requirements:
- python 2.7
- virtualenv 
- pip
- BeautifulSoup4

###### Using easy_install or pip to install
```
$ easy_install virtualenv
$ easy_install pip
$ easy_install BeautifulSoup4
```

(Note - for installations, you may need to use sudo. New versions of python may have pip already installed.)


#### Step 1: Clone this repository
```
$ git clone https://github.com/tumrod/bisque-lungMap.git
```

#### Step 2: Create a virtualenv  
you may need to specify the python path with: -p < python path >

```
$ virtualenv bqapi
$ source bqapi/bin/activate 
```

#### Step 3: Fetch bqapi with the CAS option
```
(bqapi) $ pip install -i http://biodev.ece.ucsb.edu/py/bisque/dev bqapi[CAS]
```

#### Step 4: Move necessary packages into site-packages
```
(bqapi) $ sh setup_src.sh
```

#### Step 5: Run the script file
```
(bqapi) $ python <script_file.py>
```

### Tips: 
- You may need to use sudo at start of other commands if there are permission issues.
- You can deactivate the virtualenv by 
```
(bqapi) $ deactivate 
```


