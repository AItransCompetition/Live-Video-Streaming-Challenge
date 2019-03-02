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

![Image text](https://github.com/NGnetLab/Live-Video-Streaming-Challenge/blob/master/frame.png)    

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
network trace 1 -1160.3892885566877
network trace 2 754.6778329758246
network trace 3 1563.6019626338486
network trace 4 -134.73628719562478
network trace 5 697.5516669070091
network trace 6 -749.3520074196668
network trace 7 1632.1595894295158
network trace 8 1730.894881578582
network trace 9 1742.9131512235235
network trace 10 1377.708384556738
network trace 11 2604.5443832171327
network trace 12 1503.0123339929692
network trace 13 1182.3120188716962
network trace 14 103.31676372570564
network trace 15 1738.4296243574768
network trace 16 1376.159009667083
network trace 17 1742.6122824271592
network trace 18 1005.8552370641194
network trace 19 1526.3693699344235
network trace 20 2205.3716390914174
1068.7148832610592
```

The output above shows the resulting QoE value for each of the 20 runs, each using a different network trace.  The last line shows the average QoE for all 20 runs.

## Configuring the Simulator

Participants can configure the simulator by editing `run.py` and set the following parameters.

* To change the video trace used in the simulation, you can change the variable `VIDEO_TRACE`.  The default `VIDEO_TRACE` is set to `AsianCup_China_Uzbekistan`.  Other possibilities are: `Fengtimo_2018_11_3`, `YYF_2018_08_12`, `game`, `room`, and `sports`.

* To change the network trace used in the simulation, you can change the variable `NETWORK_TRACE`.  The default `NETWORK_TRACE` can be set to `fixed`, `high`, `medium`, or `low`.

* The simulator can produce detailed log files for debugging.  To turn this on, set the variable `DEBUG` to `True`.  By default, the logs will be written to a sub-directory called `log`.  This log directory can be changed by setting the `LOG_FILE_PATH` variable.  Note that you may want to set `DEBUG` to `False` if you are training an AI model as large volume of data may be written to disk when logging is on.

 
              
