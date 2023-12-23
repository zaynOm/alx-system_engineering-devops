# This manifest kiils a process named `killmenow`

exec { 'kill killmenow'
  command  => '/usr/bin/pkill -TERM killmenow',
}
