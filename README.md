# Wikipedia 2 Corpus - this is work in progress
Tools to extract and clean the Wikipedia texts to transform them into a text corpus for self-supervised NLP model training.

## Download Data
Download the raw Wikipedia dump and store it in the `data` directory:

**German language:** Select the youngest directory from https://dumps.wikimedia.org/dewiki/ and download a file called `dewiki-<yyyymmdd>-pages-articles.xml.bz2`. Its is about 5.8 GB in size. We use `dewiki-20220201-pages-articles.xml.bz2`.

**English language:** Select the youngest directory from https://dumps.wikimedia.org/enwiki/ and download a file called `dewiki-<yyyymmdd>-pages-articles.xml.bz2`. Its is about 18.1 GB in size. We use `enwiki-20220201-pages-articles.xml.bz2`.

## Extract Data
- de data: `python -m wikiextractor.WikiExtractor data/dewiki-20220201-pages-articles.xml.bz2 -o data/dewiki-20220201`
- en data: `python -m wikiextractor.WikiExtractor data/enwiki-20220201-pages-articles.xml.bz2 -o data/enwiki-20220201`
