def total_peaks(data,smoothing,th,influence): #队列不先全进，每次只进一个窗口，每次更新之后再塞
    data_series=data.copy()
    peak_list=[0 for i in range(smoothing)]
    smoothing_windows=[]  #一个存储滑动窗口的队列
    smoothing_windows.append(data[0:0+smoothing+1])
    i=0
    while smoothing_windows:
        tmp=0
        mean=sum(smoothing_windows[0][0:smoothing])/smoothing  #计算当前窗口的μ
        for j in smoothing_windows[0][0:smoothing]:  #计算当前窗口的σ
            tmp+=(j-mean)**2
        sigma=(tmp/smoothing)**0.5
        z_score=(smoothing_windows[0][smoothing]-mean)/sigma  #计算当前所判断值的z_score
        if abs(z_score) >= th:
            peak_list.append(1)
        else:
            peak_list.append(0)
        if peak_list[-1]:  #只判断peak_list的最后一位
            s=influence*data[i+smoothing]+(1-influence)*data[i+smoothing-1]
            data[i+smoothing]=s #修改data，从新data序列更新smoothing_windows
        i+=1 #窗口向后滑1
        smoothing_windows.pop()
        if i+smoothing+1<=len(data):  #防止超界
            smoothing_windows.append(data[i:i+smoothing+1])
    expected_answer=peak_list.copy()
    flag=1
    while flag:
        flag=0
        for j in range(len(expected_answer)-1):
            if expected_answer[i]==1 and expected_answer[i+1]==1:
                expected_answer.pop(i+1)
            if j==len(expected_answer)-1:
                break
        for i in range(len(expected_answer)-1):
            if expected_answer[i]==1 and expected_answer[i+1]==1:
                flag=1
                break
    return data_series,smoothing,th,influence,sum(expected_answer)

a=[0,0,-2,2,-2,2,0, 1, 10, 15, 3, 0, 7, 9, 3 , 2, 7, 12, 2, 1]
ans=total_peaks(a,8,3.0,0.0)
print(ans[4])
