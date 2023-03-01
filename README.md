# GitHub Crawler

This crawler is simply using the official GitHub API.

You need first to create a config file, `token.ini`, to store the API token. The token can be generated from [GitHub Developer Setting](https://github.com/settings/tokens?type=beta). For crawling public repo, you don't need to grant any access to this token.

```config
[DEFAULT]
token = TOKEN
```

List all repos to be crawled in `repos.txt` and run corresponding scripts to get the data. Retrieved data will be stored in `gh.db`, and you may use `sqlite3` or other SQL software to access it.
