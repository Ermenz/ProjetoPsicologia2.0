import flet as ft
from bancoDados import criar_banco, adicionar_usuario, validar_login

def main(page: ft.Page):
    criar_banco()
    
    # Define os contêineres
    left_container = ft.Container(
        bgcolor=ft.colors.BLUE,
        width=1000,
        height=1000,
        content=ft.Column(
            controls=[ft.Image(src="PSI2.png", width=900, height=800)],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    right_container = ft.Container(
        bgcolor=ft.colors.WHITE,
        width=1000,
        height=1000,
    )

    page.add(
        ft.Row(
            controls=[left_container, right_container],
            expand=True,
        )
    )

    ola = ft.Text(
        value="Login", 
        size=30,
        style=ft.TextStyle(
            font_family="Times New Roman",
            weight=ft.FontWeight.BOLD,
            color="blue"
        )
    )

    right_container.content = ft.Column(
        controls=[ola, botao_login(page)],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
    )

    page.update()  

def botao_login(page: ft.Page):
    entrada_nome = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.PERSON, size=20, color="blue"),
            ft.TextField(label="Nome", bgcolor="white", width=850)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    senha_icon = ft.Icon(name=ft.icons.LOCK, size=20, color="blue")
    entrada_senha = ft.Row(
        controls=[
            senha_icon,
            ft.TextField(label="Senha", password=True, bgcolor="white", width=850)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    botao_entrar = ft.ElevatedButton("Entrar", on_click=lambda e: validar_login_ui(page, entrada_nome, entrada_senha))
    botao_registrar = ft.ElevatedButton("Registrar", on_click=lambda e: mostrar_registro(page))

    return ft.Column(
        controls=[
            entrada_nome,
            entrada_senha,
            ft.Row(
                controls=[botao_entrar, botao_registrar],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

def mostrar_registro(page: ft.Page):
    page.clean()  # Limpa a página para mostrar o formulário de registro

    # Título
    ola = ft.Text(
        value="Tela de Registro", 
        size=30,
        style=ft.TextStyle(
            font_family="Times New Roman",
            weight=ft.FontWeight.BOLD,
            color="blue"
        )
    )

    # Centraliza cada campo de entrada na tela de registro
    entrada_nome = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.PERSON, size=20, color="blue"),
            ft.TextField(label="Nome de Usuário", bgcolor="white", width=300)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    
    entrada_senha = ft.Row(
        controls=[
            ft.Icon(name=ft.icons.LOCK, size=20, color="blue"),
            ft.TextField(label="Senha", password=True, bgcolor="white", width=300)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    botao_registrar = ft.ElevatedButton("Registrar", on_click=lambda e: registrar_usuario(page, entrada_nome, entrada_senha))

    # Contêiner branco que encapsula o formulário de registro
    container_formulario = ft.Container(
        content=ft.Column(
            controls=[ola, entrada_nome, entrada_senha, botao_registrar],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        bgcolor=ft.colors.WHITE,  # Cor de fundo branca para o contêiner do formulário
        border_radius=15,  # Bordas arredondadas
        width=400,  # Largura do contêiner do formulário
        height=400,  # Altura do contêiner do formulário
        alignment=ft.alignment.center
    )

    # Contêiner azul que ocupa a tela e centraliza o formulário
    page.add(
        ft.Container(
            content=container_formulario,
            alignment=ft.alignment.center,  # Centraliza o contêiner do formulário na tela
            expand=True,  # Faz o contêiner ocupar o espaço completo da tela
            bgcolor=ft.colors.BLUE  # Cor de fundo azul para o contêiner externo
        )
    )

    page.update()

def registrar_usuario(page: ft.Page, entrada_nome: ft.Row, entrada_senha: ft.Row):
    nome = entrada_nome.controls[1].value
    senha = entrada_senha.controls[1].value

    adicionar_usuario(nome, senha)
    page.add(ft.Text("Usuário registrado com sucesso!", color="green"))

    mostrar_login(page)  # Retorna ao formulário de login após registro

def mostrar_login(page: ft.Page):
    page.clean()  # Limpa a página para mostrar o formulário de login novamente

    ola = ft.Text(
        value="Login", 
        size=30,
        style=ft.TextStyle(
            font_family="Times New Roman",
            weight=ft.FontWeight.BOLD,
            color="black"
        )
    )

    right_container_content = botao_login(page)

    page.add(
        ft.Column(
            controls=[ola, right_container_content],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    page.update()

def validar_login_ui(page: ft.Page, entrada_nome: ft.Row, entrada_senha: ft.Row):
    nome = entrada_nome.controls[1].value
    senha = entrada_senha.controls[1].value

    if validar_login(nome, senha):
        page.add(ft.Text("Login bem-sucedido!", color="green"))
    else:
        page.add(ft.Text("Usuário ou senha incorretos.", color="red"))

    page.update()

def funcao_esqueci_senha():
    print("Função 'Esqueci Senha' chamada.")

ft.app(target=main)
