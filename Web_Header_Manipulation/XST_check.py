import requests

# line creates an array of the HTTP methods we are going to send
verbs = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'TEST']
for verb in verbs:
    req = requests.request(verb, 'http://10.224.152.109/')
    # It prints out the method and the response status code and reason:
    print(verb, req.status_code, req.reason)

    # There is a section of code to specifically test for XST

    if verb == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
            print('Possible Cross Site Tracing vulnerability found')


