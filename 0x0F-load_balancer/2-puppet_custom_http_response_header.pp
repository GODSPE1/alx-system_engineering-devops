#!/usr/bin/env bash
# practic the use of Puppet to make changes to our configuration file

file { '/etc/ssh/ssh_config':
    ensure  => 'file',
    content => "PasswordAuthentication no",
}

file_line {'Declare Identity File':
    ensure  =>  'present',
    path    =>  '/etc/ssh/ssh_config',
    line    =>  'IdentityFile ~/.ssh/school',

}
