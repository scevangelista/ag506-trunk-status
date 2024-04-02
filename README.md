# AG506 - Trunk Status - API
API para consulta das informações dos troncos E1 do Gateway AG506 via HTTP, possibilitando o monitoramento do equipamento.  
A resposta será em formato json para compatibilidade com o Zabbix e outros sistemas de monitoramento.

##
### Executando :electric_plug:  

**Requerimentos**
- Docker
</br>

**Instruções para executar:**
- Clone o repositório para um diretório de sua preferência:
```
$ git clone https://github.com/scevangelista/ag506-trunk-status.git
```
  
- Execute o docker compose build para gerar a imagem e baixar as dependências
```
$ cd ag506-trunk-status
$ docker compose build
```
  
- Execute o docker compose start para iniciar o container
```
$ docker compose up -d
```
  
- Acesse a API pela porta 7000  
http://ip_of_docker_server:7000

</br>  

##
### Exemplo de Requisição 📚
Coleta os dados no equipamento via requisição http e transforma em json para retorno.
##### URL: 
`/collect`
##### Method: 
  `POST`
##### Body:  
```
{
  'url': 'http://ag506_ip_address',
  'user': 'ag506_user',
  'password': 'ag506_password'
}
```
##### Exemplo de retorno:
```
{
  "status": true,
  "E1_Interface_1": {
    "name": "E1_Interface_1",
    "alarm": "OK",
    "status": true,
    "packets_received": "123456",
    "packets_received_total": "100.00%",
    "packets_lost": "0",
    "packets_lost_total": "0.00%",
    "sequences_lost": "1",
    "sequences_lost_total": "",
    "code_violations": "1",
    "code_violations_total": "",
    "slips": "1",
    "slips_total": "",
    "crc_errors": "0",
    "crc_errors_total": "",
    "los": "1",
    "los_total": "00:00:01",
    "ais": "0",
    "ais_total": "00:00:00",
    "bfa_error": "0",
    "bfa_error_total": "00:00:00",
    "mfa_error": "0",
    "mfa_error_total": "00:00:00",
    "rai": "954",
    "rai_total": "00:00:00",
    "total": "",
    "total_total": "600:00:00"
  },
  "E1_Interface_2": {
    "name": "E1_Interface_2",
    "alarm": "OK",
    "status": true,
    "packets_received": "123456",
    "packets_received_total": "100.00%",
    "packets_lost": "0",
    "packets_lost_total": "0.00%",
    "sequences_lost": "0",
    "sequences_lost_total": "",
    "code_violations": "0",
    "code_violations_total": "",
    "slips": "1",
    "slips_total": "",
    "crc_errors": "0",
    "crc_errors_total": "",
    "los": "0",
    "los_total": "00:00:00",
    "ais": "1",
    "ais_total": "00:00:01",
    "bfa_error": "0",
    "bfa_error_total": "00:00:00",
    "mfa_error": "0",
    "mfa_error_total": "00:00:00",
    "rai": "3",
    "rai_total": "00:00:00",
    "total": "",
    "total_total": "600:00:00"
  }
}
```
