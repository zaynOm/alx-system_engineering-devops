# fix apache by changing file extension
$file_path  = '/var/www/html/wp-settings.php'

exec { 'replace phpp with php':
  command => "sed -i '/locale./s/phpp/php/' ${file_path}",
  path    => ['/bin', '/usr/bin']
}
