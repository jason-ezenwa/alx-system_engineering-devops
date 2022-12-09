file { '/tmp/school':
  mode    => '0744',
  owner   => www-data,
  content => 'I love puppet'
}
