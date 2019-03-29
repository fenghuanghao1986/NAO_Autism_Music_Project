
# SVN $HeadURL$
# SVN $Id$


# Copyright 2009-2011 Armin Hornung, University of Freiburg
# http://www.ros.org/wiki/nao
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    # Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#    # Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#    # Neither the name of the University of Freiburg nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

import rospy

# import Aldebaran API (must be in PYTHONPATH):
try:
	import motion
	from naoqi import ALProxy
except ImportError:
	rospy.logerr("Error importing NaoQI. Please make sure that Aldebaran's NaoQI API is in your PYTHONPATH.")
	exit(1)

class NaoNode():
	def __init__(self):
		# get connection from command line:
		from optparse import OptionParser

		parser = OptionParser()
		parser.add_option("--pip", dest="pip", default="127.0.0.1",
		                  help="IP/hostname of parent broker. Default is 127.0.0.1.", metavar="IP")
		parser.add_option("--pport", dest="pport", default=9559,
		                  help="port of parent broker. Default is 9559.", metavar="PORT")

		(options, args) = parser.parse_args()
		self.pip = options.pip
		self.pport = int(options.pport)

	def connectNaoQi(self, ip, port):
		rospy.loginfo("Connecting to NaoQi at %s:%d", ip, port)


		self.motionProxy = None
		self.memProxy = None

		try:
			self.motionProxy = ALProxy("ALMotion", ip, port)
			self.memProxy = ALProxy("ALMemory", ip, port)
			# TODO: check self.memProxy.version() for > 1.6
		except RuntimeError, e:
			rospy.logerr("Could not create Proxy to ALMotion or ALMemory, exiting. \nException message:\n%s", e)
			exit(1)
			
	def getProxy(self, name, warn=True):
		proxy = None
		
		try:
			proxy = ALProxy(name,self.pip,self.pport)
		except RuntimeError,e:
			if warn:
				rospy.logerr("Could not create Proxy to \"%s\". \nException message:\n%s",name, e)
		
		return proxy
