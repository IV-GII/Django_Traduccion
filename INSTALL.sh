#!/bin/bash
# Script para instalar aplicación

# Actualizar lista de paquetes
apt-get update

# Instalar git y curl
apt-get install curl

# Instalar chef
curl -L https://www.opscode.com/chef/install.sh | bash

# Ejecución de aplicación con Chef
chef-solo -c solo.rb -j node.json
