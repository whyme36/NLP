
import urllib.request, re
import numpy as np
class Graph_from_links:
    def get_n_pages_in_category(self, url: str) ->dict:
        form_page = re.findall(r'pagerank/([^"]+)', url)
        page = urllib.request.urlopen(url)
        code = page.read().decode('utf-8')
        sites = set(re.findall(r'<a href="([^"]+)"', code))
        output_dict={form_page[0]: sites}

        path = 'https://lewoniewski.info/sw/pagerank/'
        for site in sites:
            url=path+site
            page_in_site = urllib.request.urlopen(url)
            code_in_site = page_in_site.read().decode('utf-8')
            sites_in_site = set(re.findall(r'<a href="([^"]+)"', code_in_site))
            output_dict[site]=sites_in_site
        sites_not_detected= self.is_there_any_links(output_dict)
        if sites_not_detected != []:
            for site in sites_not_detected:
                    url= path + site
                    page = urllib.request.urlopen(url)
                    code = page.read().decode('utf-8')
                    sites = set(re.findall(r'<a href="([^"]+)"', code))
                    output_dict[site] = sites
        return output_dict

    def is_there_any_links(self,graph:dict) -> list:
        links_visited=[]
        for key in graph.keys():
            links_visited.append(key)
        links_not_visited=[]
        for links in graph.values():
            for link in links:
                if link not in links_visited and link not in links_not_visited:
                    links_not_visited.append(link)
        return links_not_visited
    def make_graph_matrix(self, graph:dict):
        output=[[] for i in range(len(graph))]
        columns=[]
        for key in graph.keys():
            columns.append(key)
        for index,site in enumerate(graph.keys()):
            site_links=graph[site]
            for column_site in columns:
                if column_site in site_links:
                    output[index].append(1)
                else:
                    output[index].append(0)
        return output
class PageRank:
    def create_probabilistic_matrix(self,matrix:list,d:int):
        output_matrx=[]
        arrays_len=len(matrix[0])
        for array in matrix:
            if sum(array) == 0:
                output_matrx.append([1/arrays_len for _ in array])
            else:
                sum_elem=sum(array)
                array=[d*x/sum_elem for x in array]
                array=[round(x+((1-d)/arrays_len),4) for x in array]
                output_matrx.append(array)
        return np.array(output_matrx)
if __name__ == '__main__':
    graph=Graph_from_links()
    url='https://lewoniewski.info/sw/pagerank/poznan.html'

    page = urllib.request.urlopen(url)
    code = page.read().decode('utf-8')

    graph_of_sites=graph.get_n_pages_in_category(url)
    # print(graph_of_sites)
    d=0.85
    matrix=np.array(graph.make_graph_matrix(graph_of_sites))
    print(matrix)

    matrix=PageRank().create_probabilistic_matrix(matrix, d)
    print(matrix)
    y = np.array([1, 0, 0, 0, 0, 0, 0, 0])



    print()
    y = y.dot(matrix)
    print(y)
    # previous_y = 0
    #
    # while True:
    #     if (y>previous_y+previous_y*0.0001).all():
    #         previous_y = y
    #         y = y.dot(matrix)
    #     else:
    #         break
    #
    #
    # print(y)
