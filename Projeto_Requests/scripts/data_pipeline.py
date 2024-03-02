import requests

class Repository_Data():

    def __init__(self, owner):
        self.owner = owner
        self.access_token = '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'
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        self.api_base_url = 'https://api.github.com'
        self.url = f'{self.api_base_url}/users/{owner}/repos'

    def get_repo_data(self, repo_information: str):
        self.repo_information = repo_information

        repos = []
        information_list = []
        page = 1

        while True:
            try:
                pagina_url = f'{self.url}?page={page}'
                request_answer = requests.get(pagina_url, headers=self.headers)
                json_response  = request_answer.json()
                
                if len(json_response) == 0:
                    break

                page = page + 1
                repos.append(json_response)

            except:
                repos.append(None)

        
        number_of_pages = len(repos)
        number_repos_per_page = len(repos[0])

        try:
            for i in range(number_of_pages):
                for j in range(number_repos_per_page):
                    information_list.append(repos[i][j][repo_information])

        except:
            print('There was an error while running the script!')

        return information_list
