from scrappy_site import email_usuario, pesquisar_item, coletando_dados, passar_pagina, criar_planilha, enviar_email_cliente
from email.message import EmailMessage
from unittest.mock import MagicMock
import openpyxl
import smtplib
import pytest

lista_loja_item = ["Loja A", "Loja B", "Loja C"]
lista_preco_item = [10, 20, 30]
lista_quantidade = [5, 10, 15]


@pytest.fixture
def mock_smtplib(mocker):
    return mocker.patch('scrappy.smtplib')


@pytest.fixture
def mock_EmailMessage(mocker):
    return mocker.patch('scrappy.EmailMessage')


def test_email_usuario_input_valido(monkeypatch, capsys):
    test_input = 'test@example.com'
    monkeypatch.setattr('builtins.input', lambda _: test_input)

    email = email_usuario()

    captured = capsys.readouterr()
    assert 'Email válido' in captured.out
    assert email == test_input


def test_email_usuario_input_invalido(monkeypatch, capsys):
    test_input = 'email_invalido'
    monkeypatch.setattr('builtins.input', lambda _: test_input)

    email = email_usuario()

    captured = capsys.readouterr()
    assert 'Digite um email válido!!!' in captured.out
    assert email is None


def test_pesquisar_item():
    # Mock do webdriver
    webdriver_mock = MagicMock()
    webdriver_mock.title = "Título da Página"

    # Mock dos elementos e métodos
    wait_mock = MagicMock()
    wait_mock.until.return_value = MagicMock()
    webdriver_mock.find_element_by_xpath.return_value = wait_mock

    # Chamada da função pesquisar_item com o webdriver mock


def test_coletando_dados():
    # Mock dos valores de exemplo para simular os retornos esperados
    localizacao_item_mock = MagicMock()
    localizacao_item_mock.text = "Localização do Item"

    preco_item_mock = MagicMock()
    preco_item_mock.text = "Preço do Item"

    quantidade_mock = MagicMock()
    quantidade_mock.text = "Quantidade do Item"

    # Mock do WebDriver e seus métodos
    driver_mock = MagicMock()
    driver_mock.current_url = "https://exemplo.com"
    driver_mock.find_element_by_xpath.side_effect = [localizacao_item_mock, preco_item_mock, quantidade_mock]

    # Chame a função coletando_dados com o WebDriver mock
    resultado = coletando_dados(driver_mock)


def test_passar_pagina():
    # Mock dos valores de exemplo para simular os retornos esperados
    localizacao_item_mock = MagicMock()
    localizacao_item_mock.text = "Localização do Item"

    preco_item_mock = MagicMock()
    preco_item_mock.text = "Preço do Item"

    quantidade_mock = MagicMock()
    quantidade_mock.text = "Quantidade do Item"

    # Mock do WebDriver e seus métodos
    driver_mock = MagicMock()
    driver_mock.current_url = "https://exemplo.com"
    driver_mock.find_element_by_xpath.side_effect = [localizacao_item_mock, preco_item_mock, quantidade_mock]

    # Chame a função passar_pagina com o WebDriver mock
    resultado = passar_pagina(driver_mock)



def test_criar_planilha(tmp_path):
    # Setup - Criando listas de exemplo
    lista_preco_item = [10]
    lista_loja_item = ['Loja A']
    lista_quantidade = [5]
    nome_item = 'Fogo Rápido'

    # Caminho do arquivo temporário
    file_path = tmp_path / "planilha_Ragnarok.xlsx"

    # Chama a função a ser testada
    criar_planilha(
        lista_preco_item=lista_preco_item,
        lista_loja_item=lista_loja_item,
        lista_quantidade=lista_quantidade,
        nome_item=nome_item 
    )


    wb = openpyxl.load_workbook('planilha_Ragnarok.xlsx')
    sheet = wb['Preço e localização de itens']
    assert sheet['A1'].value == 'Fogo Rápido'
    assert sheet['B1'].value == 'Preço'
    assert sheet['C1'].value == 'Localização'
    assert sheet['D1'].value == 'Quantidade'


@pytest.fixture
def mock_smtp(monkeypatch):
    class MockSMTP:
        def __init__(self, *args, **kwargs):
            pass

        def login(self, *args, **kwargs):
            pass

        def send_message(self, *args, **kwargs):
            pass

        def quit(self):
            pass

        def ehlo(self):
            pass

        def starttls(self):
            pass
    # Substitui a função smtplib.SMTP por MockSMTP
    monkeypatch.setattr(smtplib, 'SMTP', MockSMTP)


def test_enviar_email_cliente(mocker):
    # Mock do smtplib.SMTP
    mock_smtp = mocker.patch('smtplib.SMTP')

    email_teste = 'exemplo@teste.com'
    enviar_email_cliente(email_teste)

    # Verifica se smtplib.SMTP foi chamado
    mock_smtp.assert_called_once()