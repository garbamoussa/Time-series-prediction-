Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:48:43.766131Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON Itron_database_365D"
Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:48:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+Itron_database_365D HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 8943d755-dcfa-11e8-aa41-0000000
00000 455
Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:48:43.767000Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ITRON_365D"
Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:48:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+ITRON_365D HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 8943f903-dcfa-11e8-aa42-000000000000 445
Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:48:43.767894Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON test_arima"
Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:48:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+test_arima HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 89441a29-dcfa-11e8-aa43-000000000000 434
Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:48:43.768672Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp_stat\""
Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:48:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-temp_stat%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 89443a99-dcfa-11e8-aa44-
000000000000 478
Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:48:43.769626Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp\""
Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:48:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-temp%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 89445cf0-dcfa-11e8-aa45-00000
0000000 415
Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:48:43.770344Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-sinus\""
Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:48:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-sinus%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 89447abe-dcfa-11e8-aa46-0000
00000000 367
Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:48:43.771086Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW SUBSCRIPTIONS"
Oct 31 11:48:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:48:43 +0100] "POST /query?db=&q=SHOW+SUBSCRIPTIONS HTTP/1.1" 200 321 "-" "KapacitorInfluxDBClient" 8944971a-dcfa-11e8-aa47-000000000000 723
Oct 31 11:48:50 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:48:50 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 8d2946be-dcfa-11e8-aa48-000000000000 24413
Oct 31 11:48:50 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:48:50+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="35.657µs" status=200
Oct 31 11:48:51 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67


Oct 31 11:49:00 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:00.003366Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SELECT responsetime FROM telegraf.autogen.servicepilot_ping WHERE time >= '2018-10-23T10
:49:00Z' AND time < '2018-10-30T10:49:00Z' GROUP BY object"

Oct 31 11:49:00 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:00 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 931f3316-dcfa-11e8-aa4a-000000000000 14868
Oct 31 11:49:00 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:49:00+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="45.038µs" status=200
Oct 31 11:49:02 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67

Oct 31 11:49:08 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:00 +0100] "POST /query?db=&q=SELECT+responsetime+FROM+telegraf.autogen.servicepilot_ping+WHERE+time+%3E%3D+%272018-10-23T10%3A49%3A00Z%27+AND+time+%3C+%272
018-10-30T10%3A49%3A00Z%27+GROUP+BY+object HTTP/1.1" 200 5613933 "-" "KapacitorInfluxDBClient" 92f16841-dcfa-11e8-aa49-000000000000 8102277

Oct 31 11:49:10 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:10 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 991504af-dcfa-11e8-aa4b-000000000000 14470
Oct 31 11:49:10 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:49:10+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="41.732µs" status=200

Oct 31 11:49:11 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:11,641 INFO:root: Begin batch
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:13,651 INFO:root: SIZE OF INPUT: 7607
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:13,653 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: Test Statistic                -25.211
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: Lags                               32
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:13,717 INFO:root: ending batch

Oct 31 11:49:13 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:13,718 INFO:root: Begin batch
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:15,674 INFO:root: SIZE OF INPUT: 7606
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:15,675 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: Test Statistic                -30.697
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: Lags                               28
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:15,725 INFO:root: ending batch

Oct 31 11:49:15 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:15,727 INFO:root: Begin batch
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:17,517 INFO:root: SIZE OF INPUT: 7632
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:17,517 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: Test Statistic                -31.673
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:17,565 INFO:root: ending batch

Oct 31 11:49:17 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:17,567 INFO:root: Begin batch
Oct 31 11:49:18 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:19,343 INFO:root: SIZE OF INPUT: 7632
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:19,344 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: Test Statistic                -25.803
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: Lags                               32
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:19,397 INFO:root: ending batch

Oct 31 11:49:19 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:19,398 INFO:root: Begin batch
Oct 31 11:49:20 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:20 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 9f0ae02a-dcfa-11e8-aa4c-000000000000 15293
Oct 31 11:49:20 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:49:20+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="27.111µs" status=200
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:21,365 INFO:root: SIZE OF INPUT: 7668
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:21,365 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: Test Statistic                -30.434
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:21,424 INFO:root: ending batch

Oct 31 11:49:21 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:21,426 INFO:root: Begin batch
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:23,415 INFO:root: SIZE OF INPUT: 7662
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:23,416 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.279
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:23,480 INFO:root: ending batch
Oct 31 11:49:23 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:23,482 INFO:root: Begin batch
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:25,484 INFO:root: SIZE OF INPUT: 7654
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:25,485 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.526
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:25,541 INFO:root: ending batch
Oct 31 11:49:25 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:25,543 INFO:root: Begin batch
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:27,387 INFO:root: SIZE OF INPUT: 7649
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:27,389 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: Test Statistic                -30.417
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:27,445 INFO:root: ending batch
Oct 31 11:49:27 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:27,447 INFO:root: Begin batch
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:29,432 INFO:root: SIZE OF INPUT: 7645
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:29,433 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: Test Statistic                -28.387
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: Lags                               30
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:29,491 INFO:root: ending batch
Oct 31 11:49:29 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:29,492 INFO:root: Begin batch
Oct 31 11:49:30 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:49:30 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:30 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" a500c49c-dcfa-11e8-aa4d-000000000000 16062
Oct 31 11:49:30 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:49:30+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="27.18µs" status=200
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:31,463 INFO:root: SIZE OF INPUT: 7655
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:31,463 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.887
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:31,561 INFO:root: ending batch
Oct 31 11:49:31 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:31,563 INFO:root: Begin batch
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:33,436 INFO:root: SIZE OF INPUT: 7667
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:33,437 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.044
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: Lags                               30
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:33,490 INFO:root: ending batch
Oct 31 11:49:33 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:33,493 INFO:root: Begin batch
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:35,481 INFO:root: SIZE OF INPUT: 7638
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:35,482 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: Test Statistic                -25.714
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: Lags                               33
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:35,552 INFO:root: ending batch
Oct 31 11:49:35 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:35,554 INFO:root: Begin batch
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:37,548 INFO:root: SIZE OF INPUT: 7636
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:37,548 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: Test Statistic                -24.573
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: Lags                               36
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:37,616 INFO:root: ending batch
Oct 31 11:49:37 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:37,618 INFO:root: Begin batch
Oct 31 11:49:37 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:39,696 INFO:root: SIZE OF INPUT: 7639
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:39,697 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: Test Statistic                -26.978
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: Lags                               32
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:39,768 INFO:root: ending batch
Oct 31 11:49:39 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:39,771 INFO:root: Begin batch
Oct 31 11:49:40 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:40 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" aaf6a9c5-dcfa-11e8-aa4e-000000000000 14626
Oct 31 11:49:40 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:49:40+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="27.641µs" status=200
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:41,860 INFO:root: SIZE OF INPUT: 7621
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:41,861 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: Test Statistic                -25.437
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: Lags                               33
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:41,923 INFO:root: ending batch

