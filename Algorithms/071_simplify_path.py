#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        i = 0
        folders = []
        path_length = len(path)
        start_index_of_folder = -1
        
        while i < path_length:
            current = path[i]
            
            if current == '/' and start_index_of_folder != -1:
                folder = path[start_index_of_folder:i]
                    
                self.append_folder(folders, folder)
                        
                start_index_of_folder = -1
            elif current != '/' and start_index_of_folder == -1:
                start_index_of_folder = i
            
            i += 1

        if start_index_of_folder != -1:
            folder = path[start_index_of_folder:]
            
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
