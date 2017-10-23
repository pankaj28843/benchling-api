import os
import requests
from marshpillow import *
from marshmallow import pprint


class BenchlingAPIException(Exception):
    """Generic Exception for BenchlingAPI"""


class BenchlingLoginError(Exception):
    """Errors for incorrect login credentials"""


class RequestDecorator(object):
    """
    Wraps a function to raise error with unexpected request status codes
    """

    def __init__(self, status_codes):
        if not isinstance(status_codes, list):
            status_codes = [status_codes]
        self.code = status_codes

    def __call__(self, f):
        def wrapped_f(*args, **kwargs):
            args = list(args)
            args[1] = os.path.join(args[0].home, args[1])
            r = f(*args)
            if r.status_code not in self.code:
                http_codes = {
                    403: "FORBIDDEN",
                    404: "NOT FOUND",
                    500: "INTERNAL SERVER ERROR",
                    503: "SERVICE UNAVAILABLE",
                    504: "SERVER TIMEOUT"}
                msg = ""
                if r.status_code in http_codes:
                    msg = http_codes[r.status_code]
                    msg += "\n" + str(r.__dict__)
                raise BenchlingAPIException("HTTP Response Failed {} {}".format(
                        r.status_code, msg))
            return r.json()

        return wrapped_f

# Benchling API Info: https://api.benchling.com/docs/#sequence-sequence-collections-post

class BenchlingAPI(SessionManager):
    """ Generic api wrapper for Benchling """

    # TODO: Create SQLite Database for sequences
    def __init__(self, api_key, home='https://api.benchling.com/v1/'):
        """
        Connects to Benchling

        :param api_key: api key
        :type api_key: str
        :param home: url
        :type home: str
        """
        self.home = home
        self.auth = (api_key, '')

    def update(self):
        """
        Updates the api cache

        :return: None
        :rtype: None
        """
        self._update_dictionaries()

    @RequestDecorator([200, 201, 202])
    def post(self, what, data):
        print(what)
        print(data)
        print(self.auth)
        return requests.post(what, json=data, auth=self.auth)

    @RequestDecorator([200, 201])
    def patch(self, what, data):
        return requests.patch(what, json=data, auth=self.auth)

    @RequestDecorator(200)
    def get(self, what, data=None):
        if data is None:
            data = {}
        print(what)
        print(data)
        print(self.auth)
        return requests.get(what, json=data, auth=self.auth)

    @RequestDecorator(200)
    def delete(self, what):
        return requests.delete(what, auth=self.auth)