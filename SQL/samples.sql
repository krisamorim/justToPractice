create database kris;
use kris;
CREATE TABLE `kris`.`costumers` (
  `idcostumers` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `lastName` VARCHAR(80) NULL,
  `completeName` VARCHAR(160) NULL,
  `gender` CHAR(2) NULL,
  `yearBirth` INT NULL,
  `payment` INT NULL,
  PRIMARY KEY (`idcostumers`));
  
  --list tables
  show tables;
  
  --list table structure
  desc costumers;

  --add data
  INSERT INTO costumers (name, lastName, completeName, gender, yearBirth, payment) VALUES ("Alice","Smith","Alice Smith","F",2005, 19123),("Sophia","Johnson","Sophia Johnson","F",1981, 11943),("Helena","Williams","Helena Williams","M",1970, 2385),("Valentina","Jones","Valentina Jones","M",1964, 28898),("Laura","Brown","Laura Brown","M",1999, 3293),("Isabella","Davis","Isabella Davis","F",1932, 15585),("Manuela","Miller","Manuela Miller","M",1956, 26415),("Júlia","Wilson","Júlia Wilson","M",1947, 3704),("Heloísa","Moore","Heloísa Moore","F",1995, 33629),("Luiza","Taylor","Luiza Taylor","F",1984, 15808),("Maria Luiza","Anderson","Maria Luiza Anderson","F",1944, 13805),("Lorena","Thomas","Lorena Thomas","F",1943, 8970),("Lívia","Jackson","Lívia Jackson","F",1993, 9250),("Giovanna","White","Giovanna White","F",1986, 22730),("Maria Eduarda","Harris","Maria Eduarda Harris","F",2005, 25991),("Beatriz","Martin","Beatriz Martin","M",1990, 1792),("Maria Clara","Thompson","Maria Clara Thompson","M",1989, 24545),("Cecília","Garcia","Cecília Garcia","F",2020, 29819),("Eloá","Martinez","Eloá Martinez","M",1992, 7080),("Lara","Robinson","Lara Robinson","M",1938, 28329),("Maria Júlia","Clark","Maria Júlia Clark","M",1935, 23256),("Isadora","Rodriguez","Isadora Rodriguez","F",1980, 7710),("Mariana","Lewis","Mariana Lewis","M",1972, 9404),("Emanuelly","Lee","Emanuelly Lee","M",2006, 24297),("Ana Júlia","Walker","Ana Júlia Walker","M",1999, 16483),("Ana Luiza","Hall","Ana Luiza Hall","F",2018, 30854),("Ana Clara","Allen","Ana Clara Allen","F",1985, 3998),("Melissa","Young","Melissa Young","M",1992, 7355),("Yasmin","Hernandez","Yasmin Hernandez","M",2014, 9669),("Maria Alice","King","Maria Alice King","F",1992, 30172),("Isabelly","Wright","Isabelly Wright","F",1974, 17044),("Lavínia","Lopez","Lavínia Lopez","M",2018, 9599),("Esther","Hill","Esther Hill","F",1986, 21867),("Sarah","Scott","Sarah Scott","M",1937, 13943),("Elisa","Green","Elisa Green","M",1948, 1679),("Antonella","Adams","Antonella Adams","M",2014, 2780),("Rafaela","Baker","Rafaela Baker","M",1995, 14413),("Maria Cecília","Gonzalez","Maria Cecília Gonzalez","M",2001, 4153),("Liz","Nelson","Liz Nelson","M",1936, 6273),("Marina","Carter","Marina Carter","F",2019, 7533),("Nicole","Mitchell","Nicole Mitchell","F",1977, 33520),("Maitê","Perez","Maitê Perez","M",1934, 28344),("Isis","Roberts","Isis Roberts","M",1981, 23798),("Alícia","Turner","Alícia Turner","F",1947, 33917),("Luna","Phillips","Luna Phillips","F",1930, 34881),("Rebeca","Campbell","Rebeca Campbell","M",1970, 1901),("Agatha","Parker","Agatha Parker","M",1930, 22236),("Letícia","Evans","Letícia Evans","F",1962, 9443),("Maria-","Edwards","Maria- Edwards","M",2010, 32878),("Gabriela","Collins","Gabriela Collins","F",1960, 29313),("Ana Laura","Stewart","Ana Laura Stewart","F",1934, 30731),("Catarina","Sanchez","Catarina Sanchez","F",2020, 11861),("Clara","Morris","Clara Morris","M",1932, 19690),("Ana Beatriz","Rogers","Ana Beatriz Rogers","M",1989, 16199),("Vitória","Reed","Vitória Reed","M",2011, 30826),("Olívia","Cook","Olívia Cook","F",1958, 26991),("Maria Fernanda","Morgan","Maria Fernanda Morgan","F",1953, 27071),("Emilly","Bell","Emilly Bell","F",1994, 8579),("Maria Valentina","Murphy","Maria Valentina Murphy","F",1959, 18752),("Milena","Bailey","Milena Bailey","M",1977, 9033),("Maria Helena","Rivera","Maria Helena Rivera","F",1994, 16422),("Bianca","Cooper","Bianca Cooper","M",1942, 3306),("Larissa","Richardson","Larissa Richardson","F",1989, 25055),("Mirella","Cox","Mirella Cox","M",2016, 18989),("Maria Flor","Howard","Maria Flor Howard","M",2010, 15698),("Allana","Ward","Allana Ward","M",2004, 32733),("Ana Sophia","Torres","Ana Sophia Torres","F",2006, 10982),("Clarice","Peterson","Clarice Peterson","M",1975, 1751),("Pietra","Gray","Pietra Gray","M",1951, 29657),("Maria Vitória","Ramirez","Maria Vitória Ramirez","M",1955, 13399),("Maya","James","Maya James","M",2003, 24190),("Laís","Watson","Laís Watson","M",1930, 26613),("Ayla","Brooks","Ayla Brooks","M",1954, 17115),("Ana Lívia","Kelly","Ana Lívia Kelly","M",2020, 12188),("Eduarda","Sanders","Eduarda Sanders","M",1946, 3242),("Mariah","Price","Mariah Price","F",1999, 31513),("Stella","Bennett","Stella Bennett","M",1970, 11931),("Ana","Wood","Ana Wood","F",1936, 6275),("Gabrielly","Barnes","Gabrielly Barnes","F",2011, 17629),("Sophie","Ross","Sophie Ross","F",1998, 29862),("Carolina","Henderson","Carolina Henderson","F",1990, 6872),("Maria Laura","Coleman","Maria Laura Coleman","F",1967, 13500),("Maria Heloísa","Jenkins","Maria Heloísa Jenkins","M",1967, 21130),("Maria Sophia","Perry","Maria Sophia Perry","M",2007, 23954),("Fernanda","Powell","Fernanda Powell","M",1996, 2680),("Malu","Long","Malu Long","F",1980, 30113),("Analu","Patterson","Analu Patterson","F",1972, 23051),("Amanda","Hughes","Amanda Hughes","F",2012, 10985),("Aurora","Flores","Aurora Flores","M",1949, 25008),("Maria Isis","Washington","Maria Isis Washington","F",1998, 2220),("Louise","Butler","Louise Butler","F",1973, 15241),("Heloise","Simmons","Heloise Simmons","F",2019, 21379),("Ana Vitória","Foster","Ana Vitória Foster","M",1931, 24676),("Ana Cecília","Gonzales","Ana Cecília Gonzales","M",1983, 14727),("Ana Liz","Bryant","Ana Liz Bryant","F",1945, 4465),("Joana","Alexander","Joana Alexander","F",1998, 18983),("Luana","Russell","Luana Russell","M",1956, 26648),("Antônia","Griffin","Antônia Griffin","F",2017, 31599),("Isabel","Diaz","Isabel Diaz","M",1996, 2347),("Bruna","Hayes English","Bruna Hayes English","M",1978, 22623),("Miguel","Cahill","Miguel Cahill","F",1997, 3057),("Arthur","Caldwell","Arthur Caldwell","M",1967, 7044),("Bernardo","Calhoun","Bernardo Calhoun","M",1966, 30463),("Heitor","Callahan","Heitor Callahan","M",1972, 6377),("Davi","Cameron","Davi Cameron","M",2007, 14440),("Lorenzo","Campbell","Lorenzo Campbell","F",1964, 25462),("Théo","Cannon","Théo Cannon","F",2013, 12023),("Pedro","Cantrell","Pedro Cantrell","F",2011, 34548),("Gabriel","Cantu","Gabriel Cantu","M",1997, 17130),("Enzo","Cardenas","Enzo Cardenas","F",1988, 13333),("Matheus","Carey","Matheus Carey","M",1951, 9265),("Lucas","Carlson","Lucas Carlson","M",1993, 28007),("Benjamin","Carney","Benjamin Carney","M",2020, 22433),("Nicolas","Carpenter","Nicolas Carpenter","M",1989, 18132),("Guilherme","Carr","Guilherme Carr","F",2021, 17192),("Rafael","Carroll","Rafael Carroll","M",2009, 5930),("Joaquim","Carson","Joaquim Carson","M",2021, 27437),("Samuel","Carter","Samuel Carter","M",1990, 22014),("Enzo Gabriel","Carver","Enzo Gabriel Carver","F",2016, 18299),("João Miguel","Casey","João Miguel Casey","M",1976, 26285),("Henrique","Cassidy","Henrique Cassidy","F",2006, 9707),("Gustavo","Castillo","Gustavo Castillo","F",1948, 16199),("Murilo","Castro","Murilo Castro","F",1953, 21049),("Pedro Henrique","Chandler","Pedro Henrique Chandler","M",1970, 8909),("Pietro","Chaney","Pietro Chaney","F",1956, 1068),("Lucca","Chapman","Lucca Chapman","F",1944, 29402),("Felipe","Chase","Felipe Chase","F",2003, 34512),("João Pedro","Chavez","João Pedro Chavez","M",2005, 11723),("Isaac","Childers","Isaac Childers","F",1932, 18619),("Benício","Choate","Benício Choate","M",1978, 8195),("Daniel","Christian","Daniel Christian","M",1993, 17733),("Anthony","Christie","Anthony Christie","F",1999, 29683),("Leonardo","Church","Leonardo Church","M",2020, 22841),("Davi Lucca","Churchill","Davi Lucca Churchill","M",1970, 29656),("Bryan","Clancy","Bryan Clancy","M",2002, 19053),("Eduardo","Clark","Eduardo Clark","M",2020, 13949),("João Lucas","Clark","João Lucas Clark","F",1961, 3637),("Victor","Clarke","Victor Clarke","M",1979, 21918),("João","Clay","João Clay","F",1973, 10288),("Cauã","Clayton","Cauã Clayton","M",1974, 5467),("Antônio","Cleveland","Antônio Cleveland","M",2005, 8143),("Vicente","Clifford","Vicente Clifford","M",1932, 1247),("Caleb","Cobb","Caleb Cobb","F",1963, 33231),("Gael","Cochran","Gael Cochran","M",1987, 17277),("Bento","Cochrane","Bento Cochrane","F",1941, 25290),("Caio","Coffey","Caio Coffey","M",1961, 25830),("Emanuel","Cole","Emanuel Cole","M",1933, 22776),("Vinícius","Coleman","Vinícius Coleman","F",1966, 21687),("João Guilherme","Coleman","João Guilherme Coleman","M",1994, 17280),("Davi Lucas","Collier","Davi Lucas Collier","M",2018, 3674),("Noah","Collins","Noah Collins","M",1939, 18415),("João Gabriel","Collins","João Gabriel Collins","M",1987, 14846),("João Victor","Combs","João Victor Combs","M",1994, 2833),("Luiz Miguel","Compton","Luiz Miguel Compton","M",2001, 22782),("Francisco","Conley","Francisco Conley","M",1931, 8623),("Kaique","Connell","Kaique Connell","M",2007, 7696),("Otávio","Connolly","Otávio Connolly","F",1977, 24572),("Augusto","Conrad","Augusto Conrad","M",2018, 32345),("Levi","Conway","Levi Conway","F",1987, 28471),("Yuri","Cook","Yuri Cook","F",1984, 15903),("Enrico","Cooke","Enrico Cooke","M",1933, 19851),("Thiago","Cooley","Thiago Cooley","F",1966, 8950),("Ian","Cooney","Ian Cooney","F",1987, 17979),("Victor Hugo","Cooper","Victor Hugo Cooper","M",2012, 8092),("Thomas","Copeland","Thomas Copeland","M",1998, 29549),("Henry","Corbett","Henry Corbett","M",1998, 21458),("Luiz Felipe","Corcoran","Luiz Felipe Corcoran","M",1984, 13873),("Ryan","Cormier","Ryan Cormier","M",1972, 9013),("Arthur Miguel","Costello","Arthur Miguel Costello","F",1983, 26261),("Davi Luiz","Coughlin","Davi Luiz Coughlin","F",1996, 1416),("Nathan","Cowan","Nathan Cowan","M",1974, 24706),("Pedro Lucas","Cox","Pedro Lucas Cox","F",1957, 21439),("Davi Miguel","Cox","Davi Miguel Cox","M",2010, 15950),("Raul","Coyle","Raul Coyle","F",1936, 12169),("Pedro Miguel","Coyne","Pedro Miguel Coyne","F",1966, 16689),("Luiz Henrique","Crabtree","Luiz Henrique Crabtree","M",2000, 4441),("Luan","Craig","Luan Craig","M",1976, 4445),("Erick","Crawford","Erick Crawford","F",1952, 31007),("Martin","Crockett","Martin Crockett","F",2009, 10110),("Bruno","Cross","Bruno Cross","M",2012, 8203),("Rodrigo","Crouch","Rodrigo Crouch","M",2000, 21991),("Luiz Gustavo","Crowley","Luiz Gustavo Crowley","F",1935, 10198),("Arthur Gabriel","Cruz","Arthur Gabriel Cruz","M",2014, 20765),("Breno","Cullen","Breno Cullen","M",1953, 5003),("Kauê","Cunningham","Kauê Cunningham","F",1968, 3982),("Enzo Miguel","Curran","Enzo Miguel Curran","F",1952, 27056),("Fernando","Curtis","Fernando Curtis","F",1975, 24941),("Arthur Henrique","Silva","Arthur Henrique Silva","M",1998, 1916),("Luiz Otávio","Amorim","Luiz Otávio Amorim","F",1979, 12518),("Carlos Eduardo","Furtado","Carlos Eduardo Furtado","F",1985, 15005),("Tomás","Costa","Tomás Costa","M",1976, 2056),("Lucas Gabriel","Soares","Lucas Gabriel Soares","M",1981, 26420),("André","Ferreira","André Ferreira","M",1982, 7963),("José","Coelho","José Coelho","F",1939, 17511),("Yago","Alves","Yago Alves","F",1986, 22231),("Danilo","Conceição","Danilo Conceição","F",1977, 18260),("Anthony Gabriel","Faro","Anthony Gabriel Faro","M",2010, 11546),("Ruan","Santana","Ruan Santana","F",2017, 16356),("Miguel Henrique","Akemi","Miguel Henrique Akemi","F",1954, 6096),("Oliver","Nakata","Oliver Nakata","F",1976, 7394),("Alice","Kamada","Alice Kamada","F",1939, 11454),("Sophia","Santos","Sophia Santos","F",1945, 33132),("Helena","Pires","Helena Pires","M",1944, 11366),("Valentina","Espindola","Valentina Espindola","F",1976, 8759),("Laura","Oliveira","Laura Oliveira","M",1961, 5923),("Isabella","Souza","Isabella Souza","F",1975, 1430),("Manuela","Rodrigues","Manuela Rodrigues","M",2007, 10954),("Júlia","Lopes","Júlia Lopes","F",1968, 24283),("Heloísa","Pereira","Heloísa Pereira","M",1931, 10859),("Luiza","Cabral","Luiza Cabral","F",1998, 18811),("Maria Luiza","Gomes","Maria Luiza Gomes","F",2021, 28709),("Lorena","Lima","Lorena Lima","M",2000, 4097),("Lívia","Ribeiro","Lívia Ribeiro","F",1955, 6936),("Giovanna","Martins","Giovanna Martins","M",1938, 26066),("Maria Eduarda","Carvallho","Maria Eduarda Carvallho","F",1945, 7075),("Beatriz","Almeida","Beatriz Almeida","F",1955, 24925),("Maria Clara","Fernandes","Maria Clara Fernandes","M",1947, 23309),("Cecília","Vieira","Cecília Vieira","M",1952, 22115),("Eloá","Barbosa","Eloá Barbosa","F",1943, 13106),("Lara","Rocha ","Lara Rocha ","F",1958, 11864),("Maria Júlia","Dias","Maria Júlia Dias","M",2003, 21775),("Isadora","Nascimento","Isadora Nascimento","M",1972, 29634),("Mariana","Andrade","Mariana Andrade","F",2001, 28751),("Emanuelly","Moreira","Emanuelly Moreira","M",1970, 28456),("Ana Júlia","Nunes","Ana Júlia Nunes","F",1954, 21992),("Ana Luiza","Marques","Ana Luiza Marques","M",1963, 15207),("Ana Clara","Machado","Ana Clara Machado","M",1961, 4601);
  
  SELECT * FROM costumers;
  SELECT gender FROM costumers;
  SELECT DISTINCT gender FROM costumers;
  SELECT * FROM costumers WHERE gender = 'F' and (name = 'Ana' or name = 'Ana Clara');
  --All except ANA
  SELECT name FROM costumers WHERE name <> 'Ana';
  SELECT name, payment FROM costumers WHERE payment > 15000;
  SELECT name, payment FROM costumers WHERE payment > 23000 AND payment < 25000;
  SELECT idcostumers, name, completeName FROM costumers;

  CREATE TABLE `kris`.`contact` (
  `idcontact` INT NOT NULL AUTO_INCREMENT,
  `idcostumers` INT NULL,
  `email` VARCHAR(85) NULL,
  `phone` INT NULL,
  PRIMARY KEY (`idcontact`),
  CONSTRAINT `fk_costumers_contact` FOREIGN KEY (`idcostumers`) REFERENCES `kris`.`costumers` (`idcostumers`));
     
  show tables;
  desc contact;
  select * from contact;

