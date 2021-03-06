#-------------------------------------------------------------------#
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

from webob import request


class ThreatMitigationController(object):
    """Base controller class for Threat Mitigation API."""

    # _service_name will be redefined in sub controller

    _service_name = None

    def __init__(self, plugin):

        self._plugin = plugin
        super(ThreatMitigationController, self).__init__()

    def _cleanse_request_body(self, body, params):

        """
        :rtype : object
        :param body: request body
        :param params: sets defaults for anything missing
        """

        try:
            if body is None:
                # Initialize empty resource for setting default value
                body = {self._service_name: {}}
            bodydata = body[self._service_name]
        except KeyError:
            # raise if _service_name is not in req body.
            raise request.HTTPBadRequest("Unable to find '%s' in the body" % self._service_name)
        for p in params:
            param_name = p['param-name']
            param_value = bodydata.get(param_name)
            # If the parameter wasn't found and it was required, return 400
            if param_value is None and p['required']:
                msg = ("Failed to parse request. You have to specify Parameter '%s' " % param_name)
                raise request.HTTPBadRequest(msg)
            bodydata[param_name] = param_value or p.get('default-value')
        return body