Oct 31 11:49:41 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:41,925 INFO:root: Begin batch
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "GET /ping HTTP/1.1" 204 0 "-" "KapacitorInfluxDBClient" ad05dfc3-dcfa-11e8-aa4f-000000000000 19
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.758236Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW DATABASES"
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+DATABASES HTTP/1.1" 200 197 "-" "KapacitorInfluxDBClient" ad05eb35-dcfa-11e8-aa50-000000000000 704
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.759411Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON telegraf"
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+telegraf HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" ad06199a-dcfa-11e8-aa51-000000000000 330
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.760688Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON _internal"
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+_internal HTTP/1.1" 200 153 "-" "KapacitorInfluxDBClient" ad064a86-dcfa-11e8-aa52-000000000000 230
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.761821Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON chronograf"
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+chronograf HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" ad0676db-dcfa-11e8-aa53-000000000000 224
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.762906Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ML"
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+ML HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" ad06a148-dcfa-11e8-aa54-000000000000 224
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.763713Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON testtxt"
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+testtxt HTTP/1.1" 200 169 "-" "KapacitorInfluxDBClient" ad06c0f9-dcfa-11e8-aa55-000000000000 228
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.764501Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON NOAA_water_database"
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+NOAA_water_database HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" ad06df5a-dcfa-11e8-aa56-0000000
00000 229
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.765253Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON Itron_database_365D"
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+Itron_database_365D HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" ad06fceb-dcfa-11e8-aa57-0000000
00000 223
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.766011Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ITRON_365D"
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+ITRON_365D HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" ad071a98-dcfa-11e8-aa58-000000000000 221
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.766739Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON test_arima"
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+test_arima HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" ad07372a-dcfa-11e8-aa59-000000000000 217
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.767505Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp_stat\""
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-temp_stat%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" ad07539d-dcfa-11e8-aa5a-
000000000000 283
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.768074Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp\""
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-temp%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" ad076b23-dcfa-11e8-aa5b-00000
0000000 228
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.768562Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-sinus\""
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-sinus%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" ad077e03-dcfa-11e8-aa5c-0000
00000000 227
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:49:43.769029Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW SUBSCRIPTIONS"
Oct 31 11:49:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:43 +0100] "POST /query?db=&q=SHOW+SUBSCRIPTIONS HTTP/1.1" 200 321 "-" "KapacitorInfluxDBClient" ad07906f-dcfa-11e8-aa5d-000000000000 369
Oct 31 11:49:43 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:43,959 INFO:root: SIZE OF INPUT: 7643
Oct 31 11:49:43 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:44 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:43,959 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:44 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:44 EQLFRCL1PDL201 python2[2050]: Test Statistic                -23.335
Oct 31 11:49:44 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:44 EQLFRCL1PDL201 python2[2050]: Lags                               35
Oct 31 11:49:44 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:44 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:44 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:44 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:44 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:44 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:44 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:44,027 INFO:root: ending batch
Oct 31 11:49:44 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:44,029 INFO:root: Begin batch
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:46,023 INFO:root: SIZE OF INPUT: 7625
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:46,023 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: Test Statistic                -22.886
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: Lags                               35
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:46,086 INFO:root: ending batch
Oct 31 11:49:46 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:46,088 INFO:root: Begin batch
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:48,187 INFO:root: SIZE OF INPUT: 7639
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:48,187 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: Test Statistic                -24.536
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: Lags                               36
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:48,255 INFO:root: ending batch
Oct 31 11:49:48 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:48,257 INFO:root: Begin batch
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:50,286 INFO:root: SIZE OF INPUT: 7639
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:50 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:49:50 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" b0ec821c-dcfa-11e8-aa5e-000000000000 15557
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:50,287 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: Test Statistic                -25.438
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: Lags                               36
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:50,355 INFO:root: ending batch
Oct 31 11:49:50 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:50,357 INFO:root: Begin batch
Oct 31 11:49:50 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:49:50+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="49.021µs" status=200
Oct 31 11:49:50 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:52,370 INFO:root: SIZE OF INPUT: 7640
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:52,371 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: Test Statistic                -26.416
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:52,425 INFO:root: ending batch
Oct 31 11:49:52 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:52,427 INFO:root: Begin batch
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:54,374 INFO:root: SIZE OF INPUT: 7639
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:54,375 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: Test Statistic                -23.865
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: Lags                               34
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:54,430 INFO:root: ending batch
Oct 31 11:49:54 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:54,431 INFO:root: Begin batch
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:56,428 INFO:root: SIZE OF INPUT: 7614
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:56,428 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: Test Statistic                -32.198
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: Lags                               28
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:56,533 INFO:root: ending batch
Oct 31 11:49:56 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:56,535 INFO:root: Begin batch
Oct 31 11:49:57 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:58,635 INFO:root: SIZE OF INPUT: 7614
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:58,635 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: Test Statistic                -25.394
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: Lags                               33
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:58,691 INFO:root: ending batch
Oct 31 11:49:58 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:49:58,692 INFO:root: Begin batch
Oct 31 11:50:00 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:00 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" b6e26554-dcfa-11e8-aa5f-000000000000 15196
Oct 31 11:50:00 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:00+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="54.665µs" status=200
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:00,832 INFO:root: SIZE OF INPUT: 7575
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:00,833 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: Test Statistic                -27.659
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: Lags                               31
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:00,889 INFO:root: ending batch
Oct 31 11:50:00 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:00,890 INFO:root: Begin batch
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:02,866 INFO:root: SIZE OF INPUT: 7650
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:02,867 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.792
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:02,927 INFO:root: ending batch
Oct 31 11:50:02 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:02,929 INFO:root: Begin batch
Oct 31 11:50:04 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:04,962 INFO:root: SIZE OF INPUT: 7645
Oct 31 11:50:04 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:05 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:04,963 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:05 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:05 EQLFRCL1PDL201 python2[2050]: Test Statistic                -30.745
Oct 31 11:50:05 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:05 EQLFRCL1PDL201 python2[2050]: Lags                               28
Oct 31 11:50:05 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:05 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:05 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:05 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:05 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:05 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:05 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:05,016 INFO:root: ending batch
Oct 31 11:50:05 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:05,018 INFO:root: Begin batch
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:06,927 INFO:root: SIZE OF INPUT: 7655
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:06,927 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: Test Statistic                -28.776
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: Lags                               30
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:06,977 INFO:root: ending batch
Oct 31 11:50:06 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:06,978 INFO:root: Begin batch
Oct 31 11:50:07 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:50:08 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:08,981 INFO:root: SIZE OF INPUT: 7645
Oct 31 11:50:08 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:09 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:08,982 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:09 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:09 EQLFRCL1PDL201 python2[2050]: Test Statistic                -25.188
Oct 31 11:50:09 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:09 EQLFRCL1PDL201 python2[2050]: Lags                               32
Oct 31 11:50:09 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:09 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:09 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:09 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:09 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:09 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:09 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:09,039 INFO:root: ending batch
Oct 31 11:50:09 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:09,041 INFO:root: Begin batch
Oct 31 11:50:10 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:10 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" bcd84a8b-dcfa-11e8-aa60-000000000000 15816
Oct 31 11:50:10 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:10+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="49.807µs" status=200
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:11,213 INFO:root: SIZE OF INPUT: 7649
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:11,215 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: Test Statistic                -23.573
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: Lags                               34
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:11,276 INFO:root: ending batch
Oct 31 11:50:11 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:11,278 INFO:root: Begin batch
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:13,333 INFO:root: SIZE OF INPUT: 7630
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:13,334 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: Test Statistic                -28.312
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: Lags                               30
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:13,392 INFO:root: ending batch
Oct 31 11:50:13 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:13,393 INFO:root: Begin batch
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:15,245 INFO:root: SIZE OF INPUT: 7645
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:15,246 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.734
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:15,302 INFO:root: ending batch
Oct 31 11:50:15 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:15,303 INFO:root: Begin batch
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:17,135 INFO:root: SIZE OF INPUT: 7644
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:17,135 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: Test Statistic                -23.180
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: Lags                               34
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:17,190 INFO:root: ending batch
Oct 31 11:50:17 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:17,192 INFO:root: Begin batch
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:19,143 INFO:root: SIZE OF INPUT: 7659
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:19,143 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: Test Statistic                -27.479
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: Lags                               31
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:19,202 INFO:root: ending batch
Oct 31 11:50:19 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:19,204 INFO:root: Begin batch
Oct 31 11:50:20 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:20 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" c2ce2920-dcfa-11e8-aa61-000000000000 16569
Oct 31 11:50:20 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:20+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="26.282µs" status=200
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:21,298 INFO:root: SIZE OF INPUT: 7647
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:21,299 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: Test Statistic                -31.147
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:21,354 INFO:root: ending batch
Oct 31 11:50:21 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:21,356 INFO:root: Begin batch
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:23,436 INFO:root: SIZE OF INPUT: 7643
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:23,437 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.944
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:23,491 INFO:root: ending batch
Oct 31 11:50:23 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:23,492 INFO:root: Begin batch
Oct 31 11:50:24 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:25,490 INFO:root: SIZE OF INPUT: 7649
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:25,491 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: Test Statistic                -24.320
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: Lags                               35
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:25,548 INFO:root: ending batch
Oct 31 11:50:25 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:25,550 INFO:root: Begin batch
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:27,340 INFO:root: SIZE OF INPUT: 7644
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:27,341 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: Test Statistic                -26.853
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: Lags                               32
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:27,393 INFO:root: ending batch
Oct 31 11:50:27 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:27,394 INFO:root: Begin batch
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:29,180 INFO:root: SIZE OF INPUT: 7652
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:29,181 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.378
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:29,230 INFO:root: ending batch
Oct 31 11:50:29 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:29,232 INFO:root: Begin batch
Oct 31 11:50:30 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:30 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" c8c40e54-dcfa-11e8-aa62-000000000000 15219
Oct 31 11:50:30 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:30+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="33.464µs" status=200
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:31,212 INFO:root: SIZE OF INPUT: 7645
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:31,213 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: Test Statistic                -26.552
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: Lags                               33
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:31,284 INFO:root: ending batch
Oct 31 11:50:31 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:31,286 INFO:root: Begin batch
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:33,221 INFO:root: SIZE OF INPUT: 7650
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:33,221 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.177
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: Lags                               31
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:33,272 INFO:root: ending batch
Oct 31 11:50:33 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:33,274 INFO:root: Begin batch
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:35,099 INFO:root: SIZE OF INPUT: 7643
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:35,101 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.782
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: Lags                               28
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:35,165 INFO:root: ending batch
Oct 31 11:50:35 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:35,166 INFO:root: Begin batch
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:37,167 INFO:root: SIZE OF INPUT: 7659
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:37,168 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: Test Statistic                -26.387
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: Lags                               33
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:37,230 INFO:root: ending batch
Oct 31 11:50:37 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:37,232 INFO:root: Begin batch
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:39,243 INFO:root: SIZE OF INPUT: 7647
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:39,244 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.706
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:39,346 INFO:root: ending batch
Oct 31 11:50:39 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:39,348 INFO:root: Begin batch
Oct 31 11:50:40 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:40 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" ceb9faf2-dcfa-11e8-aa63-000000000000 15774
Oct 31 11:50:40 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:40+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="25.803µs" status=200
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:41 +0100] "GET /ping HTTP/1.1" 204 0 "-" "Go-http-client/1.1" cf4d313f-dcfa-11e8-aa64-000000000000 20
Oct 31 11:50:41 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:41+01:00" level=info msg="Response: No Content" component=server method=GET remote_addr="192.168.2.72:60769" response_time=1.171881ms status=204
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.269822Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW DATABASES"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - garbamoussa [31/Oct/2018:11:50:41 +0100] "POST /query?db=&epoch=ms&q=SHOW+DATABASES&rp= HTTP/1.1" 200 197 "-" "Go-http-client/1.1" cf4d7dd0-dcfa-11e8-aa65-000000000000 487
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.270540Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SELECT fieldKey, fieldType FROM telegraf.autogen._fieldKeys WHERE _name = 'myprohet-temp
'"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - garbamoussa [31/Oct/2018:11:50:41 +0100] "POST /query?db=telegraf&epoch=ms&q=SHOW+FIELD+KEYS+FROM+%22autogen%22.%22myprohet-temp%22&rp= HTTP/1.1" 200 143 "-" "Go-http-client/1.
1" cf4d975b-dcfa-11e8-aa66-000000000000 1352
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.271940Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW MEASUREMENTS ON telegraf"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - garbamoussa [31/Oct/2018:11:50:41 +0100] "POST /query?db=telegraf&epoch=ms&q=SHOW+MEASUREMENTS&rp= HTTP/1.1" 200 468 "-" "Go-http-client/1.1" cf4dcfb3-dcfa-11e8-aa67-0000000000
00 431
Oct 31 11:50:41 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:41+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60789" response_time=1.185594ms status=200
Oct 31 11:50:41 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:41+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60790" response_time=2.073887ms status=200
Oct 31 11:50:41 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:41+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60789" response_time="359.328µs" status=200
Oct 31 11:50:41 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:41+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60769" response_time=2.888377ms status=200
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.300504Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON telegraf"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.300534Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON _internal"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.300553Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON chronograf"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.300568Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ML"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.300584Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON testtxt"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.300599Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON NOAA_water_database"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.300616Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON Itron_database_365D"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.300630Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ITRON_365D"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.300646Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON test_arima"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.300660Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp_stat\""
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.300676Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp\""
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.300690Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-sinus\""
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - garbamoussa [31/Oct/2018:11:50:41 +0100] "POST /query?db=&epoch=ms&q=SHOW+RETENTION+POLICIES+ON+%22telegraf%22%3BSHOW+RETENTION+POLICIES+ON+%22_internal%22%3BSHOW+RETENTION+POL
ICIES+ON+%22chronograf%22%3BSHOW+RETENTION+POLICIES+ON+%22ML%22%3BSHOW+RETENTION+POLICIES+ON+%22testtxt%22%3BSHOW+RETENTION+POLICIES+ON+%22NOAA_water_database%22%3BSHOW+RETENTION+POLICIES+ON+%22Itron_database_365D%22%3BSHOW+RETENTION+POL
ICIES+ON+%22ITRON_365D%22%3BSHOW+RETENTION+POLICIES+ON+%22test_arima%22%3BSHOW+RETENTION+POLICIES+ON+%22test_arima-temp_stat%22%3BSHOW+RETENTION+POLICIES+ON+%22test_arima-temp%22%3BSHOW+RETENTION+POLICIES+ON+%22test_arima-sinus%22&rp= HT
TP/1.1" 200 233 "-" "Go-http-client/1.1" cf52271a-dcfa-11e8-aa68-000000000000 860
Oct 31 11:50:41 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:41+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60769" response_time=1.594415ms status=200
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.316247Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW TAG KEYS ON telegraf WHERE _name = 'myprohet-temp'"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - garbamoussa [31/Oct/2018:11:50:41 +0100] "POST /query?db=telegraf&epoch=ms&q=SHOW+TAG+KEYS+FROM+%22autogen%22.%22myprohet-temp%22&rp=autogen HTTP/1.1" 200 57 "-" "Go-http-clien
t/1.1" cf549368-dcfa-11e8-aa69-000000000000 425
Oct 31 11:50:41 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:41+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60769" response_time=5.427003ms status=200
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:41.370448Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SELECT yhat_lower, yhat_upper, yhat FROM telegraf.autogen.\"myprohet-temp\" WHERE time >
 now() - 15m"
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - garbamoussa [31/Oct/2018:11:50:41 +0100] "POST /query?db=&epoch=ms&q=SELECT+%22yhat_lower%22%2C+%22yhat_upper%22%2C+%22yhat%22+FROM+%22telegraf%22.%22autogen%22.%22myprohet-tem
p%22+WHERE+time+%3E+now%28%29+-+15m&rp= HTTP/1.1" 200 561 "-" "Go-http-client/1.1" cf5cd309-dcfa-11e8-aa6a-000000000000 1027
Oct 31 11:50:41 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:41+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60769" response_time=1.786335ms status=200
Oct 31 11:50:41 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - garbamoussa [31/Oct/2018:11:50:41 +0100] "POST /query?db=telegraf&epoch=ms&q=SHOW+TAG+VALUES+FROM+%22autogen%22.%22myprohet-temp%22+WITH+KEY+IN+%28%29&rp=autogen HTTP/1.1" 400
81 "-" "Go-http-client/1.1" cf5f8538-dcfa-11e8-aa6b-000000000000 84
Oct 31 11:50:41 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:41+01:00" level=error msg="Error message received status code 400 from server: err: error parsing query: found ), expected identifier at line 1, char 61" component=
server http_status =400
Oct 31 11:50:41 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:41+01:00" level=info msg="Response: Bad Request" component=server method=POST remote_addr="192.168.2.72:60769" response_time="958.157µs" status=400
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:41,490 INFO:root: SIZE OF INPUT: 7638
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:41,491 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.239
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: Lags                               30
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:41,545 INFO:root: ending batch
Oct 31 11:50:41 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:41,546 INFO:root: Begin batch
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:43,548 INFO:root: SIZE OF INPUT: 7639
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:43,550 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: Test Statistic                -31.599
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: Lags                               28
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:43,612 INFO:root: ending batch
Oct 31 11:50:43 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:43,614 INFO:root: Begin batch
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "GET /ping HTTP/1.1" 204 0 "-" "KapacitorInfluxDBClient" d0c92b1d-dcfa-11e8-aa6c-000000000000 20
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.758962Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW DATABASES"
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+DATABASES HTTP/1.1" 200 197 "-" "KapacitorInfluxDBClient" d0c94dc0-dcfa-11e8-aa6d-000000000000 465
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.759810Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON telegraf"
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+telegraf HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" d0c96cae-dcfa-11e8-aa6e-000000000000 271
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.761312Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON _internal"
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+_internal HTTP/1.1" 200 153 "-" "KapacitorInfluxDBClient" d0c9a958-dcfa-11e8-aa6f-000000000000 217
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.762429Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON chronograf"
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+chronograf HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" d0c9d304-dcfa-11e8-aa70-000000000000 270
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.763500Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ML"
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+ML HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" d0c9fea3-dcfa-11e8-aa71-000000000000 219
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.764270Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON testtxt"
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+testtxt HTTP/1.1" 200 169 "-" "KapacitorInfluxDBClient" d0ca1c64-dcfa-11e8-aa72-000000000000 235
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.764802Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON NOAA_water_database"
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+NOAA_water_database HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" d0ca312b-dcfa-11e8-aa73-0000000
00000 226
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.765375Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON Itron_database_365D"
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+Itron_database_365D HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" d0ca47b7-dcfa-11e8-aa74-0000000
00000 223
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.765879Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ITRON_365D"
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+ITRON_365D HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" d0ca5b46-dcfa-11e8-aa75-000000000000 229
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.766363Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON test_arima"
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+test_arima HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" d0ca6e25-dcfa-11e8-aa76-000000000000 229
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.766903Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp_stat\""
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-temp_stat%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" d0ca839b-dcfa-11e8-aa77-
000000000000 217
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.767410Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp\""
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-temp%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" d0ca9723-dcfa-11e8-aa78-00000
0000000 226
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.767896Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-sinus\""
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-sinus%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" d0caaa95-dcfa-11e8-aa79-0000
00000000 211
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:43.768467Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW SUBSCRIPTIONS"
Oct 31 11:50:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:43 +0100] "POST /query?db=&q=SHOW+SUBSCRIPTIONS HTTP/1.1" 200 321 "-" "KapacitorInfluxDBClient" d0cabf62-dcfa-11e8-aa7a-000000000000 435
Oct 31 11:50:44 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:45,577 INFO:root: SIZE OF INPUT: 7657
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:45,577 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: Test Statistic                -31.003
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: Lags                               28
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:45,628 INFO:root: ending batch
Oct 31 11:50:45 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:45,630 INFO:root: Begin batch
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:47,434 INFO:root: SIZE OF INPUT: 7655
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:47,434 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.489
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: Lags                               28
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:47,487 INFO:root: ending batch
Oct 31 11:50:47 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:47,489 INFO:root: Begin batch
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:49,298 INFO:root: SIZE OF INPUT: 7646
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:49,298 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: Test Statistic                -31.082
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: Lags                               28
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:49,350 INFO:root: ending batch
Oct 31 11:50:49 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:49,351 INFO:root: Begin batch
Oct 31 11:50:50 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:50:50 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" d4afcab9-dcfa-11e8-aa7b-000000000000 17055
Oct 31 11:50:50 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:50+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="26.357µs" status=200
Oct 31 11:50:51 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:51.295609Z lvl=info msg="Retention policy deletion check (start)" log_id=0BSDJnDW000 service=retention trace_id=0BURnt7l000 op_name=retention_delete_check op_event=start
Oct 31 11:50:51 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:51.295823Z lvl=info msg="Retention policy deletion check (end)" log_id=0BSDJnDW000 service=retention trace_id=0BURnt7l000 op_name=retention_delete_check op_event=end op_e
lapsed=0.222ms
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:51,319 INFO:root: SIZE OF INPUT: 7662
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:51,319 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: Test Statistic                -27.171
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: Lags                               32
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:51,377 INFO:root: ending batch
Oct 31 11:50:51 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:51,378 INFO:root: Begin batch
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:53,433 INFO:root: SIZE OF INPUT: 7656
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:53,434 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: Test Statistic                -26.519
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: Lags                               32
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:53,491 INFO:root: ending batch
Oct 31 11:50:53 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:53,492 INFO:root: Begin batch
Oct 31 11:50:53 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:55,480 INFO:root: SIZE OF INPUT: 7610
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:55,481 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: Test Statistic                -31.182
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:55,532 INFO:root: ending batch
Oct 31 11:50:55 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:55,534 INFO:root: Begin batch
Oct 31 11:50:55 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:55+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60769" response_time="343.246µs" status=200
Oct 31 11:50:55 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:55.805158Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SELECT yhat_lower, yhat FROM telegraf.autogen.\"myprohet-temp\" WHERE time > now() - 15m
"
Oct 31 11:50:55 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - garbamoussa [31/Oct/2018:11:50:55 +0100] "POST /query?db=&epoch=ms&q=SELECT+%22yhat_lower%22%2C+%22yhat%22+FROM+%22telegraf%22.%22autogen%22.%22myprohet-temp%22+WHERE+time+%3E+
now%28%29+-+15m&rp= HTTP/1.1" 200 433 "-" "Go-http-client/1.1" d7f75ddb-dcfa-11e8-aa7c-000000000000 838
Oct 31 11:50:55 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:55+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60769" response_time=1.57359ms status=200
Oct 31 11:50:56 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:56+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60769" response_time="261.029µs" status=200
Oct 31 11:50:56 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:50:56.517848Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SELECT yhat FROM telegraf.autogen.\"myprohet-temp\" WHERE time > now() - 15m"
Oct 31 11:50:56 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - garbamoussa [31/Oct/2018:11:50:56 +0100] "POST /query?db=&epoch=ms&q=SELECT+%22yhat%22+FROM+%22telegraf%22.%22autogen%22.%22myprohet-temp%22+WHERE+time+%3E+now%28%29+-+15m&rp=
HTTP/1.1" 200 301 "-" "Go-http-client/1.1" d86420e3-dcfa-11e8-aa7d-000000000000 687
Oct 31 11:50:56 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:50:56+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60769" response_time=1.324965ms status=200
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:57,362 INFO:root: SIZE OF INPUT: 7616
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:57,363 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: Test Statistic                -31.202
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: Lags                               28
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:57,410 INFO:root: ending batch
Oct 31 11:50:57 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:57,412 INFO:root: Begin batch
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:59,222 INFO:root: SIZE OF INPUT: 7611
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:59,222 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.675
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: Lags                               28
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:59,280 INFO:root: ending batch
Oct 31 11:50:59 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:50:59,282 INFO:root: Begin batch
Oct 31 11:51:00 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:00 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" daa5b255-dcfa-11e8-aa7e-000000000000 16524
Oct 31 11:51:00 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:00+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="28.514µs" status=200
Oct 31 11:51:01 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:01,393 INFO:root: SIZE OF INPUT: 7612
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:01,394 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: Test Statistic                -32.189
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: Lags                               28
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:01,455 INFO:root: ending batch
Oct 31 11:51:01 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:01,457 INFO:root: Begin batch
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:03,484 INFO:root: SIZE OF INPUT: 7646
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:03,485 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: Test Statistic                -22.328
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: Lags                               35
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:03,544 INFO:root: ending batch
Oct 31 11:51:03 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:03,546 INFO:root: Begin batch
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:05,495 INFO:root: SIZE OF INPUT: 7644
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:05,496 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: Test Statistic                -25.741
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: Lags                               32
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:05,549 INFO:root: ending batch
Oct 31 11:51:05 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:05,551 INFO:root: Begin batch
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:07,638 INFO:root: SIZE OF INPUT: 7624
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:07,639 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: Test Statistic                -23.779
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: Lags                               33
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:07,703 INFO:root: ending batch
Oct 31 11:51:07 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:07,704 INFO:root: Begin batch
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:09,479 INFO:root: SIZE OF INPUT: 6821
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:09,479 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: Test Statistic                -23.504
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: Lags                               33
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:09,550 INFO:root: ending batch
Oct 31 11:51:09 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:09,551 INFO:root: Begin batch
Oct 31 11:51:10 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:10 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" e09b8d86-dcfa-11e8-aa7f-000000000000 17366
Oct 31 11:51:10 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:10+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="26.321µs" status=200
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:11,223 INFO:root: SIZE OF INPUT: 6862
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:11,224 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: Test Statistic                -22.962
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: Lags                               32
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:11,270 INFO:root: ending batch
Oct 31 11:51:11 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:11,272 INFO:root: Begin batch
Oct 31 11:51:11 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:12,941 INFO:root: SIZE OF INPUT: 6866
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:12,942 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: Test Statistic                -22.468
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: Lags                               34
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:12,992 INFO:root: ending batch
Oct 31 11:51:12 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:12,993 INFO:root: Begin batch
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:14,821 INFO:root: SIZE OF INPUT: 7647
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:14,822 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: Test Statistic                -24.455
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: Lags                               36
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:14,878 INFO:root: ending batch
Oct 31 11:51:14 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:14,880 INFO:root: Begin batch
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:16,524 INFO:root: SIZE OF INPUT: 6934
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:16,524 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: Test Statistic                -23.809
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: Lags                               35
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:16,575 INFO:root: ending batch
Oct 31 11:51:16 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:16,576 INFO:root: Begin batch
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:18,397 INFO:root: SIZE OF INPUT: 7623
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:18,397 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: Test Statistic                -27.434
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: Lags                               32
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:18,450 INFO:root: ending batch
Oct 31 11:51:18 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:18,452 INFO:root: Begin batch
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:20,276 INFO:root: SIZE OF INPUT: 7622
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:20,276 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: Test Statistic                -24.871
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: Lags                               30
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:20,326 INFO:root: ending batch
Oct 31 11:51:20 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:20,328 INFO:root: Begin batch
Oct 31 11:51:20 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:20 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" e6916b22-dcfa-11e8-aa80-000000000000 26271
Oct 31 11:51:20 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:20+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time="41.665µs" status=200
Oct 31 11:51:21 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:21 +0100] "GET /ping HTTP/1.1" 204 0 "-" "Go-http-client/1.1" e78d83a7-dcfa-11e8-aa81-000000000000 20
Oct 31 11:51:21 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:21+01:00" level=info msg="Response: No Content" component=server method=GET remote_addr="192.168.2.72:60769" response_time="452.856µs" status=204
Oct 31 11:51:21 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:21+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60789" response_time="785.507µs" status=200
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:22,241 INFO:root: SIZE OF INPUT: 7487
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:22,241 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: Test Statistic                -18.506
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: Lags                               36
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:22,297 INFO:root: ending batch
Oct 31 11:51:22 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:22,299 INFO:root: Begin batch
Oct 31 11:51:23 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:23 +0100] "GET /ping HTTP/1.1" 204 0 "-" "Go-http-client/1.1" e839714c-dcfa-11e8-aa82-000000000000 19
Oct 31 11:51:23 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:23+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60789" response_time="110.475µs" status=200
Oct 31 11:51:23 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:23+01:00" level=info msg="Response: No Content" component=server method=GET remote_addr="192.168.2.72:60769" response_time="546.906µs" status=204
Oct 31 11:51:23 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:23+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60769" response_time=664.924855ms status=200
Oct 31 11:51:23 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:24,455 INFO:root: SIZE OF INPUT: 7616
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:24,456 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: Test Statistic                -32.071
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:24,521 INFO:root: ending batch
Oct 31 11:51:24 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:24,523 INFO:root: Begin batch
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:25 +0100] "GET /ping HTTP/1.1" 204 0 "-" "Go-http-client/1.1" e9b9cfec-dcfa-11e8-aa83-000000000000 19
Oct 31 11:51:25 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:25+01:00" level=info msg="Response: No Content" component=server method=GET remote_addr="192.168.2.72:60769" response_time=4.446754ms status=204
Oct 31 11:51:25 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:25+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="142.031µs" status=200
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:25.605126Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW DATABASES"
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - garbamoussa [31/Oct/2018:11:51:25 +0100] "POST /query?db=&epoch=ms&q=SHOW+DATABASES&rp= HTTP/1.1" 200 197 "-" "Go-http-client/1.1" e9ba8155-dcfa-11e8-aa84-000000000000 382
Oct 31 11:51:25 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:25+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60789" response_time=5.193048ms status=200
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:25.617276Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON telegraf"
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:25.617310Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON _internal"
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:25.617331Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON chronograf"
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:25.617345Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ML"
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:25.617361Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON testtxt"
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:25.617376Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON NOAA_water_database"
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:25.617391Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON Itron_database_365D"
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:25.617406Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ITRON_365D"
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:25.617425Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON test_arima"
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:25.617439Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp_stat\""
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:25.617456Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp\""
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:25.617470Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-sinus\""
Oct 31 11:51:25 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - garbamoussa [31/Oct/2018:11:51:25 +0100] "POST /query?db=&epoch=ms&q=SHOW+RETENTION+POLICIES+ON+%22telegraf%22%3BSHOW+RETENTION+POLICIES+ON+%22_internal%22%3BSHOW+RETENTION+POL
ICIES+ON+%22chronograf%22%3BSHOW+RETENTION+POLICIES+ON+%22ML%22%3BSHOW+RETENTION+POLICIES+ON+%22testtxt%22%3BSHOW+RETENTION+POLICIES+ON+%22NOAA_water_database%22%3BSHOW+RETENTION+POLICIES+ON+%22Itron_database_365D%22%3BSHOW+RETENTION+POL
ICIES+ON+%22ITRON_365D%22%3BSHOW+RETENTION+POLICIES+ON+%22test_arima%22%3BSHOW+RETENTION+POLICIES+ON+%22test_arima-temp_stat%22%3BSHOW+RETENTION+POLICIES+ON+%22test_arima-temp%22%3BSHOW+RETENTION+POLICIES+ON+%22test_arima-sinus%22&rp= HT
TP/1.1" 200 233 "-" "Go-http-client/1.1" e9bc56af-dcfa-11e8-aa85-000000000000 793
Oct 31 11:51:25 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:25+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60769" response_time=1.506636ms status=200
Oct 31 11:51:25 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:25+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60789" response_time=5.79131ms status=200
Oct 31 11:51:25 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:25+01:00" level=info msg="Response: No Content" component=server method=GET remote_addr="192.168.2.72:60769" response_time="752.604µs" status=204
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:26,469 INFO:root: SIZE OF INPUT: 7596
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:26,470 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: Test Statistic                -32.832
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:26,518 INFO:root: ending batch
Oct 31 11:51:26 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:26,519 INFO:root: Begin batch
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:28,343 INFO:root: SIZE OF INPUT: 7646
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:28,344 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: Test Statistic                -24.848
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: Lags                               36
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:28,398 INFO:root: ending batch
Oct 31 11:51:28 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:28,400 INFO:root: Begin batch
Oct 31 11:51:29 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:29+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="95.278µs" status=200
Oct 31 11:51:29 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:29 +0100] "GET /ping HTTP/1.1" 204 0 "-" "Go-http-client/1.1" ec1bdfd4-dcfa-11e8-aa86-000000000000 19
Oct 31 11:51:29 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:29+01:00" level=info msg="Response: No Content" component=server method=GET remote_addr="192.168.2.72:60789" response_time="514.52µs" status=204
Oct 31 11:51:30 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:30+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60789" response_time=545.897807ms status=200
Oct 31 11:51:30 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:30 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" ec8751c4-dcfa-11e8-aa87-000000000000 16891
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:30,367 INFO:root: SIZE OF INPUT: 7645
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:30,368 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: Test Statistic                -33.420
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: Lags                               28
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:30,418 INFO:root: ending batch
Oct 31 11:51:30 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:30,420 INFO:root: Begin batch
Oct 31 11:51:31 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:31+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60789" response_time="29.688µs" status=200
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:32,398 INFO:root: SIZE OF INPUT: 7639
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:32,399 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: Test Statistic                -24.358
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: Lags                               35
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:32,465 INFO:root: ending batch
Oct 31 11:51:32 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:32,466 INFO:root: Agent finished connection 4
Oct 31 11:51:32 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:32+01:00" level=info msg="Response: OK" component=server method=PATCH remote_addr="192.168.2.72:60789" response_time=707.549772ms status=200
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:32 +0100] "GET /ping HTTP/1.1" 204 0 "-" "Go-http-client/1.1" ee1bf460-dcfa-11e8-aa88-000000000000 26
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:32.954914Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW DATABASES"
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - garbamoussa [31/Oct/2018:11:51:32 +0100] "POST /query?db=&epoch=ms&q=SHOW+DATABASES&rp= HTTP/1.1" 200 197 "-" "Go-http-client/1.1" ee1bfbc1-dcfa-11e8-aa89-000000000000 542
Oct 31 11:51:32 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:32+01:00" level=info msg="Response: No Content" component=server method=GET remote_addr="192.168.2.72:60789" response_time=1.337185ms status=204
Oct 31 11:51:32 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:32+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60789" response_time="201.454µs" status=200
Oct 31 11:51:32 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:32+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60790" response_time=1.977532ms status=200
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:32.969226Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON telegraf"
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:32.969335Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON _internal"
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:32.969368Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON chronograf"
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:32.969392Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ML"
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:32.969420Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON testtxt"
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:32.969451Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON NOAA_water_database"
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:32.969478Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON Itron_database_365D"
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:32.969502Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ITRON_365D"
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:32.969528Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON test_arima"
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:32.969552Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp_stat\""
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:32.969580Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp\""
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:32.969604Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-sinus\""
Oct 31 11:51:32 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:32+01:00" level=info msg="Response: OK" component=server method=POST remote_addr="192.168.2.72:60790" response_time=2.248064ms status=200
Oct 31 11:51:32 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:32+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60789" response_time=10.723719ms status=200
Oct 31 11:51:32 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - garbamoussa [31/Oct/2018:11:51:32 +0100] "POST /query?db=&epoch=ms&q=SHOW+RETENTION+POLICIES+ON+%22telegraf%22%3BSHOW+RETENTION+POLICIES+ON+%22_internal%22%3BSHOW+RETENTION+POL
ICIES+ON+%22chronograf%22%3BSHOW+RETENTION+POLICIES+ON+%22ML%22%3BSHOW+RETENTION+POLICIES+ON+%22testtxt%22%3BSHOW+RETENTION+POLICIES+ON+%22NOAA_water_database%22%3BSHOW+RETENTION+POLICIES+ON+%22Itron_database_365D%22%3BSHOW+RETENTION+POL
ICIES+ON+%22ITRON_365D%22%3BSHOW+RETENTION+POLICIES+ON+%22test_arima%22%3BSHOW+RETENTION+POLICIES+ON+%22test_arima-temp_stat%22%3BSHOW+RETENTION+POLICIES+ON+%22test_arima-temp%22%3BSHOW+RETENTION+POLICIES+ON+%22test_arima-sinus%22&rp= HT
TP/1.1" 200 233 "-" "Go-http-client/1.1" ee1e218f-dcfa-11e8-aa8a-000000000000 1309
Oct 31 11:51:33 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:33+01:00" level=info msg="Response: No Content" component=server method=GET remote_addr="192.168.2.72:60789" response_time=1.814491ms status=204
Oct 31 11:51:37 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:51:40 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:40 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" f27d3bb7-dcfa-11e8-aa8b-000000000000 17737
Oct 31 11:51:41 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:41+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="37.043µs" status=200
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "GET /ping HTTP/1.1" 204 0 "-" "KapacitorInfluxDBClient" f48c7867-dcfa-11e8-aa8c-000000000000 26
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.758855Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW DATABASES"
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+DATABASES HTTP/1.1" 200 197 "-" "KapacitorInfluxDBClient" f48c88fd-dcfa-11e8-aa8d-000000000000 1011
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.760387Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON telegraf"
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+telegraf HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" f48cc2ec-dcfa-11e8-aa8e-000000000000 522
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.761210Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON _internal"
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+_internal HTTP/1.1" 200 153 "-" "KapacitorInfluxDBClient" f48ce822-dcfa-11e8-aa8f-000000000000 357
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.762233Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON chronograf"
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+chronograf HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" f48d04d0-dcfa-11e8-aa90-000000000000 643
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.763268Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ML"
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+ML HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" f48d2efd-dcfa-11e8-aa91-000000000000 655
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.764343Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON testtxt"
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+testtxt HTTP/1.1" 200 169 "-" "KapacitorInfluxDBClient" f48d5aea-dcfa-11e8-aa92-000000000000 700
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.765487Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON NOAA_water_database"
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+NOAA_water_database HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" f48d8d48-dcfa-11e8-aa93-0000000
00000 545
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.766437Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON Itron_database_365D"
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+Itron_database_365D HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" f48db2c9-dcfa-11e8-aa94-0000000
00000 581
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.767436Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ITRON_365D"
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+ITRON_365D HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" f48ddaf7-dcfa-11e8-aa95-000000000000 538
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.768429Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON test_arima"
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+test_arima HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" f48e0107-dcfa-11e8-aa96-000000000000 548
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.769384Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp_stat\""
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-temp_stat%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" f48e26ba-dcfa-11e8-aa97-
000000000000 426
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.770196Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp\""
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-temp%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" f48e473c-dcfa-11e8-aa98-00000
0000000 393
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.771021Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-sinus\""
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-sinus%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" f48e66cf-dcfa-11e8-aa99-0000
00000000 411
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:51:43.771778Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW SUBSCRIPTIONS"
Oct 31 11:51:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:43 +0100] "POST /query?db=&q=SHOW+SUBSCRIPTIONS HTTP/1.1" 200 321 "-" "KapacitorInfluxDBClient" f48e8524-dcfa-11e8-aa9a-000000000000 652
Oct 31 11:51:44 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:44+01:00" level=info msg="Response: OK" component=server method=PUT remote_addr="192.168.2.72:60790" response_time=58.482366ms status=200
Oct 31 11:51:46 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:46 +0100] "GET /ping HTTP/1.1" 204 0 "-" "Go-http-client/1.1" f66a08bc-dcfa-11e8-aa9b-000000000000 26
Oct 31 11:51:46 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:46+01:00" level=info msg="Response: No Content" component=server method=GET remote_addr="192.168.2.72:60790" response_time="614.743µs" status=204
Oct 31 11:51:46 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:46+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60798" response_time="166.847µs" status=200
Oct 31 11:51:47 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:47+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time=916.895325ms status=200
Oct 31 11:51:50 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:51:50 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" f8731c58-dcfa-11e8-aa9c-000000000000 16669
Oct 31 11:51:50 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:50,952 INFO:root: Starting Agent for connection 5
Oct 31 11:51:50 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:51:50,953 INFO:root: init
Oct 31 11:51:50 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:50+01:00" level=info msg="Response: OK" component=server method=PATCH remote_addr="192.168.2.72:60790" response_time=84.741278ms status=200
Oct 31 11:51:51 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:51:51+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="26.089µs" status=200
Oct 31 11:51:53 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:52:00 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:00 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" fe6906d9-dcfa-11e8-aa9d-000000000000 15809
Oct 31 11:52:01 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:52:01+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="45.683µs" status=200
Oct 31 11:52:06 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:52:10 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:10 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 045edd44-dcfb-11e8-aa9e-000000000000 16923
Oct 31 11:52:11 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:52:11+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="52.894µs" status=200
Oct 31 11:52:20 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:20 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 0a54b945-dcfb-11e8-aa9f-000000000000 17742
Oct 31 11:52:21 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:52:21+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="34.019µs" status=200
Oct 31 11:52:22 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:52:30 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:30 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 104a9e37-dcfb-11e8-aaa0-000000000000 18347
Oct 31 11:52:31 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:52:31+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="40.558µs" status=200
Oct 31 11:52:34 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:52:40 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:40 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 16407ced-dcfb-11e8-aaa1-000000000000 19259
Oct 31 11:52:41 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:52:41+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="33.799µs" status=200
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "GET /ping HTTP/1.1" 204 0 "-" "KapacitorInfluxDBClient" 184fc07a-dcfb-11e8-aaa2-000000000000 82
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.758892Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW DATABASES"
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+DATABASES HTTP/1.1" 200 197 "-" "KapacitorInfluxDBClient" 184fd443-dcfb-11e8-aaa3-000000000000 690
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.759968Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON telegraf"
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+telegraf HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 184fff89-dcfb-11e8-aaa4-000000000000 527
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.760891Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON _internal"
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+_internal HTTP/1.1" 200 153 "-" "KapacitorInfluxDBClient" 185021ba-dcfb-11e8-aaa5-000000000000 393
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.761720Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON chronograf"
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+chronograf HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 18504166-dcfb-11e8-aaa6-000000000000 429
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.762589Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ML"
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+ML HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 18505f91-dcfb-11e8-aaa7-000000000000 528
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.763478Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON testtxt"
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+testtxt HTTP/1.1" 200 169 "-" "KapacitorInfluxDBClient" 1850829a-dcfb-11e8-aaa8-000000000000 581
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.764501Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON NOAA_water_database"
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+NOAA_water_database HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 1850a92f-dcfb-11e8-aaa9-0000000
00000 547
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.765383Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON Itron_database_365D"
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+Itron_database_365D HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 1850ce11-dcfb-11e8-aaaa-0000000
00000 563
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.766399Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ITRON_365D"
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+ITRON_365D HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 1850f292-dcfb-11e8-aaab-000000000000 565
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.767595Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON test_arima"
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+test_arima HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 185126be-dcfb-11e8-aaac-000000000000 404
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.768559Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp_stat\""
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-temp_stat%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 185149dd-dcfb-11e8-aaad-
000000000000 586
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.769663Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp\""
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-temp%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 18517440-dcfb-11e8-aaae-00000
0000000 504
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.770463Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-sinus\""
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-sinus%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 185198eb-dcfb-11e8-aaaf-0000
00000000 567
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:52:43.771451Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW SUBSCRIPTIONS"
Oct 31 11:52:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:43 +0100] "POST /query?db=&q=SHOW+SUBSCRIPTIONS HTTP/1.1" 200 321 "-" "KapacitorInfluxDBClient" 1851c008-dcfb-11e8-aab0-000000000000 738
Oct 31 11:52:48 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:52:50 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:52:50 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 1c3661a0-dcfb-11e8-aab1-000000000000 17896
Oct 31 11:52:51 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:52:51+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time=2.185243ms status=200
Oct 31 11:53:00 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:00.003184Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SELECT responsetime FROM telegraf.autogen.servicepilot_ping WHERE time >= '2018-10-23T10
:53:00Z' AND time < '2018-10-30T10:53:00Z' GROUP BY object"
Oct 31 11:53:00 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:00 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 222c360c-dcfb-11e8-aab3-000000000000 17596
Oct 31 11:53:01 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:53:01 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:53:01+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="33.251µs" status=200
Oct 31 11:53:08 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:00 +0100] "POST /query?db=&q=SELECT+responsetime+FROM+telegraf.autogen.servicepilot_ping+WHERE+time+%3E%3D+%272018-10-23T10%3A53%3A00Z%27+AND+time+%3C+%272
018-10-30T10%3A53%3A00Z%27+GROUP+BY+object HTTP/1.1" 200 5614214 "-" "KapacitorInfluxDBClient" 21fe7a30-dcfb-11e8-aab2-000000000000 8104165
Oct 31 11:53:10 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:10 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 28222045-dcfb-11e8-aab4-000000000000 91854
Oct 31 11:53:10 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:10,903 INFO:root: Begin batch
Oct 31 11:53:11 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:53:11+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="26.485µs" status=200
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:12,885 INFO:root: SIZE OF INPUT: 7607
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:12,886 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: Test Statistic                -25.208
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: Lags                               32
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:12,942 INFO:root: ending batch
Oct 31 11:53:12 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:12,944 INFO:root: Begin batch
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:14,878 INFO:root: SIZE OF INPUT: 7606
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:14,879 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: Test Statistic                -30.687
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: Lags                               28
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:14,931 INFO:root: ending batch
Oct 31 11:53:14 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:14,932 INFO:root: Begin batch
Oct 31 11:53:16 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:17,008 INFO:root: SIZE OF INPUT: 7632
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:17,009 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: Test Statistic                -31.674
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:17,069 INFO:root: ending batch
Oct 31 11:53:17 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:17,071 INFO:root: Begin batch
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:19,104 INFO:root: SIZE OF INPUT: 7632
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:19,105 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: Test Statistic                -25.803
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: Lags                               32
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:19,191 INFO:root: ending batch
Oct 31 11:53:19 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:19,194 INFO:root: Begin batch
Oct 31 11:53:20 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:20 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 2e17f741-dcfb-11e8-aab5-000000000000 15181
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:21,313 INFO:root: SIZE OF INPUT: 7668
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:21,314 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: Test Statistic                -30.435
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:21,368 INFO:root: ending batch
Oct 31 11:53:21 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:21,369 INFO:root: Begin batch
Oct 31 11:53:21 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:53:21+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="27.673µs" status=200
Oct 31 11:53:23 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:23,266 INFO:root: SIZE OF INPUT: 7662
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:23,267 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.279
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:23,316 INFO:root: ending batch
Oct 31 11:53:23 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:23,318 INFO:root: Begin batch
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:25,350 INFO:root: SIZE OF INPUT: 7654
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:25,351 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.527
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:25,404 INFO:root: ending batch
Oct 31 11:53:25 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:25,405 INFO:root: Begin batch
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:27,443 INFO:root: SIZE OF INPUT: 7649
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:27,444 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: Test Statistic                -30.420
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:27,502 INFO:root: ending batch
Oct 31 11:53:27 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:27,504 INFO:root: Begin batch
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:29,442 INFO:root: SIZE OF INPUT: 7645
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:29,443 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: Test Statistic                -28.400
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: Lags                               30
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:29,493 INFO:root: ending batch
Oct 31 11:53:29 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:29,495 INFO:root: Begin batch
Oct 31 11:53:30 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:30 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 340dea9f-dcfb-11e8-aab6-000000000000 17366
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:31,610 INFO:root: SIZE OF INPUT: 7655
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:31 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:53:31+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="28.275µs" status=200
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:31,611 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.875
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: Lags                               29
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:31,665 INFO:root: ending batch
Oct 31 11:53:31 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:31,667 INFO:root: Begin batch
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:33,670 INFO:root: SIZE OF INPUT: 7667
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:33,670 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: Test Statistic                -29.049
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: Lags                               30
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:33,724 INFO:root: ending batch
Oct 31 11:53:33 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:33,725 INFO:root: Begin batch
Oct 31 11:53:34 EQLFRCL1PDL201 dhclient[586]: DHCPREQUEST of 192.168.2.177 on eth0 to 192.168.2.26 port 67
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:35,792 INFO:root: SIZE OF INPUT: 7638
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:35,792 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: Test Statistic                -25.728
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: Lags                               33
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:35,848 INFO:root: ending batch
Oct 31 11:53:35 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:35,850 INFO:root: Begin batch
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:37,778 INFO:root: SIZE OF INPUT: 7636
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:37,779 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: Test Statistic                -24.550
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: Lags                               36
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:37,849 INFO:root: ending batch
Oct 31 11:53:37 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:37,851 INFO:root: Begin batch
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:39,927 INFO:root: SIZE OF INPUT: 7639
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:39,928 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: Test Statistic                -26.954
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: Lags                               32
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:39,983 INFO:root: ending batch
Oct 31 11:53:39 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:39,985 INFO:root: Begin batch
Oct 31 11:53:40 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:40 +0100] "POST /write?db=telegraf HTTP/1.1" 204 0 "-" "telegraf" 3a03bacb-dcfb-11e8-aab7-000000000000 14504
Oct 31 11:53:41 EQLFRCL1PDL201 chronograf[16176]: time="2018-10-31T11:53:41+01:00" level=info msg="Response: OK" component=server method=GET remote_addr="192.168.2.72:60790" response_time="26.854µs" status=200
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:41,888 INFO:root: SIZE OF INPUT: 7621
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:41,889 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: Test Statistic                -25.466
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: Lags                               33
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:41,941 INFO:root: ending batch
Oct 31 11:53:41 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:41,943 INFO:root: Begin batch
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:43,748 INFO:root: SIZE OF INPUT: 7643
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "GET /ping HTTP/1.1" 204 0 "-" "KapacitorInfluxDBClient" 3c12fbf0-dcfb-11e8-aab8-000000000000 19
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.758648Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW DATABASES"
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+DATABASES HTTP/1.1" 200 197 "-" "KapacitorInfluxDBClient" 3c131371-dcfb-11e8-aab9-000000000000 481
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.759926Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON telegraf"
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+telegraf HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 3c1346b7-dcfb-11e8-aaba-000000000000 336
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.760559Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON _internal"
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+_internal HTTP/1.1" 200 153 "-" "KapacitorInfluxDBClient" 3c135d91-dcfb-11e8-aabb-000000000000 218
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.761022Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON chronograf"
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+chronograf HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 3c136faf-dcfb-11e8-aabc-000000000000 214
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.761474Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ML"
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+ML HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 3c1381ed-dcfb-11e8-aabd-000000000000 200
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.764463Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON testtxt"
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+testtxt HTTP/1.1" 200 169 "-" "KapacitorInfluxDBClient" 3c13f6a9-dcfb-11e8-aabe-000000000000 207
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.764939Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON NOAA_water_database"
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+NOAA_water_database HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 3c14092b-dcfb-11e8-aabf-0000000
00000 217
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.765420Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON Itron_database_365D"
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+Itron_database_365D HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 3c141c10-dcfb-11e8-aac0-0000000
00000 199
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.765911Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON ITRON_365D"
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+ITRON_365D HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 3c142f4e-dcfb-11e8-aac1-000000000000 198
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.766379Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON test_arima"
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+test_arima HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 3c144063-dcfb-11e8-aac2-000000000000 251
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.766880Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp_stat\""
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-temp_stat%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 3c14544b-dcfb-11e8-aac3-
000000000000 224
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.767326Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-temp\""
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-temp%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 3c14673b-dcfb-11e8-aac4-00000
0000000 352
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.767906Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW RETENTION POLICIES ON \"test_arima-sinus\""
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+RETENTION+POLICIES+ON+%22test_arima-sinus%22 HTTP/1.1" 200 149 "-" "KapacitorInfluxDBClient" 3c147e66-dcfb-11e8-aac5-0000
00000000 338
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: ts=2018-10-31T10:53:43.768509Z lvl=info msg="Executing query" log_id=0BSDJnDW000 service=query query="SHOW SUBSCRIPTIONS"
Oct 31 11:53:43 EQLFRCL1PDL201 influxd[16026]: [httpd] ::1 - - [31/Oct/2018:11:53:43 +0100] "POST /query?db=&q=SHOW+SUBSCRIPTIONS HTTP/1.1" 200 321 "-" "KapacitorInfluxDBClient" 3c149503-dcfb-11e8-aac6-000000000000 319
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:43,749 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: Test Statistic                -23.372
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: Lags                               35
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:43,821 INFO:root: ending batch
Oct 31 11:53:43 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:43,823 INFO:root: Begin batch
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:45,792 INFO:root: SIZE OF INPUT: 7625
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:45,792 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: Test Statistic                -22.845
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: Lags                               35
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:45,850 INFO:root: ending batch
Oct 31 11:53:45 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:45,851 INFO:root: Begin batch
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:47,730 INFO:root: SIZE OF INPUT: 7639
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:47,731 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: Test Statistic                -24.518
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: Lags                               36
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:47,786 INFO:root: ending batch
Oct 31 11:53:47 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:47,787 INFO:root: Begin batch
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:49,835 INFO:root: SIZE OF INPUT: 7639
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: RESULTS OF DICKEY_FULLER TEST !!!
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:49,835 DEBUG:root: TEST_ADF    Augmented Dickey-Fuller Results
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: =====================================
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: Test Statistic                -25.415
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: P-value                         0.000
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: Lags                               36
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: -------------------------------------
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: Trend: Constant, Linear and Quadratic Time Trends
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: Critical Values: -4.37 (1%), -3.83 (5%), -3.55 (10%)
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: Null Hypothesis: The process contains a unit root.
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: Alternative Hypothesis: The process is weakly stationary.
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: STATIONNAIRE !!!
Oct 31 11:53:49 EQLFRCL1PDL201 python2[2050]: 2018-10-31 11:53:49,898 INFO:root: ending batch
