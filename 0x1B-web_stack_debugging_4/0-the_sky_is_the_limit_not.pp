# Define the Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/usr/share/nginx/html/index.html'],  # Restart nginx if the index.html file changes
}


file { '/usr/share/nginx/html/index.html':
  ensure => absent,
  before => File['/usr/share/nginx/html/new_index.html'],
}

file { '/usr/share/nginx/html/50x.html':
  ensure => file,
  path   => '/usr/share/nginx/html/index.html',
  require => File['/usr/share/nginx/html/index.html'],
}

exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => File['/usr/share/nginx/html/index.html'],
}

