import os

class Welcome:
    """Welcome user"""
    def __init__(self):
        self.first_name = os.environ.get('FIRST_NAME')
        self.last_name = os.environ.get('LAST_NAME')
        
        print(f'Bienvenido/a {self.first_name} {self.last_name}')