#!/usr/bin/env python

import sys
import os
import shlex
from subprocess import check_output

if __name__ == '__main__':

	if len(sys.argv) < 3:
		print 'Usage: python deleted-unused-modules.py <frontend dir> <comma separated string of extensions>'
		sys.exit(0)

	frontend_path = sys.argv[1]
	file_extensions = tuple(['.' + ext if len(ext) > 0 and ext[0] is not '.' else ext for ext in sys.argv[2].split(',')])

	webpack_command = 'webpack --profile --json'
	args = shlex.split(webpack_command)

	webpack_output = check_output(args)

	files = [(f, os.path.join(subdir, f)) for (subdir, dirs, files) in os.walk(frontend_path) for f in files if f.endswith(file_extensions) and 'node_modules' not in subdir]

	safe_to_delete = []
	for f in files:
		if f[0]  not in webpack_output:
			safe_to_delete.append(f)

	if len(safe_to_delete) is 0:
		print 'There are no unused modules!'
		sys.exit(0)

	print 'Unused modules that should be safe to delete:'
	for f in safe_to_delete:
		print '"' + f[0] + '"'


	print '\nDelete the modules:'
	for f in safe_to_delete:
		os.system('rm -i ' + f[1])
