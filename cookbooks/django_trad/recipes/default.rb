package 'git'
package 'python'

directory "/home/django_trad/" do
	owner "root"
	group "root"
	mode 00777
	action :create
end

git "/home/django_trad/" do
	repository "https://github.com/IV-GII/Django_Traduccion.git"
	revision "aprov"
	action :sync
end
