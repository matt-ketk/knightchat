import logging
import logging.handlers

from wsgiref.simple_server import make_server

import boto
import boto.s3
import sys
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = 'AKIAIPFKDYUIFAY4M5FQ'
AWS_SECRET_ACCESS_KEY = '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'

bucket_name = 'knightchat-storage'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)

bucket = conn.create_bucket(bucket_name,
    location=boto.s3.connection.Location.DEFAULT)

conn_ = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)
bucket_private = conn_.create_bucket('j2sffb-5nbdsnh562swh3asjc', location = boto.s3.connection.Location.DEFAULT)

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def write_to_s3(filename):
    k = Key(bucket)
    k.key = filename
    k.set_contents_from_filename(filename,
        cb=percent_cb, num_cb=10)

def write_to_s3_priv(filename):
    k = Key(bucket_private)
    k.key = filename
    k.set_contents_from_filename(filename,
        cb=percent_cb, num_cb=10)


# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler
LOG_FILE = '/opt/python/log/sample-app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)

import requests as r

signup = r.get('https://s3.us-east-2.amazonaws.com/p5n89-yz5nb-nhyl2owhgazjc/signup.html').text
client = r.get('https://s3.us-east-2.amazonaws.com/p5n89-yz5nb-nhyl2owhgazjc/client.html').text
signin = r.get('https://s3.us-east-2.amazonaws.com/p5n89-yz5nb-nhyl2owhgazjc/signin.html').text

import time

import json
import requests as r

import cgi

servers = {}
colors = {}
server_log = {}

bans = {}

access_codes_currently_processing = []

s_log = r.get('https://s3.amazonaws.com/knightchat-storage/server_log.txt').text
s_colors = r.get('https://s3.amazonaws.com/knightchat-storage/colors_info.txt').text
s_servers = r.get('https://s3.amazonaws.com/knightchat-storage/servers_info.txt').text

s_counter = r.get("https://s3.amazonaws.com/knightchat-storage/counter.txt").text

s_users = r.get('https://s3.amazonaws.com/knightchat-storage/users.txt').text

if s_counter[:3] == '<?x' or s_counter == "":
    server_log = {'abcdefgh' : [], 'test' : [], 'anothertest' : [], 'finaltest' : []}

    message_counter = 0

else:
    server_log = json.loads(s_log)
    colors = json.loads(s_colors)
    servers = json.loads(s_servers)

    message_counter = int(s_counter)

colors = {'s-yann' : "skyblue", 'kavel' : '#0084FF'}
temporary_messages = {'abcdefgh' : [], 'test' : [], 'anothertest' : [], 'finaltest' : []}
server_users = {'abcdefgh' : ['s-yann', 'kavel'], 'test' : ['s-yann'], 'anothertest':['s-yann'], 'finaltest' : ['mattk', 's-yann', 'kavel', 'johnl']}
aliases = {'abcdefgh' : 'newport', 'test' : "testerino", 'anothertest' : 'anothertesterino', "finaltest" : "danktest"}

users = json.loads(s_users)

messages = []
import hashlib
import base64
import urllib

import cgi

import random

def find(query, d):
    if query in d:
        return d[query]
    else:
        return ''

def create_salt(length):
    v = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''.join([v[random.randint(0, len(v))] for i in range (length)])

    return s

