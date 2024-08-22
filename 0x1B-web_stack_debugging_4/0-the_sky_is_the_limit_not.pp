# Solve so the software can handle a high amount of requests by fixing the limit

exec {'replace':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
} ->

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
