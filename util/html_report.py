import unittest
from TestCase.demo import demo
from HTMLTESTRunner import HTMLTestRunner

if __name__=='__main__':
    suite=unittest.makeSuite(demo)
    filename='D:\\myreport.html'
    fp=file(filename,'wb')
    runner=HTMLTestRunner(fp,title=u'my unit test',description=u'This is a report test')
    runner.run(suite)
