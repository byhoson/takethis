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
## Initialzing Cache (optional)
```
python3 scripts/refresh-cache.py
```
