import os
import configparser

#config_path = r'C:\Users\aturhal\Desktop\ai\source\test_config.conf'
config_path = r'/home/asyaturhal/desktop/ai/test_config.conf'
config = configparser.ConfigParser()
config.read(config_path)
log_path = r'/home/asyaturhal/desktop/ai/log_diff'
#log_path = r'C:\Users\aturhal\Desktop\test_logs'
log_path = log_path + '/' + sorted(os.listdir(log_path))[-1]

def check_top_value(file, threshold):
    with open(file, 'r') as f:

        model_name = file.split('/')[-1].split('.')[0]
        # Read all lines in the file
        lines = f.readlines()
        # Extract the last line and convert it to a float
        top1 = lines[-1].split()
        epoch_num = int(top1[0])
        top1_diff = float(top1[1])
        #top5_diff = float(top1[2])

    if top1_diff < threshold:
         
        print("\033[31m\u2718\033[0m Test failed for {} since in Top1 value changed {} at {}th epoch.".format(model_name, top1_diff, epoch_num))
        return False
    
    else:

        print("\033[32m\u2714\033[0m Test passed for {} since in Top1 value changed {} at {}th epoch.".format(model_name, top1_diff, epoch_num))
        return True
    
for logs in os.listdir(log_path):
    if logs in config:
        threshold = float(list(config['{}'.format(logs)]["threshold"])[0])
    else:
        threshold = 0
    logs = log_path + '/' + str(logs)
    check_top_value(logs, threshold)
