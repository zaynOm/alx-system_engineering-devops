# This manifest adds a custom HTTP header to nginx server

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure => installed,
}
-> file_line { 'add HTTP header':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => "\n\tadd_header X-Served-By \"${hostname}\";",
}
-> exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
}
