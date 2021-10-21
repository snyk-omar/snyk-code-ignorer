# Snyk Code Ignorer 🙈

 Ignore individual Snyk Code issues for your reason and timeline.

## Getting Started



Pipe `snyk code test --json > examples/code_tests.json` into a file for ignoring.

Create an `ignore.json` with the same format as `ignores/code_ignores.json`

Now run `code_test_report` with paths to "Code Tests JSON" and "Ignores JSON" as args, respectively.

Like the following:

`python3 code_test_report examples/code_tests.json ignores/code_ignores.json`

Now you're ignoring individual issues, enjoy!
