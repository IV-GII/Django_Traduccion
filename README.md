Django_Traduccion
=================

Aplicación utilizando Django y Bootstrap para empresa de traducción.


INSTALACIÓN
===========

Instalación de Chef:

```
curl -L https://www.opscode.com/chef/install.sh | sudo bash
```

Desplegar fuentes de la aplicación:

```
git clone -b aprov https://github.com/IV-GII/Django_Traduccion.git
```

Instalación de la aplicación:

```
sudo chef-solo -c Django_Traduccion/solo.rb -j Django_Traduccion/node.json
```


EJECUCIÓN
=========

```
python manage.py runserver
```


ACCESO
======

http://127.0.0.1:8000