-- add data in to contact table
INSERT INTO contact (idcostumers, email, phone) VALUES (1,"alice.smith@hotmail.com",191232005), (2,"sophia.johnson@hotmail.com",119431981), (3,"helena.williams@hotmail.com",923851970), (4,"valentina.jones@hotmail.com",288981964), (5,"laura.brown@hotmail.com",932931999), (6,"isabella.davis@hotmail.com",155851932), (7,"manuela.miller@hotmail.com",264151956), (8,"julia.wilson@hotmail.com",937041947), (9,"heloisa.moore@hotmail.com",336291995), (10,"luiza.taylor@hotmail.com",158081984), (11,"maria.luiza.anderson@hotmail.com",138051944), (12,"lorena.thomas@hotmail.com",989701943), (13,"livia.jackson@hotmail.com",992501993), (14,"giovanna.white@hotmail.com",227301986), (15,"maria.eduarda.harris@hotmail.com",259912005), (16,"beatriz.martin@hotmail.com",917921990), (17,"maria.clara.thompson@hotmail.com",245451989), (18,"cecilia.garcia@gmail.com",298192020), (19,"eloa.martinez@hotmail.com",970801992), (20,"lara.robinson@hotmail.com",283291938), (21,"maria.julia.clark@hotmail.com",232561935), (22,"isadora.rodriguez@hotmail.com",977101980), (23,"mariana.lewis@hotmail.com",994041972), (24,"emanuelly.lee@gmail.com",242972006), (25,"ana.julia.walker@hotmail.com",164831999), (26,"ana.luiza.hall@gmail.com",308542018), (27,"ana.clara.allen@hotmail.com",939981985), (28,"melissa.young@hotmail.com",973551992), (29,"yasmin.hernandez@gmail.com",996692014), (30,"maria.alice.king@hotmail.com",301721992), (31,"isabelly.wright@hotmail.com",170441974), (32,"lavinia.lopez@gmail.com",995992018), (33,"esther.hill@hotmail.com",218671986), (34,"sarah.scott@hotmail.com",139431937), (35,"elisa.green@hotmail.com",916791948), (36,"antonella.adams@gmail.com",927802014), (37,"rafaela.baker@hotmail.com",144131995), (38,"maria.cecilia.gonzalez@hotmail.com",941532001), (39,"liz.nelson@hotmail.com",962731936), (40,"marina.carter@gmail.com",975332019), (41,"nicole.mitchell@hotmail.com",335201977), (42,"maitê.perez@hotmail.com",283441934), (43,"isis.roberts@hotmail.com",237981981), (44,"alicia.turner@hotmail.com",339171947), (45,"luna.phillips@hotmail.com",348811930), (46,"rebeca.campbell@hotmail.com",919011970), (47,"agatha.parker@hotmail.com",222361930), (48,"leticia.evans@hotmail.com",994431962), (49,"maria-.edwards@gmail.com",328782010), (50,"gabriela.collins@hotmail.com",293131960), (51,"ana.laura.stewart@hotmail.com",307311934), (52,"catarina.sanchez@gmail.com",118612020), (53,"clara.morris@hotmail.com",196901932), (54,"ana.beatriz.rogers@hotmail.com",161991989), (55,"vitoria.reed@gmail.com",308262011), (56,"olivia.cook@hotmail.com",269911958), (57,"maria.fernanda.morgan@hotmail.com",270711953), (58,"emilly.bell@hotmail.com",985791994), (59,"maria.valentina.murphy@hotmail.com",187521959), (60,"milena.bailey@hotmail.com",990331977), (61,"maria.helena.rivera@hotmail.com",164221994), (62,"bianca.cooper@hotmail.com",933061942), (63,"larissa.richardson@hotmail.com",250551989), (64,"mirella.cox@gmail.com",189892016), (65,"maria.flor.howard@gmail.com",156982010), (66,"allana.ward@hotmail.com",327332004), (67,"ana.sophia.torres@gmail.com",109822006), (68,"clarice.peterson@hotmail.com",917511975), (69,"pietra.gray@hotmail.com",296571951), (70,"maria.vitoria.ramirez@hotmail.com",133991955), (71,"maya.james@hotmail.com",241902003), (72,"lais.watson@hotmail.com",266131930), (73,"ayla.brooks@hotmail.com",171151954), (74,"ana.livia.kelly@gmail.com",121882020), (75,"eduarda.sanders@hotmail.com",932421946), (76,"mariah.price@hotmail.com",315131999), (77,"stella.bennett@hotmail.com",119311970), (78,"ana.wood@hotmail.com",962751936), (79,"gabrielly.barnes@gmail.com",176292011), (80,"sophie.ross@hotmail.com",298621998), (81,"carolina.henderson@hotmail.com",968721990), (82,"maria.laura.coleman@hotmail.com",135001967), (83,"maria.heloisa.jenkins@hotmail.com",211301967), (84,"maria.sophia.perry@gmail.com",239542007), (85,"fernanda.powell@hotmail.com",926801996), (86,"malu.long@hotmail.com",301131980), (87,"analu.patterson@hotmail.com",230511972), (88,"amanda.hughes@gmail.com",109852012), (89,"aurora.flores@hotmail.com",250081949), (90,"maria.isis.washington@hotmail.com",922201998), (91,"louise.butler@hotmail.com",152411973), (92,"heloise.simmons@gmail.com",213792019), (93,"ana.vitoria.foster@hotmail.com",246761931), (94,"ana.cecilia.gonzales@hotmail.com",147271983), (95,"ana.liz.bryant@hotmail.com",944651945), (96,"joana.alexander@hotmail.com",189831998), (97,"luana.russell@hotmail.com",266481956), (98,"antônia.griffin@gmail.com",315992017), (99,"isabel.diaz@hotmail.com",923471996), (100,"bruna.hayes.english@hotmail.com",226231978), (101,"miguel.cahill@hotmail.com",930571997), (102,"arthur.caldwell@hotmail.com",970441967), (103,"bernardo.calhoun@hotmail.com",304631966), (104,"heitor.callahan@hotmail.com",963771972), (105,"davi.cameron@gmail.com",144402007), (106,"lorenzo.campbell@hotmail.com",254621964), (107,"theo.cannon@gmail.com",120232013), (108,"pedro.cantrell@gmail.com",345482011), (109,"gabriel.cantu@hotmail.com",171301997), (110,"enzo.cardenas@hotmail.com",133331988), (111,"matheus.carey@hotmail.com",992651951), (112,"lucas.carlson@hotmail.com",280071993), (113,"benjamin.carney@gmail.com",224332020), (114,"nicolas.carpenter@hotmail.com",181321989), (115,"guilherme.carr@gmail.com",171922021), (116,"rafael.carroll@gmail.com",959302009), (117,"joaquim.carson@gmail.com",274372021), (118,"samuel.carter@hotmail.com",220141990), (119,"enzo.gabriel.carver@gmail.com",182992016), (120,"joão.miguel.casey@hotmail.com",262851976), (121,"henrique.cassidy@gmail.com",997072006), (122,"gustavo.castillo@hotmail.com",161991948), (123,"murilo.castro@hotmail.com",210491953), (124,"pedro.henrique.chandler@hotmail.com",989091970), (125,"pietro.chaney@hotmail.com",910681956), (126,"lucca.chapman@hotmail.com",294021944), (127,"felipe.chase@hotmail.com",345122003), (128,"joão.pedro.chavez@hotmail.com",117232005), (129,"isaac.childers@hotmail.com",186191932), (130,"benicio.choate@hotmail.com",981951978), (131,"daniel.christian@hotmail.com",177331993), (132,"anthony.christie@hotmail.com",296831999), (133,"leonardo.church@gmail.com",228412020), (134,"davi.lucca.churchill@hotmail.com",296561970), (135,"bryan.clancy@hotmail.com",190532002), (136,"eduardo.clark@gmail.com",139492020), (137,"joão.lucas.clark@hotmail.com",936371961), (138,"victor.clarke@hotmail.com",219181979), (139,"joão.clay@hotmail.com",102881973), (140,"cauã.clayton@hotmail.com",954671974), (141,"antônio.cleveland@hotmail.com",981432005), (142,"vicente.clifford@hotmail.com",912471932), (143,"caleb.cobb@hotmail.com",332311963), (144,"gael.cochran@hotmail.com",172771987), (145,"bento.cochrane@hotmail.com",252901941), (146,"caio.coffey@hotmail.com",258301961), (147,"emanuel.cole@hotmail.com",227761933), (148,"vinicius.coleman@hotmail.com",216871966), (149,"joão.guilherme.coleman@hotmail.com",172801994), (150,"davi.lucas.collier@gmail.com",936742018), (151,"noah.collins@hotmail.com",184151939), (152,"joão.gabriel.collins@hotmail.com",148461987), (153,"joão.victor.combs@hotmail.com",928331994), (154,"luiz.miguel.compton@hotmail.com",227822001), (155,"francisco.conley@hotmail.com",986231931), (156,"kaique.connell@gmail.com",976962007), (157,"otavio.connolly@hotmail.com",245721977), (158,"augusto.conrad@gmail.com",323452018), (159,"levi.conway@hotmail.com",284711987), (160,"yuri.cook@hotmail.com",159031984), (161,"enrico.cooke@hotmail.com",198511933), (162,"thiago.cooley@hotmail.com",989501966), (163,"ian.cooney@hotmail.com",179791987), (164,"victor.hugo.cooper@gmail.com",980922012), (165,"thomas.copeland@hotmail.com",295491998), (166,"henry.corbett@hotmail.com",214581998), (167,"luiz.felipe.corcoran@hotmail.com",138731984), (168,"ryan.cormier@hotmail.com",990131972), (169,"arthur.miguel.costello@hotmail.com",262611983), (170,"davi.luiz.coughlin@hotmail.com",914161996), (171,"nathan.cowan@hotmail.com",247061974), (172,"pedro.lucas.cox@hotmail.com",214391957), (173,"davi.miguel.cox@gmail.com",159502010), (174,"raul.coyle@hotmail.com",121691936), (175,"pedro.miguel.coyne@hotmail.com",166891966), (176,"luiz.henrique.crabtree@hotmail.com",944412000), (177,"luan.craig@hotmail.com",944451976), (178,"erick.crawford@hotmail.com",310071952), (179,"martin.crockett@gmail.com",101102009), (180,"bruno.cross@gmail.com",982032012), (181,"rodrigo.crouch@hotmail.com",219912000), (182,"luiz.gustavo.crowley@hotmail.com",101981935), (183,"arthur.gabriel.cruz@gmail.com",207652014), (184,"breno.cullen@hotmail.com",950031953), (185,"kauê.cunningham@hotmail.com",939821968), (186,"enzo.miguel.curran@hotmail.com",270561952), (187,"fernando.curtis@hotmail.com",249411975), (188,"arthur.henrique.silva@hotmail.com",919161998), (189,"luiz.otavio.amorim@hotmail.com",125181979), (190,"carlos.eduardo.furtado@hotmail.com",150051985), (191,"tomas.costa@hotmail.com",920561976), (192,"lucas.gabriel.soares@hotmail.com",264201981), (193,"andre.ferreira@hotmail.com",979631982), (194,"jose.coelho@hotmail.com",175111939), (195,"yago.alves@hotmail.com",222311986), (196,"danilo.conceição@hotmail.com",182601977), (197,"anthony.gabriel.faro@gmail.com",115462010), (198,"ruan.santana@gmail.com",163562017), (199,"miguel.henrique.akemi@hotmail.com",960961954), (200,"oliver.nakata@hotmail.com",973941976), (201,"alice.kamada@hotmail.com",114541939), (202,"sophia.santos@hotmail.com",331321945), (203,"helena.pires@hotmail.com",113661944), (204,"valentina.espindola@hotmail.com",987591976), (205,"laura.oliveira@hotmail.com",959231961), (206,"isabella.souza@hotmail.com",914301975), (207,"manuela.rodrigues@gmail.com",109542007), (208,"julia.lopes@hotmail.com",242831968), (209,"heloisa.pereira@hotmail.com",108591931), (210,"luiza.cabral@hotmail.com",188111998), (211,"maria.luiza.gomes@gmail.com",287092021), (212,"lorena.lima@hotmail.com",940972000), (213,"livia.ribeiro@hotmail.com",969361955), (214,"giovanna.martins@hotmail.com",260661938), (215,"maria.eduarda.carvallho@hotmail.com",970751945), (216,"beatriz.almeida@hotmail.com",249251955), (217,"maria.clara.fernandes@hotmail.com",233091947), (218,"cecilia.vieira@hotmail.com",221151952), (219,"eloa.barbosa@hotmail.com",131061943), (220,"lara.rocha.@hotmail.com",118641958), (221,"maria.julia.dias@hotmail.com",217752003), (222,"isadora.nascimento@hotmail.com",296341972), (223,"mariana.andrade@hotmail.com",287512001), (224,"emanuelly.moreira@hotmail.com",284561970), (225,"ana.julia.nunes@hotmail.com",219921954), (226,"ana.luiza.marques@hotmail.com",152071963), (227,"ana.clara.machado@hotmail.com",946011961);


