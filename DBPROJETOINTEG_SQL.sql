-- APAGANDO BANCO DE DADOS CASO EXISTA
DROP DATABASE IF EXISTS PROJETO_INTEGRADOR_MODULO1; 

-- CRIANDO O BANCO DE DADOS
CREATE DATABASE PROJETO_INTEGRADOR_MODULO1;

-- CONECTANDO AO BANCO DE DADOS
USE PROJETO_INTEGRADOR_MODULO1;

-- CRIANDO AS TABELAS
CREATE TABLE IMIGRANTE(
	IDIMIGRANTE INT AUTO_INCREMENT NOT NULL
    , PRIMEIRO_NOME VARCHAR(60) NOT NULL
    , SOBRENOME VARCHAR(180) NOT NULL
    , NACIONALIDADE VARCHAR(120) NOT NULL
    , IDIOMA VARCHAR(120) NOT NULL
    , DATA_NASCIMENTO DATE NOT NULL
    , DOCUMENTO_IDENTIFICACAO VARCHAR(45)
    , CONTATO VARCHAR(120)
    , PRIMARY KEY(IDIMIGRANTE)
    
);


CREATE TABLE APOIO (
	IDAPOIO INT AUTO_INCREMENT
	, TIPO_SERVICO VARCHAR(120) NOT NULL
	, DESCRICAO VARCHAR(200) NOT NULL
    , NOME_INSTITUICAO VARCHAR(120) NOT NULL
    , ENDERECO_RUA VARCHAR(120)
    , ENDERECO_NUMERO VARCHAR(10)
    , ENDERECO_COMPLEMENTO VARCHAR(45)
    , ENDERECO_CIDADE VARCHAR(120) NOT NULL
    , ENDERECO_ESTADO VARCHAR(45) NOT NULL
    , TELEFONE VARCHAR(45)
    , PRIMARY KEY(IDAPOIO)
);

CREATE TABLE COMPLEMENTO (
	IDCOMPLEMENTO INT auto_increment
    , TIPO_COMPLEMENTO VARCHAR(120)
    , DESCRICAO VARCHAR(200)
    , ANO_INICIO INT
    , ANO_TERMINO INT
    , IDIMIGRANTE INT 
    , PRIMARY KEY(IDCOMPLEMENTO)
    , FOREIGN KEY(IDIMIGRANTE) REFERENCES IMIGRANTE(IDIMIGRANTE)
);

INSERT INTO IMIGRANTE(PRIMEIRO_NOME, SOBRENOME, NACIONALIDADE, IDIOMA, DATA_NASCIMENTO, DOCUMENTO_IDENTIFICACAO, CONTATO)
values ('Helen', 'DOS SANTOS JORGE FERREIRA', 'BRASILEIRA BR', 'Português', '1995-07-03', '2124545454', 'helen@hotmail.com')
, ('Luca', 'Bianchi', 'ITALIANA IT', 'Italiano e Inglês', '1985-07-22', 'IT123456789', 'luca.bianchi@outlook.it')
,('Mei', 'Zhang', 'CHINESA CN', 'Mandarim e Inglês', '1992-11-05', 'CN9988776655', 'mei.zhang@wechat.cn')
,('Carlos', 'Ramírez', 'MEXICANO MX', 'Espanhol', '1978-06-30', 'MX1122334455', 'carlos.ramirez@hotmail.com')
,('Fatou', 'Diop', 'SENEGALÊS SN', 'Francês e Wolof', '1995-01-18', 'SN5566778899', 'fatou.diop@africa.net')
,('Olga', 'Petrovna', 'RUSSA RU', 'Russo e Inglês', '1983-09-12', 'RU4455667788', 'olga.petrovna@mail.ru')
,('João', 'da Silva', 'BRASILEIRO BR', 'Português', '2000-05-25', 'BR12345678900', 'joao.silva@gmail.com')
,('Leila', 'Haddad', 'LIBANESA LB', 'Árabe, Francês', '1998-12-03', 'LB7788990011', 'leila.haddad@libano.org'),
('Noah', 'Smith', 'AMERICANO US', 'Inglês', '1993-04-17', 'US9988776655', 'noah.smith@usa.com')
,('Ayumi', 'Tanaka', 'JAPONESA JP', 'Japonês e Inglês', '1989-08-09', 'JP6677889900', 'ayumi.tanaka@japan.jp')
, ('ANA MARCELLA', 'GONZALEZ', 'VENEZUELANA VEN', 'Espanhol', '1978-07-01', '776677696', '24-22442244')
, ('ANA LAIZ', 'RODRIGUEZ', 'URUGUAI', 'Espanhol', '1978-11-21', '95644221', '61-55555555')
;

INSERT INTO COMPLEMENTO(IDIMIGRANTE, TIPO_COMPLEMENTO, DESCRICAO, ANO_INICIO, ANO_TERMINO)
values ('1', 'Curso', 'Cabeleireira', '2020', '2021')
, ('2', 'Curso', 'Vigilante', '2015', '2016')
, ('3', 'Enfermeiro', 'Hospital KR Cheng', '2009', '2013')
, ('4', 'Barista', 'Serena Bar', '2010', '2015')
, ('5', 'Curso Tecnico', 'Segurança Patrimonial', '2021', '2023')
, ('6', 'Curso', 'Informatica', '2006', '2007')
, ('7', 'Curso', 'Confeitaria', '2024', '2025')
, ('8', 'Curso', 'Manicure', '2019', '2020')
, ('9', 'Curso', 'Mecânica automotiva', '2015', '2016')
, ('10', 'Atendente', 'Yann MK', '2022', '2023')
, ('1', 'Garçonete', 'Quiosque', '2016', '2018')
, ('5', 'Eletricista', 'Ieah Yinn', '2019', '2023')
, ('9', 'Curso', 'Soldador', '2020', '2021');

INSERT INTO APOIO(TIPO_SERVICO, DESCRICAO, NOME_INSTITUICAO, ENDERECO_RUA, ENDERECO_NUMERO, ENDERECO_COMPLEMENTO, ENDERECO_CIDADE, ENDERECO_ESTADO)
values ('Emissão de documentos pessoais', 'RG, CPF, CARTEIRA DE TRABALHO', 'SECRETARIA DE SEGURANÇA PUBLICA SSP', 'RUA DOS ALMEIDAS', '1044', '', 'Florianópolis', 'SC')
, ('Vacinação', 'Vacinas para todas as idades', 'Secretaria de Saúde do Estado de Santa Catarina', 'Rua Severino Madeira', '24', '', 'São José', 'SC')
, ('Idiomas', 'Cursos de idiomas como português para estrangeiros', 'Instituto Federal de Educação', 'Av Mauro Ramos', 's/n', 'Centro', 'Florianópolis', 'SC')
, ('Recolocação Profissional', 'Orientação e encaminhamento para o primeiro emprego no país', 'ONG BR', 'Rua Sete de setembro', '1020', 'centro', 'Curitiba', 'PR') 
, ('Programas Sociais', 'Assistência Social, auxilio aos principais programas governamentais', 'Assistência Social', 'Rua das Palmeiras', '29', 'casa', 'Rio de Janeiro', 'RJ')
, ('Libras', 'Aulas de Libras', 'APAE', 'Rua Alfredo Wagner', '655', '', 'Biguaçu', 'SC');

SELECT * from APOIO;