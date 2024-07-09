# kill process killmenow by pkill

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
