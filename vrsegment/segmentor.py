#!/usr/bin/env python3

import os.path
import sys
import json

dictionary_file_path = "src/thai-wordlist.json"
dictionary_file  = open(dictionary_file_path,'r')
dictionary = json.load(dictionary_file)

test_set_file = "src/test_set.txt"

key_set_file = "src/key_set.txt"


#import pickle
#dictionary_file_path = "src/thdict"
#fileObject = open(dictionary_file_path,'rb')
#dictionary = pickle.load(fileObject)

class Segmentor:

    @staticmethod
    def check(word):
        global dictionary
        if word in dictionary:
            return True
        else:
            return False
    #end def

    @staticmethod
    def segment(sentence):
        list_position = []
        list_answer = []
        start = 0
        end = 0
        i = 0
        while i < len(sentence):
            answer = list()
            position = list()
            end = start
            for j in range(i, len(sentence) + 1):
                word = sentence[i:j]
                if Segmentor.check(word):
                    #print(word)
                    last_word = ""
                    if len(answer) != 0:
                        last_word = answer.pop()
                        position = position.pop()
                    if i != start:
                        try:
                            list_answer.pop()
                            list_position.pop()
                        except IndexError:
                            pass
                        list_answer.append(sentence[start:i])
                        list_position.append(i)
                    answer.append(word)
                    position.append([i])
                    end = j
            if end == start:
                i = i+1
            else:
                start = end
                i = start
                list_answer.append(answer[-1])
                list_position.append(position[-1])
                #end if
            #end for
        #end while
        if i != start:
            list_answer.append(sentence[start:])
        return list_answer
    #end def

    @staticmethod
    def test():
        print("Testing VRSegment")

        try:
            test_file = open(test_set_file, 'r',encoding="UTF-8")
            key_file  = open(key_set_file, 'r',encoding="UTF-8")
            num_lines = len(open(test_set_file).readlines())
            for line in test_file:
                sentence = line.strip("\n")
                segmented = Segmentor.segment(sentence)
                key = key_file.readline()
                print(">> input:\t"+sentence)
                print(">> output:\t"+"|".join(segmented))
                print(">> key:\t\t"+key)
                print()
            #end for
            test_file.close()
        except FileNotFoundError:
            pass
    #end def
