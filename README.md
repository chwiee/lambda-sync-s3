# Lambda Sync S3

## O que e

Essa Lambda irá copiar o arquivo sempre que o mesmo for criado no bucket, essa movimentacao pode ser na mesma conta (outr bucket) ou entre constas diferentes

## Como usar

1. Crie a lambda com o código que está escrito no main.py

2. Configure a Trigger da lambda para o seu bucket

3. Faça um teste, a lambda irá 'printar' o nome do arquivo que está sendo movido

