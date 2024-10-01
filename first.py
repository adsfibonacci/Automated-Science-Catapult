fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
round = 0
min_angle = 20
max_angle = 120
trial_angle = []
trial_angle.append((max_angle - min_angle) * fib[-2] / fib[-1] + min_angle)
band_count = 2
distances = [0, 0]
recent = 0 #positive distance for undershot and negative distance for overshot from target

distances[0] = float(input())

print("Trial angle degree of ", trial_angle[-1])

if(distances[0] > 0): #undershot
    band_count += 1
else: #overshot
    band_count -= 1
    pass
print("Round: 1")
distances[1] = float(input())

if(abs(distances[0]) < abs(distances[1])): #two bands was closer
    band_count = 2
else: #two bands was further
    pass
print("Bands: ", band_count)
if(distances[1] > 0): #undershot
    min_angle = trial_angle[-1]
else:
    max_angle = trial_angle[-1]
    pass

print("Round: 2")
for i in range(3, 14):
    recent = float(input())
    distances.append(recent)

    if(recent > 0): #undershot
        min_angle = trial_angle[-1]
    else: #overshot
        max_angle = trial_angle[-1]
        pass

    del fib[-1]
    trial_angle.append((max_angle - min_angle) * fib[-2] / fib[-1] + min_angle)
    print("Round: ", i, "\tTrial Angle: ", trial_angle[-1], "\tFibonacci Sizes", len(fib))
    pass
print("The optimal band count is ", band_count, " and the draw angle is ", trial_angle[-1], " resulting in a distance of ", distances[-1])
