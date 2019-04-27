import tensorflow as tf

#NN_MODEL = "/home/team/"YOUR TEAM NAME"/submit/results/nn_model_ep_18200.ckpt" # model path settings

class Algorithm:
     def __init__(self):
     # fill your init vars
         self.buffer_size = 0
         
     # Intial 
     def Initial(self):

             IntialVars = []
                 
             return IntialVars

     #Define your algorithm
     def run(self, time, S_time_interval, S_send_data_size, S_chunk_len, S_rebuf, S_buffer_size, S_play_time_len,S_end_delay, S_decision_flag, S_buffer_flag,S_cdn_flag,S_skip_time, end_of_video, cdn_newest_id,download_id,cdn_has_frame, IntialVars):
    
         bit_rate = 1
         target_buffer = 1
         latency_limit = 7
         return bit_rate, target_buffer, latency_limit


         # If you choose other
         #......