SELECT COUNT(*) FROM contact;
SELECT COUNT(DISTINCT name) FROM costumers;
SELECT COUNT(name) FROM costumers;
SELECT COUNT(phone) FROM contact;
SELECT COUNT(DISTINCT phone) FROM contact;


ELECT DISTINCT firstName FROM person.Person;

SELECT * FROM person.Person;

SELECT * FROM person.Person WHERE MiddleName = 'A';

SELECT * FROM Production.Product WHERE color = 'black';
SELECT * FROM Production.Product Where ListPrice > 1500 and ListPrice <5000;
SELECT Name, Weight FROM Production.Product WHERE Weight> 500 and Weight < 700;

SELECT * FROM HumanResources.Employee WHERE MaritalStatus = 'm' and SalariedFlag = 'true';

select * from Person.Person where FirstName = 'peter' and LastName='krebs';

select count(*) From Production.Product;

Select count( size) from Production.Product;

select TOP 5 * from Production.Product;

select TOP 6 * from Production.Product order by Name;

select FirstName, LastName from Person.Person order by FirstName asc, LastName desc;

select * from Production.Product;
select top 3 ProductID, ListPrice FROM Production.Product order by ListPrice desc;
select top 3 ProductID, ListPrice FROM Production.Product order by ListPrice asc;

