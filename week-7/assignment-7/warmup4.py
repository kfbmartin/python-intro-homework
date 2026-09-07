#Print today's date
#datetime.now() and .strftime().

from datetime import datetime

now = datetime.now()
print(f"Today is {now.strftime('%B %d, %Y')}") 