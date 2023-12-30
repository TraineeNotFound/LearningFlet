from flet import *
import time as tm

def main(page: Page):
    page.vertical_alignment = MainAxisAlignment.START
    page.title = 'Seletor de Rotas' # título da aplicação
    page.route = '/'                # defino a raíz como a rota que desejo ir

    rotas = ['/', '1', '2']         # lista das rotas do sistema

    def PageRouteTratado():
        pageRoute = page.route
        pageRouteTratado = pageRoute.replace('/','')
        return(pageRouteTratado)

    def navegar(e, nova_rota):      # função para navegar até a próxima rota
        if nova_rota != page.route: # se a rota que eu quero ir é diferente da que estou
            page.route = nova_rota  # defino a nova rota 
            page.clean()            #limpo a página
            page.update()           # atualizo com a nova página

    class Botoes():                 # classe para criar dois botões: um em foco e outro sem foco
        def criar(self, nome, evento, foco: bool):     
            if foco:
                return ElevatedButton(nome, on_click=lambda e: evento(e, nome), color=colors.WHITE, bgcolor=colors.PRIMARY) # botão com foco
            else:
                return ElevatedButton(nome, on_click=lambda e: evento(e, nome), color=colors.PRIMARY, bgcolor=colors.WHITE) # botão sem foco
        def botoes_navegacao():
                for i in range(len(rotas)): # loop para criar os botões de navegação - esse será chamado toda vez que a página atualizar
                    if page.route == rotas[i]:
                        page.add(Botoes().criar(rotas[i], navegar, True)) # nome serve tanto para o a descrição do botão, quanto para definir a nova rota em "evento(e, nome)"
                    else:
                        page.add(Botoes().criar(rotas[i], navegar, False))          
        
    def new_route(route):           # função que define qual será os comandos executados no evento "page.on_route_change" chamado pelo "page.update"
        page.clean()
        page.update()
        
        if page.route == rotas[0]:
            # a partir daqui eu construo minha página
            page.add(Text('Esta é a raíz', size=30))
            Botoes.botoes_navegacao()

        elif page.route == rotas[1]:
            # a partir daqui eu construo minha página
            page.add(Text('Esta é a primeira página', size=30))
            Botoes.botoes_navegacao()

        elif page.route == rotas[2]:
            # a partir daqui eu construo minha página
            page.add(Text('Esta é a segunda página', size=30))
            Botoes.botoes_navegacao()

        else: # se estou tentando acessar uma rota fora da lista, a resposta deve ser ERROR_404
            page.add(Text('ERRO_404\npagina_nao_encontrada. Redirecionando para a raíz em 3... 2... 1...'))
            page.update()
            tm.sleep(3)
            page.clean()
            page.route = '/'
            page.update()

    new_route('/')
    page.on_route_change = new_route # executado toda vez que atualizar a página
    

app(target=main, view=WEB_BROWSER)
