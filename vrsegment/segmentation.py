#!/usr/bin/env python3

import os
import sys
import json

dictionary_file_path = "/usr/local/vrsegment/dictionary.json"
dictionary_file  = open(dictionary_file_path,'r')
dictionary = json.load(dictionary_file)

test_set_file = "/usr/local/vrsegment/test_set.txt"

key_set_file = "/usr/local/vrsegment/key_set.txt"

def check(word):
    global dictionary
    if word in dictionary:
        return True
    else:
        return False
#end def

def forwardCut(sentence):
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
            #print(sentence[i:j])
            if check(word):
                #print(word)
                last_word = ""
                if len(answer) != 0:
                    last_word = answer.pop()
                    position = position.pop()
                    #print("pop: "+last_word)
                elif i != start:
                    '''
                    try:
                        list_answer.pop()
                        list_position.pop()
                    except IndexError:
                        pass
                    '''
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
        #print(answer)
    #end while
    if i != start:
        list_answer.append(sentence[start:])
    return list_answer
#end def

def backwardCut(sentence):
    cuttedSentence = performBackwardCut(sentence)
    ans = recursiveDecompose(cuttedSentence)
    return ans

def performBackwardCut(sentence):
    #reverse the sentence

    # search from back of the string (front of reversed)
        # increment the lenngth of word-to-be-cut
        # if found in the dictionary keep the word as maxlength
        # else pass
    # if maxlength isset
        # return maxlength
    # else
        # word not found in dictionary skip one char and retry

    # return [left,word,right]
    if type(sentence) is not list :
        sentence = [sentence,"",""]

    [inleft, inskipword, inright] = sentence
    max_word = ''
    reversed_sentence = inleft[::-1]
    for length in range(1,len(reversed_sentence)+1):
        word = reversed_sentence[:length][::-1]
        if(word in dictionary):
            # search dictionary
            max_word = word
            ## print('found = '+max_word)
        else:
            pass

    if (max_word != ''):
        ## found in dictionary
        left = inleft[:-len(max_word)]
        skipword = ''
        right = max_word
        #print("Left = "+left+" word = "+word)
        return [performBackwardCut([left,'','']),skipword,right]
    else:
        ## not found in dictionary or done
        try:
            left = inleft[:-len(max_word)-1]
            skipword = inleft[-1]
            right = ''
            #print("Left = "+left+" word = "+word)
            return [performBackwardCut([left,'','']),skipword,right]
        except IndexError:
            pass
            #print("DONE")

def recursiveDecompose(sentencelist,ans=[]):

    ans = [] if len(ans)==0 else ans

    [left, skipword, right] = sentencelist

    if right is not None and right != '':
        ans.insert(0,right)
    if skipword is not None and skipword != '':
        ans.insert(0,skipword)
    if left is not None:
        recursiveDecompose(left,ans)
    return ans
    '''if(type(left) is not list):
        if(skipword == ''):
            if(string[0] == '|'):
                recursivePrint(left,"|"+right+string)
            else:
                recursivePrint(left,right+"|"+string)
        else:
            recursivePrint(left,skipword+string)
    else:
        ## print back
        print(right+"|"+string)
    '''
def calculateAcc(key,output):
    num_key = len(key)
    num_output = len(output)
    match_words = [word for word in output if word in key]
    if (len(match_words)/num_key<(len(match_words)/num_output)):
        return len(match_words)/num_key*100
    else:
        return len(match_words)/num_output*100


def test():
    print("Testing VRSegment")

    try:
        test_file = open(test_set_file, 'r',encoding="UTF-8")
        key_file  = open(key_set_file, 'r',encoding="UTF-8")
        num_lines = len(open(test_set_file).readlines())
        forward_avg = 0
        backward_avg = 0
        for line in test_file:
            sentence = line.strip("\n")
            key = key_file.readline().strip("\n")
            keyCutted = key.split("|")
            forwardCutted = forwardCut(sentence)
            backwardCutted = backwardCut(sentence)
            print(">> input:\t"+sentence)
            print(">> key:\t\t"+key)
            print(">> output 1:\t"+"|".join(forwardCutted))
            print(">> output 2:\t"+"|".join(backwardCutted))
            forward_acc = calculateAcc(keyCutted,forwardCutted)
            backward_acc = calculateAcc(keyCutted,backwardCutted)
            forward_avg = forward_avg + forward_acc
            backward_avg = backward_avg + backward_acc
            print(">> output 1 accuracy: \t"+"{:5.2f}".format(forward_acc))
            print(">> output 2 accuracy: \t"+"{:5.2f}".format(backward_acc))
        #end for
        forward_avg = forward_avg/num_lines
        backward_avg = backward_avg/num_lines
        print()
        print(">> output 1 avg: \t"+"{:5.2f}".format(forward_avg))
        print(">> output 2 avg: \t"+"{:5.2f}".format(backward_avg))
        test_file.close()
    except FileNotFoundError:
        pass
#end def
