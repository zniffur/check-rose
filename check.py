from bs4 import BeautifulSoup
import requests

proxies = {
    'http': '',
    'https': '',
}


def check_rose_print():
    try:
        r = requests.get('http://leghe.fantagazzetta.com/fantatilab/rose')
    except requests.exceptions.ProxyError:
        r = requests.get(
            'http://leghe.fantagazzetta.com/fantatilab/rose', proxies=proxies)

    html_doc = r.content
    soup = BeautifulSoup(html_doc, "html5lib")

    link_list = soup.find_all("li", class_="list-rosters-item")

    for link in link_list:
        print(link.h4.text)  # nome fantasq
        # print('----------')
        tmplist = []
        for child in link.table.tbody.children:
            # tabella calciatori fantasq
            if child.span is not None:
                # print(child.span.text)
                tmplist.append(child.span.text)
        print(tmplist.count('P'), tmplist.count('D'),
              tmplist.count('C'), tmplist.count('A'))
        if (tmplist.count('P') > 4 or tmplist.count('D') > 10 or tmplist.count('C') > 10 or tmplist.count('A') > 8):
            players = link.table.tbody
            for player in players:
                if player.span is not None:
                    print(player.span.text, player.a.text)
        print('--------------')

    return r.status_code


def check_rose():
    try:
        r = requests.get('http://leghe.fantagazzetta.com/fantatilab/rose')
    except requests.exceptions.ProxyError:
        r = requests.get(
            'http://leghe.fantagazzetta.com/fantatilab/rose', proxies=proxies)

    html_doc = r.content
    soup = BeautifulSoup(html_doc, "html5lib")

    link_list = soup.find_all("li", class_="list-rosters-item")

    return_string = ''
    for link in link_list:
        # print(link.h4.text)  # nome fantasq
        return_string += link.h4.text + '\n'
        # print('----------')
        tmplist = []
        for child in link.table.tbody.children:
            # tabella calciatori fantasq
            if child.span is not None:
                # print(child.span.text)
                tmplist.append(child.span.text)
        # print(tmplist.count('P'), tmplist.count('D'),
        #       tmplist.count('C'), tmplist.count('A'))
        return_string += str(tmplist.count('P')) + ' ' + str(tmplist.count('D')) + \
            ' ' + str(tmplist.count('C')) + ' ' + \
            str(tmplist.count('A')) + '\n'
        if (tmplist.count('P') > 4 or tmplist.count('D') > 10 or tmplist.count('C') > 10 or tmplist.count('A') > 8):
            players = link.table.tbody
            for player in players:
                if player.span is not None:
                    # print(player.span.text, player.a.text)
                    return_string += player.span.text + ' ' + player.a.text + '\n'
        # print('--------------')
        return_string += '--------------' + '\n'

    return return_string


def check_rose_html():
    try:
        r = requests.get(
            'http://leghe.fantagazzetta.com/fantatilab/rose', proxies=proxies)
        print('PROXY ', str(r.status_code))
    except requests.exceptions.ProxyError:
        r = requests.get('http://leghe.fantagazzetta.com/fantatilab/rose')
        print('NO PROXY ', str(r.status_code))

    if r.status_code == 200:
        html_doc = r.content
        soup = BeautifulSoup(html_doc, "html5lib")

        link_list = soup.find_all("li", class_="list-rosters-item")

        return_string = ''
        for link in link_list:
            # print(link.h4.text)  # nome fantasq
            return_string += link.h4.text + '<br>'
            # print('----------')
            tmplist = []
            for child in link.table.tbody.children:
                # tabella calciatori fantasq
                if child.span is not None:
                    # print(child.span.text)
                    tmplist.append(child.span.text)
            # print(tmplist.count('P'), tmplist.count('D'),
            #       tmplist.count('C'), tmplist.count('A'))
            return_string += str(tmplist.count('P')) + ' ' + str(tmplist.count(
                'D')) + ' ' + str(tmplist.count('C')) + ' ' + str(tmplist.count('A')) + '<br>'
            if (tmplist.count('P') > 4 or tmplist.count('D') > 10 or tmplist.count('C') > 10 or tmplist.count('A') > 8):
                players = link.table.tbody
                for player in players:
                    if player.span is not None:
                        # print(player.span.text, player.a.text)
                        return_string += player.span.text + ' ' + player.a.text + '<br>'
            # print('--------------')
            return_string += '--------------' + '<br>'
    else:
        return_string = 'Torno subito.'

    return return_string


if __name__ == '__main__':
    # ret_code = check_rose_print()
    # mystring = check_rose()
    mystring_html = check_rose_html()
    # print(mystring)
    print(mystring_html)
