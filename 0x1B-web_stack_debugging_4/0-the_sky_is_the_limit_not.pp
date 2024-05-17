# Define the Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
}

# Remove the existing index.html file
file { '/usr/share/nginx/html/index.html':
  ensure => absent,
}

# Rename 50x.html to index.html
file { '/usr/share/nginx/html/index.html':
  ensure  => file,
  content => file('/usr/share/nginx/html/50x.html'),
  require => File['/usr/share/nginx/html/index.html'],  # Ensure the index.html is absent before creating new one
  notify  => Service['nginx'],  # Notify nginx service if this file changes
}

# Modify max open files limit setting for Nginx and restart Nginx service
exec { 'modify max open files limit setting':
  command => 'sed -i "s/15/10000/" /etc/default/nginx && service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
  unless  => 'grep -q "10000" /etc/default/nginx',
}