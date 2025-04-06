import unittest
from main import Jogos

class TestJogos(unittest.TestCase):
    def setUp(self):
        # Configurar os dados de teste
        self.jogos = Jogos("teste.csv")
        self.jogos.jogos = [
            ["",1122334,"Pixel Racer Turbo","Aug 15, 2022 ","5000 - 100000",0,0,11.99,0,"A high-speed 2D racing game with customizable pixel cars, multiplayer mode, and drift challenges. Inspired by classic arcade racing.","['English','Japanese']","['English']","","https://cdn.akamai.steamstatic.com/steam/apps/1122334/header.jpg?t=1583449032","http://pixelracerturbo.com","http://pixelracerturbo.com/contact","help@pixelracerturbo.com",False,False,True,1200,"",50,7,1,"",600,400,"",300,100,70,"PixelGarage Studios","PixelGarage Studios","","Racing","Arcade","https://cdn.akamai.steamstatic.com/steam/apps/1122334/ss_1.jpg,https://cdn.akamai.steamstatic.com/steam/apps/1122334/ss_2.jpg",""],
            ["",1234567,"Super Adventure Quest","Jan 10, 2020 ","0 - 50000",0,0,4.99,0,"An exciting platformer where you explore magical lands, defeat bosses, and rescue the kingdom. A pixel-art indie gem with challenging levels and retro sound effects.","['English']","['English']","","https://cdn.akamai.steamstatic.com/steam/apps/1234567/header.jpg?t=1583449032","http://superquest.com","http://superquest.com/support","support@superquest.com",True,False,False,100,"",10,3,1,"",200,150,"",100,50,30,"IndieDev Co.","IndieDev Co.","","Adventure","Platformer","https://cdn.akamai.steamstatic.com/steam/apps/1234567/ss_1.jpg,https://cdn.akamai.steamstatic.com/steam/apps/1234567/ss_2.jpg",""],
            ["",7654321,"Galactic Trader 3000","Dec 1, 2020 ","1000 - 30000",0,0,0.00,0,"A strategy game where you manage interstellar trade routes, negotiate with alien factions, and become the richest merchant in the galaxy.","['English','Spanish']","['English']","","https://cdn.akamai.steamstatic.com/steam/apps/7654321/header.jpg?t=1583449032","http://galactictrader.com","http://galactictrader.com/help","contact@galactictrader.com",True,True,False,500,"",100,1,1,"",800,50,"",100,50,30,"Starbound Games","Starbound Games","","Strategy","Simulation","https://cdn.akamai.steamstatic.com/steam/apps/7654321/ss_1.jpg,https://cdn.akamai.steamstatic.com/steam/apps/7654321/ss_2.jpg",""]
]
        

    def test_ano_mais_lancamentos(self):
        resultado = self.jogos.calcular_ano_mais_lancamentos()
        self.assertEqual(resultado, "Ano com mais lançamentos: 2020")

    def test_percentual_gratuitos_pagos(self):
        resultado = self.jogos.calcular_gratuitos_pagos()
        self.assertEqual(resultado, "O percentual de jogos gratuitos é de 33.33% e o percentual de jogos pagos: 66.67%")
   
    def test_jogos_menos_dez_bem_avaliados(self):
        resultado = self.jogos.calcular_jogos_menos_dez_bem_avaliados()
        self.assertEqual(resultado, 1)

suite = unittest.TestLoader().loadTestsFromTestCase(TestJogos)
unittest.TextTestRunner().run(suite)
