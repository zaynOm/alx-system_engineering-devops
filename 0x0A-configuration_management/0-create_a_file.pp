# This manifest creates a file with some content, permission, owner and group
file { 'school':
  ensure  => 'file',
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
