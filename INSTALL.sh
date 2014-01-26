#!/bin/bash
# Script para instalar aplicación

# Actualizar lista de paquetes
apt-get update

# Instalar git y curl
apt-get install git curl

# Instalar chef
curl -L https://www.opscode.com/chef/install.sh | bash

# Desplegar fuentes de la aplicación
# git clone https://github.com/IV-GII/Django_Traduccion.git	# Usar este para desplegar solo cuando versión final lista
git clone -b aprov https://github.com/IV-GII/Django_Traduccion.git

# Ejecución de aplicación con Chef
chef-solo -c solo.rb -j node.json
