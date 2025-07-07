import sys
import os
from pathlib import Path
from ScriptCollection.GeneralUtilities import GeneralUtilities
from ScriptCollection.TasksForCommonProjectStructure import TasksForCommonProjectStructure


def build():
    script_file = str(Path(__file__).absolute())
    dependency_folder = GeneralUtilities.resolve_relative_path("../../Resources/Dependencies/Bitcoin", script_file)
    version_file = os.path.join(dependency_folder, "Version.txt")
    bitcoin_version = GeneralUtilities.read_text_from_file(version_file)
    arguments = dict[str, str]()
    arguments["BitcoinVersion"] = bitcoin_version
    TasksForCommonProjectStructure().standardized_tasks_build_for_docker_project_with_additional_build_arguments(str(Path(__file__).absolute()), "QualityCheck", 1, sys.argv, arguments)


if __name__ == "__main__":
    build()
