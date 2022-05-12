<img src="https://amazingjoe.github.io/imgs/Easyscrape.png" />
# EasyScrape-GoogleSuggest

Scrape Google Auto Suggest Results

## Instructions

1. Install:

```
pip install easyscrape-googlesuggest
```

2. Get Google Suggestions for a Search Term:

```python
from easyscrape_googlesuggest import getsuggestions as ES

# Request suggestions for a search term
ESResults = ES.query("Mony Python")
ESResults

['monty python and the holy grail', 'monty python movies', 'monty python cast', 'monty python life of brian', 'monty python and the holy grail quotes', "monty python's flying circus", 'monty python rabbit', 'monty python quotes']
```

3. ES_query returns a list of strings with the results. You can optionally set the requests header as the second argument if you wish to include a custom header.
