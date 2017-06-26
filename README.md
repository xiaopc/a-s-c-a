# a simple course assistant
(only suitable for Pizhou Taixue)

What you need:

1. supervisor (absolutely Python 2.7)
2. include `conf/*.conf` in supervisord.conf
3. Python 3+
4. PHP (allow function `exec()`)
5. If you can't access Google Fonts, you should ~~***"deng lu, then bian cheng a mao."***~~ change css.
6. I deleted some critical code ;> ,so you should be able to edit by yourself.
7. You'd like to change `gettime.php` to your secret code rule.

Please noted that it is under Apache License 2.0.

### a simple structure

user input -> conf file -> server.py task controlled by surpervisor -> log file