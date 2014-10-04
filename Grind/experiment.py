import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
from scipy import stats

coord_font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 13,
        }

# figure a
fg5=plt.subplot(2,4,1)
records5 = [1885, 3769, 5653, 7537, 9425, 9425] 
objs5 = [92036792, 174789544, 259954488, 345406000, 420835528, 423091448]
for i in range(0, len(objs5)):
    objs5[i] = objs5[i] / 1024 / 1024
plt.plot(records5, objs5, 'bo-')
plt.xlabel('Map Input Records $(\\times 1k)$', fontsize = 13)
plt.ylabel('Size(HashMap) (MB)', fontsize = 13)
plt.xticks((np.arange(10)+1)*1000, (np.arange(10)+1))
#xlabels = fg5.get_xticklabels()
#for label in xlabels:
#    label.set_rotation(-30) 
plt.title('a: MemWordCount-map()')
plt.grid(color='gray')
plt.annotate('p = 0.99 \nrObj = 2.15MB \ny = 0.042 * x + 9.69', xy=(2000, 365),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
    
                )

plt.annotate('Large accumulated results', xy=(3500, 75),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )
print('pearson in MemWordCount = ', pearsonr(records5[0:len(records5) - 1], objs5[0:len(objs5) - 1]))

x = np.array(records5[0:len(records5) - 1])
y = np.array(objs5[0:len(objs5) - 1])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)
#plt.plot(x, predict_y, 'k-')



# figure b
fg2=plt.subplot(2,4,2)
records2 = [1, 149587, 299173, 448759, 598345, 747932, 747932] 
objs2 = [0, 31506440, 57967480, 70306040, 81076232, 93186928, 194068360]
for i in range(0, len(objs2)):
    objs2[i] = objs2[i] / 1024 / 1024
plt.plot(records2, objs2, 'bo-')
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
plt.annotate('p = 0.97 \nIn 263rd group \nrObj = 96.2MB \ncObj = 0MB \ny = 0.000114 * x + 10.38', xy=(90000, 140),  xycoords='data',
                 xytext=(0, 0), textcoords='offset points',
                 #bbox=dict(boxstyle="round", fc="0.8"),
                 )
plt.annotate('Large accumulated results\nLarge intermediate results', xy=(250000, 15),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )
plt.grid(color='gray')
plt.title('b: Count(distinct)1-combine()')
print('pearson in Count(distinct)1 = ', pearsonr(records2[0:len(records2)-1], objs2[0:len(objs2)-1]))
x = np.array(records2[0:len(records2) - 1])
y = np.array(objs2[0:len(objs2) - 1])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)

# figure c
fg7=plt.subplot(2,4,3)
records7 = [1068023, 2136045, 3204067, 4272089, 5340116, 6364863, 6364863]
objs7 = [184549440, 366073088, 549082552, 734379208, 922989280, 1094168776, 1094241536]
for i in range(0, len(objs7)):
    objs7[i] = objs7[i] / 1024 / 1024 
plt.plot(records7, objs7, 'bo-')
plt.xlabel('Reduce Input Records $(\\times 10k)$', fontsize = 13)
plt.ylabel('Size(ArrayList) (MB)', fontsize = 13)
plt.xticks((np.arange(6)+1)*1000000, (np.arange(12)+1)*100)
plt.title('c: ReduceJoin-reduce()')
plt.annotate('Large accumulated results', xy=(2500000, 180),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )
plt.grid(color='gray')
print('pearson in ReduceJoin = ', pearsonr(records7[0:len(records7)-1], objs7[0:len(objs7)-1]))
x = np.array(records7[0:len(records7) - 1])
y = np.array(objs7[0:len(objs7) - 1])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)
plt.annotate('p = 0.99 \nIn 1st group\nrObj = 71KB \ncObj = 0MB \ny = 0.000164 * x - 0.99', xy=(1450000, 800),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
                )


# figure d
plt.subplot(2,4,4)
records1 = [1, 4, 7, 10, 13, 17, 17]
objs1 = [0, 89160424, 146957744, 184394120, 219994928, 300900952, 376398384]
for i in range(0, len(objs1)):
    objs1[i] = objs1[i] / 1024 / 1024
    #plt.text(records1[i], objs1[i], '(%d,%.1f)'%(records1[i], objs1[i]), coord_font)
plt.plot(records1, objs1, 'bo-')
plt.xlabel('Reduce Input Records', fontsize = 13)
plt.ylabel('Size(String2IntOpenHashMap) (MB)', fontsize = 13)
plt.title('d: CooccurMatrix-reduce()')