def application(environ, start_response):
    global message_counter

    try:
        path    = environ['PATH_INFO']
        method  = environ['REQUEST_METHOD']

        message_counter += 1

        if method == 'POST':
            try:
                if path == '/client':
                    status = '200 OK'
                    headers = [('Content-type', 'text/html'), ('Access-Control-Allow-Origin', '*')]

                    start_response(status, headers)

                    formdata = cgi.FieldStorage(environ=environ, fp=environ['wsgi.input'])

                    m = hashlib.md5()
                    m.update(str(formdata['password'].value).encode())
                    password = m.hexdigest()

                    if str(formdata['username'].value) not in users:
                        start_response('302 Found', [('Location','http://knightchat.newportrocketry.com?account=denied')])

                        return ["1"]


                    if users[str(formdata['username'].value)] == str(password):

                        start_response(status, headers)

                        return [r.get('https://p5n89-yz5nb-nhyl2owhgazjc.s3.amazonaws.com/client.html').text]
                    else:

                        start_response('302 Found', [('Location','http://knightchat.newportrocketry.com/?account=denied')])

                        return ["1"]


                elif path == '/file':
                    status = '204 OK'
                    headers = [('Content-type', 'text/html'), ('Access-Control-Allow-Origin', '*')]

                    start_response(status, headers)


                    request_body_size = int(environ['CONTENT_LENGTH'])

                    formdata = cgi.FieldStorage(environ=environ, fp=environ['wsgi.input'])

                    if 'newfile' in formdata and formdata['newfile'].filename != '':

                        file_data = formdata['newfile'].file.read()
                        filename = formdata['newfile'].filename

                        # write the content of the uploaded file to a local file
                        # TODO: Add a salt to the filename to prevent same file names
                        salt = create_salt(10)

                        filename_no_extension = '.'.join(filename.split('.')[:-1])
                        extension = filename.split('.')[-1].lower()

                        target = filename_no_extension + salt + '.' + extension
                        f = open(target, 'wb')
                        f.write(file_data)
                        f.close()

                        write_to_s3(target)

                        s = servers[formdata['server'].value]

                        if s['last'] == formdata['handle'].value:
                            # REAL IMPORTANT, KEEP THIS LIST LIMITED

                            if extension == 'jpeg' or extension == 'jpg' or extension == 'tif' or extension == 'tiff' or extension == 'png':
                                # ( means image + same person

                                server_log[formdata['server'].value].append(formdata['handle'].value + '\x00' + '<a target="_blank" style = "border-radius:inherit;" href = "https://s3.amazonaws.com/knightchat-storage/' + target + '"><img src = "https://s3.amazonaws.com/knightchat-storage/' + target + '" style = "border-radius:inherit; max-width:300px"></a>(' + '\x00' + 'rgba(0, 0, 0, 0)' + '\x00' + str(message_counter))
                            else:
                                server_log[formdata['server'].value].append(formdata['handle'].value + '\x00' + '<a target="_blank" href = "https://s3.amazonaws.com/knightchat-storage/' + target + '">' + filename_no_extension + '.' + extension + '</a>*' + '\x00' + colors[formdata['handle'].value] + '\x00' + str(message_counter))
                        else:
                            if extension == 'jpeg' or extension == 'jpg' or extension == 'tif' or extension == 'tiff' or extension == 'png':
                                # ) means image + different person

                                server_log[formdata['server'].value].append(formdata['handle'].value + '\x00' + '<a target="_blank" style = "border-radius:inherit;" href = "https://s3.amazonaws.com/knightchat-storage/' + target + '"><img src = "https://s3.amazonaws.com/knightchat-storage/' + target + '" style = "border-radius:inherit; max-width:300px"></a>)' + '\x00' + 'rgba(0, 0, 0, 0)' + '\x00' + str(message_counter))
                            else:
                                server_log[formdata['server'].value].append(formdata['handle'].value + '\x00' + '<a target="_blank" href = "https://s3.amazonaws.com/knightchat-storage/' + target + '">' + filename_no_extension + '.' + extension + '</a>^' + '\x00' + colors[formdata['handle'].value] + '\x00' + str(message_counter))

                        for k in s:
                            if k != "last" and k != "name":
                                if s['last'] == formdata['handle'].value:

                                    # REAL IMPORTANT, KEEP THIS LIST LIMITED
                                    if extension == 'jpeg' or extension == 'jpg' or extension == 'tif' or extension == 'tiff' or extension == 'png':
                                        s[k].append(formdata['handle'].value + '\x00' + '<a target="_blank" style = "border-radius:inherit;" href = "https://s3.amazonaws.com/knightchat-storage/' + target + '"><img src = "https://s3.amazonaws.com/knightchat-storage/' + target + '" style = "border-radius:inherit; max-width:300px"></a>(' + '\x00' + 'rgba(0, 0, 0, 0)' + '\x00' + str(message_counter))
                                    else:
                                        s[k].append(formdata['handle'].value + '\x00' + '<a target="_blank" href = "https://s3.amazonaws.com/knightchat-storage/' + target + '">' + filename_no_extension + '.' + extension + '</a>*' + '\x00' + colors[formdata['handle'].value] + '\x00' + str(message_counter))
                                else:
                                    if extension == 'jpeg' or extension == 'jpg' or extension == 'tif' or extension == 'tiff' or extension == 'png':

                                        s[k].append(formdata['handle'].value + '\x00' + '<a target="_blank" style = "border-radius:inherit;" href = "https://s3.amazonaws.com/knightchat-storage/' + target + '"><img src = "https://s3.amazonaws.com/knightchat-storage/' + target + '" style = "border-radius:inherit; max-width:300px"></a>)' + '\x00' + 'rgba(0, 0, 0, 0)' + '\x00' + str(message_counter))
                                    else:
                                        s[k].append(formdata['handle'].value + '\x00' + '<a target="_blank" href = "https://s3.amazonaws.com/knightchat-storage/' + target + '">' + filename_no_extension + '.' + extension + '</a>^' + '\x00' + colors[formdata['handle'].value] + '\x00' + str(message_counter))

                        s['last'] = formdata['handle'].value

                    return ["target: " + target]

                elif path == '/register':
                    request_body_size = int(environ['CONTENT_LENGTH'])

                    request_body = environ['wsgi.input'].read(request_body_size).decode()

                    status = '200 OK'
                    headers = [('Content-type', 'text/html'), ('Access-Control-Allow-Origin', '*')]

                    start_response(status, headers)

                    request_bodies = request_body.split('\x00')
                    main_body = request_bodies[1:]
                    query = request_bodies[0]


                    if query == 'USER_HANDLE':
                        if main_body[0] not in users:
                            pass
                        else:
                            return ["Username has already been taken"]

                        if set(main_body[0]).intersection(set('`~!@#$%^&*()+=[]{}\\|\'\";:/?.>,< ')):
                            return ["No special characters allowed, letters a-z + A-Z, underscores, dashes, and numbers only"]

                        return ["OK"]

                    elif query == 'USER_SUBMIT':
                        all_codes = r.get('https://j2sffb-5nbdsnh562swh3asjc.s3.amazonaws.com/codes.txt').text
                        taken_codes = r.get('https://j2sffb-5nbdsnh562swh3asjc.s3.amazonaws.com/codes-taken.txt').text

                        all_codes_split = set(all_codes.split('\r\n'))
                        taken_codes_split = set(taken_codes.split('\n'))


                        available_codes = all_codes_split.difference(taken_codes_split)

                        if main_body[-1] not in available_codes:
                            return ['Invalid code. If you don\'t have a code, contact us at newportknightchat@gmail.com to receive one.']
                        else:
                            taken_codes += main_body[-1] + '\n'

                            # update taken_codes
                            u = open('codes-taken.txt', 'w')
                            u.write(taken_codes)
                            u.close()

                            write_to_s3_priv('codes-taken.txt')

                        if main_body[0] not in users:
                            users[main_body[0]] = main_body[1]
                            new_users = open("users.txt", 'w')
                            new_users.write(json.dumps(users))

                            new_users.close()

                            write_to_s3("users.txt")

                        else:
                            return ["Username has already been taken"]

                        if set(main_body[0]).intersection(set('`~!@#$%^&*()+=[]{}\\|\'\";:/?.>,< ')):
                            return ["No special characters allowed, letters a-z + A-Z, underscores, dashes, and numbers only"]

                        return ["OK"]


                    elif query == 'USER_ACCESS':
                        all_codes = r.get('https://j2sffb-5nbdsnh562swh3asjc.s3.amazonaws.com/codes.txt').text
                        taken_codes = r.get('https://j2sffb-5nbdsnh562swh3asjc.s3.amazonaws.com/codes-taken.txt').text

                        all_codes_split = set(all_codes.split('\r\n'))
                        taken_codes_split = set(taken_codes.split('\n'))

                        available_codes = all_codes_split.difference(taken_codes_split)

                        if main_body[0] in available_codes:
                            return ["OK"]
                        else:
                            return ["Invalid code. If you don't have a code, contact us at newportknightchat@gmail.com to receive one."]

                    else:
                        return ["something"]

                elif path == '/create-account':

                    start_response('302 Found', [('Location','http://knightchat.newportrocketry.com')])

                    formdata = cgi.FieldStorage(environ=environ, fp=environ['wsgi.input'])

                    all_codes = r.get('https://j2sffb-5nbdsnh562swh3asjc.s3.amazonaws.com/codes.txt').text
                    taken_codes = r.get('https://j2sffb-5nbdsnh562swh3asjc.s3.amazonaws.com/codes-taken.txt').text

                    all_codes_split = set(all_codes.split('\r\n'))
                    taken_codes_split = set(taken_codes.split('\n'))

                    available_codes = all_codes_split.difference(taken_codes_split)

                    if formdata['access'].value not in available_codes:
                        return ['Invalid code. If you don\'t have a code, contact us at newportknightchat@gmail.com to receive one.']
                    else:
                        taken_codes += formdata['access'].value + '\n'

                        # update taken_codes
                        u = open('codes-taken.txt', 'w')
                        u.write(taken_codes)
                        u.close()

                        write_to_s3_priv('codes-taken.txt')

                    if formdata['username'].value not in users:
                        m = hashlib.md5()
                        m.update(formdata['password'].value.encode())

                        users[formdata['username'].value] = m.hexdigest()
                        new_users = open("users.txt", 'w')
                        new_users.write(json.dumps(users))

                        new_users.close()

                        write_to_s3("users.txt")

                    else:
                        return ["Username has already been taken"]

                    if set(formdata['username'].value).intersection(set('`~!@#$%^&*()+=[]{}\\|\'\";:/?.>,< ')):
                        return ["No special characters allowed, letters a-z + A-Z, underscores, dashes, and numbers only"]


                    try:

                        if 'newfile' in formdata and formdata['newfile'].filename != '' and formdata['newfile'].filename.split('.')[-1].lower() in ['jpg', 'png', 'tiff']:

                            file_data = formdata['newfile'].file.read()
                            filename = formdata['newfile'].filename

                            # write the content of the uploaded file to a local file
                            # TODO: Add a salt to the filename to prevent same file names
                            salt = ''

                            filename_no_extension = '.'.join(filename.split('.')[:-1])
                            extension = filename.split('.')[-1].lower()

                            target = filename_no_extension + salt + '.' + extension
                            f = open(formdata['username'].value + '-profile.jpg', 'wb')
                            f.write(file_data)
                            f.close()

                            write_to_s3(formdata['username'].value + '-profile.jpg')

                    except Exception as e:
                        return [str(e)]

                    time.sleep(5)
                    return ["1"]

                elif path == '/':

                    request_body_size = int(environ['CONTENT_LENGTH'])
                    request_body = environ['wsgi.input'].read(request_body_size).decode()
                    logger.info("Received message: %s" % request_body)

                    status = '200 OK'
                    headers = [('Content-type', 'text/html'), ('Access-Control-Allow-Origin', '*')]

                    start_response(status, headers)

                    json_body = json.loads(request_body)

                    message_type = find('type', json_body)
                    message_sender = find('sender', json_body)
                    message_content = find('content', json_body)
                    message_affect_id = find('affected-message-id', json_body)
                    message_conversation = find('conversation', json_body)
                    message_new_alias = find('new-alias', json_body)
                    message_new_color = find('new-color', json_body)

                    from_id = find('starting-from', json_body)

                    message_type_coarse, message_type_fine = message_type.split('/')

                    if (message_type_fine == 'last100'):
                        relevant_log = server_log[message_conversation]

                        return_message = json.dumps({
                            "type" : 'response/last100',
                            "messages" : [json.dumps(m) for m in relevant_log[-100:]]
                        })

                        return [return_message]

                    elif (message_type_fine == 'join'):
                        server_users[message_conversation].append(message_sender)

                    elif (message_type_fine == 'user-handle-validity'):
                        if message_content not in users:
                            return_message = json.dumps({
                                "type" : "response/user-handle-validity",
                                "validity" : "We didn't find that username! If you would like to register, visit <a href = 'courier.newportrocketry.com/register'>our register page</a>"
                            })
                        else:
                            return_message = json.dumps({
                                "type" : "response/user-handle-validity",
                                "validity" : "OK"
                            })

                        return [return_message]


                    elif (message_type_fine == 'servers-user-in'):
                        servers_user_in = []
                        for s in server_users:
                            if message_sender in server_users[s]:
                                servers_user_in.append({"name" : s, "alias" : aliases[s], "users" : server_users[s]})

                        return_message = json.dumps({
                            "type" : "response/servers-user-in",
                            "server-info" : [servers_user_in[i] for i in range (len(servers_user_in))]
                        })

                        return [return_message]

                    elif (message_type_fine == 'change-color'):
                        colors[message_sender] = message_new_color

                        relevant_log = temporary_messages[message_conversation]

                        message = {
                            "type" : message_type,
                            "sender" : message_sender,
                            "new-color" : message_new_color,
                            "conversation" : message_conversation,
                            "id" : len(relevant_log)
                        }

                        relevant_log.append(message)

                        for s in server_log:
                            for m in server_log[s]:
                                if "background-color" in m:
                                    if m['sender'] == message_sender:
                                        m['background-color'] = message_new_color

                        return_message = json.dumps({
                            "type" : "response/change-color",
                            "content" : "OK"
                        })

                        return [return_message]

                    elif (message_type_fine == 'change-alias'):
                        relevant_log = temporary_messages[message_conversation]
                        relevant_nontemp_log = server_log[message_conversation]

                        aliases[message_conversation] = message_new_alias

                        message = {
                            "type" : message_type,
                            "sender" : message_sender,
                            "conversation" : message_conversation,
                            "new-alias" : message_new_alias,
                            "id" : len(relevant_log)
                        }

                        relevant_log.append(message)

                        nontemp_message = {
                            "type" : "message/server-message",
                            "content" : message_sender + " named the group " + message_new_alias,
                            "sender" : "server",
                            "recipient" : {
                                "type" : "conversation",
                                "name" : message_conversation
                                },
                            "modifiers" : [],
                            "id" : len(relevant_nontemp_log),
                            "affected-message-id" : -1
                        }

                        relevant_nontemp_log.append(nontemp_message)

                        return_message = json.dumps({
                            "type" : "response/send",
                            "content" : "OK"
                        })

                        return [return_message]

                    elif (message_type_coarse == 'message'):
                        relevant_log = server_log[message_conversation]

                        modifiers = []

                        if relevant_log != [] and (message_sender) == relevant_log[-1]['sender']:
                            modifiers.append("after-message")
                        else:
                            modifiers.append("first-message")

                        message = {
                            "type" : message_type,
                            "content" : message_content,
                            "recipient" : {
                                "type" : "conversation",
                                "name" : message_conversation
                            },

                            "sender" : message_sender,
                            "modifiers" : modifiers,
                            "reacts" : {},
                            "id" : len(relevant_log),
                            "affected-message-id" : message_affect_id,
                            "background-color" : colors[message_sender]

                        }

                        relevant_log.append(message)

                        return_message = json.dumps({
                            "type" : "response/send",
                            "content" : "OK"
                        })

                        return [return_message]

                    elif (message_type_coarse == 'request' and message_type_fine == 'all-missing'):
                        relevant_log = server_log[message_conversation]

                        timer = 0
                        while (not relevant_log[from_id:]):
                            time.sleep(0.2)
                            timer += 1

                            if (timer > 50):
                                return_message = json.dumps({
                                    "type": "response/all-missing",
                                    "message" : []
                                })

                                return [return_message]

                        return_message = json.dumps({
                            "type" : "response/all-missing",
                            "messages" : [json.dumps(m) for m in relevant_log[from_id:]]
                        })

                        return [return_message]

                    elif (message_type_coarse == 'request' and message_type_fine == 'all-missing-temp'):
                        relevant_log = temporary_messages[message_conversation]

                        timer = 0
                        while (not relevant_log[from_id:]):
                            time.sleep(0.5)
                            timer += 1

                            if (timer > 20):
                                return_message = json.dumps({
                                    "type" : "response/all-missing-temp",
                                    "messages" : []
                                })

                                return [return_message]

                        return_message = json.dumps({
                            "type" : "response/all-missing-temp",
                            "messages" : [json.dumps(m) for m in relevant_log[from_id:]]
                        })

                        return [return_message]

                    elif (message_type_coarse == 'react'):
                        relevant_log = server_log[message_conversation]
                        return_message = json.dumps({
                            "type" : message_type,
                            "content" : message_content,
                            "recipient" : {
                                "type" : "conversation",
                                "name" : message_conversation
                            },

                            "sender" : message_sender,
                            "modifiers" : [],
                            "reacts" : {},
                            "id" : len(relevant_log),
                            "affected-message-id" : message_affect_id,
                            "background-color" : colors[message_sender]

                        })
                    #
                    #{
                    #    "type" : "message/text-only",
                    #    "content" : "hello world",
                    #    "affected-message-id" : 31415      // -1 if the client message does not affect any message
                    #}

                    return [request_body]
                elif path == '/scheduled':
                    logger.info("Received task %s scheduled at %s", environ['HTTP_X_AWS_SQSD_TASKNAME'], environ['HTTP_X_AWS_SQSD_SCHEDULED_AT'])
            except Exception as e:
                status = '200 OK'
                headers = [('Content-type', 'text/html'), ('Access-Control-Allow-Origin', '*')]
                start_response(status, headers)

                return [str(e)]
                logger.warning('Error retrieving request body for async work.')
            response = ''
        else:
            if path == '/':
                status = '200 OK'
                headers = [('Content-type', 'text/html'), ('Access-Control-Allow-Origin', '*')]
                start_response(status, headers)

                response = r.get('https://p5n89-yz5nb-nhyl2owhgazjc.s3.us-east-2.amazonaws.com/signin.html').text
                #response = r.get('https://p5n89-yz5nb-nhyl2owhgazjc.s3.amazonaws.com/lost.html').text

                return [response]

            elif path == '/register':
                status = '200 OK'
                headers = [('Content-type', 'text/html'), ('Access-Control-Allow-Origin', '*')]
                start_response(status, headers)

                #response = r.get('https://p5n89-yz5nb-nhyl2owhgazjc.s3.us-east-2.amazonaws.com/signup.html').text
                response = r.get('https://p5n89-yz5nb-nhyl2owhgazjc.s3.amazonaws.com/signup.html').text

                return [response]

        status = '200 OK'
        headers = [('Content-type', 'text/html'), ('Access-Control-Allow-Origin', '*')]
        start_response(status, headers)

        return [r.get('https://p5n89-yz5nb-nhyl2owhgazjc.s3.amazonaws.com/lost.html').text]
    except:
        status = '200 OK'
        headers = [('Content-type', 'text/html'), ('Access-Control-Allow-Origin', '*')]
        start_response(status, headers)

        return ['failed']

if __name__ == '__main__':
    httpd = make_server('', 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
