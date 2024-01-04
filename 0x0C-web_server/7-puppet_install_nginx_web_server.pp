# This manifest installs and configures a Nginx server

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

exec { 'redirect_me':
  command => '/usr/bin/sed -i "s|^}$|\n\tlocation /redirect_me {return 301 /;}\n}|" /etc/nginx/sites-available/default',
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
}