SELECT TOP 4 ProductID, name, productnumber FROM Production.Product ORDER BY ProductID asc;
SELECT TOP 4 ProductID, name, productnumber FROM Production.Product;
SELECT TOP 4 ProductID, name, productnumber FROM Production.Product ORDER BY ProductID desc;

SELECT Name, ListPrice FROM Production.Product WHERE ListPrice BETWEEN 1000 and 1500;

SELECT Name, ListPrice FROM Production.Product WHERE ListPrice NOT BETWEEN 1000 and 1500;

SELECT * FROM HumanResources.Employee WHERE HireDate BETWEEN '2009/01/01' AND '2010/01/01' ORDER BY HireDate desc;
SELECT * FROM Person.Person WHERE BusinessEntityID IN (2,7,13,116,19,22);
--using like
SELECT * FROM Person.Person WHERE FirstName like 'ovi%';
SELECT * FROM Person.Person WHERE FirstName like '%essa%';
--using underscore
SELECT * FROM Person.Person WHERE FirstName like '%ro_%';
SELECT * FROM Person.Person WHERE FirstName like '%ro__%';


SELECT COUNT(*) FROM Production.Product WHERE ListPrice > 1500;

SELECT COUNT(*) FROM Person.Person WHERE LastName like 'P%';

SELECT COUNT(DISTINCT City) FROM Person.Address;

