class datetimeformat:
    '''datetimeformat class has methods which take user input datetime 
        format and convert them into user defineddatetime format. 
        Note that input and output values are string type. By default, the output datetime format has values.'''
    def __init__(self):
        pass
    
    
    #takes string as input , split it using '%' as delimiter
    # and returned cleaned list and delimiter
    def get_itemformat(self, x):
        x_list=str(x).split('%')[1:]
        delimiter=x_list[0][1:]
        for i in range(len(x_list)-1):
            x_list[i]=x_list[i][0]
            
        return([x_list, delimiter])
    
    # string is split using delimiter and returns the list
    def get_itemformat_value(self, x, delimiter):
        return(str(x).split(delimiter))
    
    # maps y=value, m=value, d=value or h=value, m=value, d=value
    def format_value_map(self, x_format, x):
        x_dict={}
        for i in range(len(x)):
            x_dict[x_format[i]]=x[i]
            
        return(x_dict)
    
    def get_output_list(self, x_dict, y_format_list):
        output_list=[]
        for i in range(len(y_format_list)):
            value=x_dict[y_format_list[i]]
            output_list.append(value)
        
        return(output_list)
        
    
    def dateformat(self, x, x_format, y_format='%y-%m-%d'):
        '''
        dateformat method takes three input of string type
        input1: date value
        input2: dateformat of input1
        input3: output date format 
        output: date value is converted into user defined date value with format done on input1 using input 3
        '''
        x_format_list, x_delimiter=self.get_itemformat(x_format)
        x_list=self.get_itemformat_value(x, x_delimiter)
        
        x_dict=self.format_value_map(x_format_list, x_list)
        
        y_format_list, y_delimiter=self.get_itemformat(y_format)
        output_list=self.get_output_list(x_dict, y_format_list)
        output_string=str(y_delimiter).join(output_list)
        
        return(output_string)
    
        
    def timeformat(self, x, x_format, y_format='h:m:s'):
        '''
        timeformat method takes three input of string type
        input1: date value
        input2: timeformat of input1
        input3: output time format 
        output: time value is converted into user defined time value with format done on input1 using input 3
        '''
        x_delimiter=x_format[1]
        x_format_list=self.get_itemformat_value(x_format, x_delimiter)
        x_list=self.get_itemformat_value(x, x_delimiter)
        
        x_dict=self.format_value_map(x_format_list, x_list)
        
        y_delimiter=y_format[1]
        y_format_list=self.get_itemformat_value(y_format, y_delimiter)
        
        output_list=self.get_output_list(x_dict, y_format_list)
        output_time=str(y_delimiter).join(output_list)
        return(output_time)
        
        
    
    def datetimeformat(self, x, x_format, y_format='%y-%m-%d h:m:s'):
        '''
        datetimeformat method takes three input of string type
        input1: datetime value
        input2: datetimeformat of input1
        input3: output datetime format 
        output: datetime value is converted into user defined datetime value with format done on input1 using input 3
        '''
        x_date, x_time=self.get_itemformat_value(x, ' ')
        x_format_date, x_format_time=self.get_itemformat_value(x_format, ' ')
        y_format_date, y_format_time=self.get_itemformat_value(y_format, ' ')
        
        output_date=self.dateformat(x_date, x_format_date, y_format_date)
        output_time=self.timeformat(x_time, x_format_time, y_format_time)
        output=[output_date, output_time]
        output_datetime=' '.join(output)
        return(output_datetime)
        
        
    










