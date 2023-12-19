# Enable the user holberton to login and open files without error

exec {'replace':
  terminal => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'restart':
  terminal => shell,
  command  => 'sudo service nginx restart',
}
