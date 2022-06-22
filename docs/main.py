from bs4 import BeautifulSoup
import re
import os
import importlib
import pandas as pd




def LoadConfig(config_file):
    config_path = os.path.dirname(config_file)
    config_base = os.path.basename(config_file)
    config_name, _ = os.path.splitext(config_base)
    os.sys.path.insert(0, config_path)
    lib = importlib.import_module(config_name)
    os.sys.path.pop(0)

    return lib.cfg

cfg = LoadConfig('config.py')


class HTML:
    def __init__(self,filename='index.html'):
        HTMLFile = open("index.html", "r", encoding='utf8')

        # Reading the file
        index = HTMLFile.read()

        # Creating a BeautifulSoup object and specifying the parser
        self.S = BeautifulSoup(index, 'lxml')

        self.result_num = 0

    def set_title(self,title):
        old_text = self.S.find('title')
        new_text = old_text.find(text=re.compile('Title Here')).replace_with(title)
        old_text = self.S.find('span')
        new_text = old_text.find(text=re.compile('Title Here')).replace_with(title)



    def set_abstract(self,abstract):
        old_text = self.S.find('p',{'id':'abstract'})
        new_text = old_text.find(text=re.compile('Abstract Here')).replace_with(abstract)


    def set_author(self,authors,institutions):
        author_header = "<table id=\"authors_new\" align=\"center\" width=\"800px\"><tbody><tr>"

        author_footer = " </tr></tbody></table><br>"

        body = ''

        for idx, author in enumerate(authors):
            body += '<td align=\"center\" width=\"160px\"><center><span style=\"font-size:16px\">%s</a><sup>%s</sup></span></center></td>'%(author,authors[author])
            if idx == 4:
                body += '</tr><tr>'


        html = author_header  + body + author_footer
        html = BeautifulSoup(
            html, "html.parser"
        )

        self.S.find(id='authors').insert_after(html)
        self.S.find(id='authors').extract()


        institution_header = "<table id=\"instutions_new\" align=\"center\" width=\"800px\"><tbody>"

        institution_footer = " </tbody></table><br>"

        body = ''

        for idx, institution in enumerate(institutions):
            body += '<tr align=\"center\" width=\"160px\"><center><span style=\"font-size:16px\"><sup>%s</sup>%s</a></span></center></tr>'%(institution,institutions[institution])


        html = institution_header  + body + institution_footer
        html = BeautifulSoup(
            html, "html.parser"
        )

        self.S.find(id='institutions').insert_after(html)
        self.S.find(id='institutions').extract()

    def set_codelinks(self, codelinks):

        table = self.S.find(id='links')
        for row in table.findAll("tr"):
            cells = row.findAll("td")
            for idx,cell in enumerate(cells):
                if idx <= 1:
                    for linkitem in cell.find_all('a'):
                        linkitem['href']= linkitem['href'].replace('code link',str(codelinks[idx]))


    def set_method(self, method,graphabstract):
        old_text = self.S.find('p', {'id': 'method'})
        old_text.find(text=re.compile('Method Here')).replace_with(method)

        old_text = self.S.find('table',{'id':'graph abstract'})
        old_text.find_all('img')[0]['src'] = graphabstract


    def set_results(self, title,filepath,caption,type='figure',width=800):
        if type == 'figure':
            html = '<p align="left"><strong>%s</strong></p>'\
                '<table align="center" width="800px">'\
                    '<tbody><tr>'\
                    '<td align="center" width="%ipx">'\
                    '<center>'\
                    '<img style="width:600px" src="%s"></img>'\
                    ' </center>'\
                    ' </td>'\
                    '</tr></tbody>'\
                    ' </table> <p align="left">%s</p>'%(title,width,filepath,caption)
        elif type == 'table':
            table = pd.read_excel(filepath)
            html = table.to_html()
            html = '<p align="left"><b>%s</b></p>'%title +  html + ' </table> <p align="left">%s</p>'%(caption)

        elif type == 'text':
            pass
        else:
            raise ValueError('Only table,figure and text can be added as results')

        html = BeautifulSoup(
            html, "html.parser"
        )


        self.S.find('h2',{'id':'results'}).insert_after(html)



    def save_html(self):
        with open('new.html', 'wb') as f_output:
            f_output.write(self.S.prettify('utf-8'))



if __name__ == '__main__':
    page = HTML()
    page.set_title(cfg.title)
    page.set_author(cfg.authors,cfg.institutions)
    page.set_abstract(cfg.abstract)
    page.set_codelinks(cfg.codelinks)
    page.set_method(cfg.method,cfg.graphabstract)
    for i in range(len(cfg.results),0,-1):
        page.set_results(getattr(cfg.results, 'item%i'%i).title,
                        getattr(cfg.results, 'item%i'%i).filepath,
                         getattr(cfg.results, 'item%i'%i).caption,
                         type=getattr(cfg.results, 'item%i'%i).type)
    page.save_html()
    a = 0