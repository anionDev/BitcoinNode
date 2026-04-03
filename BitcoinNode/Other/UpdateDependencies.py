from pathlib import Path
import re
import requests
from packaging.version import Version
from pathlib import Path
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.TFCPS.TFCPS_Tools_General import TFCPS_Tools_General
from ScriptCollection.TFCPS.Docker.TFCPS_CodeUnitSpecific_Docker import TFCPS_CodeUnitSpecific_Docker_Functions,TFCPS_CodeUnitSpecific_Docker_CLI



def get_latest_bitcoin_version()->str:
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
    sc = ScriptCollectionCore()
    TFCPS_Tools_General(sc).update_dependency_in_resources_folder(script_file, "Bitcoin", get_latest_bitcoin_version())


if __name__ == "__main__":
    update_dependencies()
