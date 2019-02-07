Table of Contents
=================

   * [Data Setting]()
   * [Video Trace]()
   * [Network Trace]()
# Data Setting Structure 
* ![Image text](https://github.com/NGnetLab/Live-Video-Streaming-Challenge/blob/master/frame.png)
# Video Trace(Frame Trace) 
* This Trace contains the time and size of each frame captured on the transcoding server and CDN to reach the CDN. 
* Video trace format   
   
        |   Time(s)  | frame_data_size(b) |  is_I_flag |
        |------------|--------------------|------------|
        | 22.1131    | 321312             |   1        |  
* Notice: 
    * CHUNK or GOP is composed of an I frame and an infinite number of P frames, and the bit rate must be switched only on I frame.
    * CHUNK or GOP coding structure is I/P/P/P/P/P/ 
    * Is_I_flag = 1 means I frame, Is_I_flag = 0 means P frame.
# Network Trace
* The network information of some mobile phones in wifi and LTE is collected, mainly simulating the network status under strong network, medium network and weak network
* Network trace Format:   
   
        |Time(s)  | throughput(kpbs) | 
        |---------|------------------|
        |20.5     | 1.312            | 
