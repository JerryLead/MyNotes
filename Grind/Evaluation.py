import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
from scipy import stats

coord_font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 13,
        }

####### figure set ############
#0.05, 0.08, 0.97, 0.93, 0.29, 0.37
###############################


#########################
# figure a MemWordCount
#########################

fg=plt.subplot(2,4,1)
records = [1, 1885, 3769, 5653, 7537, 9425] 
objs = [0, 92036792, 174789544, 259954488, 345406000, 420835528]

records_tail = [9425]
objs_tail = [423091448]
records_line = [9425,9425]
objs_line = [420835528, 423091448]

for i in range(0, len(objs_tail)):
    objs_tail[i] = objs_tail[i] / 1024 / 1024
plt.plot(records_tail, objs_tail, 'r*-')
for i in range(0, len(objs_line)):
    objs_line[i] = objs_line[i] / 1024 / 1024
plt.plot(records_line, objs_line, 'r-')
for i in range(0, len(objs)):
    objs[i] = objs[i] / 1024 / 1024
plt.plot(records, objs, 'bo-')
    
plt.xlabel('Map Input Records $(\\times 1k)$', fontsize = 13)
plt.ylabel('Size(HashMap) (MB)', fontsize = 13)
plt.xticks((np.arange(10)+1)*1000, (np.arange(10)+1))

plt.title('a: MemWordCount-map()')
plt.grid(color='gray')
plt.annotate('p = 0.99 \ny = 0.043 * x + 4.6 \n$\Delta$s = 2.15MB \nlastRec = 151KB \niResult = 128KB', xy=(1000, 290),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
    
                )

plt.annotate('Large accumulated results', xy=(2500, 50),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )
print('pearson in MemWordCount = ', pearsonr(records[0:len(records) - 1], objs[0:len(objs) - 1]))

x = np.array(records[0:len(records) - 1])
y = np.array(objs[0:len(objs) - 1])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)
#plt.plot(x, predict_y, 'k-')

#########################
# figure b NLPLemmatizer
#########################
fg=plt.subplot(2,4,2)
records = [1, 3, 5, 7, 9] 
objs = [13464, 14720, 14720, 14720, 14720]

records_tail = [9]
objs_tail = [402918776]
records_line = [9, 9]
objs_line = [14720, 402918776]

for i in range(0, len(objs_tail)):
    objs_tail[i] = objs_tail[i] / 1024 / 1024
plt.plot(records_tail, objs_tail, 'r*-')
for i in range(0, len(objs_line)):
    objs_line[i] = objs_line[i] / 1024 / 1024
plt.plot(records_line, objs_line, 'r-')
for i in range(0, len(objs)):
    objs[i] = objs[i] / 1024 / 1024
plt.plot(records, objs, 'bo-')

plt.xlabel('Map Input Records', fontsize = 13)
plt.ylabel('Size(objects in map()) (MB)', fontsize = 13)
plt.xticks((np.arange(10)+1), (np.arange(10)+1))

plt.annotate('$\Delta$s = 385MB \nlastRec = 9MB \niResult = 385MB', xy=(2, 300),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
    
                )
plt.annotate('Large intermediate results', xy=(2, 45),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )

plt.grid(color='gray')
plt.title('b: NLP-Lemmatizer-map()')
print('pearson in NLPLemmatizer = ', pearsonr(records[0:len(records)-1], objs[0:len(objs)-1]))
x = np.array(records[0:len(records) - 1])
y = np.array(objs[0:len(objs) - 1])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)

 
######################
# figure c PigMapJoin
######################

plt.subplot(2,4,3)
mapFileBytesRead = [0, 63746048, 135704576, 206819328, 244887552, 251080704] 
for i in range(0, len(mapFileBytesRead)):
    mapFileBytesRead[i] = mapFileBytesRead[i] / 1024 / 1024
uObjHashMap = [0, 501211128, 693551104, 1028338784, 1186304896, 1221481328]
for i in range(0, len(uObjHashMap)):
    uObjHashMap[i] = uObjHashMap[i] / 1024 / 1024
plt.plot(mapFileBytesRead, uObjHashMap, 'bo-')
plt.ylabel('Size(HashMap) (MB)', fontsize = 13)
plt.xlabel('Bytes Read from Local File (MB)', fontsize = 13)
plt.title('c: PigMapJoin-map()')
plt.grid(color='gray') 
plt.annotate('p = 0.99 \ny = 4.56 * x + 82.7', xy=(25, 1000),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
    
                )
plt.annotate('Large external data', xy=(110, 130),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )

