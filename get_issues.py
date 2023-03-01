import requests
import sqlite3
import json
import configparser
import time

config = configparser.ConfigParser()
config.read('token.ini')

HEADERS = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f"Bearer {config['DEFAULT']['token']}",
    'X-GitHub-Api-Version': '2022-11-28'
}


def get_repo_issues(repo):
    url = f'https://api.github.com/repos/{repo}/issues?state=all&per_page=100'

    p = 1

    while True:
        _url = url + f'&page={p}'
        r = requests.get(_url, headers=HEADERS)
        j = r.json()

        if len(j) == 0: break

        cur.executemany('INSERT OR REPLACE INTO issues VALUES (?, ?, ?)', [(_data['id'], repo, json.dumps(_data)) for _data in j])
        con.commit()
        print(f'{repo}: Page {p} done. ({len(j)} issues)')

        p += 1
        time.sleep(1)

    print(f'{repo}: Done.')


if __name__ == '__main__':
    
    con = sqlite3.connect('gh.db')
    cur = con.cursor()

    cur.executescript('''
        CREATE TABLE IF NOT EXISTS issues (
            id INTEGER PRIMARY KEY,
            repo TEXT NOT NULL,
            data JSON
        );
    ''')

    with open('repos.txt', 'r') as f:
        repos = f.readlines()

    print(f'Found {len(repos)} repos.')

    for repo in repos:
        get_repo_issues(repo.strip())

    con.close()