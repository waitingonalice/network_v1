check_docker_startup(){
  while true; do
    if docker ps > /dev/null 2>&1; then
        tailscale serve http://127.0.1:8080
        break
    else
        sleep 5
    fi
  done
}

check_docker_startup