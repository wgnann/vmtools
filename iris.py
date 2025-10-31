#! /usr/bin/python3

from connector import cloudstack
from sys import argv

IP = '200.144.254.25'
VM = 'iris'

def create():
    cs = cloudstack()
    ips = cs.listPublicIpAddresses()
    vms = cs.listVirtualMachines()

    [ip] = [i for i in ips['publicipaddress'] if i['ipaddress'] == IP]

    [vm] = [v for v in vms['virtualmachine'] if v['name'] == VM]

    cs.createPortForwardingRule(
            ipaddressid=ip['id'],
            privateport='80',
            protocol='tcp',
            publicport='80',
            virtualmachineid=vm['id']
    )

def delete():
    cs = cloudstack()
    rules = cs.listPortForwardingRules()

    [rule] = [r for r in rules['portforwardingrule'] if r['virtualmachinename'] == VM and r['publicport'] == '80']

    cs.deletePortForwardingRule(id=rule['id'])

if __name__ == '__main__':
    if len(argv) == 2:
        if argv[1] == 'create':
            create()
            exit()
        elif argv[1] == 'delete':
            delete()
            exit()
    print('erro')
