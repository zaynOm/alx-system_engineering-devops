# this manifest makes changes to ssh config file

file { '~/.ssh/config':
  ensure  => present,
  content => @(EOF)
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  EOF
}
