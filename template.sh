#! /bin/bash
# https://gist.github.com/Jimmy-Z/c4de0d15f89977a358996a171b9db668
# https://blog.rosnertech.com.br/arquivos/2099

# dependência: virt-customize
# apt install libguestfs-tools

VMID=151
NAME="mew.ime.usp.br"
CORES=2
MEMORY=1024
STORAGE="local-btrfs"
IMGURL="https://cloud.debian.org/images/cloud/trixie/latest/debian-13-genericcloud-amd64.qcow2"
IMGPATH="/tmp/debian_img"

wget -O $IMGPATH $IMGURL
virt-customize --add $IMGPATH --install qemu-guest-agent

qm create $VMID --name $NAME --machine q35 --ostype l26
qm set $VMID --cpu host --cores $CORES --memory $MEMORY
qm set $VMID --net0 virtio,bridge=vmbr0
qm set $VMID --serial0 socket --vga serial0
qm set $VMID --scsihw virtio-scsi-pci --scsi0 $STORAGE:0,import-from=$IMGPATH,discard=on,ssd=1,iothread=true
qm set $VMID --ide2 $STORAGE:cloudinit
qm set $VMID --boot order=scsi0
qm set $VMID --bios ovmf
qm set $VMID --agent enabled=1,fstrim_cloned_disks=1
qm template $VMID
