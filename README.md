# Snyk Code Ignorer 🙈

 Ignore individual Snyk Code issues for your reason and timeline.

## Getting Started

Pipe `snyk code test --json > examples/code_tests.json` into a file for ignoring.

Create an `ignore.json` with the same format as `ignores/code_ignores.json`

Now run `code_test_report` with paths to "Code Tests JSON" and "Ignores JSON" as args, respectively.

Like the following:

`python3 code_test_report examples/code_tests.json ignores/code_ignores.json`

Now you're ignoring individual issues, enjoy!

## Example Output

```
Issues:
        Issue: javascript/NoHardcodedPasswords
        File: typeorm-db.js
        Lines: 12 - 12

        Issue: javascript/NoHardcodedPasswords
        File: mongoose-db.js
        Lines: 52 - 52

Ignores:
        Issue: javascript/NoHardcodedCredentials
        File: typeorm-db.js
        Lines: 10 - 13
        Reason: This is a bening secret
        Expires: 2022-01-01 00:59:32.440942

Total Issues: 2
Total Ignores: 1
```
