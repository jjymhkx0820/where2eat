#!/usr/local/bin/python
# coding:utf8

import os,sys
import random
import math
import heapq
import pdb

class norm_random_list():
    def __init__(self,ds):
        self.rest_name=[]
        self.rest_weight=[]
        self.p=[]
        self.result_list=[]
        for k,v in ds.items():
            #print "k,v = %s,%d" % (k,v)
            self.rest_name.append(k)
            self.rest_weight.append(v)
        self.wtlist=[1.*x/sum(self.rest_weight) for x in self.rest_weight]
        i=0
        for t in self.wtlist:
            #print "test value %f,%f" % (1./t,1./t/3)
            self.p.append((random.normalvariate(1./t,1./t/3),i))
            i=i+1
        heapq.heapify(self.p)

    def show_heap_and_clean(self):
        while len(tt.p) > 0:
            try:
                minp,minj = heapq.heappop(self.p)
                print minp,minj
            except:
                print e

    def creat_list(self):
        assert(len(self.rest_name)>0)
        assert(len(self.rest_name) == len(self.p))
        self.result_list=[]
        maxlen=1000
        for i in range(0,maxlen):
            try:
                minp,minj=heapq.heappop(self.p)
                self.result_list.append(self.rest_name[minj])
                heapq.heappush(self.p,(random.normalvariate(1./self.wtlist[minj],1./self.wtlist[minj]/3)+minp,minj))
            except Exception,e:
                print "error in rerandom score for headppush. msg : %s" % e 
                sys.exit(1)

    def show_result_list(self):
        assert(len(self.rest_name) == len(self.rest_weight))
        s=""
        for i in self.result_list:
            try:
                s=s+self.rest_name[i]+" "
            except Exception,e:
                print e
        
        print s.strip()

if __name__ == "__main__":
    ds={"a":1,"b":2,"c":17}
    tt=norm_random_list(ds)
    tt.creat_list()
    tt.show_result_list()
