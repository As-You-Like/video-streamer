
class LoginController():
    def __init__(self):
        super()
        self.view = None

    def setView(self,view):
        self.view = view

    def select_server(self,server_addr):
        print(server_addr)