
import urllib.request, re
import numpy as np
class Graph_from_links:
    def get_n_pages_in_category(self, url: str) ->dict:
        form_page = re.findall(r'/([^"]+).html$', url)
        form_page = form_page[0].split('/')[-1]+'.html'
        page_site = re.findall(r'/([^"]+).html$', url)[0].split('/')[-2]
        page = urllib.request.urlopen(url)
        code = page.read().decode('utf-8')
        sites = set(re.findall(r'<a href="([^"]+)"', code))
        output_dict={form_page: sites}

        path = f'https://lewoniewski.info/sw/{page_site}/'
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
        graph={k: v for k, v in sorted(graph.items(), key=lambda item: item[0])}
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
                array=[x+((1-d)/arrays_len) for x in array]
                output_matrx.append(array)
        return np.array(output_matrx)
if __name__ == '__main__':
    # create conncetion matrix from url
    graph=Graph_from_links()
    # url='https://lewoniewski.info/sw/pagerank/poznan.html'
    url='https://lewoniewski.info/sw/pagerank2/polska.html'

    page = urllib.request.urlopen(url)
    code = page.read().decode('utf-8')

    graph_of_sites=graph.get_n_pages_in_category(url)
    # print(graph_of_sites)

    matrix=np.array(graph.make_graph_matrix(graph_of_sites))
    # print(matrix)
    #create PageRank matrix
    d = 0.85
    matrix=PageRank().create_probabilistic_matrix(matrix, d)
    # print(matrix)
    vector = np.array([0 for x in matrix[0]])
    vector[0]=1
    previous= np.array([0 for x in matrix[0]])
    # print()
    # print(vector)
    # print(previous)
    # iteration to best result 
    while not np.allclose(previous, vector, rtol=0, atol=1e-06):
        previous = vector
        vector = vector.dot(matrix)


    print(vector.round(4))

