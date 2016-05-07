import subprocess

from django.conf import settings
from django.http import HttpResponseRedirect

def reverse_ip(ip):
    ip = ip.split('.')
    ip.reverse()
    ip = '.'.join(ip)
    return ip


class RedirectToHiddenServiceMiddleware(object):
    def process_request(self, request):
        remote_address = request.META.get('REMOTE_ADDR', None)
        template = '{remote}.{port}.{local}.ip-port.exitlist.torproject.org'

        hostname = template.format(
            remote=reverse_ip(remote_address),
            port=80,
            local=reverse_ip(settings.SERVER_IP)
        )

        result = subprocess.run(
            ['dig', hostname, '+short'],
            stdout=subprocess.PIPE,
        ).stdout.strip().decode('utf-8')

        if result == '127.0.0.2':
            return HttpResponseRedirect(settings.HIDDEN_SERVICE)
