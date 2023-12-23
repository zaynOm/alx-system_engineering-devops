# This kills a process named killmenow, in all bin dirs

exec { 'pkill -f killmenow':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}
