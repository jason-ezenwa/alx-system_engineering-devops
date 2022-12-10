# a manifest that alters the config file

exec {'ssh':
  command => 'echo "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path    => '/usr/bin',
  }
