import regex

a = '''
    <li data-filter="1" >
        <a target="_blank" class="small-news-link" href="/news/1578625/90-دقیقه-سرنوشت-ساز-برای-احمد-نوراللهی" target="_blank" title="90 دقیقه سرنوشت ساز برای احمد نوراللهی">90 دقیقه سرنوشت ساز برای احمد نوراللهی</a>
    </li>
    <li data-filter="1" >
        <a target="_blank" class="small-news-link" href="/news/1578623/اعلام-ترکیب-تیم-ملی-برابر-فلسطین" target="_blank" title="اعلام ترکیب تیم ملی برابر فلسطین">اعلام ترکیب تیم ملی برابر فلسطین</a>
    </li>
    <li data-filter="1" >
'''
regexpattern = r'href=\"([^\"]*)\"'

resp = regex.findall(regexpattern, a)

for x in resp:
    print(x)
