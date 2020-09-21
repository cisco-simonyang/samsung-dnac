import requests, base64

session = requests.Session()

def login(ip, username, password):
    url = 'https://%s/dna/system/api/v1/auth/token' % ip
    userpass = "%s:%s" % (username, password)
    encoded_u = base64.b64encode(userpass.encode()).decode()
    headers = {
        'Content-Type' : 'application/json',
        'Authorization' : 'Basic %s' % encoded_u
    }
    res = session.post(url, headers=headers, verify=False)
    # res.cookies.add_cookie_header('ip', ip)
    res_json = res.json()
    print('login token: %s' % res_json['Token'])
    return res_json['Token']


def get_clients(ip, token):
    data = {}
    url = 'https://%s/api/assurance/v1/host' % ip
    headers = {
        'Content-Type' : 'application/json',
        'Content-Length' : '2',
        # 'X-Auth-Token' : token
        'Cookie' : 'cisco-dna-core-shell-actionItemModal=false; X-JWT-ACCESS-TOKEN=%s' % token
    }

    print ('%s, %s' % (ip, token))
    res = session.post(url, json=data, headers=headers, verify=False)
    # res = session.post(url, headers=headers, verify=False)
    print(session, res.status_code, res.text)
    res_json = res.json()
    print('get_clients reponse :::: %s' % res_json)
    return res_json