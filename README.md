# Wikipedia 2 Corpus
Tools to extract and clean the Wikipedia texts to transform them into a text corpus for self-supervised NLP model training.

We use [WikiExtractor](https://github.com/attardi/wikiextractor) to extract the Wikipedia database dumps. The texts are split into sentences by using [SoMaJo](https://github.com/tsproisl/SoMaJo). Each line of the text corpus contains one single sentence. Between each Wikipedia article is a blank line.

## Download the German text Corpus
- size of the corpus (unzipped): 6.1G
- number of lines: 59,475,915
- download the single files:
  - [dewiki-20220201-clean-part-01](https://github.com/GermanT5/wikipedia2corpus/releases/download/v1.0/dewiki-20220201-clean-part-01)
  - [dewiki-20220201-clean-part-02](https://github.com/GermanT5/wikipedia2corpus/releases/download/v1.0/dewiki-20220201-clean-part-02)
  - [dewiki-20220201-clean-part-03](https://github.com/GermanT5/wikipedia2corpus/releases/download/v1.0/dewiki-20220201-clean-part-03)
- combine the parts: `cat dewiki-20220201-clean-part-* > dewiki-20220201-clean.zip`
- check them: `sha256sum dewiki-20220201-clean.zip` should return `09c47abf6200ecc342e04902e360773f9ba2d92abb64bfa20f22c63fd660edcf`
- unzip the textfile: `unzip -t dewiki-20220201-clean.zip`

## Download the English text Corpus
- download the single files:
  - [enwiki-20220201-clean-part-00](https://github.com/GermanT5/wikipedia2corpus/releases/download/v1.0/enwiki-20220201-clean-part-00)
  - [enwiki-20220201-clean-part-01](https://github.com/GermanT5/wikipedia2corpus/releases/download/v1.0/enwiki-20220201-clean-part-01)
  - [enwiki-20220201-clean-part-02](https://github.com/GermanT5/wikipedia2corpus/releases/download/v1.0/enwiki-20220201-clean-part-02)
  - [enwiki-20220201-clean-part-03](https://github.com/GermanT5/wikipedia2corpus/releases/download/v1.0/enwiki-20220201-clean-part-03)
  - [enwiki-20220201-clean-part-04](https://github.com/GermanT5/wikipedia2corpus/releases/download/v1.0/enwiki-20220201-clean-part-04)
  - [enwiki-20220201-clean-part-05](https://github.com/GermanT5/wikipedia2corpus/releases/download/v1.0/enwiki-20220201-clean-part-05)
- combine the parts: `cat enwiki-20220201-clean-part-* > enwiki-20220201-clean.zip`
- unzip the textfile: `unzip -t enwiki-20220201-clean.zip`

## How you can replicate our work
- download the raw Wikipedia dump and store it in the `data` directory:
  - German language: Select the youngest directory from https://dumps.wikimedia.org/dewiki/ and download a file called `dewiki-<yyyymmdd>-pages-articles.xml.bz2`. Its is about 5.8 GB in size. We use `dewiki-20220201-pages-articles.xml.bz2`.
  - English language: Select the youngest directory from https://dumps.wikimedia.org/enwiki/ and download a file called `dewiki-<yyyymmdd>-pages-articles.xml.bz2`. Its is about 18.1 GB in size. We use `enwiki-20220201-pages-articles.xml.bz2`.
- create and activate a new Python environment (for example with conda)
- install the dependencies: `pip install -r requirements.txt`
- for de data run: `python -m wikiextractor.WikiExtractor data/dewiki-20220201-pages-articles.xml.bz2 -o data/dewiki-20220201`
- for en data run: `python -m wikiextractor.WikiExtractor data/enwiki-20220201-pages-articles.xml.bz2 -o data/enwiki-20220201`
- use the `process_wiki_files.py` script:
  - edit `INPUT_DIR`, `OUTPUT_DIR` and if needed `LANGUAGE`
  - run the script
- concatenate the output in `OUTPUT_DIR` by running `cat <OUTPUT_DIR> > my_clean_wiki_corpus.txt`

## License

### The Text Corpus
As Wikipedia itself, the text corpus is published under [Creative Commons Attribution-ShareAlike 3.0 Unported license](https://de.wikipedia.org/wiki/Wikipedia:Lizenzbestimmungen_Creative_Commons_Attribution-ShareAlike_3.0_Unported).

### The Script
Copyright (c) 2022 Philip May

Licensed under the **MIT License** (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License by reviewing the file
[LICENSE](https://github.com/GermanT5/wikipedia2corpus/blob/main/MIT-LICENSE) in the repository.
