# SwiftGate v2.0.0

## Synopsis

Gateway for API management, rate limiting and billing.

## Dependencies

* [Apache HTTP Server](http://httpd.apache.org/)
* [Membase Server](http://www.couchbase.org/)
* [RabbitMQ](http://www.rabbitmq.com/)
* [Python 2.x](http://python.org/)
* [mod_wsgi](http://code.google.com/p/modwsgi/)
* [Flask](http://flask.pocoo.org/)
* [Pika](http://pika.github.com/)
* [python-memcached](http://www.tummy.com/Community/software/python-memcached/)

## Ubuntu Installation

### Automatic

Run the following at the command line:

`wget -qO- --no-check-certificate https://raw.github.com/ushahidi/swiftgate/master/deploy/debian/install.sh | sudo bash`

### Manual

1. Add the RabbitMQ public key to the trusted key list.  
`wget -qO- http://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key add -`
	 	
2. Add the RabbitMQ repository to the sources.  
`echo deb http://www.rabbitmq.com/debian/ testing main >> /etc/apt/sources.list`

3. Update the sources.  
`apt-get update`

4. Upgrade the existing packages.  
`apt-get upgrade -y`

5. Download Membase.  
`wget -O /tmp/membase-server-community_x86_64_1.7.1.deb http://packages.couchbase.com/releases/1.7.1/membase-server-community_x86_64_1.7.1.deb`

6. Install Membase.  
`dpkg -i /tmp/membase-server-community_x86_64_1.7.1.deb`

7. Install the missing dependencies.  
`apt-get install -fy`

8. Remove the Membase installer.  
`rm -f /tmp/membase-server-community_x86_64_1.7.1.deb`

9. Install the other necessary Debian packages.  
`apt-get install -y apache2 libapache2-mod-wsgi python-pip rabbitmq-server git`

10. Install the necessary Python packages.  
`pip install flask python-memcached pika`

11. Create a user for SwiftGate processes to run as.  
`adduser --disabled-password --gecos "" swiftgate`

12. Create a local clone of the application.  
`git clone https://github.com/ushahidi/swiftgate.git /var/www/swiftgate`

13. Replace the default Apache configuration with the bundled one.  
`cp /var/www/swiftgate/deploy/debian/apache.conf /etc/apache2/sites-enabled/000-default`

14. Tell Apache to reload its configuration.  
`/etc/init.d/apache2 reload`

## Post-Install Configuration

1. Membase: `http://your.host:8091/`

2. RabbitMQ: `http://your.host:55672/mgmt/`

## Apache Configuration

    <VirtualHost *:80>
     WSGIDaemonProcess swiftgate user=swiftgate group=swiftgate threads=5
     WSGIScriptAlias / /var/www/swiftgate/api/wsgi.py
    </VirtualHost>

* If your application is installed in a different directory than `/var/www/swiftgate`, remember to modify the path accordingly.
* You need a user set up for the SwiftGate process to run as. In the above, we assume both the user and group will be `swiftgate`.

## Licenses

* All bundled source code is released under the [GNU Affero General Public License](http://www.gnu.org/licenses/agpl.html).
* All bundled documentation is released under the [GNU Free Documentation License](http://www.gnu.org/licenses/fdl.html).

## Support

* [SwiftRiver Mailing List](http://groups.google.com/group/swiftriver)

## See Also

* [Ushahidi](http://ushahidi.com/)
