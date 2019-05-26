class datetime_format:
    '''datetimeformat class has methods which take user input datetime 
        format and convert them into user defineddatetime format. 
        Note that input and output values are string type. By default, the output datetime format has values.
        ------methods------
        1. dateformat(input_date, input_date_format, output_date_format):e.g ('2018-16-03', '%y-%d-%m', '%y/%m/%d') => ('2018/03/16')
        2. timeformat(input_time, input_time_format, output_time_format) :e.g ('02:10:03', 'h:s:m', 'h:m:s') => ('02:03:10')
        3. datetimeformat(input_datetime, input_datetime_format, output_datetime_format):e.g ('2018-16-03 02:10:03', '%y-%d-%m h:s:m', '%y/%m/%d h:m:s') => ('2018/03/16 02:03:10')
        
        '''
    def __init__(self):
        pass
    
    
    #takes string as input , split it using '%' as delimiter
    # and returned cleaned list and delimiter
    @classmethod
    def get_itemformat(cls, x):
        x_list=str(x).split('%')[1:]
        delimiter=x_list[0][1:]
        for i in range(len(x_list)-1):
            x_list[i]=x_list[i][0]
            
        return([x_list, delimiter])
    
    # string is split using delimiter and returns the list
    @classmethod
    def get_itemformat_value(cls, x, delimiter):
        return(str(x).split(delimiter))
    
    # maps y=value, m=value, d=value or h=value, m=value, d=value
    @classmethod
    def format_value_map(cls, x_format, x):
        x_dict={}
        for i in range(len(x)):
            x_dict[x_format[i]]=x[i]
            
        return(x_dict)
        
    @classmethod
    def get_output_list(cls, x_dict, y_format_list):
        output_list=[]
        for i in range(len(y_format_list)):
            value=x_dict[y_format_list[i]]
            output_list.append(value)
        
        return(output_list)
        
    @classmethod
    def dateformat(cls, x, x_format, y_format='%y-%m-%d'):
        '''
        dateformat method takes three input of string type
        input1: date value
        input2: dateformat of input1
        input3: output date format 
        output: date value is converted into user defined date value with format done on input1 using input 3
        '''
        x_format_list, x_delimiter=cls.get_itemformat(x_format)
        x_list=cls.get_itemformat_value(x, x_delimiter)
        
        x_dict=cls.format_value_map(x_format_list, x_list)
        
        y_format_list, y_delimiter=cls.get_itemformat(y_format)
        output_list=cls.get_output_list(x_dict, y_format_list)
        output_string=str(y_delimiter).join(output_list)
        
        return(output_string)
    
    @classmethod 
    def timeformat(cls, x, x_format, y_format='h:m:s'):
        '''
        timeformat method takes three input of string type
        input1: date value
        input2: timeformat of input1
        input3: output time format 
        output: time value is converted into user defined time value with format done on input1 using input 3
        '''
        x_delimiter=x_format[1]
        x_format_list=cls.get_itemformat_value(x_format, x_delimiter)
        x_list=cls.get_itemformat_value(x, x_delimiter)
        
        x_dict=cls.format_value_map(x_format_list, x_list)
        
        y_delimiter=y_format[1]
        y_format_list=cls.get_itemformat_value(y_format, y_delimiter)
        
        output_list=cls.get_output_list(x_dict, y_format_list)
        output_time=str(y_delimiter).join(output_list)
        return(output_time)
        
        
    @classmethod
    def datetimeformat(cls, x, x_format, y_format='%y-%m-%d h:m:s'):
        '''
        datetimeformat method takes three input of string type
        input1: datetime value
        input2: datetimeformat of input1
        input3: output datetime format 
        output: datetime value is converted into user defined datetime value with format done on input1 using input 3
        '''
        x_date, x_time=cls.get_itemformat_value(x, ' ')
        x_format_date, x_format_time=cls.get_itemformat_value(x_format, ' ')
        y_format_date, y_format_time=cls.get_itemformat_value(y_format, ' ')
        
        output_date=cls.dateformat(x_date, x_format_date, y_format_date)
        output_time=cls.timeformat(x_time, x_format_time, y_format_time)
        output=[output_date, output_time]
        output_datetime=' '.join(output)
        return(output_datetime)
        



        
        
    








