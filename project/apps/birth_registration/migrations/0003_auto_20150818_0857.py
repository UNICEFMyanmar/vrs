# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import birth_registration.fields
import birth_registration.validators
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('birth_registration', '0002_auto_20150818_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='f201',
            name='CTIZ',
            field=birth_registration.fields.CitizenshipField(blank=(True,), choices=[(1, '01 - Myanmar'), (2, '02 - Indian'), (3, '03 - Pakistani'), (4, '04 - Bangladesh'), (5, '05 - Nepalese'), (6, '06 - Chinese'), (7, '07 - European/American'), (8, '08 - Other Asian'), (9, '09 - Others'), (10, '10 - Not stated')], null=(True,), verbose_name='Citizenship', validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='Date_of_Death',
            field=models.DateField(help_text='Day, month and year: <kbd>25102006</kbd>', verbose_name='Date of Death'),
        ),
        migrations.AlterField(
            model_name='f201',
            name='Date_of_Registration',
            field=models.DateField(help_text='Day, month and year: <kbd>25102006</kbd>', verbose_name='Date of registration'),
        ),
        migrations.AlterField(
            model_name='f201',
            name='NNRT',
            field=birth_registration.fields.StateDivisionField(max_length=2, choices=[(1, '01 - Kachin'), (2, '02 - Kayh'), (3, '03 - Kayin'), (4, '04 - Chin'), (5, '05 - Sagaing'), (6, '06 - Tanintharyi'), (7, '07 - Bago'), (8, '08 - Magway'), (9, '09 - Mandalay'), (10, '10 - Mon'), (11, '11 - Rakhine'), (12, '12 - Yangon'), (13, '13 - Shan'), (14, '14 - Ayyarwaddy'), (15, '15 - NayPyiTaw')], verbose_name='State/Division', validators=[birth_registration.validators.validate_2digits]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='NNRT1',
            field=birth_registration.fields.DistrictField(max_length=2, choices=[('01 - Kachin', [(1, '01 - Myitkyina'), (2, '02 - Bamaw'), (3, '03 - Puta O')]), ('02 - Kayh', [(4, '04 - Loikaw'), (5, '05 - Bawlakhei')]), ('03 - Kayin', [(6, '06 - Pha An'), (7, '07 - Myawaddy'), (8, '08 - Kawtkaraik')]), ('04 - Chin', [(9, '09 - Phalan'), (10, '10 - Mintatt')]), ('05 - Sagaing', [(11, '11 - Sagaing'), (12, '12 - Shwebo'), (13, '13 - Monywar'), (14, '14 - Kathar'), (15, '15 - Kalay'), (16, '16 - Tamu'), (17, '17 - Mawlaik'), (18, '18 - Khantee')]), ('06 - Tanintharyi', [(19, '19 - Dawei'), (20, '20 - Myeik'), (21, '21 - Kautthaung')]), ('07 - Bago', [(22, '22 - Bago'), (23, '23 - Pyay'), (24, '24 - Tharyarwaddy'), (25, '25 - Taungoo')]), ('08 - Magway', [(26, '26 - Magway'), (27, '27 - Minbu'), (28, '28 - Thayet'), (29, '29 - Pakokku'), (30, '30 - Gantgaw')]), ('09 - Mandalay', [(31, '31 - Mandalay'), (32, '32 - Pyin Oo Lwin'), (33, '33 - Kyaukse'), (34, '34 - Myingyan'), (35, '35 - Nyaung Oo'), (36, '36 - Yameithinn'), (37, '37 - Meikhtila')]), ('10 - Mon', [(38, '38 - Mawlamyaing'), (39, '39 - Thahton')]), ('11 - Rakhine', [(40, '40 - Sittwe'), (41, '41 - Maungdaw'), (42, '42 - Buthidaung'), (43, '43 - Kyaukphyu'), (44, '44 - Thandwe')]), ('12 - Yangon', [(45, '45 - Ahshaytbine (East)'), (46, '46 - Ahnoutpine (West)'), (47, '47 - Taungbine (South)'), (48, '48 - Myaukpine (North)')]), ('13 - Shan', [(49, '49 - Taungyi'), (50, '50 - Loilin'), (51, '51 - Lahsio'), (52, '52 - Muse'), (53, '53 - Kyaukmei'), (54, '54 - Kunloan'), (55, '55 - Laukkaing'), (56, '56 - Kyaington'), (57, '57 - Minesatt'), (58, '58 - Tachilaik'), (59, '59 - Minephyat')]), ('14 - Ayyarwaddy', [(60, '60 - Pathein'), (61, '61 - Hinthada'), (62, '62 - Myaungmya'), (63, '63 - Ma U Bin'), (64, '64 - Phyarpon')]), ('15 - NayPyiTaw', [(65, '65 - Zayarthiri'), (66, '66 - Dakhenathiri'), (67, '67 - Oktayathiri'), (68, '68 - Potebathiri'), (69, '69 - Zabuthiri'), (70, '70 - Tatkon'), (71, '71 - Pyinmana'), (72, '72 - Lewe')])], verbose_name='District', validators=[birth_registration.validators.validate_2digits]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='NNST',
            field=birth_registration.fields.TownshipField(max_length=2, choices=[('01 - Myitkyina', [(1, '01 - Myitkyina'), (2, '02 - Waingmaw'), (3, '03 - Ingyan Yan'), (4, '04 - Moekaung'), (5, '05 - Moehnyin'), (6, '06 - Phakant'), (7, '07 - Karmine*'), (8, '08 - Ta Naing'), (9, '09 - Chibway'), (10, '10 - Sautlaw')]), ('02 - Bamaw', [(11, '01 - Bamaw'), (12, '02 - Shwegu'), (13, '03 - Moemauk'), (14, '04 - Mansi')]), ('03 - Puta O', [(15, '01 - Puta O'), (16, '02 - Swanprabum'), (17, '03 - Machanbaw'), (18, '04 - Khaunglanphoo'), (19, '05 - Naungmon')]), ('04 - Loikaw', [(20, '01 - Loikaw'), (21, '02 - Dimawsoe'), (22, '03 - Phrusoe'), (23, '04 - Shartaw')]), ('05 - Bawlakhei', [(24, '01 - Bawlakhei'), (25, '02 - Pharsaung'), (26, '03 - Meiseit')]), ('06 - Pha An', [(27, '01 - Pha An'), (28, '02 - Hlaingbweit'), (29, '03 - Pharpon'), (30, '04 - Thandaung'), (31, '05 - Thandaungkyee')]), ('07 - Myawaddy', [(32, '01 - Myawaddy')]), ('08 - Kawtkaraik', [(33, '01 - Kawtkaraik'), (34, '02 - Kyarinseikkyi'), (35, '03 - Phayathonesu*'), (36, '04 - Kyoandoe')]), ('09 - Phalan', [(37, '01 - Phalan'), (38, '02 - Hakha'), (39, '03 - Htantalan'), (40, '04 - Teetain'), (41, '05 - Tunzan')]), ('10 - Mintatt', [(42, '01 - Mintatt'), (43, '02 - Matupi'), (44, '03 - Kanpetlet'), (45, '04 - Paletwa')]), ('11 - Sagaing', [(46, '01 - Sagaing'), (47, '02 - Myinmu'), (48, '03 - Myaung')]), ('12 - Shwebo', [(49, '01 - Shwebo'), (50, '02 - Khin Oo'), (51, '03 - Wetlet'), (52, '04 - Kantbalu'), (53, '05 - Kyunhla'), (54, '06 - Yay Oo'), (55, '07 - Dipeiyin'), (56, '08 - Tantsei')]), ('13 - Monywar', [(57, '01 - Monywar'), (58, '02 - Butalin'), (59, '03 - Ahyartaw'), (60, '04 - Chaung Oo'), (61, '05 - Yinmarbin'), (62, '06 - Kani'), (63, '07 - Salingyee'), (64, '08 - Palei')]), ('14 - Kathar', [(65, '01 - Kathar'), (66, '02 - Indaw'), (67, '03 - Hteechaink'), (68, '04 - Bamauk'), (69, '05 - Kawlin'), (70, '06 - Wuntho'), (71, '07 - Pinleibu')]), ('15 - Kalay', [(72, '01 - Kalay'), (73, '02 - Kalaywa'), (74, '03 - Minkin')]), ('16 - Tamu', [(75, '01 - Tamu')]), ('17 - Mawlaik', [(76, '01 - Mawlaik'), (77, '02 - Phaungpyin')]), ('18 - Khantee', [(78, '01 - Khantee'), (79, '02 - Hoamalin'), (80, '03 - Layshee'), (81, '04 - Lahei'), (82, '05 - Nanyon')]), ('19 - Dawei', [(83, '01 - Dawei'), (84, '02 - Launglon'), (85, '03 - Thayetchaung'), (86, '04 - Yayphyu')]), ('20 - Myeik', [(87, '01 - Myeik'), (88, '02 - Kyunsu'), (89, '03 - Pulaw'), (90, '04 - Tanintharyi')]), ('21 - Kautthaung', [(91, '01 - Kautthaung'), (92, '02 - Boatpyin')]), ('22 - Bago', [(93, '01 - Bago'), (94, '02 - Thanatpin'), (95, '03 - Kawa'), (96, '04 - Waw'), (97, '05 - Nyaunglaybin'), (98, '06 - Madauk*'), (99, '07 - Pyuntanzar*'), (100, '08 - Kyauktaga'), (101, '09 - Peinweikone*'), (102, '10 - Daik Oo'), (103, '11 - Shwekyin')]), ('23 - Pyay', [(104, '01 - Pyay'), (105, '02 - Pauk Khaung'), (106, '03 - Padaung'), (107, '04 - Paungtei'), (108, '05 - Theikone'), (109, '06 - Shwetaung')]), ('24 - Tharyarwaddy', [(110, '01 - Tharyarwaddy'), (111, '02 - Thonesei*'), (112, '03 - Letpandan'), (113, '04 - Minhla'), (114, '05 - Oakpho'), (115, '06 - Zeekone'), (116, '07 - Nattalin'), (117, '08 - Moenyo'), (118, '09 - Kyoetbinkaut')]), ('25 - Taungoo', [(119, '01 - Taungoo'), (120, '02 - Yaytarshay'), (121, '03 - Kyaukyee'), (122, '04 - Phyu'), (123, '05 - Oaktwin'), (124, '06 - Htandabin')]), ('26 - Magway', [(125, '01 - Magway'), (126, '02 - Yenanchaung'), (127, '03 - Chauk'), (128, '04 - Taungtwingyee'), (129, '05 - Myoethit'), (130, '06 - Natmauk')]), ('27 - Minbu', [(131, '01 - Minbu'), (132, '02 - Saku*'), (133, '03 - Pwintphyu'), (134, '04 - Ngaphei'), (135, '05 - Salin'), (136, '06 - Sinphyukyun*'), (137, '07 - Saytoattaya')]), ('28 - Thayet', [(138, '01 - Thayet'), (139, '02 - Minhla'), (140, '03 - Mintone'), (141, '04 - Kanma'), (142, '05 - Aunglan'), (143, '06 - Sinpaungwei')]), ('29 - Pakokku', [(144, '01 - Pakokku'), (145, '02 - Yesagyo'), (146, '03 - Myaing'), (147, '04 - Pauk'), (148, '05 - Saikphyu')]), ('30 - Gantgaw', [(149, '01 - Gantgaw'), (150, '02 - Hteelin'), (151, '03 - Saw')]), ('31 - Mandalay', [(152, '01 - Aungmyaytharzan'), (153, '02 - Chanayetharzan'), (154, '03 - MahaAungmyay'), (155, '04 - Chanmyatharsi'), (156, '05 - Pyigyeetakhun'), (157, '06 - Amarapura'), (158, '07 - Myitnge*'), (159, '08 - Patheingyee')]), ('32 - Pyin Oo Lwin', [(160, '01 - Pyin Oo Lwin'), (161, '02 - Madayar'), (162, '03 - Sintkuu'), (163, '04 - Moegauk'), (164, '05 - Thabaikkyin')]), ('33 - Kyaukse', [(165, '01 - Kyaukse'), (166, '02 - Sintkai'), (167, '03 - Myitthar'), (168, '04 - Tadaoo')]), ('34 - Myingyan', [(169, '01 - Myingyan'), (170, '02 - Taungthar'), (171, '03 - Nahtoegyee'), (172, '04 - Kyaukbadaung'), (173, '05 - Nganzun')]), ('35 - Nyaung Oo', [(174, '01 - Nyaung Oo'), (175, '02 - Bagan*'), (176, '03 - Ngatharauk*')]), ('36 - Yameithinn', [(177, '01 - Yameithinn'), (178, '02 - Pyawbwei'), (179, '03 - Tatkone'), (180, '04 - Pyinmana'), (181, '05 - Leiway')]), ('37 - Meikhtila', [(182, '01 - Meikhtila'), (183, '02 - Mahlaing'), (184, '03 - Tharzi'), (185, '04 - Wantwin')]), ('38 - Mawlamyaing', [(186, '01 - Mawlamyaing'), (187, '02 - Kyaikmayaw'), (188, '03 - Chaungzon'), (189, '04 - Thanphyuzayat'), (190, '05 - Kyaikkhami*'), (191, '06 - Mudon'), (192, '07 - Yay')]), ('39 - Thahton', [(193, '01 - Thahton'), (194, '02 - Paung'), (195, '03 - Kyaikhto'), (196, '04 - Beelin')]), ('40 - Sittwe', [(197, '01 - Sittwe'), (198, '02 - Poannakyun'), (199, '03 - Myauk Oo'), (200, '04 - Kyauktaw'), (201, '05 - Minbya'), (202, '06 - Pauktaw'), (203, '07 - Myaybon')]), ('41 - Maungdaw', [(204, '01 - Maungdaw')]), ('42 - Buthidaung', [(205, '01 - Buthidaung'), (206, '02 - Rathedaung')]), ('43 - Kyaukphyu', [(207, '01 - Kyaukphyu'), (208, '02 - Man Aung'), (209, '03 - Ranbyei'), (210, '04 - Ann')]), ('44 - Thandwe', [(211, '01 - Thandwe'), (212, '02 - Taungkauk'), (213, '03 - Gwa')]), ('45 - Ahshaytbine (East)', [(214, '01 - Thingankyun'), (215, '02 - Yankin'), (216, '03 - Taung Okkalapa'), (217, '04 - Myauk Okkalapa'), (218, '05 - Tharketa'), (219, '06 - Dawbon'), (220, '07 - Tarmwe'), (221, '08 - Pazuntaung'), (222, '09 - Botahtaung'), (223, '10 - Dagon Myothit Taung (Sounth)'), (224, '11 - Dagon Myothi Myauk (North)'), (225, '12 - Dagon Myothit Ahshayt (East)'), (226, '13 - Dagon Myothit (Seikkan)'), (227, '14 - Mingalataungnyunt')]), ('46 - Ahnoutpine (West)', [(228, '01 - Kyauktada'), (229, '02 - Panbedan'), (230, '03 - Lanmadaw'), (231, '04 - Lathar'), (232, '05 - Ahlon'), (233, '06 - Kyeemyindine'), (234, '07 - Sanchaung'), (235, '08 - Hlaing'), (236, '09 - Kamaryut'), (237, '10 - Mayangone'), (238, '11 - Dagon'), (239, '12 - Bahan'), (240, '13 - Seikkan')]), ('47 - Taungbine (South)', [(241, '01 - Thanhlyin'), (242, '02 - Kyauktan'), (243, '03 - Thonekhwa'), (244, '04 - Khayan'), (245, '05 - Tonte'), (246, '06 - Kauthmu'), (247, '07 - Kunchangone'), (248, '08 - Dala'), (249, '09 - Seikkyee'), (250, '10 - Khanaungto'), (251, '11 - Kokoe Island')]), ('48 - Myaukpine (North)', [(252, '01 - Insein'), (253, '02 - Mingalardon'), (254, '03 - Htaunkkyant*'), (255, '04 - Hmawbi'), (256, '05 - Hlegu'), (257, '06 - Tiakkyee'), (258, '07 - Oakkan*'), (259, '08 - Htantabin'), (260, '09 - Shwepyithar'), (261, '10 - Hlaingtharyar'), (262, '11 - Ahphyauk*')]), ('49 - Taungyi', [(263, '01 - Taungyi'), (264, '02 - Ayetharyar*'), (265, '03 - Hopone'), (266, '04 - Nyaungshwe'), (267, '05 - Sisaing'), (268, '06 - Kalaw'), (269, '07 - Aungban*'), (270, '08 - Pindaya'), (271, '09 - Ywarngan'), (272, '10 - Yatsauk'), (273, '11 - Pinlaung'), (274, '12 - Phekhoan')]), ('50 - Loilin', [(275, '01 - Loilin'), (276, '02 - Pinlon'), (277, '03 - Leichar'), (278, '04 - Nantsam(South)'), (279, '05 - Kunhein'), (280, '06 - Moenei'), (281, '07 - Linkhay'), (282, '08 - Maukmei'), (283, '09 - Minepan'), (284, '10 - Kyaythee'), (285, '11 - Minekaing'), (286, '12 - Mineshu')]), ('51 - Lahsio', [(287, '01 - Lashio'), (288, '02 - Theinni'), (289, '03 - Mineyei'), (290, '04 - Tantyan'), (291, '05 - Minephant'), (292, '06 - Panyang'), (293, '07 - Narphan'), (294, '08 - Panwaing'), (295, '09 - Minemaw'), (296, '10 - Pansan (Pankhan)')]), ('52 - Muse', [(297, '01 - Muse'), (298, '02 - Nantkhan'), (299, '03 - Kutkhaing'), (300, '04 - Monkoe'), (301, '05 - Kyukoak')]), ('53 - Kyaukmei', [(302, '01 - Kyaukmei'), (303, '02 - Naungcho'), (304, '03 - Thibaw'), (305, '04 - Namtu'), (306, '05 - Nantsam(North)'), (307, '06 - Moemaik'), (308, '07 - Mabain'), (309, '08 - Mantoan')]), ('54 - Kunloan', [(310, '01 - Kunloan'), (311, '02 - Hopan')]), ('55 - Laukkaing', [(312, '01 - Laukkaing'), (313, '02 - Chinshwehaw*'), (314, '03 - Koankyan')]), ('56 - Kyaington', [(315, '01 - Kyaington'), (316, '02 - Minekhat'), (317, '03 - Mineyang'), (318, '04 - Minelar'), (319, '05 - Metman')]), ('57 - Minesatt', [(320, '01 - Minesatt'), (321, '02 - Minepyinn'), (322, '03 - Minetoan')]), ('58 - Tachilaik', [(323, '01 - Tachilaik')]), ('59 - Minephyat', [(324, '01 - Minephyat'), (325, '02 - Mineyaung')]), ('60 - Pathein', [(326, '01 - Pathein'), (327, '02 - Kangyidaunt'), (328, '03 - Tharpaung'), (329, '04 - Ngaputaw'), (330, '05 - Kyoanpyaw'), (331, '06 - Yaykyi'), (332, '07 - Ngathaingchaung'), (333, '08 - Kyaungkone'), (334, '09 - Haigyikyun')]), ('61 - Hinthada', [(335, '01 - Hinthada'), (336, '02 - Zalun'), (337, '03 - Laymyethnar'), (338, '04 - Myan Aung'), (339, '05 - Ka Naung'), (340, '06 - Kyankhin'), (341, '07 - Ingapu')]), ('62 - Myaungmya', [(342, '01 - Myaungmya'), (343, '02 - Ainmei'), (344, '03 - Laputta'), (345, '04 - Warkhema'), (346, '05 - Mawlamyaingkyun')]), ('63 - Ma U Bin', [(347, '01 - Ma U Bin'), (348, '02 - Pantanaw'), (349, '03 - Nyaungtone'), (350, '04 - Danubyu')]), ('64 - Phyarpon', [(351, '01 - Phyarpon'), (352, '02 - Bogalay'), (353, '03 - Kyaiklatt'), (354, '04 - Daydayei')]), ('65 - Zayarthiri', [(355, '01 - Zayarthiri')]), ('66 - Dakhenathiri', [(356, '01 - Dakhenathiri')]), ('67 - Oktayathiri', [(357, '01 - Oktayathiri')]), ('68 - Potebathiri', [(358, '01 - Potebathiri')]), ('69 - Zabuthiri', [(359, '01 - Zabuthiri')]), ('70 - Tatkon', [(360, '01 - Tatkon')]), ('71 - Pyinmana', [(361, '01 - Pyinmana')]), ('72 - Lewe', [(362, '01 - Lewe')])], verbose_name='Township or town', validators=[birth_registration.validators.validate_2digits]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='NNVD',
            field=birth_registration.fields.AreaField(help_text='Urban/Rural', choices=[(1, '01 - Urban'), (2, '02 - Rural')], verbose_name='Area', validators=([django.core.validators.MaxValueValidator(2)],)),
        ),
        migrations.AlterField(
            model_name='f201',
            name='OCCU',
            field=birth_registration.fields.OccupationField(blank=True, null=True, verbose_name='Occupation', choices=[(1, '01 - Professional Technical and related workers'), (2, '02 - Administrative and managerial workers'), (3, '03 - Clerical and related workers'), (4, '04 - Sales workers'), (5, '05 - Services workers'), (6, '06 - Agriculture, Animal Husbandry and Forest workers, Fishermen, Hunters'), (7, '07 - Production and related workers, Transport equipment operators and labours'), (8, '08 - Not classified by occupation'), (9, '09 - Armed Forces'), (0, '00 - Economically inactive')]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='Original_form',
            field=birth_registration.fields.OriginalFormField(help_text='Please attach a scanned copy of a photograph on the original form', upload_to=b'F201/%Y/%m/%d/', null=True, verbose_name='Original Form Image', blank=(True,)),
        ),
        migrations.AlterField(
            model_name='f201',
            name='PLD',
            field=birth_registration.fields.PlaceField(help_text='Check if place of death given in entry form (may be residence). Enter area of Yangon only if a house address. If a hospital or nursing home etc. give full address.<br/><ul><li>Home/House = 1</li><li>Government Hospital = 2</li><li>Nursing Home (including any maternity and child welfare society) = 3</li><li>Private Hospital/clinic = 4</li><li>Other institution = 5</li><li>Elsewhere = 6</li></ul>', verbose_name='Place of Death', choices=[(1, '01 - Home/House'), (2, '02 - Government Hospital'), (3, '03 - Nursing Home '), (4, '04 - Private Hospital/clinic'), (5, '05 - Other institution'), (6, '06 - Elsewhere')]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='RACE',
            field=birth_registration.fields.RaceField(blank=True, choices=[(1, '01 - Kachin'), (2, '02 - Kayah'), (3, '03 - Kayin'), (4, '04 - Chin'), (5, '05 - Bamar'), (6, '06 - Mon'), (7, '07 - Rakhine'), (8, '08 - Shan'), (9, '09 - Other indigenous Races'), (10, '10 - Myanmar/Foreigners'), (11, '11 - Chinese'), (12, '12 - Indian'), (13, '13 - Pakistani'), (14, '14 - Bangladesh'), (15, '15 - Nepal'), (16, '16 - Other Asian'), (17, '17 - Others'), (18, '18 - Not stated')], null=(True,), verbose_name='Race', validators=[django.core.validators.MaxValueValidator(18)]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='REL',
            field=birth_registration.fields.ReligionField(blank=True, choices=[(1, '01 - Buddhist'), (2, '02 - Islam'), (3, '03 - Christian'), (4, '04 - Hindu'), (5, '05 - Animist'), (6, '06 - Confucion'), (7, '07 - Sikh'), (8, '08 - Jew'), (9, '09 - Others'), (10, 'Not stated')], null=True, verbose_name='Religion', validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='SEX',
            field=models.PositiveSmallIntegerField(help_text='<ul><li>Male = 1 </li><li>Female = 2 </li><li>Not stated = 3</li></ul>', choices=[(1, '01 - Male'), (2, '02 - Female'), (3, '09 - Not stated')], verbose_name='Sex', validators=[django.core.validators.RegexValidator(regex=b'(1|2|9)', message='Incorrect choice. Avaiable choices:1 - Male, 2 - Female9 - Not Stated.')]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='SNER',
            field=birth_registration.fields.SerialNoField(help_text='Enter serial No. direct into coding column. Watch carefully for sequence of serial No.If it is not in sequence make query.<br/>Code actual serial No. in full 4 digits. If serial No. is 1 to 99; Code 0001-0009, and 10-99 code 0010, 0011,\u2026\u2026\u2026..0099, 0100 and over in full', blank=(False,), verbose_name='Serial No. in Registration book', validators=[django.core.validators.MaxValueValidator(99999)]),
        ),
        migrations.AlterField(
            model_name='f201',
            name='UPCR',
            field=birth_registration.fields.TownshipField(default=1, max_length=2, choices=[('01 - Myitkyina', [(1, '01 - Myitkyina'), (2, '02 - Waingmaw'), (3, '03 - Ingyan Yan'), (4, '04 - Moekaung'), (5, '05 - Moehnyin'), (6, '06 - Phakant'), (7, '07 - Karmine*'), (8, '08 - Ta Naing'), (9, '09 - Chibway'), (10, '10 - Sautlaw')]), ('02 - Bamaw', [(11, '01 - Bamaw'), (12, '02 - Shwegu'), (13, '03 - Moemauk'), (14, '04 - Mansi')]), ('03 - Puta O', [(15, '01 - Puta O'), (16, '02 - Swanprabum'), (17, '03 - Machanbaw'), (18, '04 - Khaunglanphoo'), (19, '05 - Naungmon')]), ('04 - Loikaw', [(20, '01 - Loikaw'), (21, '02 - Dimawsoe'), (22, '03 - Phrusoe'), (23, '04 - Shartaw')]), ('05 - Bawlakhei', [(24, '01 - Bawlakhei'), (25, '02 - Pharsaung'), (26, '03 - Meiseit')]), ('06 - Pha An', [(27, '01 - Pha An'), (28, '02 - Hlaingbweit'), (29, '03 - Pharpon'), (30, '04 - Thandaung'), (31, '05 - Thandaungkyee')]), ('07 - Myawaddy', [(32, '01 - Myawaddy')]), ('08 - Kawtkaraik', [(33, '01 - Kawtkaraik'), (34, '02 - Kyarinseikkyi'), (35, '03 - Phayathonesu*'), (36, '04 - Kyoandoe')]), ('09 - Phalan', [(37, '01 - Phalan'), (38, '02 - Hakha'), (39, '03 - Htantalan'), (40, '04 - Teetain'), (41, '05 - Tunzan')]), ('10 - Mintatt', [(42, '01 - Mintatt'), (43, '02 - Matupi'), (44, '03 - Kanpetlet'), (45, '04 - Paletwa')]), ('11 - Sagaing', [(46, '01 - Sagaing'), (47, '02 - Myinmu'), (48, '03 - Myaung')]), ('12 - Shwebo', [(49, '01 - Shwebo'), (50, '02 - Khin Oo'), (51, '03 - Wetlet'), (52, '04 - Kantbalu'), (53, '05 - Kyunhla'), (54, '06 - Yay Oo'), (55, '07 - Dipeiyin'), (56, '08 - Tantsei')]), ('13 - Monywar', [(57, '01 - Monywar'), (58, '02 - Butalin'), (59, '03 - Ahyartaw'), (60, '04 - Chaung Oo'), (61, '05 - Yinmarbin'), (62, '06 - Kani'), (63, '07 - Salingyee'), (64, '08 - Palei')]), ('14 - Kathar', [(65, '01 - Kathar'), (66, '02 - Indaw'), (67, '03 - Hteechaink'), (68, '04 - Bamauk'), (69, '05 - Kawlin'), (70, '06 - Wuntho'), (71, '07 - Pinleibu')]), ('15 - Kalay', [(72, '01 - Kalay'), (73, '02 - Kalaywa'), (74, '03 - Minkin')]), ('16 - Tamu', [(75, '01 - Tamu')]), ('17 - Mawlaik', [(76, '01 - Mawlaik'), (77, '02 - Phaungpyin')]), ('18 - Khantee', [(78, '01 - Khantee'), (79, '02 - Hoamalin'), (80, '03 - Layshee'), (81, '04 - Lahei'), (82, '05 - Nanyon')]), ('19 - Dawei', [(83, '01 - Dawei'), (84, '02 - Launglon'), (85, '03 - Thayetchaung'), (86, '04 - Yayphyu')]), ('20 - Myeik', [(87, '01 - Myeik'), (88, '02 - Kyunsu'), (89, '03 - Pulaw'), (90, '04 - Tanintharyi')]), ('21 - Kautthaung', [(91, '01 - Kautthaung'), (92, '02 - Boatpyin')]), ('22 - Bago', [(93, '01 - Bago'), (94, '02 - Thanatpin'), (95, '03 - Kawa'), (96, '04 - Waw'), (97, '05 - Nyaunglaybin'), (98, '06 - Madauk*'), (99, '07 - Pyuntanzar*'), (100, '08 - Kyauktaga'), (101, '09 - Peinweikone*'), (102, '10 - Daik Oo'), (103, '11 - Shwekyin')]), ('23 - Pyay', [(104, '01 - Pyay'), (105, '02 - Pauk Khaung'), (106, '03 - Padaung'), (107, '04 - Paungtei'), (108, '05 - Theikone'), (109, '06 - Shwetaung')]), ('24 - Tharyarwaddy', [(110, '01 - Tharyarwaddy'), (111, '02 - Thonesei*'), (112, '03 - Letpandan'), (113, '04 - Minhla'), (114, '05 - Oakpho'), (115, '06 - Zeekone'), (116, '07 - Nattalin'), (117, '08 - Moenyo'), (118, '09 - Kyoetbinkaut')]), ('25 - Taungoo', [(119, '01 - Taungoo'), (120, '02 - Yaytarshay'), (121, '03 - Kyaukyee'), (122, '04 - Phyu'), (123, '05 - Oaktwin'), (124, '06 - Htandabin')]), ('26 - Magway', [(125, '01 - Magway'), (126, '02 - Yenanchaung'), (127, '03 - Chauk'), (128, '04 - Taungtwingyee'), (129, '05 - Myoethit'), (130, '06 - Natmauk')]), ('27 - Minbu', [(131, '01 - Minbu'), (132, '02 - Saku*'), (133, '03 - Pwintphyu'), (134, '04 - Ngaphei'), (135, '05 - Salin'), (136, '06 - Sinphyukyun*'), (137, '07 - Saytoattaya')]), ('28 - Thayet', [(138, '01 - Thayet'), (139, '02 - Minhla'), (140, '03 - Mintone'), (141, '04 - Kanma'), (142, '05 - Aunglan'), (143, '06 - Sinpaungwei')]), ('29 - Pakokku', [(144, '01 - Pakokku'), (145, '02 - Yesagyo'), (146, '03 - Myaing'), (147, '04 - Pauk'), (148, '05 - Saikphyu')]), ('30 - Gantgaw', [(149, '01 - Gantgaw'), (150, '02 - Hteelin'), (151, '03 - Saw')]), ('31 - Mandalay', [(152, '01 - Aungmyaytharzan'), (153, '02 - Chanayetharzan'), (154, '03 - MahaAungmyay'), (155, '04 - Chanmyatharsi'), (156, '05 - Pyigyeetakhun'), (157, '06 - Amarapura'), (158, '07 - Myitnge*'), (159, '08 - Patheingyee')]), ('32 - Pyin Oo Lwin', [(160, '01 - Pyin Oo Lwin'), (161, '02 - Madayar'), (162, '03 - Sintkuu'), (163, '04 - Moegauk'), (164, '05 - Thabaikkyin')]), ('33 - Kyaukse', [(165, '01 - Kyaukse'), (166, '02 - Sintkai'), (167, '03 - Myitthar'), (168, '04 - Tadaoo')]), ('34 - Myingyan', [(169, '01 - Myingyan'), (170, '02 - Taungthar'), (171, '03 - Nahtoegyee'), (172, '04 - Kyaukbadaung'), (173, '05 - Nganzun')]), ('35 - Nyaung Oo', [(174, '01 - Nyaung Oo'), (175, '02 - Bagan*'), (176, '03 - Ngatharauk*')]), ('36 - Yameithinn', [(177, '01 - Yameithinn'), (178, '02 - Pyawbwei'), (179, '03 - Tatkone'), (180, '04 - Pyinmana'), (181, '05 - Leiway')]), ('37 - Meikhtila', [(182, '01 - Meikhtila'), (183, '02 - Mahlaing'), (184, '03 - Tharzi'), (185, '04 - Wantwin')]), ('38 - Mawlamyaing', [(186, '01 - Mawlamyaing'), (187, '02 - Kyaikmayaw'), (188, '03 - Chaungzon'), (189, '04 - Thanphyuzayat'), (190, '05 - Kyaikkhami*'), (191, '06 - Mudon'), (192, '07 - Yay')]), ('39 - Thahton', [(193, '01 - Thahton'), (194, '02 - Paung'), (195, '03 - Kyaikhto'), (196, '04 - Beelin')]), ('40 - Sittwe', [(197, '01 - Sittwe'), (198, '02 - Poannakyun'), (199, '03 - Myauk Oo'), (200, '04 - Kyauktaw'), (201, '05 - Minbya'), (202, '06 - Pauktaw'), (203, '07 - Myaybon')]), ('41 - Maungdaw', [(204, '01 - Maungdaw')]), ('42 - Buthidaung', [(205, '01 - Buthidaung'), (206, '02 - Rathedaung')]), ('43 - Kyaukphyu', [(207, '01 - Kyaukphyu'), (208, '02 - Man Aung'), (209, '03 - Ranbyei'), (210, '04 - Ann')]), ('44 - Thandwe', [(211, '01 - Thandwe'), (212, '02 - Taungkauk'), (213, '03 - Gwa')]), ('45 - Ahshaytbine (East)', [(214, '01 - Thingankyun'), (215, '02 - Yankin'), (216, '03 - Taung Okkalapa'), (217, '04 - Myauk Okkalapa'), (218, '05 - Tharketa'), (219, '06 - Dawbon'), (220, '07 - Tarmwe'), (221, '08 - Pazuntaung'), (222, '09 - Botahtaung'), (223, '10 - Dagon Myothit Taung (Sounth)'), (224, '11 - Dagon Myothi Myauk (North)'), (225, '12 - Dagon Myothit Ahshayt (East)'), (226, '13 - Dagon Myothit (Seikkan)'), (227, '14 - Mingalataungnyunt')]), ('46 - Ahnoutpine (West)', [(228, '01 - Kyauktada'), (229, '02 - Panbedan'), (230, '03 - Lanmadaw'), (231, '04 - Lathar'), (232, '05 - Ahlon'), (233, '06 - Kyeemyindine'), (234, '07 - Sanchaung'), (235, '08 - Hlaing'), (236, '09 - Kamaryut'), (237, '10 - Mayangone'), (238, '11 - Dagon'), (239, '12 - Bahan'), (240, '13 - Seikkan')]), ('47 - Taungbine (South)', [(241, '01 - Thanhlyin'), (242, '02 - Kyauktan'), (243, '03 - Thonekhwa'), (244, '04 - Khayan'), (245, '05 - Tonte'), (246, '06 - Kauthmu'), (247, '07 - Kunchangone'), (248, '08 - Dala'), (249, '09 - Seikkyee'), (250, '10 - Khanaungto'), (251, '11 - Kokoe Island')]), ('48 - Myaukpine (North)', [(252, '01 - Insein'), (253, '02 - Mingalardon'), (254, '03 - Htaunkkyant*'), (255, '04 - Hmawbi'), (256, '05 - Hlegu'), (257, '06 - Tiakkyee'), (258, '07 - Oakkan*'), (259, '08 - Htantabin'), (260, '09 - Shwepyithar'), (261, '10 - Hlaingtharyar'), (262, '11 - Ahphyauk*')]), ('49 - Taungyi', [(263, '01 - Taungyi'), (264, '02 - Ayetharyar*'), (265, '03 - Hopone'), (266, '04 - Nyaungshwe'), (267, '05 - Sisaing'), (268, '06 - Kalaw'), (269, '07 - Aungban*'), (270, '08 - Pindaya'), (271, '09 - Ywarngan'), (272, '10 - Yatsauk'), (273, '11 - Pinlaung'), (274, '12 - Phekhoan')]), ('50 - Loilin', [(275, '01 - Loilin'), (276, '02 - Pinlon'), (277, '03 - Leichar'), (278, '04 - Nantsam(South)'), (279, '05 - Kunhein'), (280, '06 - Moenei'), (281, '07 - Linkhay'), (282, '08 - Maukmei'), (283, '09 - Minepan'), (284, '10 - Kyaythee'), (285, '11 - Minekaing'), (286, '12 - Mineshu')]), ('51 - Lahsio', [(287, '01 - Lashio'), (288, '02 - Theinni'), (289, '03 - Mineyei'), (290, '04 - Tantyan'), (291, '05 - Minephant'), (292, '06 - Panyang'), (293, '07 - Narphan'), (294, '08 - Panwaing'), (295, '09 - Minemaw'), (296, '10 - Pansan (Pankhan)')]), ('52 - Muse', [(297, '01 - Muse'), (298, '02 - Nantkhan'), (299, '03 - Kutkhaing'), (300, '04 - Monkoe'), (301, '05 - Kyukoak')]), ('53 - Kyaukmei', [(302, '01 - Kyaukmei'), (303, '02 - Naungcho'), (304, '03 - Thibaw'), (305, '04 - Namtu'), (306, '05 - Nantsam(North)'), (307, '06 - Moemaik'), (308, '07 - Mabain'), (309, '08 - Mantoan')]), ('54 - Kunloan', [(310, '01 - Kunloan'), (311, '02 - Hopan')]), ('55 - Laukkaing', [(312, '01 - Laukkaing'), (313, '02 - Chinshwehaw*'), (314, '03 - Koankyan')]), ('56 - Kyaington', [(315, '01 - Kyaington'), (316, '02 - Minekhat'), (317, '03 - Mineyang'), (318, '04 - Minelar'), (319, '05 - Metman')]), ('57 - Minesatt', [(320, '01 - Minesatt'), (321, '02 - Minepyinn'), (322, '03 - Minetoan')]), ('58 - Tachilaik', [(323, '01 - Tachilaik')]), ('59 - Minephyat', [(324, '01 - Minephyat'), (325, '02 - Mineyaung')]), ('60 - Pathein', [(326, '01 - Pathein'), (327, '02 - Kangyidaunt'), (328, '03 - Tharpaung'), (329, '04 - Ngaputaw'), (330, '05 - Kyoanpyaw'), (331, '06 - Yaykyi'), (332, '07 - Ngathaingchaung'), (333, '08 - Kyaungkone'), (334, '09 - Haigyikyun')]), ('61 - Hinthada', [(335, '01 - Hinthada'), (336, '02 - Zalun'), (337, '03 - Laymyethnar'), (338, '04 - Myan Aung'), (339, '05 - Ka Naung'), (340, '06 - Kyankhin'), (341, '07 - Ingapu')]), ('62 - Myaungmya', [(342, '01 - Myaungmya'), (343, '02 - Ainmei'), (344, '03 - Laputta'), (345, '04 - Warkhema'), (346, '05 - Mawlamyaingkyun')]), ('63 - Ma U Bin', [(347, '01 - Ma U Bin'), (348, '02 - Pantanaw'), (349, '03 - Nyaungtone'), (350, '04 - Danubyu')]), ('64 - Phyarpon', [(351, '01 - Phyarpon'), (352, '02 - Bogalay'), (353, '03 - Kyaiklatt'), (354, '04 - Daydayei')]), ('65 - Zayarthiri', [(355, '01 - Zayarthiri')]), ('66 - Dakhenathiri', [(356, '01 - Dakhenathiri')]), ('67 - Oktayathiri', [(357, '01 - Oktayathiri')]), ('68 - Potebathiri', [(358, '01 - Potebathiri')]), ('69 - Zabuthiri', [(359, '01 - Zabuthiri')]), ('70 - Tatkon', [(360, '01 - Tatkon')]), ('71 - Pyinmana', [(361, '01 - Pyinmana')]), ('72 - Lewe', [(362, '01 - Lewe')])], validators=[birth_registration.validators.validate_2digits]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='f201',
            name='UPRS',
            field=birth_registration.fields.StateDivisionField(default=1, max_length=2, choices=[(1, '01 - Kachin'), (2, '02 - Kayh'), (3, '03 - Kayin'), (4, '04 - Chin'), (5, '05 - Sagaing'), (6, '06 - Tanintharyi'), (7, '07 - Bago'), (8, '08 - Magway'), (9, '09 - Mandalay'), (10, '10 - Mon'), (11, '11 - Rakhine'), (12, '12 - Yangon'), (13, '13 - Shan'), (14, '14 - Ayyarwaddy'), (15, '15 - NayPyiTaw')], validators=[birth_registration.validators.validate_2digits]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='f201',
            name='UPRS1',
            field=birth_registration.fields.DistrictField(default=1, max_length=2, choices=[('01 - Kachin', [(1, '01 - Myitkyina'), (2, '02 - Bamaw'), (3, '03 - Puta O')]), ('02 - Kayh', [(4, '04 - Loikaw'), (5, '05 - Bawlakhei')]), ('03 - Kayin', [(6, '06 - Pha An'), (7, '07 - Myawaddy'), (8, '08 - Kawtkaraik')]), ('04 - Chin', [(9, '09 - Phalan'), (10, '10 - Mintatt')]), ('05 - Sagaing', [(11, '11 - Sagaing'), (12, '12 - Shwebo'), (13, '13 - Monywar'), (14, '14 - Kathar'), (15, '15 - Kalay'), (16, '16 - Tamu'), (17, '17 - Mawlaik'), (18, '18 - Khantee')]), ('06 - Tanintharyi', [(19, '19 - Dawei'), (20, '20 - Myeik'), (21, '21 - Kautthaung')]), ('07 - Bago', [(22, '22 - Bago'), (23, '23 - Pyay'), (24, '24 - Tharyarwaddy'), (25, '25 - Taungoo')]), ('08 - Magway', [(26, '26 - Magway'), (27, '27 - Minbu'), (28, '28 - Thayet'), (29, '29 - Pakokku'), (30, '30 - Gantgaw')]), ('09 - Mandalay', [(31, '31 - Mandalay'), (32, '32 - Pyin Oo Lwin'), (33, '33 - Kyaukse'), (34, '34 - Myingyan'), (35, '35 - Nyaung Oo'), (36, '36 - Yameithinn'), (37, '37 - Meikhtila')]), ('10 - Mon', [(38, '38 - Mawlamyaing'), (39, '39 - Thahton')]), ('11 - Rakhine', [(40, '40 - Sittwe'), (41, '41 - Maungdaw'), (42, '42 - Buthidaung'), (43, '43 - Kyaukphyu'), (44, '44 - Thandwe')]), ('12 - Yangon', [(45, '45 - Ahshaytbine (East)'), (46, '46 - Ahnoutpine (West)'), (47, '47 - Taungbine (South)'), (48, '48 - Myaukpine (North)')]), ('13 - Shan', [(49, '49 - Taungyi'), (50, '50 - Loilin'), (51, '51 - Lahsio'), (52, '52 - Muse'), (53, '53 - Kyaukmei'), (54, '54 - Kunloan'), (55, '55 - Laukkaing'), (56, '56 - Kyaington'), (57, '57 - Minesatt'), (58, '58 - Tachilaik'), (59, '59 - Minephyat')]), ('14 - Ayyarwaddy', [(60, '60 - Pathein'), (61, '61 - Hinthada'), (62, '62 - Myaungmya'), (63, '63 - Ma U Bin'), (64, '64 - Phyarpon')]), ('15 - NayPyiTaw', [(65, '65 - Zayarthiri'), (66, '66 - Dakhenathiri'), (67, '67 - Oktayathiri'), (68, '68 - Potebathiri'), (69, '69 - Zabuthiri'), (70, '70 - Tatkon'), (71, '71 - Pyinmana'), (72, '72 - Lewe')])], validators=[birth_registration.validators.validate_2digits]),
            preserve_default=False,
        ),
    ]
