FROM alpine:3.6

COPY cronjobs /etc/crontabs/root

# start crond with log level 8 in foreground, output to stderr
CMD ["crond", "-f", "-d", "8"]
