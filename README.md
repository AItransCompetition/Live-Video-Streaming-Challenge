# ACM Multimedia 2019 Grand Challenge: Live Video Streaming

This repository contains the simulator code being used for ACM Multimedia 2019 Live Video Streaming.  The simulator is a frame-level DASH video streaming simulator with a pluggable client module for bitrate control and latency control.

## Files

![Image text](https://github.com/NGnetLab/Live-Video-Streaming-Challenge/blob/master/幻灯片1.gif)

The simulator contains the following files:

* `run.py` : An SDK to call the SIM and ABR
* `ABR.py` : your ABR algorithm
* `fixed_env.py` : SIM code simulates live streaming player download, play, card, skip frame, etc
* `load_trace.py` : load trace to memory

The folder `dataset` contains the network traces and video traces.  Please see the README.md file in the dataset directory for decsription of the dataset.

# The Simulator

The simulator simulates a live video player，including downloading and playback of video frames.  It reads as inputs:

1. A video trace, which contains the size of each video frame in a video file.
2. A network trace, which contains the network throughput at each time instance.
3. The bitrate control and latency control algorithm provided by participant.

The simulator output the following:

|   params           | params description                       |  example   |
| ------------------ | ---------------------------------------- | ---------- |
| time(s)            | physical time                            |   0.46(s)  |
| time_interval(s)   | duration in this cycle                   |   0.012(s) |  
| send_data_size(bit)| The data size downloaded in this cycle   |   14871(b) |
| frame_time_len(s)  | The time length of the frame currently   |   0.04(s)  |
| rebuf(s)           | The rebuf time of this cycle             |   0.00(s)  |
| buffer_size(s)     | The buffer size time length              |   1.26(s)  |
| play_time_len(s)   | The time length of playing in this cycle |   0.012(s) |
| end_delay(s)       | Current end-to-to delay                  |   1.31(s)  |
| cdn_newest_id      | Cdn the newest frame id                  |   85       |
| download_id        | Download frame id                        |   41       |
| cdn_has_frame      | cdn cumulative frame info                |   1.31(s)  |
| decision_flag      | Gop boundary flag or I frame flag        |   False    |
| buffer_flag        | Whether the player is buffering          |   False    |
| cdn_rebuf_flag     | Whether the cdn is rebuf                 |   False    |
| end_of_video       | Whether the end of video                 |   False    |

## Requirement

You will need Python 3 to run the simulator.

## Running the Simulator

To run the simulator, you execute

```
python run.py
```

The given default code should produce something like the following:

```
network traceID, network_reward, avg_running_time 1 1352.0162385703647 2.6768960660546604e-06
network traceID, network_reward, avg_running_time 2 1369.6498845601943 1.7594162136067256e-06
network traceID, network_reward, avg_running_time 3 1424.1866612345154 1.7338476473242459e-06
network traceID, network_reward, avg_running_time 4 1283.078401733983 1.6881894932483895e-06
network traceID, network_reward, avg_running_time 5 1431.9056303686343 1.736504121743205e-06
network traceID, network_reward, avg_running_time 6 1336.4567676353715 1.802085833961253e-06
network traceID, network_reward, avg_running_time 7 1422.2614517244535 1.7979350926816296e-06
network traceID, network_reward, avg_running_time 8 1343.4732742884667 1.770706229887301e-06
network traceID, network_reward, avg_running_time 9 1422.6834159560547 1.6881894932483895e-06
network traceID, network_reward, avg_running_time 10 1320.6092354238306 1.7544353240711776e-06
network traceID, network_reward, avg_running_time 11 1375.1834048004598 1.7155843856939035e-06
network traceID, network_reward, avg_running_time 12 1325.1692162039294 1.8302571898138067e-06
network traceID, network_reward, avg_running_time 13 1408.3942550208378 1.6885215525507595e-06
network traceID, network_reward, avg_running_time 14 1203.2877950641343 1.7167465932521979e-06
network traceID, network_reward, avg_running_time 15 1402.5958404064256 1.7351758845337253e-06
network traceID, network_reward, avg_running_time 16 1325.0882620208095 1.8970547944390343e-06
network traceID, network_reward, avg_running_time 17 1403.0285174814185 1.8051692417689732e-06
network traceID, network_reward, avg_running_time 18 1313.5680543047313 1.7504506124427393e-06
network traceID, network_reward, avg_running_time 19 1297.0031906126276 1.7051245176692527e-06
network traceID, network_reward, avg_running_time 20 1395.751751267894 1.7599143025602802e-06
[1357.769562433957, 1.8006102295275824e-06]

```

The output above shows the resulting QoE value and your ABR algorithm's average running time for each of the 20 runs, each using a different network trace.  The last line shows the average QoE and average running time for all 20 runs.

## Configuring the Simulator

Participants can configure the simulator by editing `run.py` and set the following parameters.

* To change the video trace used in the simulation, you can change the variable `VIDEO_TRACE`.  The default `VIDEO_TRACE` is set to `AsianCup_China_Uzbekistan`.  Other possibilities are: `Fengtimo_2018_11_3`, `YYF_2018_08_12`, `game`, `room`, and `sports`.

* To change the network trace used in the simulation, you can change the variable `NETWORK_TRACE`.  The default `NETWORK_TRACE` can be set to `fixed`, `high`, `medium`, or `low`.

* The simulator can produce detailed log files for debugging.  To turn this on, set the variable `DEBUG` to `True`.  By default, the logs will be written to a sub-directory called `log`.  This log directory can be changed by setting the `LOG_FILE_PATH` variable.  Note that you may want to set `DEBUG` to `False` if you are training an AI model as large volume of data may be written to disk when logging is on.

 
              
