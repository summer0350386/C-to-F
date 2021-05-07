car = input('你有沒有開過車')
if car != 'yes' and car != 'no':
	print('只能 yes or no')
	raise SystemExit

if car == 'yes':
	age = input('你幾歲?')
	if int(age) > 20:
		print('good')
	else:
		print('違反交通規則')


elif car == 'no':
	print('OK')

else:
	print('error')




