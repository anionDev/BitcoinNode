from pathlib import Path
import re
import requests
from packaging.version import Version
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def get_latest_bitcoin_version():
    headers = {'Cache-Control': 'no-cache'}
    response = requests.get("https://bitcoin.org/bin", timeout=5, headers=headers)
    if response.status_code != 200:
        raise ValueError(f"Checking for latest bitcoin-version resulted in HTTP-response-code {response.status_code}.")
    content = response.text
    link_regex = r"<a href=\"bitcoin\-core\-\d+\.\d+(\.\d+)?\/\">bitcoin\-core\-(\d+\.\d+(\.\d+)?)\/<\/a>"
    pattern = re.compile(link_regex)
    matches = pattern.findall(content)
    versions: list[str] = list[str]()
    for linkmatch in matches:
        version = linkmatch[1]
        versions.append(version)
    versions.sort(key=Version)
    result = versions[-1]
    return result


def update_dependencies():
    script_file = str(Path(__file__).absolute())
    TasksForCommonProjectStructure().update_dependency_in_resources_folder(script_file, "Bitcoin", get_latest_bitcoin_version())


if __name__ == "__main__":
    update_dependencies()
