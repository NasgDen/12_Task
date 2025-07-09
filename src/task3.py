import requests


def get_github_repos(username: str) -> list[str]:
    """Функция выводит список репозиториев в github"""
    repositories = []
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            repositories.append(repo.get("name"))
    return repositories


if __name__ == "__main__":
    repos = get_github_repos('NasgDen')
    print(repos)
