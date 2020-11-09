# ACM Multimedia 2019 Live Video Streaming Grand Challenge 
## Dataset
There are two datasets provided for this grand challenge. 

### Video Trace

This dataset contains frame-level traces of six video sequences encoded with IPPP frame structure.  Traces for each video sequence is stored under a subdirectory.  There are four representations for each video sequence.  The trace for each representation is stored in the files `frame_trace_0` to `frame_trace_3`. 

The traces are stored in text format, with each line corresponds to a frame in the representation of the video.  A line contains three numbers:

- The first floating point number corresponds to the timestamp of the video frame.
- The second floating point number correponds to the size of the video frame, in bits.
- The third integer, is either `1` or `0`, and is a flag that indicates if the frame is an I-frame (if `1`) or a P-frame (if `0`).

The client can only switch to a different representation on an I-frame.

### Network Trace

Four network traces are provided.  The network traces corresponds to measured throughput under different network conditions using WiFi and LTE.  The traces are named `fixed`, `low`, `medium`, `high` respectively.  Each network trace is a text file containing multiple lines.  Each line contains two floating point numbers:

- The first corresponds to the timestamp in seconds.
- The second corresponds to the measured throughput in Mbps.

These dataset are read and processed in the file `fixed_env.py`. 
