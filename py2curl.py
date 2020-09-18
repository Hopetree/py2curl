# -*- coding:utf-8 -*-
import json


def render(request, debug=True, verify=False):
    """request object to curl cmd

    :param request:
    :param debug: bool, if True add -v to curl
    :param verify: bool, if False add -k to curl only for https
    :return:
    """
    args = [
        'curl',
        '-X %s' % request.method
    ]

    if debug:
        args.insert(1, '-v')

    if not verify and request.url.startswith('https'):
        args.insert(1, '-k')

    for k, v in sorted(request.headers.items()):
        args.append('-H ' + json.dumps('{}: {}'.format(k, v)))

    if request.body:
        args.append('-d ' + json.dumps(request.body))

    args.append(request.url)

    return ' '.join(args)
