#!/usr/bin/env python3

import sys
import json

file_system={
"/":
{
    "name" : "/",
    "type" : "directory",
    "permition" : "drw-r--r--",
    "hide" : False, 
    "children" : {
            "home":
            {
            "name" : "home",
            "type" : "directory",
            "permition" : "drw-r--r--",
            "hide" : False, 
            "children" : {
                "admin":
                {
                    "permition" : "drw-r--r--",
                    "name" : "admin",
                    "type" : "directory",
                    "hide" : False, 
                    "children" : {
                "Desktop":
                    {
                        "permition" : "drw-r--r--",
                        "name" : "Desktop",
                        "type" : "directory",
                        "hide" : False, 
                        "children" : {
                            
                        }
                    },
                "Documents":
                    {
                        "permition" : "drw-r--r--",
                        "hide" : False, 
                        "name" : "Documents",
                        "type" : "directory",
                        "children" : {
                            
                        }
                    },
                "Music":
                    {
                        "permition" : "drw-r--r--",
                        "hide" : False, 
                        "name" : "Music",
                        "type" : "directory",
                        "children" : {
                            
                        }
                    },
                "Pictures":
                    {
                        "permition" : "drw-r--r--",
                        "hide" : False, 
                        "name" : "Pictures",
                        "type" : "directory",
                        "children" : {
                            
                        }
                    },
                "Public":
                    {
                        "permition" : "drw-r--r--",
                        "hide" : False, 
                        "name" : "Public",
                        "type" : "directory",
                        "children" : {
                            
                        }
                    },
                "Videos":
                    {
                        "permition" : "drw-r--r--",
                        "hide" : False, 
                        "name" : "Videos",
                        "type" : "directory",
                        "children" : {
                            
                        }
                    } 
                    }
                } 
            }
        },
            ".config":{
                "name" : "Videos",
                "type" : "file",
                "permition" : "drw-r--r--",
                "hide" : True, 
            },
    }
}
}


class PyOSShell:
    def __init__(self):
        self.path = "/home/admin"
        self.commands = {
            "exit": self.exit,
            "ls": self.ls,
            "cd": self.cd,
            "pwd": self.pwd,
            "sudo" : self.sudo
        }

    def sudo(self,args):
        
        pass

    def refresh_aliases():
        
        pass

    def make_absolute(self, target: str) -> str:
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
            self.path = self.make_absolute(args[0])
        else:
            self.path = self.make_absolute("~")
        pass

    def pwd(self,args):
        if len(args) == 0:
            print(self.path)
        else:
            print(f"pwd: to many arguments.")
        return

    def get_directory(self, path: str):
        """Возвращает узел файловой системы по абсолютному пути"""
        if path == "/":
            return file_system["/"]

        parts = [p for p in path.split("/") if p]
        current = file_system["/"]

        for part in parts:
            if current.get("type") != "directory":
                return None
            children = current.get("children", {})
            if part not in children:
                return None
            current = children[part]

        return current
    
    def ls(self, args):
        show_all = False      # -a
        long_format = False   # -l
        target = "."

        # Парсинг аргументов
        i = 0
        while i < len(args):
            arg = args[i]
            if arg.startswith("-") and arg != "-":
                for char in arg[1:]:
                    if char == "a":
                        show_all = True
                    elif char == "l":
                        long_format = True
                    else:
                        print(f"ls: invalid option -- '{char}'")
                        return
            else:
                target = arg
            i += 1

        abs_path = self.make_absolute(target)
        node = self.get_directory(abs_path)

        if node is None:
            print(f"ls: cannot access '{target}': No such file or directory")
            return

        # Если это файл, а не директория
        if node["type"] != "directory":
            print(node["name"])
            return

        # Получаем содержимое
        children = node.get("children", {})

        # Формируем список элементов
        items = []
        for name, item in children.items():
            if not show_all and item.get("hide", False):
                continue
            items.append((name, item))

        # Сортируем по имени
        items.sort(key=lambda x: x[0])

        if not items:
            return

        # Вывод
        if long_format:
            for name, item in items:
                item_type = "d" if item["type"] == "directory" else "-"
                # Простая имитация прав и размера
                print(f"{item_type}rw-r--r-- 1 admin admin  4096 Apr 10 12:00 {name}")
        else:
            # Обычный вывод в одну строку
            names = [name for name, _ in items]
            print("  ".join(names))

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