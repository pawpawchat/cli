import pages.auth
import system

class CommandLineTool:

    def __init__(self):
        self.user = None
        self.page = pages.auth.menu

    def run(self):
        while self.page: 
            system.clear_terminal()
            data = self.page(self)
            if data is not None:
                system.clear_terminal()
                print(data)
                input("\nPress enter to go next")
            
CommandLineTool().run()