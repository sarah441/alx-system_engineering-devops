# puppet fix to find why Apache is returning a 500 error

exec { 'Fix wordpress site':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  path     => ['/bin','/usr/bin']
}
