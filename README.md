# NEWS INC - SCRAPPER


## Table of Contents

* [Summary](#summary)
* [Concerning of Data Science](#concerning-of-data-dcience)
* [How to Use it](#how-to-use-it)
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

[imagen bien cool del logo de python]

The libraries used to program the scraper are:
* pyymaml: To save the data configuration in a config.yaml.
* requests: To request information about a web-page.
* lxml: It's the most rich feature to process xml and html data. In this case, the xpath to the information.
* pandas: The dataset is build and cleaned in this library.
* urllib3: For this, we used the methods exception, to be specific MaxRetryError.
* logging: To keep a log for what the scraper is doing.
* re: We use regular expressions to know if a url is built properly, or if a url is a pdf.
* pymongo: It's the official library for MongoDB, with this one, we can connect to the database and send the data scraped.

# HOW TO USE IT?

It's quite easy, just follow the next steps.
1. Make sure you have a virtual environment. `python3 -m venv venv`.
2. Activate the virtual environment. `source venv/bin/activate`.
3. Install the dependencies in requirements.txt. `pip3 install -r requirements.txt`.
4. Once the dependencies are installed, you can run the scraper. `python3 main.py`.
