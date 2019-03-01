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

## Running The Simulator

To run the simulator, you execute

```
python online.py
```

The given default code should produce something like the following:

```
video count 0 1182.2642188716964
video count 1 1377.7223845567382
video count 2 2205.3576390914172
video count 3 1563.6229626338486
video count 4 1005.8552370641194
video count 5 1730.894881578582
video count 6 1742.591282427159
video count 7 1742.9341512235237
video count 8 -1160.3554885566875
video count 9 754.6778329758246
video count 10 2604.537383217133
video count 11 1526.3693699344235
video count 12 1738.4296243574768
video count 13 1632.1525894295157
video count 14 103.31676372570564
video count 15 -134.73628719562478
video count 16 1503.0123339929692
video count 17 697.5516669070091
video count 18 1376.166009667083
video count 19 -749.3520074196668
22.44301254848225
```

        
# Online
* Setting
    * video trace setting:     
        
                   13 video_size_file = './video_size_'      #video trace path setting,
                   
    * network trace setting:
    
                   12 TRAIN_TRACES = './train_sim_traces/'   #train trace path setting, 
                   
    * log setting
        * the log is used to debug the code. you can set you log file path:

                   14 LogFile_Path = "./log/"                #log file trace path setting, 
        
        * if you are debugging your code, you can let the DEBUG = True.
        * if you are trainning your model, consider the I/O, advise you let the DEBUG = False
    * plot setting
        * if you want to Debug the code, the Draw = True, the image will let you know all kinds of indicators
        * ![Image text](https://github.com/NGnetLab/LiveStreamingDemo/blob/master/figure_1.png)

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
# ABR
* The participant should submit your ABR algorithm.
* The code must obey the demo sample.
# Submit
* for detail info, Please vist the submit.
# DataSet
* for detail info, Please vist the Dataset.
