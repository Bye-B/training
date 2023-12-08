from abc import ABC
from mrjob . job import MRJob

class Count (MRJob, ABC) :
    
    def mapper (self ,_ , line) :
        for word in line.split() :
            print(word)
            yield word , 1

    def reducer(self , word , counts ) :
        print(word, sum(counts))
        print("hi")
        yield word , sum(counts)

    def run(self):
        self.mapper(self,)

if __name__ == ' main ' :
    Count.run()
