#package 'git'
package 'python'

#group "django_trad" do
#	system true
#	action :create	
#end

#user "django_trad" do
#	comment "Usuario de la aplicacion"
#	system true
#	shell "/bin/false"
#	action :create
#end

#directory "/home/django_trad/" do
#	# owner "root"
#	# group "root"
#	# mode 00777
#	owner "django_trad"
#       group "djando_trad"
#	mode 00754
#	action :create
#end

#git "/home/django_trad/" do
#	repository "https://github.com/IV-GII/Django_Traduccion.git"
#	revision "aprov"
#	action :sync
#end

