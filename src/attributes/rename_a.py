def rename(new_name):
	def decorator(func):
		func.__name__ = new_name
		return func
	return decorator