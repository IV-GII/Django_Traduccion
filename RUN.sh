#!/bin/bash
# Script para ejecución de la aplicación

sudo chef-solo -c solo.rb -j node.json
