import urllib.request, re

class Solution:
    """
    This is a class task:
    Prepare a program that extracts the following information from the HTML code of the first n articles of the Polish-language Wikipedia in the indicated category:
    * Names of other Wikipedia articles linked to (internal) links in the current article, along with the content links
    * URLs of the used images
    * Source URLs (external)
    * Names of assigned categories to the article
    """
    def get_n_pages_in_category(self,url:str,n:int):
        # url='https://pl.wikipedia.org/wiki/Kategoria:Miasta_w_Polsce'
        # n=5
        page = urllib.request.urlopen(url)

        code=page.read().decode('utf-8')

        output=re.findall(r'<li><a href="/wiki/([^"]+)"',code)
        page_to_download=[]
        for element in output[:n]:
            page_to_download.append(element)
        return page_to_download
    def get_contentLinks_imgLinks_categoryLinks_footnoteLInks_and_write_file(self,page_to_download):
        for index,web in enumerate(page_to_download):
            url='https://pl.wikipedia.org/wiki/'+web
            page = urllib.request.urlopen(url)
            code=page.read().decode('utf-8')
            print (str(index+1)+'.txt')
            output_addresses=re.findall(r'<a href="/wiki/([^"]+)"[^>]*>([^<]+)</a>',code)
            output_imgs=re.findall(r'src="//([^"]+)"',code)
            output_footnote = re.findall(r'class="external text" href="([^"]+)"', code)
            output_categories = re.findall(r'<li><a href="/wiki/Kategoria:([^"]+)"', code)
            with open(str(index + 1) + '.txt', 'w', encoding='utf-8') as plik:
                plik.write(
                    'Nazwy innych artykułów Wikipedii do których prowadzą odnośniki (wewnętrzne) w bieżącym artykule wraz z treścią odnośników: \n')
                for w in output_addresses:
                    if ':' not in w[0]:
                        plik.write(f'{w[0]}\t{w[1]}\n')
                plik.write('addresses URL wykorzystanych obrazków: \n')
                for w in output_imgs:
                    plik.write(f'{w}\n')
                plik.write('addresses URL źródeł (zewnętrzne): \n')
                for w in output_footnote:
                    plik.write(f'{w}\n')
                plik.write('Nazwy przypisanych kategorii do artykułu: \n')
                for w in output_categories:
                    if 'Artyku' not in w:
                        plik.write(f'{w}\n')
if __name__ == '__main__':
    s=Solution()
    category_link=input()
    nb_of_links=int(input())
    page_to_download=s.get_n_pages_in_category(url=category_link,n=nb_of_links)
    s.get_contentLinks_imgLinks_categoryLinks_footnoteLInks_and_write_file(page_to_download=page_to_download)
