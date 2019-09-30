#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json

class Student(object):

	def __init__(self,name,score):
		self.__name=name
		self.__score=score

	def print_score(self):
		print "%s: %s"%(self.__name,self.__score)


if __name__=='__main__':

	bart=Student('Bart simpson',59)
	lisa=Student('Lisa Simpson',87)
	bart.print_score()
	lisa.print_score()
	print json.dumps(bart,default=lambda obj:obj.__dict__)
	print json.dumps(lisa,default=lambda obj:obj.__dict__)