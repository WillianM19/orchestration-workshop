# Oficina - Orquestração de serviços

Este repositório contém a atividade da oficina desenvolvida durante a matéria de Desenvolvimento de Sistemas Distribuídos - IFRN. 
O projeto demonstra uma implementação básica de uma orquestração de serviços com Django. 

Os microsserviços incluídos neste projeto são:

- inventory-service: Gerencia o inventário de produtos.
- order-service: Responsável pelo gerenciamento de pedidos.
- payment-service: Lida com o processamento de pagamentos.
- orchestrator: Coordena as interações entre os outros microsserviços.

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- Python 3.8 ou superior
- Virtualenv
- Git

## Passos para Configuração e Execução

1. Clone o Repositório

   Clone este repositório para sua máquina local:
    
   ```bash
   git clone https://github.com/WillianM19/orchestration-workshop
   cd orchestration-workshop
   ```

2. Configuração de Ambiente Virtual

   Crie um ambiente virtual:
  
   ```bash
   py -m venv venv
   source venv/bin/activate
   ```

3. Instalação das depêndencias:

   Instale as depêndencias de cada microserviço:
  
   ```bash
   pip install -r microservico/requirements.txt
   ```

5. Configuração do Banco de Dados:

   Execute as migrações para configurar o banco de dados em cada serviço:
  
   ```bash
   python microservico/manage.py migrate
   ```

6. Execute todos os serviços:

   ```bash
   python microservico/manage.py runserver
   ```

### Testando o projeto

Para testar o projeto faça uma requisição POST para a rota:

```http://localhost:8000/api/purchase/```

Exemplo de conteúdo:

```json
{
  "product_id": 1,
  "quantity": 1
}
```

