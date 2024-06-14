import requests
from bs4 import BeautifulSoup
import re 

page = requests.get("https://www.google.com/search?client=safari&rls=en&q=%22support+analyst%22+%22career%22+%22canada%22+%22remote%22+-site%3Alinkedin.com+-site%3Aindeed.com+-site%3Aglassdoor.ca&ie=UTF-8&oe=UTF-8")
soup = BeautifulSoup(page.content, "html.parser"
                     )

for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    print(re.split(":(?=http)",link["href"].replace("/url?q=","")))
