#! /usr/bin/python3

from connector import cloudstack

cs = cloudstack()
rules = cs.listPortForwardingRules()
config = {}

# povoa o template de configuração
for rule in rules['portforwardingrule']:
    name = rule['virtualmachinename']
    ip = rule['ipaddress'] 
    port = rule['publicport']
    private_port = rule['privateport']

    if private_port == '22':
        if ip not in config:
            config[ip] = []
            config[ip].append({'name': name, 'port': port})
        else:
            config[ip].append({'name': name, 'port': port})

text = '''Host {name}
    Port {port}
'''

for ip in config:
    print('# ' + ip)
    for vm in config[ip]:
        print(text.format(**vm))
