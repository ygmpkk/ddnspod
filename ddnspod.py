#!/usr/bin/env python
#coding=utf-8

#DnsPod.Com Python Client
#Author: Timothy(ygmpkk@gmail.com)
#Data:   2012-11-25
#Example:
#
#
#
#
#
#
#
#
#

import os
import sys
import json
import urllib
from optparse import OptionParser 

parser = OptionParser()
parser.add_option('-a','--auth',dest='auth',default='',
                  help='Get authtoken'
                       'All the rest apis need authtoken generated bu thie one.'
                       'Resource url:DnsPodAPI[''auth'']'
                       'Format:JSON'
                       'Method:GET'
                       'Request parameters:'
                       'email:password')
parser.add_option('-d','--domain',dest='domain',default='',
                  help='Get Domain list')
parser.add_option('-s','--search',dest='search',default='',
                  help='Search Domain')
parser.add_option('-g','--group',dest='group',default='',
                  help='Get all groups')
parser.add_option('-r','--record',dest='record',default='',
                  help='Get all records of domain')

(options,args) = parser.parse_args(sys.argv[1:])

if options.auth:
    print('Auth')
else:
    leftEnv = ''
    rightEnv = ''

class DDnspod:
    DnsPodAPI = {'auth':'https://www.dnspod.com/api/auth',
                 'domain':'https://www.dnspod.com/api/domains',
                 'search':'https://www.dnspod.com/api/search',
                 'group':'https://www.dnspod.com/api/groups',
                 'record':'https://www.dnspod.com/api/records'}

    HttpMethods = {'get':'GET',
                   'post':'POST',
                   'put':'PUT',
                   'delete':'DELETE'}

    HttpStatusCode = {200: 'OK',
                      201: 'Created',
                      400: 'Bad Request',
                      403: 'Forbidden',
                      404: 'Not Found',
                      405: 'Method Not Allowed',
                      406: 'Not Acceptable',
                      408: 'Request Timeout',
                      409: 'Conflict',
                      500: 'Internal Server Error'}

    Logininfo = ''
    filedata = ''

    def Isloged(path):
        try:
            if(os.path.isfile(path)):
                filedata = file(path)
                filedata = filedata.read()
        except:
            print>>sys.stderr,'Check Auth Error\nException%s' % (e)
            return false

    def Auth(email,password):
        if len(email)==0:
            print('email can\'t empty')
        if len(password)==0:
            print('password can\'t empty')
        Isloged()
        try:
            authopen = urllib.open('%s?email=%s&password=%s' % (DnsPodAPI['auth'],email,password))
            authopen = authopen.read()
            authjson = json.loads(authopen)
            Logininfo = 'mario=%s' % (authjson['mario'])
            return true
        except:
            print>>stderr,'Auth Error\nException:%s' % (e)
            return false

if __name__=="__main__":
    if len(sys.argv) < 3:
        print("For usage:%s --help" % (sys.argv[0]))
    else:
        DDnspod()
