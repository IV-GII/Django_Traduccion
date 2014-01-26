#!/bin/bash
# Script para ejecución de la aplicación

chef-solo -c solo.rb -j node.json
