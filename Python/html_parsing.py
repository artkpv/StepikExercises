from requests import get
from re import findall, search

def print_sites(text) :
    found = []
    for href in findall(r'(?i)\<a[^>]+?href\s*=\s*("[^"]+"|\'[^\']+\')', text) :
        href = href.strip('\'"')
        #print("parsing:",href)
        site = search(r'^(\w+://)?((\.?[\w-]+)+)', href)
        if site and site.group(2) not in found :
            found.append(site.group(2))
    print('\n'.join(sorted(found)))

url = input()
r = get(url)
if r.status_code == 200 :
    print_sites(r.text)



test = '''<li><a href="http://redir.rbc.ru/cgi-bin/redirect.cgi?http://hc.ru/ru/">Хостинг</a></li> #ссылку из редиректа ﻿(hc.ru/ru) не ловим!!
<li><a href="http://www.m-2.ru/">M2</a></li>
<a target="_top" href="http://banner.rbc.ru/banredir.cgi?lid=firstpage_left" empty="true" style="display:none"></a></div>
<li><a href="http://www.biztorg.ru/search.shtml?cfg=biztorg&type=S">Предложения о продаже</a></li>
<li><a href="http://biztorg.ru:80/main_services_new.shtml">Оценка бизнеса</a></li>
<a href="http://static.feed.rbc.ru/rbc/internal/rss.rbc.ru/rbcdaily.ru/mainnews.rss" class="flRight small" style="margin:0 0 0 5px;">
'''

print_sites(test)

