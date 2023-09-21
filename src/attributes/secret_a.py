def secret(func):
	func.secret = True
	return func