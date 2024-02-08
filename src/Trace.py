#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from __future__ import annotations
from os.path import isdir, isfile, abspath, dirname
from os import listdir, access, X_OK
from typing import List


class InternalUnit():
    # type 0:dir 1:normal file 2:execute file
    def __init__(self, parentPath: str, index: int = 0):
        self.parentPath = parentPath
        self.index = index

    def __iter__(self):
        attrs = vars(self)
        for key, value in attrs.items():
            yield value

    def print(self) -> InternalUnit:
        attrs = vars(self)
        print(', '.join("%s: %s" % item for item in attrs.items()))
        return self

    def get(self) -> tuple:
        return tuple(self)

    def getByKey(self, key: str) -> str | int:
        attrs = vars(self)
        for k, value in attrs.items():
            if key == k:
                return value


class Unit(InternalUnit):
    def __init__(self, parentPath: str, index: int = 0):
        super().__init__(parentPath, index)

    @property
    def name(self) -> str:
        return sorted(listdir(self.parentPath))[self.index]

    @property
    def type(self) -> int:
        target = "%s/%s" % (self.parentPath, self.name)
        result = -1
        if isdir(target):
            result = 0
        elif access(target, X_OK):
            result = 2
        elif isfile(target):
            result = 1

        return result

    def _properties(self,) -> List[str]:
        class_items = self.__class__.__dict__.items()
        return dict((k, getattr(self, k))
                    for k, v in class_items
                    if isinstance(v, property))

    def print(self) -> Unit:
        InternalUnit.print(self)
        print(self._properties())
        return self


class Trace:
    def __init__(self, rootFolder: str = 'entry', Unit=Unit):
        self.rootFolder = rootFolder
        self.Unit = Unit
        self.list: list[self.Unit] = []
        # inital
        # check the folder exists
        if not isdir(abspath("%s" % (rootFolder))):
            print('the %s not exists' % (rootFolder))
            exit(1)
        self.append()

    def print(self) -> None:
        for item in self.list:
            item.print()

    def peek(self) -> Unit:
        if len(self.list) == 0:
            return None
        return self.list[-1]

    def append(self) -> Unit:
        lastUnit = self.peek()
        if lastUnit == None:
            target = self.rootFolder
        else:
            target = "%s/%s" % (lastUnit.parentPath, lastUnit.name)
        if isdir(target) and len(listdir(target)) > 0:
            unit = self.Unit(target)
            self.list.append(unit)

        return self.peek()

    def pop(self) -> Unit:
        if len(self.list) != 1:
            return self.list.pop()

    def getName(self, offset: int = 0) -> str:
        nowUnit = self.peek()
        return sorted(listdir(nowUnit.parentPath))[nowUnit.index+offset]

    def up(self) -> Unit:
        index = self.peek().index
        if self.peek().index != 0:
            self.peek().index = index-1
        return self.peek()

    def down(self) -> Unit:
        # check number of file the folder have
        index = self.peek().index
        parentPath = self.peek().parentPath
        if index != len(listdir(parentPath))-1:
            self.peek().index = index+1
        return self.peek()
