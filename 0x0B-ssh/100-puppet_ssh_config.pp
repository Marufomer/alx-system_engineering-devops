#!/usr/bin/env bash
# using puppet to make changes to configuration file

file { 'etc/ssh/ssh_cofig':
	ensure => present,
content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",

}