print('pearson in PigMapJoin = ', pearsonr(mapFileBytesRead, uObjHashMap))
x = np.array(mapFileBytesRead)
y = np.array(uObjHashMap)
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)

######################
# figure d Mahout-classifier
######################

plt.subplot(2,4,4)
records = [0, 30193493, 32565153, 61818883, 71302477, 104461660, 116007939] 
for i in range(0, len(records)):
    records[i] = records[i] / 1024 / 1024
objs = [0, 99259664, 116554032, 200828464, 219277040, 393230760, 426268640]
for i in range(0, len(objs)):
    objs[i] = objs[i] / 1024 / 1024 
plt.plot(records, objs, 'bo-')
plt.ylabel('Size(objects in map()) (MB)', fontsize = 13)
plt.xlabel('Bytes Read from Local File (MB)', fontsize = 13)
plt.title('d: Mahout-classifier-map()')
plt.grid(color='gray')
plt.annotate('p = 0.99 \ny = 3.70 * x - 11.7', xy=(15, 375),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
                )
plt.annotate('Large external data', xy=(55, 50),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )
print('pearson in Mahout-classifier = ', pearsonr(records, objs))
x = np.array(records)
y = np.array(objs)
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)

###########################
# figure e Count(distinct1)-map
###########################

fg=plt.subplot(2,4,5)
records = [1, 149587, 299173, 448759, 598345, 747932] 
objs = [0, 62506440, 114967480, 140306040, 162076232, 186186928]
records_tail = [747932]
objs_tail = [388068360]
records_line = [747932,747932]
objs_line = [186186928,388068360]
for i in range(0, len(objs_tail)):
    objs_tail[i] = objs_tail[i] / 1024 / 1024
plt.plot(records_tail, objs_tail, 'r*-')
for i in range(0, len(objs_line)):
    objs_line[i] = objs_line[i] / 1024 / 1024
plt.plot(records_line, objs_line, 'r--')
for i in range(0, len(objs)):
    objs[i] = objs[i] / 1024 / 1024
plt.plot(records, objs, 'bo-')
plt.xlabel('Combine Input Records $(\\times 1k)$', fontsize = 13)
plt.ylabel('Size(objects in combine()) (MB)', fontsize = 13)
plt.xticks((np.arange(8)+1)*100000,(np.arange(8)+1)*100)
# plt.annotate(' Explosion of \n intermediate\n computing\n result', xy=(727000, 110),  xycoords='data',
#                 xytext=(-140, -10), textcoords='offset points',
#                 bbox=dict(boxstyle="round", fc="0.8"),
#                 arrowprops=dict(arrowstyle="fancy",
#                                 fc="0.6", ec="none",
#                                 connectionstyle="angle3,angleA=0,angleB=-80"),
#                 )
plt.annotate('In 263rd (k,list(v)) group \np = 0.97 \ny = 0.000229 * x + 20.4 \nreduce-level objs = 0MB \n$\Delta$s = 96.2MB \nlastRec = 320B \niResult = 92KB', xy=(90000, 230),  xycoords='data',
                 xytext=(0, 0), textcoords='offset points',
                 #bbox=dict(boxstyle="round", fc="0.8"),
                 )
plt.annotate('Large accumulated results', xy=(250000, 20),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )
plt.grid(color='gray')
plt.title('e: Count(distinct)1-combine()')
print('pearson in Count(distinct)1 = ', pearsonr(records[0:len(records)-1], objs[0:len(objs)-1]))
x = np.array(records[0:len(records) - 1])
y = np.array(objs[0:len(objs) - 1])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)


###########################
# figure f Count(distinct1)-reduce
###########################
plt.subplot(2,4,6)
records = [1, 5, 9, 13, 17, 21]
objs = [0,101259576, 246406095, 298697037, 408942349, 503025192]
records_tailf = [21]
objs_tailf = [1050166065]
records_linef = [21,21]
objs_linef = [503025192, 1050166065]
for i in range(0, len(objs_linef)):
    objs_linef[i] = objs_linef[i] / 1024 / 1024
for i in range(0, len(objs_tailf)):
    objs_tailf[i] = objs_tailf[i] / 1024 / 1024
for i in range(0, len(objs)):
    objs[i] = objs[i] / 1024 / 1024
