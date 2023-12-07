# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats

# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# slope, intercept, r, p, std_err = stats.linregress(x, y)

# def func(x):
#     return slope * x + intercept

# mymodel = np.poly1d(np.polyfit(x, y, 3))

# myline = np.linspace(1, 22, 100)

# # speed = func(10)
# # print(round(speed, 2), round(r, 2))
# speed = mymodel(17)
# print(speed)
# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show()

nums = [-3,4,3,90]
target = 0

def indece_returner(nums, target):
    if nums[0] + nums[-1] == target:
        return [0,len(nums)-1]
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if nums[i] + nums[j+1] == target:
                return [i,j+1]
            
def reverse_int(x):
    if (-2)**31 <= x and x <= 2**31 - 1:
        if x<0:
            x_rev = str(abs(x))[::-1]
            x_rev = int(x_rev) * (-1)
        else:
            x_rev = str(abs(x))[::-1]
            x_rev = int(x_rev)
    else:
        return 0
    return x_rev
    
print(reverse_int(1534236469))