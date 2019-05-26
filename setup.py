from distutils.core import setup
setup(
      name = 'datetime_format',         # How you named your package folder (MyLib)
      packages = ['datetime_format'],   # Chose the same as "name"
      version = '1.0.4',      # Start with a small number and increase it with every change you make
      license=None,        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
      description = 'It converts dateime string into another datetime string with formatting done on it by user',   # Give a short description about your library
      author = 'Prakash Besra',                   # Type in your name
      author_email = 'psbesra@gmail.com',      # Type in your E-Mail
      url = 'https://github.com/pbesra',   # Provide either the link to your github or to your website
      download_url = 'https://github.com/pbesra/datetime_format/archive/v1.0.4.tar.gz',    
      keywords = ['date', 'time', 'datetime', 'dateformat', 'timeformat', 'datetimeformat'],   # Keywords that define your package best
      
      classifiers=[
              'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
              'Intended Audience :: Developers',      # Define that your audience are developers
              'Topic :: Software Development :: Build Tools',
              'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
              'Programming Language :: Python :: 3.7',
              ],
)