plt.annotate('Large accumulated results\nLarge intermediate results', xy=(5, 20),  xycoords='data',
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
plt.annotate('p = 0.98 \nIn 3897853rd group\nrObj = 72MB \ncObj = 0MB \ny =  16.76 * x + 4.40', xy=(2, 270),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
                )


# figure e
plt.subplot(2,4,5)
mapFileBytesRead = [63746048, 135704576, 206819328, 244887552, 251080704] 
for i in range(0, len(mapFileBytesRead)):
    mapFileBytesRead[i] = mapFileBytesRead[i] / 1024 / 1024
uObjHashMap = [521211128, 693551104, 1028338784, 1186304896, 1221481328]
for i in range(0, len(uObjHashMap)):
    uObjHashMap[i] = uObjHashMap[i] / 1024 / 1024
plt.plot(mapFileBytesRead, uObjHashMap, 'bo-')
plt.ylabel('Size(HashMap) (MB)', fontsize = 13)
plt.xlabel('Bytes Read from Local File (MB)', fontsize = 13)
plt.title('e: PigMapJoin-map()')
plt.grid(color='gray') 
plt.annotate('p = 0.99 \ny = 3.85 * x + 224.75', xy=(80, 1050),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
    
                )
plt.annotate('Large external data', xy=(140, 490),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )

print('pearson in PigMapJoin = ', pearsonr(mapFileBytesRead, uObjHashMap))
x = np.array(mapFileBytesRead)
y = np.array(uObjHashMap)
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)

# figure f
plt.subplot(2,4,6)
records4 = [30193493, 32565153, 61818883, 71302477, 104461660, 116007939] 
for i in range(0, len(records4)):
    records4[i] = records4[i] / 1024 / 1024
objs4 = [99259664, 116554032, 200828464, 219277040, 393230760, 426268640]
for i in range(0, len(objs4)):
    objs4[i] = objs4[i] / 1024 / 1024 
plt.plot(records4, objs4, 'bo-')
plt.ylabel('Size(objects in map()) (MB)', fontsize = 13)
plt.xlabel('Bytes Read from Local File (MB)', fontsize = 13)
plt.title('f: Mahout-classifier-map()')
plt.grid(color='gray')
plt.annotate('p = 0.99 \ny = 3.83 * x - 22.45', xy=(30, 375),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
                )
plt.annotate('Large external data', xy=(60, 100),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )
print('pearson in Mahout-classifier = ', pearsonr(records4, objs4))
x = np.array(records4)
y = np.array(objs4)
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)




# figure g
plt.subplot(2,4,7)
records3 = [1, 5, 9, 13, 17, 21, 21]
#objs3 = [37234256, 159548984, 124346608, 16568576, 124242904, 124217560, 189601016]
objs3 = [37234256, 159548984, 124346608, 16568576, 124242904, 4021312, 189601016]
for i in range(0, len(objs3)):
    objs3[i] = objs3[i] / 1024 / 1024
plt.plot(records3, objs3, 'bo-')
plt.xlabel('Combine Input Records', fontsize = 13)
plt.yticks(np.arange(9)*25)
plt.ylabel('Size(objects in combine()) (MB)', fontsize = 13)
plt.title('g: Count(distinct)2-combine()')
plt.grid(color='gray')
print('pearson in Count(distinct)2 = ', pearsonr(records3[0:len(records3)-1], objs3[0:len(objs3)-1]))
plt.annotate('p = -0.31 \nIn 1st group \nrObj = 176.98MB \ncObj = 0MB', xy=(2, 157),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
                )





# figure h
plt.subplot(2,4,8)
records3 = [1, 5, 9, 13, 17, 21, 21]
objs3 = [37234256, 201259576, 506406095, 618697037, 828942349, 953025192, 1850166065]
for i in range(0, len(objs3)):
    objs3[i] = objs3[i] / 1024 / 1024
plt.plot(records3, objs3, 'bo-')
plt.xlabel('Combine Input Records', fontsize = 13)
#plt.yticks(np.arange(9)*25)
plt.ylabel('Size(objects in combine()) (MB)', fontsize = 13)
plt.title('h: Count(distinct)2-combine()')
plt.annotate('After adding the\non-disk objects', xy=(12, 200),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                bbox=dict(boxstyle="round", fc="0.8"),
                )
plt.grid(color='gray')
print('pearson in Total Count(distinct)2 = ', pearsonr(records3[0:len(records3)-1], objs3[0:len(objs3)-1]))
x = np.array(records3[0:len(records3) - 1])
y = np.array(objs3[0:len(objs3) - 1])
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x, y)
predict_y = intercept + slope * x
print(intercept, slope)
plt.annotate('p = 0.99 \nIn 1st group \nrObj = 855.6MB \ncObj = 0MB \ny = 44.78 * x + 7.35', xy=(3, 1200),  xycoords='data',
                xytext=(0, 0), textcoords='offset points',
                #bbox=dict(boxstyle="round", fc="0.8"),
                )


'''
# figure 8
fg8=plt.subplot(2,4,8)
records8 = [1425883, 2851765, 4277647, 5703529, 7129414, 7129415]
objs8 = [244347408, 490189264, 735305208, 983771976, 1221969080, 1221969288]
for i in range(0, len(objs8)):
    objs8[i] = objs8[i] / 1024 / 1024
plt.plot(records8, objs8, 'p-', color='lightskyblue')
plt.xlabel('Reduce Input Records $(\\times 10k)$')
plt.ylabel('Size(ArrayList) (MB)')
plt.xticks((np.arange(8)+1)*1000000,(np.arange(8)+1)*100)
xlabels = fg8.get_xticklabels()
plt.title('Reduce-join-nobuffer')
plt.grid()
'''

plt.show()

