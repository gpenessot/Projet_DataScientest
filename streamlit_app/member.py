import os
PATH = os.getcwd()
print(PATH)

class Member:
    def __init__(
        self, name: str, linkedin_url: str = None, github_url: str = None
    ) -> None:
        self.name = name
        self.linkedin_url = linkedin_url
        self.github_url = github_url

    def sidebar_markdown(self):

        markdown = f'<b style="display: inline-block; color: white; vertical-align: middle; height: 100%"> ▹ {self.name}</b>'

        if self.linkedin_url is not None:
            markdown += f' <a href={self.linkedin_url} target="_blank"><img src="https://raw.githubusercontent.com/gpenessot/cancer_project_streamlit/main/assets/linkedin-logo-black.png?token=GHSAT0AAAAAABWZJNLCZ6CPR6I4GWPVVOHCYWZ2DOA" alt="linkedin" width="25" style="vertical-align: middle; margin-left: 5px"/></a> '

        if self.github_url is not None:
            markdown += f' <a href={self.github_url} target="_blank"><img src="https://raw.githubusercontent.com/gpenessot/cancer_project_streamlit/0c05eb54e62dd466e4b019ad14c2bc3d036dd0e9/assets/github-logo.png?token=GHSAT0AAAAAABWZJNLDBVPSAN4FROAACROIYWZ2CGA" alt="github" width="20" style="vertical-align: middle; margin-left: 5px"/></a> '

        return markdown
