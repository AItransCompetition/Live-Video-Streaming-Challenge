# Submit Demo
* The type of file you submit is *.zip. the name is like submit.zip
* The submit.zip is gotten by compressed a folder called submit.The path is like following:
```
Submit
│   README.md
│   ABR.py    
└───results
│   │   your_model.pb
│   │   your_other_file

```

# ABR.py
* PATH
if you want to call your model ,the path setting is 
```
NN_MODEL = "/root/mmgc/team/"$YOUR TEAM NAME"/submit/results/nn_model_ep_18200.ckpt" # model path settings
```
* Algorithm
* * Init: you can init some self.params 
```
 def __init__(self):
     # fill your init vars
         self.buffer_size = 0
```
* * Initial your params: 
```
# Intial 
     def Initial(self):
             IntialVars = []
             return IntialVars

```
* * Run: your algorithm logic
```
def run(self, time, S_time_interval, S_send_data_size, S_chunk_len, S_rebuf, S_buffer_size, S_play_time_len,S_end_delay, S_decision_flag, S_buffer_flag,S_cdn_flag,S_skip_time, end_of_video, cdn_newest_id,download_id,cdn_has_frame, IntialVars):
    
         bit_rate = 1
         target_buffer = 1
         latency_limit = 7
         return bit_rate, target_buffer, latency_limit
```

# Import package
* If you want to add some site package ,please concact bupt-steven@foxmail.com
