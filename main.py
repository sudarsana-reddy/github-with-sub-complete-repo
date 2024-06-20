import os 
import json
import sys

from github_package_versions_api import GitHubPackageVersionsAPI

class MainClass:
    def __init__(self, token, owner):
        self.api = GitHubPackageVersionsAPI(token, owner)
    

if __name__ == "__main__":
    # Replace these variables with your GitHub token, owner, repo, and package name
    packages = json.loads(os.getenv("PACKAGE_LIST", '[]'))
    package_type = os.getenv("PACKAGE_TYPE", "npm")
    owner = os.getenv("OWNER", "sudarsana-reddy")
    token = os.getenv("PAT")
    retention_number = os.getenv("RETENTION_NUMBER", 4) 
    delete_versions_pattern = os.getenv("DELETE_VERSIONS_PATTERN", "0.")

    if(len(packages) == 0):
        print("No packages found in the package list")
        sys.exit(1)

    main_class = MainClass(token, owner)
    for package in packages:
        main_class.api.deleteOldVersions(package, package_type, retention_number, delete_versions_pattern)
    