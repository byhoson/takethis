# Project TakeThis

## Getting Started
Dependencies:
  - keybert-0.5.0

---
## Directory Structure
```
course
- [data].\*
- [data].json
- [data]-db.json
- course-db.json

career
- [data]-db.json
- career-db.json

scripts
- parse-raw-data.py
- build-course-db.py
- build-career-db.py
- refresh-cache.py
```
---
## Creating DB
[data].* -> [data].json
```
python3 [parse | crawl]-[data].py
```

[data].json -> [data]-db.json
```
python3 extract-data.py
```
---
## Creating Signatures
prerequisite : google custom search api
you first have to obtain your private api key from cse.google.com in order to create signatures for arbitrary career keywords.
For cached keywords, api is not necessary.
after creating one, you should add your api key and cx into API_KEYS.txt in the root directory in the following form:
```
<API_KEYS.txt>
your_api_key
your_cx
```
---
## Initializing The Cache (optional)
To accelerate the query, the cache system for preestablished career keywords is provided.
to refresh the cache, type
```
python3 scripts/refresh-cache.py
```

to clean the cache, type
```
python3 scripts/clean-cache.sh
```
---
# Querying Courses
