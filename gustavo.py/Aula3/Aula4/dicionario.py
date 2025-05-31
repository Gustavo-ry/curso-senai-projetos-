
listaDeLivros = []

livro = {'ISBN'   :'12-12-50-10',
         'titulo' :'programação em python',
         'Autor'  :'Nilo Ney Coutinho Menezes',
         'Editora':'Novatec',
         'Paginas': 328,
         'Ano'    : 2019,
         'Genero' :'Tecnologia'
         }

listaDeLivros.append(livro)
livro = {'ISBN'   :'978-85-98078-50-2',
         'titulo' :'Aonde a gente vai papai',
         'Autor'  :'Jean-Louis Fournier',
         'Editora':'Intrinseca',
         'Paginas': 158,
         'Ano'    : 2009,
         'Genero' :'Drama'
         }
listaDeLivros.append(livro)

print(listaDeLivros[0]['titulo'])
print(listaDeLivros[1]['titulo'])


