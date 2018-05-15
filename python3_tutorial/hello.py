#!/usr/bin/env python3
# name=input('please enter your name:')
# print('hello,',name)

# hello.py

# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'<h1>Hello, web!</h1>']


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    # print(environ['PATH_INFO'])
    return [body.encode('utf-8')]
