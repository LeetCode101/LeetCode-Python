#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        i = 0
        folder = ''
        folders = []
        path_length = len(path)
        
        while i < path_length:
            current = path[i]
            
            if current == '/' and folder != '':
                self.append_folder(folders, folder)
                        
                folder = ''
            elif current != '/':
                folder += current
            
            i += 1

        if folder != '':
            self.append_folder(folders, folder)
        
        return '/' + '/'.join(folders)

    def append_folder(self, folders, folder):
        if folder == '.':
            pass
        elif folder == '..':
            if len(folders) > 0:
                folders.pop()
        else:
            folders.append(folder)
