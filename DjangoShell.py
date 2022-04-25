import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')

import django
django.setup()

from MainApp.models import Topic

topics = Topic.objects.all() # Behaves like select * from Topic in SQL

for t in topics:
    print(t.id, ' ', t) # 't' prints as the topic text because of the __str__ method from models.py

t = Topic.objects.get(id = 1) # Behaves like select * from Topic where id = 1 in SQL
print(t.text)
print(t.date_added)

entries = t.entry_set.all()

for e in entries:
    print(e)
