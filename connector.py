#! /usr/bin/python3
from decouple import config

def proxmox():
    from proxmoxer import ProxmoxAPI
    pve = ProxmoxAPI(
        config('PVE_HOST'),
        verify_ssl  = False,
        user        = config('PVE_USER'),
        token_name  = config('PVE_TOKEN_NAME'),
        token_value = config('PVE_TOKEN_VALUE')
    )
    return pve

def cloudstack():
    from cs import CloudStack
    cs = CloudStack(
        endpoint = config('CS_ENDPOINT'),
        key      = config('CS_KEY'),
        secret   = config('CS_SECRET')
    )
    return cs
