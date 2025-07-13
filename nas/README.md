## Jellyfin
JellyFin is a media server that can be used to stream media files to devices.

### Usage
Jellyfin should contain these volumes to run:
- jelly-config
- movies
- tv

## MinIO
MinIO is an object storage server that can be used to store files.
It is similar to Amazon S3.

Uses port `9000` for web interface and `9001` for S3.

### Usage
MinIO should contain these volumes to run:
- s3

## Cloudflare Tunnel
Cloudflare Tunnel is a service that allows you to expose your local server to the internet.

### Usage
- Requires `startup.sh` to be run first to generate the tunnel ID and secret.
  - The script contains the command to run the tunnel. If the script is lost, you can find the command in the Cloudflare dashboard, under zero-trust/tunnels/docker config.

### Useful guides
- [How to use Nginx Proxy Manager to reverse proxy to a local server](https://www.reddit.com/r/nginxproxymanager/comments/17h427w/how_can_i_use_nginx_proxy_manager_to_reverse/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)


## NAS
Linux NAS set up requires the installation of samba.
- Link to setting up samba: [Ubuntu official site](https://ubuntu.com/tutorials/install-and-configure-samba#1-overview)
- Link to support backing up mac with NAS: [Link](https://adamdemasi.com/2018/03/24/using-samba-as-a-time-machine-network-server.html)
### Usage
```
[wilson-server]
path=/home/wilson-server/home-network
writable=yes
browsable=yes
create mask=0777
directory mask=0777
public=no

[wilson-timemachine]
path = /home/wilson-server/time-machine
browseable = yes
writeable = yes
create mask = 0600
directory mask = 0700
spotlight = yes
vfs objects = catia fruit streams_xattr
fruit:aapl = yes
fruit:time machine = yes
```
<!---->
# SET UP V2

### TrueNAS 
Create SMB shared drives
- [TrueNAS SMB share guide](https://www.youtube.com/watch?v=67KtKoW4IM0)

### Media VM
Mount smb drives in VM
- Connect to SMB drive and list shared drives
	- Requires the installation of `smbclient` 
	- Enter command: `smbclient -L //server_address -U username
- To mount shared drive: 
	- mkdir <dirnmame>
	- sudo mount -t cifs //<server_address>/<share_name> /<dirname> -o username=<your username> password=<your password> 
- Once mounted, point docker volume to shared drive, all content should appear in shared drive now
