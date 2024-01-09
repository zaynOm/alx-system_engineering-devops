# This manifest adds a custom HTTP header to nginx server

exec { 'apt-get update':
  path => '/usr/bin',
}

-> package { 'nginx':
  ensure => installed,
}

-> file_line { 'add custom header':
  path   => '/etc/nginx/sites-available/default',
  after  => 'location / {',
  line   => '\n\tadd_header X-Served-By \"$hostname\";',
}

-> exec { 'service nginx restart':
  path => '/usr/sbin',
}
