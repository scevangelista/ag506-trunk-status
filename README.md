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
$ docker compose start
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
  'user': 'myuser',
  'password': 'mypass'
}
```
##### Exemplo de retorno:
```
{}
```
