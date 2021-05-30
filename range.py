# range

import random
range(5) #[0,1,2,3,4] 自動0開始,不包含5

for i in range(3):
	r = random.randint(1, 10)
	print(i)
	print('hi')
	print('這是第', i + 1, '次產生隨機數', r)

range(2, 5) #[2, 3, 4]
range(2, 10, 3) #[2, 5, 8]
range(10, 3, -2) #[10, 8, 6, 4]

range(100)
for i in range(100):
	print('hi')