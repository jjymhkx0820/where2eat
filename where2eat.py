#!/usr/local/bin/python
# -*- coding: utf8 -*-

import os,sys
import random
import hashlib
import cPickle as pickle
import pdb

from result_list import result_rank 
from norm_random_list import norm_random_list 

def print_error_msg(s):
    print "record in config file format error. [%s]" % s.strip()
    print "the right format like this:"
    print "    kfc|2  ##restaurant'name | eay_times/weeks(must > 0)"
    
def get_sign(filename):
    f=open(filename)
    s1=hashlib.sha1()
    s1.update(f.read())
    return s1.hexdigest()

def parse(line,ds):
    list=line.strip().split("|")
    if len(list) != 2:
        print_error_msg(line)
        raise RuntimeError("config line %s is illegal." % line.strip())

    try:
        ds[list[0]]=int(list[1])
    except Exception,e:
        print_error_msg(e)
        raise RuntimeError("config line %s is illegal." % line.strip())

def check_file(filename):
    if not os.path.exists(filename):
        print "config file %s is not exist." % filename
        sys.exit(1)

def load_ds(filename,ds):
    file=open(filename)
    try:
        for line in file:
            parse(line,ds)
    except:
        sys.exit(1)
    finally:
        file.close()

def load_object(result_list):
    f=open(result_list,"r+")
    try:
        tt=pickle.load(f)
        #print tt.nowidx
        return tt
    except Exception,e:
        print "load_object error."
    finally:
        f.close()

def dump_object(result_list,tt):
    f=open(result_list,"wb")
    try:
        pickle.dump(tt,f)
    except Exception,e:
        print "dump_object error."
    finally:
        f.close()

def creat_new_rr(sign,ds):
    rr=result_rank()
    rr.sign=sign
    rr.nowidx=0
    tt=norm_random_list(ds)
    tt.creat_list()
    rr.result_list=tt.result_list
    return rr

def update_rr(result_list,tt):
    tt=load_object(result_list)
    print tt.nowidx
    tt.nowidx=tt.nowidx+1
    dump_object(result_list,tt)

if __name__ == "__main__":
    config_file="base.config"
    result_list=".resulttlist"
    sign=""

    if(len(sys.argv)>1):
        config_file=sys.argv[1]
    check_file(config_file)
    sign=get_sign(config_file)

    ds={}
    load_ds(config_file,ds)

    if not os.path.exists(result_list):
        rr=creat_new_rr(sign,ds)
        if rr.nowidx < len(rr.result_list):
            print rr.result_list[rr.nowidx]
            rr.nowidx=rr.nowidx+1
            dump_object(result_list,rr)
        else:
            print "error: rr.nowidx >= len(rr.result_list)."
            sys.exit(1)
    else:
        tt=load_object(result_list)
        if tt.sign == sign:
            print tt.result_list[tt.nowidx]
            tt.nowidx=tt.nowidx+1
            dump_object(result_list,tt)
        else:
            rr=creat_new_rr(sing,ds)
            if rr.nowidx < len(tt.result_list):
                print rr.result_list[rr.nowidx]
                rr.nowidx=rr.nowidx+1
                dump_object(result_list,rr)
            else:
                print "error: tt.nowidx >= len(tt.result_list)."
                sys.exit(1)

