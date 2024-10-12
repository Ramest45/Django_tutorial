class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self,value):
        return int(value)
    
    def to_url(self,value):
        return f'{value:4d}'
        #     or
        # return '%4d' % value
        #isme 4 denotes kr rha no. of digits ko and d represent kr rha integer ko.