# This manifest adds a custom HTTP header to nginx server

exec { 'refresh package database':
  command => '/usr/bin/apt-get update',
}

-> package { 'nginx':
  ensure => installed,
}

-> file_line { 'add custom header':
  path  => '/etc/nginx/sites-available/default',
  after => 'location / {',
  line  => '\n\tadd_header X-Served-By \"$hostname\";',
}

-> exec { 'restart nginx server':
  command => '/usr/sbin/service nginx restart',
}
