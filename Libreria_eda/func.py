def get_root_path(n):
    """Función para saber el directorio"""
    path = os.getcwd()
    for i in range(n):
        print(path)
        path = os.path.dirname(path)
        print("-------")
    print(path)
    sys.path.append(path)

get_root_path(n=5)


def remove_dollar(x):# Utilizariamos el .apply para llamar a la función, ej: Chipo["item_price"].apply(remove_dollar)
	return float(x[1:-1])


    # To show beautiful html. Lo usamos para web scraping
def show_html(html_str):
    print(BeautifulSoup(str(html_str), 'html.parser').prettify())

    show_html(soup) #así la llamamos


def get_page_contents(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"}) # Cabia la forma de ver la web. es decir si tenemos una cabecera u otra vemos la web de una forma u otra. ie, en movil la cabecera es diferente al pc, por eso vemos las webs en movil dif que en pc.
    return BeautifulSoup(page.text, "html.parser")
soup = get_page_contents(url)
show_html(soup.text)