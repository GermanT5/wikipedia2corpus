# Wikipedia 2 Corpus - this is work in progress
Tools to extract and clean the Wikipedia texts to transform them into a text corpus for self-supervised NLP model training.

## Download the Data

### German Pages
- download the single files:
  - [dewiki-20220201-clean-part-01](https://github.com/GermanT5/wikipedia2corpus/releases/download/v1.0/dewiki-20220201-clean-part-01)
  - [dewiki-20220201-clean-part-02](https://github.com/GermanT5/wikipedia2corpus/releases/download/v1.0/dewiki-20220201-clean-part-02)
  - [dewiki-20220201-clean-part-03](https://github.com/GermanT5/wikipedia2corpus/releases/download/v1.0/dewiki-20220201-clean-part-03)
- combine the parts: `cat dewiki-20220201-clean-part-* > dewiki-20220201-clean.zip`
- check them: `sha256sum dewiki-20220201-clean.zip` should return `09c47abf6200ecc342e04902e360773f9ba2d92abb64bfa20f22c63fd660edcf`
- unzip the textfile: `unzip -t dewiki-20220201-clean.zip`

## Download Data
Download the raw Wikipedia dump and store it in the `data` directory:

**German language:** Select the youngest directory from https://dumps.wikimedia.org/dewiki/ and download a file called `dewiki-<yyyymmdd>-pages-articles.xml.bz2`. Its is about 5.8 GB in size. We use `dewiki-20220201-pages-articles.xml.bz2`.

**English language:** Select the youngest directory from https://dumps.wikimedia.org/enwiki/ and download a file called `dewiki-<yyyymmdd>-pages-articles.xml.bz2`. Its is about 18.1 GB in size. We use `enwiki-20220201-pages-articles.xml.bz2`.

## Extract Data
- de data: `python -m wikiextractor.WikiExtractor data/dewiki-20220201-pages-articles.xml.bz2 -o data/dewiki-20220201`
- en data: `python -m wikiextractor.WikiExtractor data/enwiki-20220201-pages-articles.xml.bz2 -o data/enwiki-20220201`