SELECT DISTINCT City From Person.Address;

SELECT Color, ListPrice FROM Production.Product WHERE Color = 'Red' and ListPrice BETWEEN 500 and 1000;
SELECT COUNT(*) FROM Production.Product WHERE Color = 'Red' and ListPrice BETWEEN 500 and 1000;

SELECT Name FROM Production.Product WHERE Name LIKE'%road%';
SELECT COUNT(*) FROM Production.Product WHERE Name LIKE '%road%';

--Using sum, min, max, avg and AS
SELECT sum(lineTotal) AS "Soma" FROM Sales.SalesOrderDetail;
SELECT max(linetotal) FROM SAles.SalesOrderDetail;
SELECT min(linetotal) FROM SAles.SalesOrderDetail;
SELECT avg(linetotal) FROM SAles.SalesOrderDetail;

--Group BY
SELECT  SpecialOfferID, sum(UnitPrice) FROM Sales.SalesOrderDetail GROUP BY SpecialOfferID; --correct
SELECT  SpecialOfferID, UnitPrice FROM Sales.SalesOrderDetail GROUP BY SpecialOfferID; --wrong because missing agregate sintax like sum, min, ma
SELECT ProductId, COUNT(ProductId) FROM Sales.SalesOrderDetail Group BY ProductID; 
SELECT ProductID, sum(OrderQty) AS "Tot Pedidos" FROM Sales.SalesOrderDetail Group BY ProductID ;

