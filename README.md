# Socialhome

Socialhome is a Django application that acts as a social homepage for a user. The plan is to allow adding boxes or similar containers which contain information or a feed from an external site.

External site information will be synced as background jobs to minimize outgoing queries to sites.

[See an example here](http://jasonrobinson.me).

## Tech stack

* Python 2.7
* Built with [Django](http://djangoproject.com).
* [South](http://south.aeracode.org/) for database migrations.

## Deployment

Some example Ansible tasks are provided, adjust to needs.

## License

MIT
