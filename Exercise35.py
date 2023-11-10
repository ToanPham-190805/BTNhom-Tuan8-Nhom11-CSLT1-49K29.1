human = int(input('Nhập tuổi người:'))
if human < 0:
	print('Thông báo tuổi không hợp lệ')
elif human <= 2:
	dog = human * 10.5
else:
	dog = 21 + (human - 2)*4
print('Số tuổi của chú chó là:', dog)