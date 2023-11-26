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
        def inner_put(func):
            self.put_dict[path] = func

        return inner_put
    
    def post(self, path):
        def inner_post(func):
            self.post_dict[path] = func

        return inner_post
    
    def delete(self, path):
        def inner_delete(func):
            self.delete_dict[path] = func

        return inner_delete