#!/usr/bin/env python3

import sys
import json
from datetime import datetime

GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'

def get_data_from_file(file_path: str) -> dict:
    with open(file_path) as f:
        data = json.load(f)
    return data


def fetch_simple_results(data: dict) -> list:
    results = data["runs"][0]["results"]

    simple_results = []

    for result in results:
        simple_result = {}
        simple_result["type"] = result["ruleId"]
        simple_result["level"] = result["level"]
        simple_result["message"] = result["message"]["text"]
        simple_result["file"] = result["locations"][0]["physicalLocation"][
            "artifactLocation"
        ]["uri"]
        simple_result["file"] = result["locations"][0]["physicalLocation"][
            "artifactLocation"
        ]["uri"]
        simple_result["startLine"] = result["locations"][0]["physicalLocation"][
            "region"
        ]["startLine"]
        simple_result["endLine"] = result["locations"][0]["physicalLocation"][
            "region"
        ]["endLine"]
        simple_results.append(simple_result)

    return simple_results

def cli():
    ignores = []
    issues = []
    
    # 0. Get Issues JSON and Ignores JSON
    ignores_json = get_data_from_file('ignores/code_ignores.json')
    issues_json = get_data_from_file('examples/code_tests.json')
    simple_issues_json = fetch_simple_results(issues_json)

    # 1. Cross reference each issue with the ignores
    for issue in simple_issues_json:
        for ignore in ignores_json:
            if  issue.get('file', 1) == ignore.get('file', 0) \
                and issue.get('type', 1) ==  ignore.get('type', 0)\
                and issue.get('endLine', -1) <= ignore.get('endLine', -2) \
                and issue.get('startLine', sys.maxsize - 1) >= ignore.get('startLine', sys.maxsize) \
                and str(datetime.now()) < ignore.get('expires', ''):
                ignores.append(ignore)
            else:
                issues.append(issue)

    # 2. Print remaining Issues
    if len(issues) > 0:
        print(RED + "\nIssues:" + END)
    for result in issues:
        print(
            "\tIssue: {}\n\tFile: {}\n\tLines: {}\n"
            .format(
                result['type'],
                result['file'],
                '{} - {}'.format(result['startLine'], result['endLine']),
            )
        )

    # 3. Print successful Ignores
    if len(ignores) > 0:
        print(GREEN + '\nIgnores:' + END)
    for ignore in ignores:
        print(
            "\tIssue: {}\n\tFile: {}\n\tLines: {}\n\tReason: {}\n\tExpires: {}\n"
            .format(
                ignore['type'],
                ignore['file'],
                '{} - {}'.format(ignore['startLine'], ignore['endLine']),
                ignore['reason'],
                ignore['expires'],
            )
        )

    # 4. Print a tally for both
    print('{}Total Issues{}: {}'.format(RED, END, len(issues)))
    print('{}Total Ignores{}: {}'.format(GREEN, END, len(ignores)))

    sys.exit(0 if len(issues) == 0 else 1)

# 0. Get Issues JSON and Ignores JSON
# 1. Cross reference each issue with the ignores
# 2. Print remaining Issues
# 3. Print successful Ignores
# 4. Print a tally for both
# Currently O(n^2) could be O(nlogn) but who cares
if __name__ == "__main__":
    cli()
