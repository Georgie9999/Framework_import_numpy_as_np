class BestApi:
    def __init__(self):
        self.get_dict = {}
        self.post_dict = {}
        self.put_dict = {}
        self.delete_dict = {}

    def get(self, path):
        def inner_get(func):
            self.get_dict[path] = func

        return inner_get
    
    def put(self, path):
        def inner_get(func):
            self.put_dict[path] = func

        return inner_get
    
    def post(self, path):
        def inner_get(func):
            self.post_dict[path] = func

        return inner_get
    
    def delete(self, path):
        def inner_get(func):
            self.delete_dict[path] = func

        return inner_get