# Web Infrastructure Design

This team project introduces learners to the web's infrastructure design.

## Key Concepts and Resources

*DNS* ,
*Server* ,
*Monitoring* ,
*Web server* ,
*Load balancer* 

- [Network basics](https://youtu.be/bj-Yfakjllc?si=QOdP5OUVQh4m42dG)
- [Web Infrastructure](https://youtu.be/lQNEW76KdYg)
- [What is a database](https://www.oracle.com/ke/database/what-is-database/)
- [What’s the difference between a web server and an app server?](https://www.infoworld.com/article/2077354/app-server-web-server-what-s-the-difference.html)
- [DNS record types](https://www.site24x7.com/learn/dns-record-types.html)
- [Single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure)
- [How to avoid downtime when deploying new code](https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header)
- [High availability cluster (active-active/active-passive)](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA712)
- [What is HTTPS](https://www.instantssl.com/http-vs-https)
- [What is a firewall](https://www.webopedia.com/definitions/firewall/)

## Project Tasks

Each task file contains a link to an image hosted on Imgur and/or an explanatory file (.md) as part of the project requirements described below: <br />

### [0-simple_web_stack](0-simple_web_stack)

Design a one server web infrastructure that hosts the website that is reachable via `www.foobar.com.` Start your explanation by having a user wanting to access your website. <br />

You must use:

* 1 physical server

* 1 web server (Nginx)

* 1 application server

* 1 application files (your code base)

* 1 database (MySQL)

* 1 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`

### [1-distributed_web_infrastructure](1-distributed_web_infrastructure)

Design a three-server web infrastructure that host the website `www.foobar.com`. <br />

You must add to [0-simple_web_stack](0-simple_web_stack):

* 2 physical servers

* 1 web server (Nginx)

* 1 application server

* 1 load-balancer (HAproxy)

* 1 application files (your code base)

* 1 database (MySQL)

### [2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure)

Design a three-server web infrastructure that host the website `www.foobar.com`, it must be secured, serve encrypted traffic and be monitored. <br />

You must add to [1-distributed_web_infrastructure](1-distributed_web_infrastructure):

* 3 firewalls

* 1 SSL certificate to serve `www.foobar.com` over HTTPS

* 3 monitoring clients (data collector for Sumologic or other monitoring services)

### [3-scale_up](3-scale_up)

You must add to [2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure):

* 1 physical server

* 1 load-balancer (HAproxy) configured as cluster with the other one

* Split components (web server, application server, database) with their own server

## Files

| Filename | Description |
| -------- | ----------- |
| [`0-simple_web_stack`](./0-simple_web_stack)  | Web Infrastructure Design with a LAMP stack. This contains: 1 server, 1 web server, 1 application server, 1 database and 1 domain name |
| [`1-distributed_web_infrastructure`](./1-distributed_web_infrastructure) | Web Infrastructure Design, based on `0-simple_web_stack` that contains some additional components: 1 server, 1 web server, 1 application server, 1 load-balancer, 1 set of application files, 1 database |
| [`2-secured_and_monitored_web_infrastructure`](2-secured_and_monitored_web_infrastructure) | Web Infrastructure Design, based on `1-distributed_web_infrastructure` that contains some additional components: 3 firewalls, 1 SSL certificate, 3 monitoring clients |
| [`3-scale_up`](3-scale_up) | Web Infrastructure Design, based on `2-secured_and_monitored_web_infrastructure` that contains some additional components: 1 server, 1 load-balancer |


## Authors
<details>
    <summary>Matilda Dogbatsey</summary>
    <ul>
    <li><a href="https://www.github.com/KafuiPraise">Github</a></li>
    <li><a href="mailto:matildapraise@gmail.com">e-mail</a></li>
    </ul>
</details>
<details>
    <summary>Pomaa Ewurah-Abena Oppong</summary>
    <ul>
    <li><a href="https://www.github.com/ewurapoms">Github</a></li>
    <li><a href="https://www.twitter.com/abbenapomaa">Twitter</a></li>
    <li><a href="mailto:apowurah@outlook.com">e-mail</a></li>
    </ul>

