# kill process by pkill

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
