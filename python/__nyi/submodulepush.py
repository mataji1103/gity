# Copyright Aaron Smith 2009
# 
# This file is part of Gity.
# 
# Gity is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Gity is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Gity. If not, see <http://www.gnu.org/licenses/>.
from _util import *
try:
	import re,os,subprocess,simplejson as json
except Exception,e:
	glog(str(e))
	sys.stderr.write(str(e))
	exit(84)
try:
	from _argv import *
	if not options.misc: raise Exception("Gitty Error: The submodule update command requires a submodule")
	submodule=sanitize_str(options.misc[0])
	os.chdir(submodule)
	command="%s %s"%(options.git,"push")
	rcode,stout,sterr=run_command(command)
	exit_if_server_unreachable(sterr)
	exit_if_server_hungup(sterr)
	rcode_for_git_exit(rcode,sterr)
	exit(0)
except Exception, e:
	sys.stderr.write("The submodule add command through this error: " + str(e))
	exit(84)