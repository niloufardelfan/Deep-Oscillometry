import numpy as np

def peak_finding_backward(data,x,point,window_size):
    data_extended = np.concatenate([np.zeros(window_size),data,np.zeros(window_size)])
    max_list = []
    min_list = []  

    for i,value in enumerate(data_extended):
        if (i >= window_size) and (i < len(data_extended)-window_size):
            try:
                max_left = data_extended[(i-window_size):i+1].max()
                max_right = data_extended[i:(i+window_size)+1].max()
                check_value = data_extended[i] - ((max_left+max_right)/2)
            except ValueError:
                pass
                
            if (check_value >=0):
                max_list.append(((i-window_size),x[(i-window_size)],data[(i-window_size)]))
    
    for j in range(len(max_list)-1):
        inx1,_,_=max_list[j]
        inx2,_,maximum=max_list[j+1]
        minimum=data_extended[(inx1+window_size):(inx2+window_size)].min()
        threshold=(maximum-minimum)*4/5
        for i in range(inx2-inx1):
            if data[inx2-point-i] < data[inx2-point-i-1] and data[inx2-point-i] < data[inx2-point-i+1] and abs(maximum-data[inx2-point-i]) > threshold :
                min_list.append(((inx2-point-i),x[(inx2-point-i)],data[inx2-point-i]))
                break

    return np.array(max_list),np.array(min_list)