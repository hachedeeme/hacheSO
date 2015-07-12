import cmd
import os

class HelloWorld(cmd.Cmd):
    prompt = "hache@so:~$ "
    
    intro = "Simple command processor example."
    
    def do_greet(self, person):
        """greet [person]
        Greet the named person"""
        if person:
            print("hi,", person)
        else:
            print('hi')
    
    def help_greet(self):
        print('\n'.join([ 'greet [person]',
                        'Greet the named person',
                           ]))
        
    last_output = ''

    def do_shell(self, line):
        "Run a shell command"
        print ("running shell command:", line)
        output = os.popen(line).read()
        print(output)
        self.last_output = output
    
    def do_echo(self, line):
        "Print the input, replacing '$out' with the output of the last shell command"
        # Obviously not robust
        print(line.replace('$out', self.last_output))
    
    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()

"""class Illustrate(cmd.Cmd):
    "Illustrate the base class method use."
    
    def cmdloop(self, intro=None):
        print('cmdloop(%s)' % intro)
        return cmd.Cmd.cmdloop(self, intro)
    
    def preloop(self):
        print('preloop()')
    
    def postloop(self):
        print('postloop()')
        
    def parseline(self, line):
        print ('parseline(%s) =>' % line,)
        ret = cmd.Cmd.parseline(self, line)
        print (ret)
        return ret
    
    def onecmd(self, s):
        print ('onecmd(%s)' % s)
        return cmd.Cmd.onecmd(self, s)

    def emptyline(self):
        print ('emptyline()')
        return cmd.Cmd.emptyline(self)
    
    def default(self, line):
        print ('default(%s)' % line)
        return cmd.Cmd.default(self, line)
    
    def precmd(self, line):
        print ('precmd(%s)' % line)
        return cmd.Cmd.precmd(self, line)
    
    def postcmd(self, stop, line):
        print ('postcmd(%s, %s)' % (stop, line))
        return cmd.Cmd.postcmd(self, stop, line)
    
    def do_greet(self, line):
        print ('hello,', line)

    def do_EOF(self, line):
        "Exit"
        return True

if __name__ == '__main__':
    Illustrate().cmdloop('Illustrating the methods of cmd.Cmd')"""