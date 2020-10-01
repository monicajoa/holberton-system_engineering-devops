# Strace is your friend
# Fix error 500 in apache server with puppet
exec { '/var/www/html/wp-setting.php':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php"
}
