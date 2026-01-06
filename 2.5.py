import os
import time
from git import Repo

WATCH_DIR = "/home/user/important_files"  # что бэкапим
REPO_DIR = "./"        # git-репозиторий
CHECK_INTERVAL = 60                        # секунд

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
        print("Бэкап создан")
    print("Проверка закончилась")
    time.sleep(CHECK_INTERVAL)
