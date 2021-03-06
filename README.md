# tornado-session
(This project has been renamed as `redis_session` please navigate to https://github.com/devfans/redis-session for latest update.)
tornado session implementation with redis store


## Description
Implementated for python3 and tornado, using redis hashes to save session data.

+ For control expiration of sessions, we are using redis key expiration, and we only control session expiration at server/database side, using default expiration time of secure cookie for session id

+ We are using tornado.options module, so please run below once at starting
```
tornado.options.parse_command_line()
# or
tornado.options.parse_config_file("/etc/server.conf")
```
+ Please specify `cookie_secret` for we are using secure cookie key


## Command line parameters

```
define('session-redis', default='redis://localhost:6379', help='session store redis url', type=str)
define('session-redis-prefix', help='redis key prefix', type=str)
define('session-expire', help='session ttl(seconds)', type=int)
define('session-cookie-id', help='cookie key, default: session-id', type=str)
```

## Setup & Install

```
python setup.py build && python setup.py install
```

## Example

```
import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import options, define, parse_command_line
from tornado_redis_session import SessionHandler

define('port', default=3000, help='run on the given port', type=int)
define('debug', default=False, help='run in debug mode')

class MainHandler(SessionHandler):
    def get(self):
        self.write('Redis Session Example\n')
        count = self.session.count.int
        self.write(f'Current Session Value:{count}\n')
        self.session.count = count + 1
        self.write(f'Current Session Value:{self.session.count.int}\n')

def main():
    parse_command_line()
    application = tornado.web.Application([(r'/', MainHandler)], cookie_secret='udxas-efasx-ase323fs-3efsxf3eFdes')
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
```
