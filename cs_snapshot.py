#! /usr/bin/python3

from connector import cloudstack
from time import sleep

cs = cloudstack()
snapshots = cs.listVMSnapshot()
vms = cs.listVirtualMachines()

# apaga os antigos, pois o limite de snapshots é 2
for snapshot in snapshots['vmSnapshot']:
    if snapshot['current'] == False:
        cs.deleteVMSnapshot(vmsnapshotid=snapshot['id'])
        print("apagando: "+snapshot['displayname'])

# espera expungir
empty = False
while not empty:
    empty = True
    snapwait = cs.listVMSnapshot()
    for snapshot in snapwait['vmSnapshot']:
        if snapshot['current'] == False:
            print(snapshot['displayname'])
            empty = False
    sleep(30)

# cria os novos
for vm in vms['virtualmachine']:
    if vm['state'] == 'Running':
        cs.createVMSnapshot(virtualmachineid=vm['id'], name=vm['name'])

# mostra os snapshots
snapshots = cs.listVMSnapshot()
for snapshot in snapshots['vmSnapshot']:
    print(snapshot['displayname'], snapshot['created'])
