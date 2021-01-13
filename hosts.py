#! /usr/bin/python3

def pve_data():
    from connector import proxmox
    pve = proxmox()
    lxc = []
    qemu = []

    for node in pve.nodes.get():
        name = node['node']
        for ct in pve.nodes(name).lxc.get():
            if ct['status'] == 'running':
                lxc.append(ct['name'].replace('.ime.usp.br',''))
        for vm in pve.nodes(name).qemu.get():
            if vm['status'] == 'running':
                qemu.append(vm['name'].replace('.ime.usp.br',''))

    return (lxc, qemu)

def cs_data():
    from connector import cloudstack
    cs = cloudstack()
    vms = []

    for vm in cs.listVirtualMachines()['virtualmachine']:
        if vm['state'] == 'Running':
            vms.append(vm['displayname'])

    return vms

def hw():
    import requests
    phys = requests.get('https://si.ime.usp.br/servers.hw').text.split()

    for host in phys:
        if '#' in host:
            phys.remove(host)

    return phys

def dokuwiki(phys, lxc, qemu, vms):
    print('===== Físicos =====')
    for host in sorted(phys):
        print("  * [[server:%s]]"%(host))

    print('\n===== PVE =====')
    print('\n==== Containers ====')
    for host in sorted(lxc):
        print("  * [[server:%s]]"%(host))

    print('\n==== VMs ====')
    for host in sorted(qemu):
        print("  * [[server:%s]]"%(host))

    print('\n===== Internuvem =====')
    for host in sorted(vms):
        print("  * [[server:%s]]"%(host))

def plain(phys, lxc, qemu, vms):
    hosts = []
    for host in phys:
        hosts.append(host)
    for host in lxc:
        hosts.append(host)
    for host in qemu:
        hosts.append(host)
    for host in vms:
        hosts.append(host)

    for host in sorted(hosts):
        print(host)

def main():
    import sys

    phys = hw()
    (lxc, qemu) = pve_data()
    vms = cs_data()

    if len(sys.argv) > 1:
        plain(phys, lxc, qemu, vms)
    else:
        dokuwiki(phys, lxc, qemu, vms)

main()
