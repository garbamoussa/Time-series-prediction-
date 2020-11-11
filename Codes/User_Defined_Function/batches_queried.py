ID: sarimax_temp_stat
Error:
Template:
Type: batch
Status: enabled
Executing: true
Created: 05 Sep 18 12:47 CEST
Modified: 05 Sep 18 12:47 CEST
LastEnabled: 05 Sep 18 12:47 CEST
Databases Retention Policies: ["test_arima-temp_stat"."autogen"]
TICKscript:
var data = batch
    |query('''
        SELECT Temp_stat
        FROM "test_arima-temp_stat"."autogen"."value"
            ''')
        .period(7d)
        .every(1m)
        .align()

data
    @sarimax()
        .field('Temp_stat')
        .predict(20)
        .type('double')
    |influxDBOut()
        .create()
        .database('telegraf')
        .retentionPolicy('autogen')
        .measurement('sarmax_temp_stat')

DOT:
digraph sarimax_temp_stat {
graph [throughput="0.00 batches/s"];

query1 [avg_exec_time_ns="20.446393ms" batches_queried="28" errors="0" points_queried="56448" working_cardinality="0" ];
query1 -> sarimax2 [processed="28"];

sarimax2 [avg_exec_time_ns="0s" errors="0" working_cardinality="0" ];
sarimax2 -> influxdb_out3 [processed="0"];

influxdb_out3 [avg_exec_time_ns="0s" errors="0" points_written="0" working_cardinality="0" write_errors="0" ];
}