plt.plot(records, objs, 'bo-')
plt.plot(records_tailf, objs_tailf, 'r*')
plt.plot(records_linef, objs_linef, 'r--')
plt.xlabel('Combine Input Records', fontsize = 13)
#plt.yticks(np.arange(9)*25)
plt.ylabel('Size(objects in combine()) (MB)', fontsize = 13)
plt.title('f: Count(distinct)2-combine()')
plt.annotate('Large accumulated results', xy=(8, 50),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )
plt.grid(color='gray')
print('pearson in Total Count(distinct)2 = ', pearsonr(records[0:len(records)-1], objs[0:len(objs)-1]))
x = np.array(records[0:len(records) - 1])
y = np.array(objs[0:len(objs) - 1])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)
plt.annotate('In 1st (k,list(v)) group \np = 0.99 \ny = 23.78 * x - 13.9 \nreduce-level objs = 0MB \n$\Delta$s = 855.6MB \nlastRec = 31MB \niResult = 35MB', xy=(3, 690),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
                )


###########################
# figure g ProcessFreebase
###########################
fg=plt.subplot(2,4,7)
records = [1, 1068023, 2136045, 3204067, 4272089, 5340116, 6364863]
objs = [0, 184549440, 366073088, 549082552, 734379208, 922989280, 1094168776]

records_tailf = [6364863]
objs_tailf = [1094241536]
records_linef = [6364863, 6364863]
objs_linef = [1094168776, 1094241536]
for i in range(0, len(objs_linef)):
    objs_linef[i] = objs_linef[i] / 1024 / 1024
for i in range(0, len(objs_tailf)):
    objs_tailf[i] = objs_tailf[i] / 1024 / 1024
for i in range(0, len(objs)):
    objs[i] = objs[i] / 1024 / 1024 
plt.plot(records_tailf, objs_tailf, 'r*')
plt.plot(records_linef, objs_linef, 'r-')

plt.plot(records, objs, 'bo-')
plt.xlabel('Reduce Input Records $(\\times 10k)$', fontsize = 13)
plt.ylabel('Size(ArrayList) (MB)', fontsize = 13)
plt.xticks((np.arange(6)+1)*1000000, (np.arange(12)+1)*100)
plt.title('g: ProcessFreebase-reduce()')
plt.annotate('Large accumulated results', xy=(2000000, 100),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )
plt.grid(color='gray')
print('pearson in ReduceJoin = ', pearsonr(records[0:len(records)-1], objs[0:len(objs)-1]))
x = np.array(records[0:len(records) - 1])
y = np.array(objs[0:len(objs) - 1])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)
plt.annotate('In 1st (k,list(v)) group \np = 0.99 \ny = 0.000164 * x - 0.53 \nrecord-level objs = 0MB \n$\Delta$s = 71KB \nlastRec = 288B \niResult = 588B', xy=(900000, 690),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
                )


###########################
# figure h CooccurMatrix
###########################
plt.subplot(2,4,8)
records1 = [1, 4, 7, 10, 13, 17]
objs1 = [0, 89160424, 146957744, 184394120, 219994928, 300900952]

records_tailf = [17]
objs_tailf = [422184304]
records_linef = [17, 17]
objs_linef = [300900952, 422184304]
for i in range(0, len(objs_linef)):
    objs_linef[i] = objs_linef[i] / 1024 / 1024
for i in range(0, len(objs_tailf)):
    objs_tailf[i] = objs_tailf[i] / 1024 / 1024
for i in range(0, len(objs1)):
    objs1[i] = objs1[i] / 1024 / 1024
plt.plot(records_tailf, objs_tailf, 'r*')
plt.plot(records_linef, objs_linef, 'r--')
    #plt.text(records1[i], objs1[i], '(%d,%.1f)'%(records1[i], objs1[i]), coord_font)
plt.plot(records1, objs1, 'bo-')
plt.xlabel('Reduce Input Records', fontsize = 13)
plt.ylabel('Size(String2IntOpenHashMap) (MB)', fontsize = 13)
plt.title('h: CooccurMatrix-reduce()')

plt.annotate('Large accumulated results', xy=(5, 20),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )

plt.grid(color='gray')
print('pearson in CooccurMatrix = ', pearsonr(records1[0:len(records1)-1], objs1[0:len(objs1)-1]))
x = np.array(records1[0:len(records1) - 1])
y = np.array(objs1[0:len(objs1) - 1])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)
plt.annotate('In 3897853rd (k,list(v)) group \np = 0.98 \ny = 16.76 * x + 4.40 \nrecord-level objs = 0MB \n$\Delta$s = 115.7MB \nlastRec = 30MB \niResult = 30MB', xy=(2, 255),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
                )
#===============================================================================
# 
#===============================================================================


plt.show()

