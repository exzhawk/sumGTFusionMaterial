from __future__ import division

Result={}
def sumMaterial(sth,num):
    for name,count in globals()[sth].items():
        if name in globals():
            sumMaterial(name,num*count)
        else:
            if name in Result:
                Result[name]+=(count*num)
            else:
                Result[name]=(count*num)
needSum={'theReactorFuel':1,'theReactor':1}
for k,v in needSum.items():
    print ''.ljust(16,'=')
    print 'to make',v,k,', you need'
    print ''.ljust(8,'-')
    sumMaterial(k,v)
    for (name,count) in sorted(Result.items()):
        print name,'\t',count
