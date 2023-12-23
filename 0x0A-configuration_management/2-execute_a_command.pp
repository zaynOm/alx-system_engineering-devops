# This manifest kiils a process named `killmenow`

exec { 'pkill -f killmenow'
  path  => '/usr/bin/',
}
