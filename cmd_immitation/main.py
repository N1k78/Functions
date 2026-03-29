#!/usr/bin/env python3

import sys
import json

file_system=[
{
    "name" : "/",
    "type" : "directory",
    "children" : [
        {
            "name" : "home",
            "type" : "directory",
            "children" : [
                {
                    "name" : "admin",
                    "type" : "directory",
                    "children" : [
                    {
                        "name" : "Desktop",
                        "type" : "directory",
                        "children" : [
                            
                        ]
                    },
                    {
                        "name" : "Documents",
                        "type" : "directory",
                        "children" : [
                            
                        ]
                    },
                    {
                        "name" : "Music",
                        "type" : "directory",
                        "children" : [
                            
                        ]
                    },
                    {
                        "name" : "Pictures",
                        "type" : "directory",
                        "children" : [
                            
                        ]
                    },
                    {
                        "name" : "Public",
                        "type" : "directory",
                        "children" : [
                            
                        ]
                    },
                    {
                        "name" : "Videos",
                        "type" : "directory",
                        "children" : [
                            
                        ]
                    } 
                    ]
                } 
            ]
        }
    ]
}
]


class PyOSShell:
    def __init__(self):
        self.path = "/home/admin"
        self.commands = {
            "exit": self.exit,
            "ls": self.ls,
            "cd": self.cd,
            "pwd": self.pwd,
        }

    def make_absolute(self, target: str) -> str:
        """Самая простая версия: текущий путь + то, что ввёл пользователь"""
        if not target:
            return self.path

        if target.startswith("~"):
            target = "/home/admin" + target[1:]

        if target.startswith("/"):
            path = target
        else:
            path = self.path.rstrip("/") + "/" + target.lstrip("/")

        # Нормализация .. и .
        parts = [p for p in path.split("/") if p]
        stack = []
        for p in parts:
            if p == "..":
                if stack:
                    stack.pop()
            elif p != ".":
                stack.append(p)

        return "/" if not stack else "/" + "/".join(stack)

    def cd(self, args):
        if args:
            self.path = args[0]
        else:
            self.path = self.make_absolute("~")
        pass

    def pwd(self,args):
        print(self.path)
        return
    
    def get_rigth_child(self,folder,name):
        return folder["children"]

    def ls(self, args):
        
        pass

    def exit(self, args):
        sys.exit(0)
    
    def execute(self, line):
        line = line.strip()
        if not line:
            return
        
        parts = line.split()
        cmd = parts[0]
        args = parts[1:]
        
        if cmd in self.commands:
            self.commands[cmd](args)
        else:
            print(f"pyshell: command '{cmd}' not found")
    
    def run(self):
        while True:
            try:
                self.execute(input(f"{self.path}> "))
            except KeyboardInterrupt:
                print()
                continue
            except EOFError:
                print()
                break



if __name__ == "__main__":
    PyOSShell().run()