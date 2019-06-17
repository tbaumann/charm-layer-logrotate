from charms.layer import options
from charmhelpers.core.templating import render
from charmhelpers.core.hookenv import log, service_name


LOGROTATE_TEMPLATE='logrotate.conf'
LOGROTATE_DIR='/etc/logrotate.d/'


def configure(opts={}):
    layer_opts = options.get('logrotate')
    context = {}
    context['options'] = {**layer_opts, **opts} #merge options, param opts overwrite
    target = LOGROTATE_DIR + service_name() + '.conf'
    if context['options']:
        log("Rendering {} with {}".format(target, context))
        render(source=LOGROTATE_TEMPLATE,
           target=target,
           context=context)


