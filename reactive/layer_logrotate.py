from charms.layer import status
from charms.layer import options
from charms.layer import logrotate
from charmhelpers.fetch import apt_install
from charmhelpers.core.hookenv import status_set

from charms.reactive import when, when_not, hook
from charms.reactive import set_flag, clear_flag

@when_not('logrotate.installed')
def install_logrotate():
    status.maintenance('installing logrotate')
    apt_install(['logrotate'])
    set_flag('logrotate.installed')
    set_flag('logrotate.init')


@when('logrotate.init', 'logrotate.installed')
def init_logrotate():
    logrotate.configure()
    clear_flag('logrotate.init')
    status.active('logrotate is set up')


@hook('upgrade-charm')
def upgrade_logrotate():
    set_flag('logrotate.init')
