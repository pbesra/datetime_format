<pre>
<h3>Description here</h3>
<code>
  It converts user input datetime string into user defined datetime string with formatting done on user input
</code>
</pre>

<pre>
<h3>Example</h3>
<code>
  <b>input</b>: ('2019-18-03 10:03:11', '%y-%d-%m h:s:m', '%y/%m/%d h:m:s')
  <b>output</b>: ('2019/03/18 10:11:03')
</code>
</pre>

<pre>
<h3>How to install</h3>
<code> C:\>pip install datetime_format
e.g
in python terminal
>>
>>from datetime_format import datetime_format
>>datetime_format.timeformat('06:09:10', 'm:s:h', 'h:m:s')
>>'10:06:09'
>>
>>datetime_format.dateformat('2018-17-04', '%y-%d-%m', '%y-%m-%d')
>>'2018-04-17'
>>
>>datetime_format.datetimeformat('2018-17-04 06:09:10', '%y-%d-%m m:s:h', '%y-%m-%d h:m:s')
>>'2018-04-17 10:06:09'
>>
</code>
</pre>
