# ACM Multimedia 2019 Grand Challenge: Live Video Streaming

This repository contains the simulator code being used for ACM Multimedia 2019 Live Video Streaming.  The simulator is a frame-level DASH video streaming simulator with a pluggable client module for bitrate control and latency control.

## Files

![Image text](https://github.com/NGnetLab/Live-Video-Streaming-Challenge/blob/master/幻灯片1.gif)

The simulator contains the following files:

* `online.py` : An SDK to call the SIM and ABR
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

## Running the Simulator

To run the simulator, you execute

```
python run.py
```

The given default code should produce something like the following:

```
run 1 1182.2642188716964
run 2 1377.7223845567382
run 3 2205.3576390914172
run 4 1563.6229626338486
run 5 1005.8552370641194
run 6 1730.894881578582
run 7 1742.591282427159
run 8 1742.9341512235237
run 9 -1160.3554885566875
run 10 754.6778329758246
run 11 2604.537383217133
run 12 1526.3693699344235
run 13 1738.4296243574768
run 14 1632.1525894295157
run 15 103.31676372570564
run 16 -134.73628719562478
run 17 1503.0123339929692
run 18 697.5516669070091
run 19 1376.166009667083
run 20 -749.3520074196668
22.44301254848225
```

The output above shows the resulting QoE value for each of the 20 runs, each using a different network trace.  The last line is the sum of the QoE for all 20 runs, scaled down by 1000.

## Configuring the Simulator

Participants can configure the simulator by editing `run.py` and set the following parameters.

* To change the video trace used in the simulation, you can change the variable `VIDEO_TRACE`.  The default `VIDEO_TRACE` is set to `AsianCup_China_Uzbekistan`.  Other possibilities are: `Fengtimo_2018_11_3`, `YYF_2018_08_12`, `game`, `room`, and `sports`.

* To change the network trace used in the simulation, you can change the variable `NETWORK_TRACE`.  The default `NETWORK_TRACE` can be set to `fixed`, `high`, `medium`, or `low`.

* The simulator can produce detailed log files for debugging.  To turn this on, set the variable `DEBUG` to `True`.  By default, the logs will be written to a sub-directory called `log`.  This log directory can be changed by setting the `LOG_FILE_PATH` variable.  Note that you may want to set `DEBUG` to `False` if you are training an AI model as large volume of data may be written to disk when logging is on.

* You can set the variable `DRAW` to `True` to ask the simulator to output a plot of the downloaded bitrate, buffer occupancy, and network throughput.  An example plot is shown below.  
                
![Image text](https://github.com/NGnetLab/LiveStreamingDemo/blob/master/figure_1.png)

        ```python
           if DRAW:
               ax = fig.add_subplot(311)
               plt.ylabel("BIT_RATE")
               plt.ylim(300,1000)
               plt.plot(id_list,bit_rate_record,'-r')
  
               ax = fig.add_subplot(312)
               plt.ylabel("Buffer_size")
               plt.ylim(0,7)
               plt.plot(id_list,buffer_record,'-b')
  
               ax = fig.add_subplot(313)
               plt.ylabel("throughput")
               plt.ylim(0,2500)
               plt.plot(id_list,throughput_record,'-g')
  
               plt.draw()
               plt.pause(0.01)
         ```
