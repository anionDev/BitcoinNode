import sys
import os
import urllib.request
from pathlib import Path
from ScriptCollection.ScriptCollectionCore import ScriptCollectionCore
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.TFCPS.Docker.TFCPS_CodeUnitSpecific_Docker import TFCPS_CodeUnitSpecific_Docker_Functions,TFCPS_CodeUnitSpecific_Docker_CLI

def download_bitcoin():
    script_file = str(Path(__file__).absolute())
    bitcoin_version_file = GeneralUtilities.resolve_relative_path("../Resources/Dependencies/Bitcoin/Version.txt", script_file)
    bitcoin_version = GeneralUtilities.read_text_from_file(bitcoin_version_file)
    folder_of_this_file = os.path.dirname(os.path.realpath(__file__))
    resource_folder = GeneralUtilities.resolve_relative_path("./Resources/Bitcoin", folder_of_this_file)
    GeneralUtilities.ensure_directory_does_not_exist(resource_folder)
    GeneralUtilities.ensure_directory_exists(resource_folder)
    target_file = os.path.join(resource_folder, "Bitcoin.tar.gz")
    link = f"https://bitcoin.org/bin/bitcoin-core-{bitcoin_version}/bitcoin-{bitcoin_version}-x86_64-linux-gnu.tar.gz"
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'whatever')
    opener.retrieve(link, target_file)


def common_tasks():
    tf:TFCPS_CodeUnitSpecific_Docker_Functions=TFCPS_CodeUnitSpecific_Docker_CLI.parse(__file__)
    download_bitcoin()
    tf.do_common_tasks(tf.get_version_of_project())#codeunit-version should alsways be the same as project-version
    bitcoin_version=tf.tfcps_Tools_General.get_dependency_version_in_resources_folder(os.path.join(tf.get_codeunit_folder(),"Other","Resources"),"Bitcoin")
    GeneralUtilities.replace_regex_each_line_of_file(os.path.join(tf.get_codeunit_folder(),"ReadMe.md"),"The currently used Bitcoin\\-version is .*\\.", f"The currently used Bitcoin-version is {bitcoin_version}.")


if __name__ == "__main__":
    common_tasks()
