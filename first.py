fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
round = 0
min_angle = 20
max_angle = 120
trial_angle = (max_angle - min_angle) * fib[-1] / fib[-2]
band_count = 2
distances = []
recent = 0 #positive distance for undershot and negative distance for overshot

recent = int(input())
distances.append(recent)
if(recent > 0): #undershot
    band_count++
else: #overshot
    band_count--
    pass

for i in range(11):
    recent = int(input())
    distances.append(recent)

    if(recent > 0): #undershot
        min_angle = trial_angle
    else: #overshot
        max_angle = trial_angle
        pass

    del fib[-1]
    trial_angle = (max_angle - min_angle) * fib[-1] / fib[-2]
    pass
print("The optimal band count is ", band_count, " and the draw angle is ", trial_angle, " resulting in a distance of ", distances[-1])
