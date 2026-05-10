# Homelab

This repository contains the configuration files and documentation for homelab.

## Servers
The hardware includes: 
- NAS (Network Attached Storage) server for storing files and backups and self-hosted media services. It is also the central database for self hosted software projects.

## Infrastructure
- TrueNAS (NAS server) is the central storage for the homelab. 
- Media server (Jellyfin and Immich) is used to store and manage media files. Any application with a GPU dependency is run on this server. 
- Kluster servers (Dell Optiplex 7010) are used to run self-hosted apps and services. The 3 servers are used to run a Kubernetes cluster for the homelab. 

## Services
The services include:
- Pihole (Network wide ad-blocking and DNS server)
- Jellyfin (Media server)
- Immich (Photo and video management)
- Qbittorrent (Torrent client)
- NAS (Network Attached Storage) 
- Proxmox (Virtualization platform)

## Set up
To set up the homelab, you will need to:
1. Start up the TrueNAS server and set up the NAS. This will be source of all the other services. 
   1. Enable SMB/CIFS or NFS storage.
   2. Create a volume for the Media Server.
   3. Set up a user for the Media Server.
   4. Set up a group for the Media Server.
   5. Take note of the IP address of the TrueNAS server. You will need to route all traffic to the TrueNAS server.

2. Set up Media Server
   1. Install Jellyfin and Immich on the Media Server.
   2. Configure the Media Server to use the NAS as the storage location with fstab entries. `nano /etc/fstab` 
   3. Example fstab entries:
      - //{NAS_IP}/{SHARE_NAME} {MOUNT_POINT} cifs username={USER},password={PASSWORD},uid=1000,gid=1000,_netdev,x-systemd.mount-timeout=60,vers=3.0 0 0
      - x-systemd.mount-timeout is a systemd mount timeout. It tells systemd to wait up to 60 seconds for the CIFS connection before giving up.
      - vers=3.0 is the version of the CIFS protocol to use.
      - uid and gid are the user and group IDs to use for the mount.
      - _netdev is a flag that tells systemd to mount the volume as a network device.
      - 0 0 are the order and pass values for the mount.
   4. Configure Docker to only start once the volumes are mounted by editing the docker.service file. `nano /lib/systemd/system/docker.service` or `systemctl edit docker.service` 
```bash
[Unit]
After={IMMICH_MOUNT_POINT}.mount {JELLYFIN_MOUNT_POINT}.mount
Requires={IMMICH_MOUNT_POINT}.mount {JELLYFIN_MOUNT_POINT}.mount
```
Full flow: 
```bash
boot → try CIFS connect → [waits for server] → mount done → continue boot → start Docker
```