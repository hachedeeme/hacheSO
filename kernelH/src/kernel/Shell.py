import cmd

class HelloWorld(cmd.Cmd):
    promp = 'hache'
    
    def do_pete(self, line):
        print(line)
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()