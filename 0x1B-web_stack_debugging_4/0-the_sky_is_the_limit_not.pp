# a puppet manifest that increases the open files limit

exec {'sed':
  command  => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 15000\"" /etc/default/nginx',
  provider => 'shell',
}

exec {'restart':
  command => 'service nginx restart',
}