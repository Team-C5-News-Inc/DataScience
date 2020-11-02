# NEWS INC - SCRAPPER

## Table of Contents

* [Summary](#summary)
* [Concerning of Data Science](#concerning-of-data-dcience)
* [How to Use it](#how-to-use-it)
* [Folder Structure](#folder-structure)
* [Tests](#tests)
---

# Summary

This is the scrapper for the project News Inc, for Platzi Master. News Inc was divided in three projects, these three projects were build by an amazing team, that is described next.
* [Frontend](https://github.com/Team-C5-cheaPlatzi/Frontend).
    * [Alejandro Gonzales](https://github.com/orgs/Team-C5-cheaPlatzi/people/alejandro1030).
    * [Bernardo Aguayo](https://github.com/orgs/Team-C5-cheaPlatzi/people/BernardoAguayoOrtega).
    * [Xavier García](https://github.com/orgs/Team-C5-cheaPlatzi/people/ElXavs).
    * [Leandro Velasco](https://github.com/orgs/Team-C5-cheaPlatzi/people/ElXavs).
* [Backend](https://github.com/Team-C5-cheaPlatzi/Backend).
    * [Johan Avila](https://github.com/orgs/Team-C5-cheaPlatzi/people/johan-avila).
    * [Julian Cubillos](https://github.com/orgs/Team-C5-cheaPlatzi/people/JulesCubs).
* [Data Science](https://github.com/Team-C5-cheaPlatzi/DataScience).
    * [Oscar Palomino](https://github.com/orgs/Team-C5-cheaPlatzi/people/OscarPalominoC).


# Concerning of Data Science.

Data Science use 100% python to program the scrapper.

![Logo](https://www.maestrosdelweb.com/images/2012/10/python-logo-master-flat1.png)

The libraries used to program the scraper are:
* pyymaml: To save the data configuration in a config.yaml.
* requests: To request information about a web-page.
* lxml: It's the most rich feature to process xml and html data. In this case, the xpath to the information.
* pandas: The dataset is build and cleaned in this library.
* urllib3: For this, we used the methods exception, to be specific MaxRetryError.
* logging: To keep a log for what the scraper is doing.
* re: We use regular expressions to know if a url is built properly, or if a url is a pdf.
* pymongo: It's the official library for MongoDB, with this one, we can connect to the database and send the data scraped.
* Unittest: This library is used to run the unit test for each function in the scrapper.

# HOW TO USE IT?

![Installation](https://cdn.activestate.com/wp-content/uploads/2019/12/how-to-install-pip-on-windows.png)

It's quite easy, just follow the next steps.
1. Make sure you have a virtual environment. `python3 -m venv venv`.
2. Activate the virtual environment. `source venv/bin/activate`.
3. Install the dependencies in requirements.txt. `pip3 install -r requirements.txt`.
4. Create your own `client.py` file, in there, use the pymongo library and create a client variable that contains the URI to your mongo database.
5. Once the dependencies are installed and the file `client.py` is created, you can run the scraper. `python3 main.py`.

# FOLDER STRUCTURE

![ETL](https://www.talend.com/wp-content/uploads/ETL-3.png)

The work flow for each data scientist must be always the ETL structure, in that order the folder structure for this project follows the same principle, Extract, Transform and Load.
1. Extract: It extracts the information for the six newspaper selected, and save it into a csv file, then, the main.py file move it to the next step.
2. Transform: Transform phase is in charge of cleaning and enrichment the data. As long as the data is transformed, it saves it into another csv file, then, the main.py file move it to the final step.
3. Load: This phase is in charge of saving the data into a mongo database. In order to ensure the integrity of this project, the `client.py` in this folder is not added, but, you can create it, all you need is a mongo DB database and use URI provided by the cluster.

# TESTS

![Tests](https://files.realpython.com/media/Getting-Started-with-Testing-in-Python_Watermarked.9f22be97343d.jpg)

This project uses unittest as the main library to run them. There are in total 14 tests distribuited in the folders extract, transform and load.

Each test verifies the functioning of each function in the files `extract.py`, `transform.py` and `load.py`.

To run the test with comfort, there is a file in the root directory named `main_test.py`. This file uses the subprocess library in python, so there is no need to run the test in each folter, all you need to do is locate yourself in the root directory and run `python3 main_test.py`.