SELECT FirstName FROM Person.Person;
SELECT FirstName, COUNT(FirstName) AS 'Qty Name' FROM Person.Person GROUP BY FirstName ORDER BY 'Qty Name' desc; 
SELECT * FROM Person.Person Where FirstName LIKE 'Gustavo';
SELECT * FROM Person.Person Where FirstName LIKE 'Yvonne';
SELECT * FROM Person.Person;
SELECT MiddleName, COUNT(MiddleName) AS 'QtyMiddleName' FROM Person.Person GROUP BY MiddleName ORDER BY 'QtyMiddleName';
SELECT * FROM Person.Person WHERE MiddleName LIKE 'William';

SELECT * FROM Production.Product;
SELECT * FROM Sales.SalesOrderDetail;

--GROUP BY and RDER BY
SELECT ProductID, avg(OrderQty) AS 'avgOrderQty' FROM Sales.SalesOrderDetail GROUP BY ProductID ORDER BY 'avgOrderQty' desc;
SELECT ProductID, sum(LineTotal) FROM Sales.SalesOrderDetail GROUP BY (ProductID) ORDER BY sum(LineTotal) desc;
SELECT * FROM Production.WorkOrder;
SELECT ProductID, COUNT(ProductID) "contagem" ,avg(OrderQty) "media" FROM Production.WorkOrder wo GROUP BY ProductID 

