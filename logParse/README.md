
The parse_deltas.py script takes 3 arguments [log_with_start_times_filepath | log_with_end_times_filepath | output_filepath]
In this folder the example command is
```shell
./parse_deltas.py start_times.csv finish_times.csv deltas.csv
```
The script gets the time a transaction takes and coorilates it with the IP in the log as it's output. The expected input is a log file in csv format with [transaction_id,start_timestamp,ip_address] and also a log file in csv format with [transaction_id,complete_timestamp,ip_address]