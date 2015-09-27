# unused-modules

A simple Python script that uses the dependecy graph of webpack to find modules that are not in use. The user is prompted to delete these modules.

## Requirements
You need Python 3.0 or later.

## Usage
The script has to be run from the same path as webpack):

`$ python unused-modules.py <frontend path> <comma separated string of extensions>`

###Example
`~/development/project-dir$ python /path/to/unused-modules.py ./frontend "jsx,js,scss"`
