# Load balancer


![](https://miro.medium.com/v2/resize:fit:1400/1*UEDws7zUq0N0dN-y3EGe5Q.png)

This project introduces learners to load balancer and webstack debugging.
Two additional servers were provided to be replicated on previous web server project
with Nginx configuration of the original server, and to set up an HAproxy
load balancer that manages both web servers.

## Tasks :page_with_curl:

* **0. Double the number of webservers**
  * [0-custom_http_response_header](./0-custom_http_response-header): Bash
  script that installs and configures Nginx on a server with a custom HTTP
  response header.
    * The name of the HTTP header is `X-Served-By`.
    * The value of the HTTP header is the hostname of the server.

* **1. Install your load balancer**
  * [1-install_load_balancer](./1-install_load_balancer): Bash script that
  installs and configures HAproxy version 1.5 on a server.
    * Enables management via the init script.
    * Requests are distributed using a round-robin algorithm.

* **2. Add a custom HTTP header with Puppet**
  * [2-puppet_custom_http_response_header.pp](./2-puppet_custom_http_response_header.pp): Automates
  Task 0 using a Puppet Manifest.
    * The name of the custom HTTP header must be X-Served-By
    * The value of the custom HTTP header must be the hostname of the server Nginx is running on
    * Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task
