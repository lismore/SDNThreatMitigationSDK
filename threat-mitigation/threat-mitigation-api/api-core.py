# Copyright 2015 Patrick Lismore

__author__ = 'Patrick Lismore'

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