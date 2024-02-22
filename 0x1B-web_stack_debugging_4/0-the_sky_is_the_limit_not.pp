# Sky is the limit, let's bring that limit higher

file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT=\"-n 10000\"\n",
}

exec { 'restart nginx':
  command  => 'service nginx restart',
  provider => 'shell',
}
