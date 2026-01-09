#! /bin/bash
# https://gist.github.com/Jimmy-Z/c4de0d15f89977a358996a171b9db668
# instalar qemu-guest-agent depois

VMID=151
NAME="mew.ime.usp.br"
CORES=2
MEMORY=1024
STORAGE="netuno3"
IMGURL="https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-generic-amd64.qcow2"
IMGPATH="/tmp/debian_img"

wget -O $IMGPATH $IMGURL

qm create $VMID --name $NAME --ostype l26
qm set $VMID --cpu host --cores $CORES --memory $MEMORY
qm set $VMID --net0 virtio,bridge=vmbr0
qm set $VMID --serial0 socket --vga serial0
qm set $VMID --scsihw virtio-scsi-single --scsi0 $STORAGE:0,import-from=$IMGPATH,discard=on,iothread=true
qm set $VMID --ide2 $STORAGE:cloudinit
qm set $VMID --boot order=scsi0
qm set $VMID --agent enabled=1,fstrim_cloned_disks=1
qm template $VMID
