import hashlibclass User:	def __init__(self, email='', password='', name=''):		self.email = email		self.passwordHash = hashlib.sha256(password).hexdigest()		self.name = name		self.tasks = []	def authenticate(self, password):		return self.passwordHash == hashlib.sha256(password).hexdigest()