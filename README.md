# EasyScrape-GoogleSuggest

Scrape Google Auto Suggest Results

## Instructions

1. Install:

```
pip install easyscrape-googlesuggest
```

2. Get Google Suggestions for a Search Term:

```python
from easyscrape_googlesuggest import getsuggestions

# Request suggestions for a search term
ESResults = getsuggestions.ES_query("Mony Python")
```

3. ES_query returns a list of strings with the results.
