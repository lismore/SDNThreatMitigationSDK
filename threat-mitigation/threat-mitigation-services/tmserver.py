# -------------------------------------------------------------------#
'''
Copyright (c) 2015, Patrick Lismore
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of SDNThreatMitigationSDK nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
__author__ = 'Patrick Lismore'
'''
#-------------------------------------------------------------------#



import socket

host = "locahost"
port = 77777

tmServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tmServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tmServerSocket.bind((host, port))
tmServerSocket.listen(1)

print "Threat Mitigation Server is running on port %d; press Ctrl-C to terminate." % port

while 1:
    clientsock, clientaddr = tmServerSocket.accept()
    client = clientsock.makefile('rw', 0)
    client.write("Welcome SDN Threat Management SDK, " + str(clientaddr) + "\n")
    client.write("Please enter a string: ")
    line = client.readline().strip()
    client.write("You entered %d characters.\n" % len(line))
    client.close()
    client.close()