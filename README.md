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
network traceID, network_reward, avg_running_time 1 641.1484318760413 2.7569223579257976e-06
network traceID, network_reward, avg_running_time 2 985.7361064180305 1.569810351953533e-06
network traceID, network_reward, avg_running_time 3 1434.0326303686352 1.506220995549704e-06
network traceID, network_reward, avg_running_time 4 909.2318048157695 1.5385812629050623e-06
network traceID, network_reward, avg_running_time 5 635.4616496246817 2.8796182701514625e-06
network traceID, network_reward, avg_running_time 6 1019.0324002078656 3.573290152802109e-06
network traceID, network_reward, avg_running_time 7 991.7406496996467 4.670511970121271e-06
network traceID, network_reward, avg_running_time 8 1055.3980756167875 3.7547605615472396e-06
network traceID, network_reward, avg_running_time 9 -163.7251464104959 3.7670135498046877e-06
network traceID, network_reward, avg_running_time 10 460.11141008945896 1.8877298097065138e-06
network traceID, network_reward, avg_running_time 11 1586.2008041285537 1.5093755589222177e-06
network traceID, network_reward, avg_running_time 12 1028.6844963417639 1.4955950978738685e-06
network traceID, network_reward, avg_running_time 13 1021.9785822724941 1.5320970756073211e-06
network traceID, network_reward, avg_running_time 14 963.8776511160278 2.4441224950933854e-06
network traceID, network_reward, avg_running_time 15 81.1547975421813 3.175536099211264e-06
network traceID, network_reward, avg_running_time 16 -19.11784167374209 2.672614120855564e-06
network traceID, network_reward, avg_running_time 17 1202.1056307541305 2.4344927753246596e-06
network traceID, network_reward, avg_running_time 18 442.34703880371285 3.3536329242844434e-06
network traceID, network_reward, avg_running_time 19 1009.585542619389 2.43250041951044e-06
network traceID, network_reward, avg_running_time 20 -307.0479419414425 2.85270988858062e-06
[748.8968386134745, 2.5903567868865584e-06]

```

The output above shows the resulting QoE value and your ABR algorithm's average running time for each of the 20 runs, each using a different network trace.  The last line shows the average QoE and average running time for all 20 runs.

## Configuring the Simulator

Participants can configure the simulator by editing `run.py` and set the following parameters.

* To change the video trace used in the simulation, you can change the variable `VIDEO_TRACE`.  The default `VIDEO_TRACE` is set to `AsianCup_China_Uzbekistan`.  Other possibilities are: `Fengtimo_2018_11_3`, `YYF_2018_08_12`, `game`, `room`, and `sports`.

* To change the network trace used in the simulation, you can change the variable `NETWORK_TRACE`.  The default `NETWORK_TRACE` can be set to `fixed`, `high`, `medium`, or `low`.

* The simulator can produce detailed log files for debugging.  To turn this on, set the variable `DEBUG` to `True`.  By default, the logs will be written to a sub-directory called `log`.  This log directory can be changed by setting the `LOG_FILE_PATH` variable.  Note that you may want to set `DEBUG` to `False` if you are training an AI model as large volume of data may be written to disk when logging is on.

 
              
