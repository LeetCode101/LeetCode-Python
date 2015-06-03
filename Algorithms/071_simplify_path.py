#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        folders = []
        paths = path.split('/')
        
        for p in paths:
            if p == '.' or p == '':
                pass
            elif p == '..':
                if len(folders) > 0:
                    folders.pop()
            else:
                folders.append(p)
        
        return '/' + '/'.join(folders)
