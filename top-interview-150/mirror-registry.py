import docker
import os
import shutil
import yaml

# Variables
mirror_registry_host = "mirror-registry.example.com"
mirror_registry_port = "5000"
upstream_registry = "registry-1.docker.io"
config_file = "/etc/docker/registry/config.yml"
config_file_local = "./config.yml"

# Create Docker client
client = docker.from_env()

# Pull the official registry image
client.images.pull("registry:2")

# Start the mirror registry container
client.containers.run(
    "registry:2",
    detach=True,
    ports={5000: (mirror_registry_host, mirror_registry_port)},
    restart_policy={"Name": "always"},
    name="mirror-registry",
)

# Wait for the registry to start
time.sleep(5)

# Retrieve the configuration file from the container
container = client.containers.get("mirror-registry")
container.copy(config_file, config_file_local)

# Update the configuration file with upstream registry information
with open(config_file_local, "r") as file:
    config_data = yaml.safe_load(file)

config_data["proxy"]["remoteurl"] = f"https://{upstream_registry}"

with open(config_file_local, "w") as file:
    yaml.safe_dump(config_data, file)

# Copy the updated configuration file back to the container
container.put(config_file_local, config_file)

# Restart the mirror registry container to apply the updated configuration
container.restart()
