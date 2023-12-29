# this manifest makes changes to ssh config file

file-line { 'Turn off passwd auth':
  path    => '~/.ssh/config',
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
  ensure  => present,
}

file-line { 'Declare identity file':
  path    => '~/.ssh/config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^IdentityFile',
  ensure  => present,
}