--Using having
SELECT StateProvinceID, COUNT(StateProvinceID) AS 'Qty' FROM Person.Address a GROUP BY StateProvinceID HAVING COUNT(StateProvinceID) > 1000 ;
SELECT ProductID, avg(lineTotal) AS 'soma' FROM Sales.SalesOrderDetail Group by ProductID HAVING avg(LineTotal) < 1000000 ORDER BY 'soma' desc;

--Others
SELECT ProductID, COUNT(ProductID) FROM Sales.SalesOrderDetail GROUP BY ProductID ORDER BY COUNT(ProductID);
SELECT ProductID, lineTotal FROM Sales.SalesOrderDetail sod WHERE ProductID = 878;

--using AS
SELECT TOP 10 FirstName as Nome, LastName AS SObrenoma FROM Person.Person p;
SELECT TOP 10 ProductNumber AS 'Numero do produto' FROM Production.Product p ;
SELECT TOP 10 unitPrice AS Preço From Sales.SalesOrderDetail sod 

--inner join
SELECT cos.name, cos.lastName , cos.payment, con.email FROM costumers cos INNER JOIN contact con ON con.idcostumers = cos.idcostumers;
SELECT cos.idcostumers, cos.completeName , con.email, con.phone FROM contact con INNER JOIN costumers cos ON cos.idcostumers = con.idcostumers;
SELECT p.ProductID, s.UnitPrice FROM Production.Product p INNER JOIN Sales.SalesOrderDetail s ON s.ProductID  = p.ProductID ;

