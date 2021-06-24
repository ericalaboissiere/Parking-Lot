<img src="Parking Lot.png" alt="Parking Lot">

**Resumo**

Esta é uma API desenvolvida em Python utilizando o framework Django para gerenciamento de estacionamentos, onde é possível cadastrar os níveis, preços e veículos. O sistema calcula automaticamente a quantidade de horas que os automóveis gastam no estacionamento e gera o valor total a ser pago.

**Iniciando o projeto**

Crie um ambiente virtual: python3 -m venv venv

Entre em seu ambiente: source venv/bin/activate cd ParkingLot

**Instalações**

pip install -r requirements.txt

**Criação do banco de dados**

python manage.py makemigrations
python manage.py migrate

**Rodando o servidor**

python manage.py runserver

**Rotas disponíveis na API**

- POST /api/accounts/ - Criação de usuários
- POST /api/login/ - Login
- POST /api/levels/ - Criação de níveis disponível aprnas para superusers
- GET /api/levels/ - Lista todos os andares e espaços disponíveis
- POST /api/pricings/ - Registra o valor final.
- POST /api/vehicles/ - Criação de veículo
- PUT /api/vehicles/int:vehicle_id/ registra o momento que o veículo deixa o estacionamento.``

**Exemplos de Requests**

- Criando um superusers: POST /api/accounts/
- > { "username": "admin", "password": "1234", "is_superuser": true, "is_staff": true }

- Login: POST /api/login/
- > { "username": "admin", "password": "1234" }

- Criando um estacionamento: POST /api/levels/
- Para acessar esta rota é necessário um token de superuser
- > { "name": "floor 1", "fill_priority": 5, "motorcycle_spaces": 30, "car_spaces": 40 }

- Criando preços: POST /api/pricings/
- Para acessar esta rota é necessário um token de superuser

- > { "a_coefficient": 1, "b_coefficient": 3 }

- Registrando veículo: POST /api/vehicles/
- Para acessar esta rota é necessário um token de superuser

- > { "vehicle_type": "car", "license_plate": "ITN1207" }

- Calculando o preço final: PUT /api/vehicles/int:vehicle_id/
- Para acessar esta rota é necessário um token de superuser
