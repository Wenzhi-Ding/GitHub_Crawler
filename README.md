# GitHub Crawler

This crawler is simply using the official GitHub API.

You need to first create a config file `token.ini` to store the API token.

```config
[DEFAULT]
token = TOKEN
```

List all repos to be crawled in `repos.txt` and run corresponding script to get the data. Retrieved data will be stored in `gh.db` and you may use `sqlite3` or other SQL software to access.