-- loking in to person and email table for BusinessEntityId, FirsName, lastName and EmailAddress column.
SELECT * FROM Person.Person p ;
SELECT TOP 10 * FROM Person.EmailAddress ea;

-- doing select
SELECT p.BusinessEntityID, p.FirstName, p.LastName, ea.EmailAddress FROM Person.Person p INNER JOIN Person.EmailAddress ea ON ea.BusinessEntityID = p.BusinessEntityID ;

-- knowing product and sales table and ProductSubcategory;
SELECT top 10 * from Production.Product p ;
select top 10 * from Sales.SalesOrderDetail sod ;
SELECT TOP 10 * FROM Production.ProductSubcategory ps2 ;

--doing select
SELECT p.Name, p.ListPrice, ps.Name FROM Production.Product p INNER JOIN Production.ProductSubcategory ps ON ps.ProductSubcategoryID = p.ProductSubcategoryID ;

--knowing and doing table using inner join
SELECT TOP 10 * FROM Person.BusinessEntityAddress bea ;
SELECT TOP 10 * FROM Person.Address a ;
SELECT TOP 10 * FROM Person.BusinessEntityAddress bea INNER JOIN Person.Address pa ON pa.AddressID = bea.AddressID ;

SELECT TOP 10 * FROM Person.PhoneNumberType pnt  ;
SELECT TOP 10 * FROM Person.PersonPhone pp ;
SELECT TOP 10 * FROM Person.Person p ;

SELECT pp.BusinessEntityID, 
pnt.Name, 
pp.PhoneNumberTypeID, 
pp.PhoneNUmber FROM Person.PersonPhone pp 
INNER JOIN Person.PhoneNumberType pnt 
ON pnt.PhoneNumberTypeID  = pp.PhoneNumberTypeID ;

SELECT TOP 10 * FROM Person.Address;
SELECT pa.AddressID , pa.City, pa.StateProvinceID, sp.Name FROM Person.Address pa INNER JOIN Person.StateProvince sp ON sp.StateProvinceID = pa.StateProvinceID;




CREATE TABLE TabelaA (
id INT NOT NULL AUTO_INCREMENT,
nome VARCHAR(45),
PRIMARY KEY (id));

CREATE TABLE TabelaB (
id INT NOT NULL AUTO_INCREMENT,
nome VARCHAR(45),
PRIMARY KEY(id));

INSERT INTO TabelaA (nome) VALUES ('Robo'),('Macaco'),('Samurai'),('Monitor');
SELECT * FROM TabelaA;

INSERT INTO TabelaB (nome) VALUES ('Espada'),('Robo'),('Mario'),('Samurai');
SELECT * FROM TabelaB;
#INNER JOIN
SELECT * FROM TabelaA INNER JOIN TabelaB ON TabelaA.nome = TabelaB.nome;

SELECT * FROM TabelaA FULL OUTER JOIN TabelaB ON TabelaA.nome = TabelaB.nome;

SELECT * FROM TabelaA LEFT JOIN TabelaB ON TabelaA.nome = TabelaB.nome;
TRUNCATE TabelaA;