import os
import time
from git import Repo

REPO_DIR = "./"
CHECK_INTERVAL = 60

repo = Repo(REPO_DIR)

def has_changes():
    repo.git.add(A=True)
    return repo.is_dirty()

while True:
    print("Проверка началась")
    if has_changes():
        commit_msg = f"Auto backup: {time.strftime('%Y-%m-%d %H:%M:%S')}"
        repo.index.commit(commit_msg)
        repo.remotes.origin.push()
        print("Данные сохранены")
    print("Проверка закончилась")
    time.sleep(CHECK_INTERVAL)
