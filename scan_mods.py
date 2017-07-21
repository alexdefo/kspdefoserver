#!/usr/bin/env python
# -*- coding: utf-8 -*-
# defo.dirty+github@gmail.com
# Sazonov Alexander
# ---------------------------------
# make DMPModControl.txt from GameData folder
# scan all folders in path
# get all dll files to  !optional–files ssection
# get all parts files to !partslist
# ---------------------------------



import sys
import os
import argparse
import commands


class PartClass:
    name = ""
    content = ""
    def __init__(self, name, path):
        self.path = path
        self.filename = name
        self.init()

    def init(self):
        self.get_content()
        self.get_name()

    def get_name(self):
        for line in self.content.split("\n"):

            if "name =" in line:
                self.name = line.split("=")[1].strip().replace("_",".")
                break



    def get_content(self):
        f = open(self.path + "/" + self.filename,'r')
        self.content = f.read()
        f.close()




    def __str__(self):
        return self.name


    def __unicode__(self):
        return self.name






class ModClass:
    def __str__(self):
        data = """\n---------------\n%s
DLL:%s
PARTS:%s""" % (self.name.encode("utf-8"), self.dll, self.parts)
        return data

    def __init__(self, name, gamedata_path):
        self.gamedata = gamedata_path
        self.name = name
        self.dll = self.find_dll()
        self.parts = self.find_parts()

    def find_parts(self):
        parts = []
        for path, mod_folders, mod_files in os.walk(self.gamedata  + self.name, topdown = False):
            if "parts" in path or "Parts" in path:

                for f in mod_files:
                    if ".cfg" in f:
                        #print path
                        part = PartClass(f, path)
                        parts.append(part)
        return parts


    def find_dll(self):
        dll = []
        for path, mod_folders, mod_files in os.walk(self.gamedata  + self.name, topdown = False):
            for f in mod_files:
                if ".dll" in f:

                    dll.append(path.replace("GameData/","") + f)

        return dll



class GameDataClass:
    path = None
    mods = []
    def __init__(self, dst):
        self.path = dst
        self.scan_mods()

    def register_mod(self, mod):
        m = ModClass(mod, self.path)
        self.mods.append(m)




    def scan_mods(self):
        for path, game_data_folders, files in os.walk(self.path, topdown = False):
            if path == self.path:
                for directory in game_data_folders:
                    self.register_mod(directory)



def main():
    parser = argparse.ArgumentParser(description='parse gamedata')
    parser.add_argument('--dst', default='GameData/')
    args = parser.parse_args()
    gamedata = GameDataClass(args.dst)
    dlls = []
    parts = []
    for mod in gamedata.mods:

        dlls.extend(mod.dll)
        parts.extend(mod.parts)

    print "!optional–files"
    for d in dlls:
        print d

    print "!partslist"
    for p in parts:
        print p


if __name__ == "__main__":
	main()
