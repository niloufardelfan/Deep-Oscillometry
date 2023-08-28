import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib
from scipy import stats
from statistics import median

def outlier_det(y,x,mintab):

    median = np.median(y)
    med_abs_deviation = stats.median_absolute_deviation(y)
    ym1=np.full_like(y, np.nan)
    y_redo = np.array(y)
    xm1=list()
    input_num="null"

    for i in range(len(y)) :
        diff_p = math.sqrt((y[i] - median) ** 2)
        z_score_p = 0.6745 * diff_p / med_abs_deviation
        if z_score_p > 10 :
            ym1[i] = y[i]
            y[i] = np.nan
    
    for i in range(len(mintab)-1):
        indx1=np.int(mintab[i])
        indx2=np.int(mintab[i+1])
        xm1.append(abs(x[indx1]-x[indx2]))

    threshold=np.median(xm1)
    #print(threshold)

    for i in range(len(mintab)-1):

        indx1=np.int(mintab[i])
        indx2=np.int(mintab[i+1])
        #print(indx1,indx2,abs(x[indx1]-x[indx2]))
        if abs(x[indx1]-x[indx2]) > (threshold + 0.3):
            #print("deleted :" ,indx1 ,indx2)
            ym1[indx1+1:indx2-1] = y[indx1+1:indx2-1]
            y[indx1+1:indx2-1] = np.nan
        if abs(x[indx1]-x[indx2]) < (threshold - 0.3):
            #print("deleted :" ,indx1 ,indx2)
            ym1[indx1+1:indx2-1] = y[indx1+1:indx2-1]
            y[indx1+1:indx2-1] = np.nan
    

    
    
    while(True):
        
        plt.plot(x,y,"b-",x,ym1,"r-")
        plt.scatter(x[np.int32(mintab)], y[np.int32(mintab)], color='black')
        plt.show(block = False)

        input_num =input ("please Enter a number :") 
        if input_num == "done":
            break

        num=np.int(input_num)
        plt.close()
        res_next = np.int(mintab[num])
        res_before = np.int(mintab[num-1])
        if not np.isnan(np.sum(y[res_before:res_next])):
            ym1[res_before:res_next] = y[res_before:res_next]
            y[res_before:res_next] = np.nan

        
        
        plt.close()
        plt.plot(x,y,"b-",x,ym1,"r-")
        plt.scatter(x[np.int32(mintab)], y_redo[np.int32(mintab)], color='red')
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        for i, txt in enumerate(mintab):
            plt.annotate(txt, (x[np.int32(mintab[i])],y_redo[np.int32(mintab[i])]))
        plt.show(block = False)

        input_num = input ("please Enter a number :") 

        if input_num == "done":
            break

        if input_num == "redo":
            input_num = input ("please enter a number to redo :") 
            num=np.int(input_num)
            if num > len(y):
                input_num =input ("invalid index please Enter another number :") 
                num=np.int(input_num)

            for i in range(len(mintab)):
                if mintab[i] > num :
                    res_next = np.int(mintab[i])
                    if i > 0 :
                        res_before = np.int(mintab[i-1])
                    else:
                        res_before = np.int(0)
                    break
            if np.isnan(np.sum(y[res_before:res_next])):
                ym1[res_before:res_next] = np.nan
                y[res_before:res_next] = y_redo[res_before:res_next]
                continue



        if input_num.isdigit():
            num=np.int(input_num)
            if num > len(y):
                input_num =input ("invalid index please Enter another number :") 
                if input_num == "done":
                    break
                num=np.int(input_num) 
            for i in range(len(mintab)):
                if mintab[i] > num :
                    res_next = np.int(mintab[i])
                    if i > 0 :
                        res_before = np.int(mintab[i-1])
                    else:
                        res_before = np.int(0)
                    break
            if not np.isnan(np.sum(y[res_before:res_next])):
                ym1[res_before:res_next] = y[res_before:res_next]
                y[res_before:res_next] = np.nan

        else :
            print("invalid input please try again")
            continue
        
    return y,ym1
