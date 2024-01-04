# This manifest installs and configures a Nginx server

package { 'nginx':
  ensure => 'installed',
}

file { 'index.html':
  ensure  => 'file',
  path    => '/var/www/html/',
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "
server {
	location /redirect_me {
		return 301 /;
	}
}
  ",

}
service { 'nginx':
  ensure => 'running',
  enable => true,
}
