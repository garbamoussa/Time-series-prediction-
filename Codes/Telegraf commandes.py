History TELEGRAF



 473  2018-10-05 14:15:00 - 14:15:00 cd /etc/telegraf
  474  2018-10-05 14:15:12 - 14:15:12 sudo vi telegraf.conf
  475  2018-10-05 14:19:38 - 14:19:38 history | grep tele
  476  2018-10-05 14:20:01 - 14:20:01 sudo service telegraf restart
  477  2018-10-05 14:20:45 - 14:20:45 curl
  478  2018-10-05 14:20:56 - 14:20:56 curl --help
  479  2018-10-05 14:28:42 - 14:28:42 netstat
  480  2018-10-05 14:28:58 - 14:28:58 more telegraf
  481  2018-10-05 14:29:02 - 14:29:02 more telegraf.conf
  482  2018-10-05 14:29:28 - 14:29:28 netstat | grep 8186
  483  2018-10-05 14:30:00 - 14:30:00 curl
  484  2018-10-05 14:30:04 - 14:30:04 curl -help
  485  2018-10-05 14:31:48 - 14:31:48 curl --user servicepilot:SPV9 -d "test" -X POST http://localhots:8186
  486  2018-10-05 14:31:52 - 14:31:52 curl --user servicepilot:SPV9 -d "test" -X POST http://localhost:8186
  487  2018-10-05 14:32:09 - 14:32:09 more telegraf.conf
  488  2018-10-05 14:32:37 - 14:32:37 sudo vi telegraf.conf
  489  2018-10-05 14:33:15 - 14:33:15 hist | grep telegraf
  490  2018-10-05 14:33:18 - 14:33:18 h | grep telegraf
  491  2018-10-05 14:33:23 - 14:33:23 history | grep telegraf
  492  2018-10-05 14:33:28 - 14:33:28 !
  493  2018-10-05 14:33:31 - 14:33:31 sudo service telegraf restart
  494  2018-10-05 14:33:35 - 14:33:35 curl --user servicepilot:SPV9 -d "test" -X POST http://localhost:8186
  495  2018-10-05 14:33:46 - 14:33:46 netstat | grep 8186


 473  2018-10-05 14:15:00 - 14:15:00 cd /etc/telegraf
  474  2018-10-05 14:15:12 - 14:15:12 sudo vi telegraf.conf
  475  2018-10-05 14:19:38 - 14:19:38 history | grep tele
  476  2018-10-05 14:20:01 - 14:20:01 sudo service telegraf restart
  477  2018-10-05 14:20:45 - 14:20:45 curl
  478  2018-10-05 14:20:56 - 14:20:56 curl --help
  479  2018-10-05 14:28:42 - 14:28:42 netstat
  480  2018-10-05 14:28:58 - 14:28:58 more telegraf
  481  2018-10-05 14:29:02 - 14:29:02 more telegraf.conf
  482  2018-10-05 14:29:28 - 14:29:28 netstat | grep 8186
  483  2018-10-05 14:30:00 - 14:30:00 curl
  484  2018-10-05 14:30:04 - 14:30:04 curl -help
  485  2018-10-05 14:31:48 - 14:31:48 curl --user servicepilot:SPV9 -d "test" -X POST http://localhots:8186
  486  2018-10-05 14:31:52 - 14:31:52 curl --user servicepilot:SPV9 -d "test" -X POST http://localhost:8186
  487  2018-10-05 14:32:09 - 14:32:09 more telegraf.conf
  488  2018-10-05 14:32:37 - 14:32:37 sudo vi telegraf.conf
  489  2018-10-05 14:33:15 - 14:33:15 hist | grep telegraf
  490  2018-10-05 14:33:18 - 14:33:18 h | grep telegraf
  491  2018-10-05 14:33:23 - 14:33:23 history | grep telegraf
  492  2018-10-05 14:33:28 - 14:33:28 !
  493  2018-10-05 14:33:31 - 14:33:31 sudo service telegraf restart
  494  2018-10-05 14:33:35 - 14:33:35 curl --user servicepilot:SPV9 -d "test" -X POST http://localhost:8186
  495  2018-10-05 14:33:46 - 14:33:46 netstat | grep 8186



9 # # Influx HTTP write listener
   3310 [[inputs.http_listener]]
   3311 #   ## Address and port to host HTTP listener on
   3312    service_address = "localhost:8186"
   3313 #
   3314 #   ## maximum duration before timing out read of the request
   3315 #   read_timeout = "10s"
   3316 #   ## maximum duration before timing out write of the response
   3317 #   write_timeout = "10s"
   3318 #
   3319 #   ## Maximum allowed http request body size in bytes.
   3320 #   ## 0 means to use the default of 536,870,912 bytes (500 mebibytes)
   3321 #   max_body_size = 0
   3322 #
   3323 #   ## Maximum line size allowed to be sent in bytes.
   3324 #   ## 0 means to use the default of 65536 bytes (64 kibibytes)
   3325 #   max_line_size = 0
   3326 #
   3327 #   ## Set one or more allowed client CA certificate file names to
   3328 #   ## enable mutually authenticated TLS connections
   3329 #   tls_allowed_cacerts = ["/etc/telegraf/clientca.pem"]
   3330 #
   3331 #   ## Add service certificate and key
   3332 #   tls_cert = "/etc/telegraf/cert.pem"
   3333 #   tls_key = "/etc/telegraf/key.pem"
   3334 #
   3335 #   ## Optional username and password to accept for HTTP basic authentication.
   3336 #   ## You probably want to make sure you have TLS configured above for this.
   3337 basic_username = "servicepilot"
   3338 basic_password = "SPV9"
   3339
   3340
   3341 # # Read JTI OpenConfig Telemetry from listed sensors
   3342 # [[inputs.jti_openconfig_telemetry]]
   3343 #   ## List of device addresses to collect telemetry from
   3344 #   servers = ["localhost:1883"]
   3345 #
   3346 #   ## Authentication details. Username and password are must if device expects
   3347 #   ## authentication. Client ID must be unique when connecting from multiple instances
   3348 #   ## of telegraf to the same device
   3349 #   username = "user"
   3350 #   password = "pass"
   3351 #   client_id = "telegraf"




  
