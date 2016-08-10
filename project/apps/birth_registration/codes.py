from django.utils.translation import ugettext_lazy as _, string_concat

URBAN = 1
RURAL = 2

BORN_ALIVE = 1
BORN_DEAD = 2

SEX_MALE = 1
SEX_FEMALE = 2
SEX_NOT_STATED = 9

PRE_DELI_YES = 1
PRE_DELI_NO = 2

YANGON_STATE_DIVISION_CODE = 12
YANGON_HOSPITAL_NOT_MENTIONED_CODE = 99
ANY_HOSPITAL_CODE = 1

CODES = [
    [
        (1, _('Kachin State')),
        [
            [
                (1, _('Myitkyina')),
                [
                    (1, 1, _('Myitkyina')),
                    (2, 2, _('Hsinbo')),
                    (3, 3, _('Waingmaw')),
                    (4, 4, _('Hsadone')),
                    (5, 5, _('Kanpaikti')),
                    (6, 6, _('Ingyanyan')),
                    (7, 7, _('Tanaing')),
                    (8, 8, _('Shinbwayyan')),
                    (9, 9, _('Chiphwe')),
                    (10, 10, _('Panwa')),
                    (11, 11, _('Hsotlaw'))
                ]
            ],
            [
                (2, _('Mohnyin')),
                [
                    (12, 1, _('Mohnyin')),
                    (13, 2, _('Hopin')),
                    (14, 3, _('Mogaung')),
                    (15, 51, _('Nanmatee')),
                    (16, 4, _('Phakant')),
                    (17, 5, _('Kamine'))
                ]
            ],
            [
                (3, _('Bhamo')),
                [
                    (18, 1, _('Bhamo')),
                    (19, 2, _('_Shwegu')),
                    (20, 3, _('Myohla')),
                    (21, 4, _('Momauk')),
                    (22, 5, _('Lwe`ge`')),
                    (23, 6, _('Dotphoneyan')),
                    (24, 7, _('Mansi'))
                ]
            ],
            [
                (4, _('Putao')),
                [
                    (25, 1, _('Putao')),
                    (26, 2, _('Sumprabum')),
                    (27, 3, _('Machanbaw')),
                    (28, 4, _('Khaunglanphoo')),
                    (29, 5, _('Naungmoon')),
                    (30, 6, _('Pannandin'))
                ]
            ]
        ]
    ],
    [
        (2, _('Kayah State')),
        [
            [
                (5, _('LoiKaw')),
                [
                    (31, 1, _('LoiKaw ')),
                    (32, 2, _('Dimawso')),
                    (33, 3, _('Phruso')),
                    (34, 4, _('Shadaw'))
                ]
            ],
            [
                (6, _('Bawlakhe')),
                [
                    (35, 1, _('Bawlakhe ')),
                    (36, 2, _('Ywathit')),
                    (37, 3, _('Phrsaung')),
                    (38, 4, _('Meisi'))
                ]
            ]
        ]
    ],
    [
        (3, _('Kayin State')),
        [
            [
                (7, _('Hpa-an')),
                [
                    (39, 1, _('Hpa-an ')),
                    (40, 2, _('Hlaingbwe')),
                    (41, 3, _('Paingkyon')),
                    (42, 4, _('Shan Ywathit')),
                    (43, 5, _('Thandaunggyi')),
                    (44, 51, _('Thandaung')),
                    (45, 6, _('Leiktho')),
                    (46, 7, _('Bawgali'))
                ]
            ],
            [
                (8, _('Kawkareik')),
                [
                    (47, 1, _('Kawkareik')),
                    (48, 51, _('Kyondoe')),
                    (49, 2, _('Kyarinseikkyi')),
                    (50, 3, _('Payarthonezu')),
                    (51, 4, _('Kyaidon'))
                ]
            ],
            [
                (9, _('Myawady')),
                [
                    (52, 1, _('Myawady')),
                    (53, 2, _('Sugali')),
                    (54, 3, _('Wawlaymyaing(Wawlay)'))
                ]
            ],
            [
                (10, _('Pharpon')), [
                (55, 1, _('Pharpon')), (56, 2, _('Kamamaung'))
            ]
            ]
        ]
    ],
    [
        (4, _('Chin State')),
        [
            [
                (11, _('Haka')), [
                (57, 1, _('Haka')), (58, 2, _('Thantlang'))
            ]
            ],
            [
                (12, _('Falam')),
                [
                    (59, 1, _('Falam')),
                    (60, 2, _('Rihkhuadal')),
                    (61, 3, _('Tedim')),
                    (62, 4, _('Tonzaung')),
                    (63, 5, _('Cikha'))
                ]
            ],
            [
                (13, _('Mindat')),
                [
                    (64, 1, _('Mindat')),
                    (65, 2, _('Matupi')),
                    (66, 3, _('Reazu')),
                    (67, 4, _('Kanpalet')),
                    (68, 5, _('Paletwa')),
                    (69, 6, _('Sami'))
                ]
            ]
        ]
    ],
    [
        (5, _('Sagaing Region')),
        [
            [
                (14, _('Monywa')),
                [
                    (70, 1, _('Monywa')),
                    (71, 2, _('Butalin')),
                    (72, 3, _('Ayartaw')),
                    (73, 4, _('Chaung Oo'))
                ]
            ],
            [
                (15, _('_ Shwebo')),
                [
                    (74, 1, _('_ Shwebo')),
                    (75, 2, _('Kyaukmyaung')),
                    (76, 3, _('Khin U')),
                    (77, 4, _('Wetlet')),
                    (78, 5, _('Depayin'))
                ]
            ],
            [
                (16, _('Kambalu')),
                [
                    (79, 1, _('Kambalu')),
                    (80, 2, _('Kyunhla')),
                    (81, 3, _('_Ye U')),
                    (82, 4, _('Tasei'))
                ]
            ],
            [
                (17, _('Sagaing')),
                [
                    (83, 1, _('Sagaing')),
                    (84, 2, _('Myinmu')),
                    (85, 3, _('Myaung'))
                ]
            ],
            [
                (18, _('Yinmarpin')),
                [
                    (86, 1, _('Yinmarpin')),
                    (87, 2, _('Kani')),
                    (88, 3, _('Sarlingyi')),
                    (89, 4, _('Palae'))
                ]
            ],
            [
                (19, _('Katha')),
                [
                    (90, 1, _('Katha')),
                    (91, 2, _('Indaw')),
                    (92, 3, _('Tigyaing')),
                    (93, 4, _('Banmauk')),
                    (94, 5, _('Kawlin')),
                    (95, 6, _('Wutho')),
                    (96, 7, _('Pinlebu'))
                ]
            ],
            [
                (20, _('Kalay')), [
                (97, 1, _('Kalay')), (98, 2, _('Kalawa')), (99, 3, _('Mingin'))
            ]
            ],
            [
                (21, _('Tamu')),
                [
                    (100, 1, _('Tamu')), (101, 2, _('Myothit')), (102, 3, _('Khampat'))
                ]
            ],
            [
                (22, _('Mawlaik')), [
                (103, 1, _('Mawlaik')), (104, 2, _('Phaungpyin'))
            ]
            ],
            [
                (23, _('Hkanmti')),
                [
                    (105, 1, _('Hkanmti')),
                    (106, 2, _('Homalin')),
                    (107, 51, _('Shwepyiaye')),
                    (108, 3, _('Lashi')),
                    (109, 4, _('Mobaingluk')),
                    (110, 5, _('Sonemara')),
                    (111, 6, _('Lahe')),
                    (112, 7, _('Htanparkway')),
                    (113, 8, _('Nanyun')),
                    (114, 9, _('Pansaung')),
                    (115, 10, _('Donhee'))
                ]
            ]
        ]
    ],
    [
        (6, _('Tanintharyi Region')),
        [
            [
                (24, _('Dawei')),
                [
                    (116, 1, _('Dawei')),
                    (117, 2, _('Myitta')),
                    (118, 3, _('_Longlone')),
                    (119, 4, _('Thayetchaung')),
                    (120, 5, _('_Yebyu')),
                    (121, 6, _('Kaleinaung'))
                ]
            ],
            [
                (25, _('Myeik ')),
                [
                    (122, 1, _('Myeik ')),
                    (123, 2, _('Kyunsu')),
                    (124, 3, _('Palaw')),
                    (125, 4, _('Palauk')),
                    (126, 5, _('Tanintharyi'))
                ]
            ],
            [
                (26, _('_ Kawthoung')),
                [
                    (127, 1, _('_Kawthoung')),
                    (128, 2, _('Khamaukkyi')),
                    (129, 3, _('Bokepyin')),
                    (130, 4, _('Pyigyimandaing')),
                    (131, 5, _('Karathuri'))
                ]
            ]
        ]
    ],
    [
        (7, _('Bago Region')),
        [
            [
                (27, _('Bago')),
                [
                    (132, 1, _('Bago')),
                    (133, 51, _('Payagyi')),
                    (134, 52, _('Inntakaw')),
                    (135, 2, _('Tanatpin')),
                    (136, 3, _('Kawa')),
                    (137, 53, _('Thetkala')),
                    (138, 4, _('Waw')),
                    (139, 5, _('Kyauktaga')),
                    (140, 54, _('Penwegon')),
                    (141, 55, _('Phado')),
                    (142, 6, _('Daik U')),
                    (143, 7, _('_Shwegyin')),
                    (144, 8, _('Nyaunglebin')),
                    (145, 56, _('Madauk')),
                    (146, 57, _('Pyuntasa')),
                    (147, 58, _('Painzaloat'))
                ]
            ],
            [
                (28, _('Taungoo')),
                [
                    (148, 1, _('Taungoo')),
                    (149, 51, _('Kaytumati')),
                    (150, 2, _('Yaedashe')),
                    (151, 52, _('Swa')),
                    (152, 3, _('_Kyauklyi')),
                    (153, 4, _('Pyu')),
                    (154, 53, _('Zayyawaddy')),
                    (155, 54, _('Kanyutkwin')),
                    (156, 5, _('Oatwin')),
                    (157, 55, _('Kyaepwe')),
                    (158, 6, _('Htantapin'))
                ]
            ],
            [
                (29, _('Pyay')),
                [
                    (159, 1, _('Pyay')),
                    (160, 51, _('Paungtale')),
                    (161, 2, _('_Paukkhaung')),
                    (162, 3, _('Padaung')),
                    (163, 52, _('Oatshitpin')),
                    (164, 4, _('_Paunde')),
                    (165, 5, _('Thegon')),
                    (166, 53, _('Patigone')),
                    (167, 6, _('Shewdaung'))
                ]
            ],
            [
                (30, _('Thayawady')),
                [
                    (168, 1, _('Thayawady')),
                    (169, 51, _('Thoneze')),
                    (170, 2, _('Letpadan')),
                    (171, 3, _('Minhla')),
                    (172, 52, _('Sitkwin')),
                    (173, 4, _('Okpo')),
                    (174, 53, _('Othekon')),
                    (175, 5, _('Zigon')),
                    (176, 6, _('Nattalin')),
                    (177, 54, _('Tarpon')),
                    (178, 7, _('Monyo')),
                    (179, 8, _('Gyobingauk'))
                ]
            ]
        ]
    ],
    [
        (8, _('Magway Region')),
        [
            [
                (31, _('Magway')),
                [
                    (180, 1, _('Magway')),
                    (181, 2, _('_Yenanyoung')),
                    (182, 3, _('Chauk')),
                    (183, 4, _('_Tawngdwingyi')),
                    (184, 5, _('Myothit')),
                    (185, 6, _('Natmauk'))
                ]
            ],
            [
                (32, _('Minbu')),
                [
                    (186, 1, _('Minbu')),
                    (187, 51, _('Sagu')),
                    (188, 2, _('Pwint Phyu')),
                    (189, 3, _('Ngape')),
                    (190, 4, _('Salin')),
                    (191, 52, _('Sinphyukyun')),
                    (192, 5, _('Saytottara'))
                ]
            ],
            [
                (33, _('Thayet')),
                [
                    (193, 1, _('Thayet')),
                    (194, 2, _('Minhla')),
                    (195, 3, _('Mindon')),
                    (196, 4, _('Kamma')),
                    (197, 5, _('Aunglan')),
                    (198, 6, _('Sinpaungwe'))
                ]
            ],
            [
                (34, _('Pakokku')),
                [
                    (199, 1, _('Pakokku')),
                    (200, 51, _('Kanma')),
                    (201, 2, _('_Yesagyo')),
                    (202, 3, _('Myaing')),
                    (203, 4, _('_Pauk')),
                    (204, 5, _('Seikphyu'))
                ]
            ],
            [
                (35, _('Gangaw')),
                [
                    (205, 1, _('Gangaw')),
                    (206, 51, _('Kyaw`')),
                    (207, 2, _('Htilin')),
                    (208, 3, _('Saw')),
                    (209, 4, _('Kyaukhtu'))
                ]
            ]
        ]
    ],
    [
        (9, _('Mandalay Region')),
        [
            [
                (36, _('Mandalay')),
                [
                    (210, 1, _('_Aungmyethazan')),
                    (211, 2, _('Chanayeharzan')),
                    (212, 3, _('Mahaaungmye')),
                    (213, 4, _('Chanmyatharzai')),
                    (214, 5, _('Pyigyidagon')),
                    (215, 6, _('Mmarapura')),
                    (216, 51, _('Myitnge')),
                    (217, 7, _('Patheingyi'))
                ]
            ],
            [
                (37, _('Pyin Oo Lwin')),
                [
                    (218, 1, _('Pyin Oo Lwin')),
                    (219, 2, _('Madaya')),
                    (220, 3, _('Sinku')),
                    (221, 4, _('Mogok')),
                    (222, 5, _('Thabeikkyin')),
                    (223, 6, _('Tagaung'))
                ]
            ],
            [
                (38, _('Kyaukse')),
                [
                    (224, 1, _('Kyaukse')),
                    (225, 2, _('Singaing')),
                    (226, 3, _('Myitthar')),
                    (227, 4, _('Tada U'))
                ]
            ],
            [
                (39, _('Myingyan')),
                [
                    (228, 1, _('Myingyan')),
                    (229, 2, _('Taungtha')),
                    (230, 3, _('Natogyi')),
                    (231, 4, _('Ngazun'))
                ]
            ],
            [
                (40, _('Nyaung U')),
                [
                    (232, 1, _('Nyaung U')),
                    (233, 51, _('Bagan')),
                    (234, 2, _('Ngathayauk')),
                    (235, 3, _('Kyaukpadaung'))
                ]
            ],
            [
                (41, _('Meiktila')),
                [
                    (236, 1, _('Meiktila')),
                    (237, 2, _('Mahling')),
                    (238, 3, _('Thazi')),
                    (239, 4, _('Wundwin'))
                ]
            ],
            [
                (42, _('Yamethin')), [
                (240, 1, _('Yamethin')), (241, 2, _('Pyawbwe'))
            ]
            ]
        ]
    ],
    [
        (10, _('Mon State')),
        [
            [
                (43, _('Mawlamyine')),
                [
                    (242, 1, _('Mawlamyine')),
                    (243, 2, _('Kyaikemaraw')),
                    (244, 3, _('Chaungzon')),
                    (245, 4, _('Thanbyuzayat')),
                    (246, 51, _('Kyaikkhami')),
                    (247, 5, _('Mudon')),
                    (248, 52, _('Kamarwat')),
                    (249, 6, _('Ye')),
                    (250, 7, _('Lamine')),
                    (251, 8, _('Khawzar'))
                ]
            ],
            [
                (44, _('Thaton')),
                [
                    (252, 1, _('Thaton')),
                    (253, 2, _('Paung')),
                    (254, 51, _('Zinkyate')),
                    (255, 3, _('Kyaikto')),
                    (256, 4, _('Bilin')),
                    (257, 52, _('Tuwanawaddy'))
                ]
            ]
        ]
    ],
    [
        (11, _('Rakhine State')),
        [
            [
                (45, _('Sittway ')),
                [
                    (258, 1, _('Sittway ')),
                    (259, 2, _('Ponnagyun')),
                    (260, 3, _('Pauktaw')),
                    (261, 4, _('Yethedaung'))
                ]
            ],
            [
                (46, _('_Myauk U')),
                [
                    (262, 1, _('_Myauk U')),
                    (263, 2, _('Kyauktaw')),
                    (264, 3, _('Minbya')),
                    (265, 4, _('Myebon')),
                    (266, 51, _('Kantauntgyi'))
                ]
            ],
            [
                (47, _('Maungtaw')),
                [
                    (267, 1, _('Maungtaw')),
                    (268, 2, _('Taungpyoletwe')),
                    (269, 3, _('Buthidaung'))
                ]
            ],
            [
                (48, _('Kuaukpyu')),
                [
                    (270, 1, _('Kuaukpyu')),
                    (271, 51, _('Sanae')),
                    (272, 2, _('Mannaung')),
                    (273, 3, _('Yanbye')),
                    (274, 4, _('An')),
                    (275, 52, _('Tattaung'))
                ]
            ],
            [
                (49, _('Thandwe')),
                [
                    (276, 1, _('Thandwe')),
                    (277, 51, _('Ngapali')),
                    (278, 2, _('Taungup')),
                    (279, 3, _('Maei')),
                    (280, 4, _('Gwa')),
                    (281, 5, _('Kyeintali'))
                ]
            ]
        ]
    ],
    [
        (12, _('Yangon Region')),
        [
            [
                (50, _('East Yangon')),
                [
                    (282, 1, _('Thingangyun')),
                    (283, 2, _('Yankin')),
                    (284, 3, _('South Okkalapa')),
                    (285, 4, _('North Okkalapa')),
                    (286, 5, _('Thakayta')),
                    (287, 6, _('Dawbon')),
                    (288, 7, _('Tamway')),
                    (289, 8, _('Pazuntaung')),
                    (290, 9, _('Botahtaung')),
                    (291, 10, _('Dagon Myothit(South)')),
                    (292, 11, _('Dagon Myothit(North)')),
                    (293, 12, _('Dagon Myothit(East)')),
                    (294, 13, _('Dagon Myothit(Seikkan)')),
                    (295, 14, _('Mingala Taungnyunt'))
                ]
            ],
            [
                (51, _('West Yangon')),
                [
                    (296, 1, _('_Kyuktada')),
                    (297, 2, _('Pabedan')),
                    (298, 3, _('Lanmadaw')),
                    (299, 4, _('Latha')),
                    (300, 5, _('Ahlon')),
                    (301, 6, _('Kyimyindine')),
                    (302, 7, _('Sangyoung')),
                    (303, 8, _('Hline')),
                    (304, 9, _('Kamayut')),
                    (305, 10, _('Mayangon')),
                    (306, 11, _('Dagon')),
                    (307, 12, _('Bahan')),
                    (308, 13, _('Seikkan'))
                ]
            ],
            [
                (52, _('South Yangon')),
                [
                    (309, 1, _('Thanlyin')),
                    (310, 2, _('Kyauktan')),
                    (311, 3, _('Tada')),
                    (312, 4, _('Thongwa')),
                    (313, 5, _('Khayan')),
                    (314, 6, _('Twantay')),
                    (315, 7, _('Kawhmu')),
                    (316, 8, _('Kungyangon')),
                    (317, 9, _('Dala')),
                    (318, 10, _('Seikkyi/Khanaungto')),
                    (319, 11, _('Cocogyun'))
                ]
            ],
            [
                (53, _('North Yangon')),
                [
                    (320, 1, _('Insein')),
                    (321, 2, _('Mingaladon')),
                    (322, 51, _('Htaukkyant')),
                    (323, 3, _('_Hmawby')),
                    (324, 4, _('Hlagu')),
                    (325, 5, _('Taikkyi')),
                    (326, 52, _('Okkan')),
                    (327, 53, _('Aphyaut')),
                    (328, 6, _('Htantabin')),
                    (329, 7, _('Shwepyitha')),
                    (330, 8, _('Hlaingthaya'))
                ]
            ]
        ]
    ],
    [
        (13, _('Shan State')),
        [
            [
                (54, _('Taunggyi')),
                [
                    (331, 1, _('Taunggyi')),
                    (332, 51, _('Ayetharyar')),
                    (333, 52, _('Shwenyaung')),
                    (334, 2, _('Kyauktalongyi')),
                    (335, 3, _('Hopon')),
                    (336, 4, _('Nyaungshwe')),
                    (337, 5, _('Hsihseng')),
                    (338, 6, _('Kalaw')),
                    (339, 53, _('Aungban')),
                    (340, 7, _('Pindaya')),
                    (341, 8, _('Ywamgan')),
                    (342, 9, _('Yatsauk')),
                    (343, 10, _('Indaw')),
                    (344, 11, _('Pinlaung')),
                    (345, 54, _('Paunglong')),
                    (346, 12, _('Naungtayar')),
                    (347, 13, _('Phekon'))
                ]
            ],
            [
                (55, _('Loilin ')),
                [
                    (348, 1, _('Loilin ')),
                    (349, 2, _('Panglong')),
                    (350, 3, _('Lechar')),
                    (351, 4, _('Nanhsam(south)')),
                    (352, 5, _('Kholan')),
                    (353, 6, _('Kunhing')),
                    (354, 7, _('Karli')),
                    (355, 8, _('Kehsi')),
                    (356, 9, _('Minenaung')),
                    (357, 10, _('Mongkai')),
                    (358, 11, _('Mineshu')),
                    (359, 12, _('Minesan (Monsan)'))
                ]
            ],
            [
                (56, _('Linkhe`')),
                [
                    (360, 1, _('Linkhe`')),
                    (361, 2, _('Homane')),
                    (362, 3, _('Mone`')),
                    (363, 4, _('Kengtaung')),
                    (364, 5, _('Maukme')),
                    (365, 6, _('Minepan'))
                ]
            ],
            [
                (57, _('Kengtung')),
                [
                    (366, 1, _('Kengtung')),
                    (367, 2, _('Minekai')),
                    (368, 3, _('Mineyan')),
                    (369, 4, _('Minepauk')),
                    (370, 5, _('Minelar')),
                    (371, 6, _('Minepyin')),
                    (372, 7, _('Tontar'))
                ]
            ],
            [
                (58, _('Minesat')),
                [
                    (373, 1, _('Minesat')),
                    (374, 2, _('Minekoke')),
                    (375, 3, _('Minetung')),
                    (376, 4, _('Ponparkyin')),
                    (377, 5, _('Monehta'))
                ]
            ],
            [
                (59, _('Tachileik')),
                [
                    (378, 1, _('Tachileik')),
                    (379, 2, _('Talay')),
                    (380, 3, _('Kenglat')),
                    (381, 4, _('Minephyat')),
                    (382, 5, _('Mineyaung')),
                    (383, 6, _('Mineyu'))
                ]
            ],
            [
                (60, _('Lashio')),
                [
                    (384, 1, _('Lashio')),
                    (385, 2, _('Theinni')),
                    (386, 3, _('Mineye')),
                    (387, 4, _('Tantyan')),
                    (388, 5, _('Kunlon'))
                ]
            ],
            [
                (61, _('Hopan')),
                [
                    (389, 1, _('Hopan')),
                    (390, 2, _('Namtik')),
                    (391, 3, _('Panlon')),
                    (392, 4, _('Panwine')),
                    (393, 5, _('Minemaw'))
                ]
            ],
            [
                (62, _('Muse')),
                [
                    (394, 1, _('Muse')),
                    (395, 2, _('Monekoe (Manhyo)')),
                    (396, 3, _('Manhero')),
                    (397, 4, _('Pansai (Kyu-kok)')),
                    (398, 5, _('Namkham')),
                    (399, 6, _('Kukai')),
                    (400, 7, _('Tamoenye'))
                ]
            ],
            [
                (63, _('Momeik')), [
                (401, 1, _('Momeik')), (402, 2, _('Mabane'))
            ]
            ],
            [
                (64, _('_Kyaukme')),
                [
                    (403, 1, _('_Kyaukme')),
                    (404, 2, _('Minengaw')),
                    (405, 3, _('Minelon')),
                    (406, 4, _('_Naungkhio')),
                    (407, 5, _('Hsipaw')),
                    (408, 6, _('Namtu')),
                    (409, 7, _('Namsan(North)')),
                    (410, 8, _('Manton'))
                ]
            ],
            [
                (65, _('Laukine')),
                [
                    (411, 1, _('Laukine')),
                    (412, 2, _('Chinshwehaw')),
                    (413, 3, _('Kongyan')),
                    (414, 4, _('Mawhtike'))
                ]
            ],
            [
                (66, _('Makman')),
                [
                    (415, 1, _('Makman')),
                    (416, 2, _('Pansan(Pankhan)')),
                    (417, 3, _('Mankan')),
                    (418, 4, _('Naphang'))
                ]
            ]
        ]
    ],
    [
        (14, _('Ayeyawady Region')),
        [
            [
                (67, _('Pathein')),
                [
                    (419, 1, _('Pathein')),
                    (420, 2, _('Shwethaungyan')),
                    (421, 3, _('Ngwehsaung')),
                    (422, 4, _('Kyaungyidaunt')),
                    (423, 5, _('Thapaung')),
                    (424, 6, _('Ngaputaw')),
                    (425, 7, _('Ngayokaung')),
                    (426, 8, _('Hainggyikyun')),
                    (427, 9, _('Kyonpyaw')),
                    (428, 51, _('Ahtaung')),
                    (429, 10, _('_Yekyi')),
                    (430, 52, _('Athot')),
                    (431, 11, _('Ngathaingchaung')),
                    (432, 12, _('Kyaungon'))
                ]
            ],
            [
                (68, _('Hinthada')),
                [
                    (433, 1, _('Hinthada')),
                    (434, 2, _('Zalun')),
                    (435, 3, _('_Laymyethna')),
                    (436, 4, _('Myanaung')),
                    (437, 51, _('Kanaung')),
                    (438, 5, _('Kyangin')),
                    (439, 52, _('Batye')),
                    (440, 6, _('Ingapu')),
                    (441, 53, _('Htoogyi'))
                ]
            ],
            [
                (69, _('Myaungmya')),
                [
                    (442, 1, _('Myaungmya')),
                    (443, 2, _('Einme')),
                    (444, 3, _('Wakema')),
                    (445, 51, _('Kyonemangay'))
                ]
            ],
            [
                (70, _('Laputta')),
                [
                    (446, 1, _('Laputta')), (447, 2, _('Pyinsalu')), (448, 3, _('Mawlamyinegyum'))
                ]
            ],
            [
                (71, _('Maubin')),
                [
                    (449, 1, _('Maubin')),
                    (450, 2, _('Pantanaw')),
                    (451, 3, _('Nyaungdon')),
                    (452, 4, _('Danypyu'))
                ]
            ],
            [
                (72, _('Phyapon')),
                [
                    (453, 1, _('Phyapon')),
                    (454, 2, _('Ahmar')),
                    (455, 3, _('Bogale')),
                    (456, 4, _('Kyaiklatt')),
                    (457, 5, _('_Kaydaye'))
                ]
            ]
        ]
    ],
    [
        (15, _('Nay Pyi Taw Council')),
        [
            [
                (73, _('Ottarathiri')),
                [
                    (458, 1, _('Ottarathiri')),
                    (459, 2, _('_Zeyarthiri')),
                    (460, 3, _('Pobbathiri')),
                    (461, 4, _('Tatkon'))
                ]
            ],
            [
                (74, _('Dekkhinathiri')),
                [
                    (462, 1, _('Dekkhinathiri')),
                    (463, 2, _('Zabuthiri')),
                    (464, 3, _('Pyinmana')),
                    (465, 4, _('Lewe'))
                ]
            ]
        ]
    ]
]

CODE_DELIMITER = " - "


def choice_from_tuple(state_division, inverted=False):
    if not inverted:
        return state_division[0], string_concat("%02d" % state_division[0], CODE_DELIMITER, state_division[1])
    else:
        return state_division[1], string_concat("%02d" % state_division[1], CODE_DELIMITER, state_division[0])


def label_from_tuple(state_division_list):
    return string_concat("%02d" % state_division_list[0], CODE_DELIMITER, state_division_list[1])


def choice_from_three_tuple(state_division):
    return state_division[0], string_concat("%02d" % state_division[1], CODE_DELIMITER, state_division[2])


def label_from_three_tuple(state_division_list):
    return string_concat("%02d" % state_division_list[1], CODE_DELIMITER, state_division_list[2])


# todo: join _load_choices and _load_validators

def load_choices(codes):
    _State_Division_Choices = []
    _District_Choices = []
    _Township_or_town_Choices = []
    _Sub_code_No_Choices = [(ANY_HOSPITAL_CODE, string_concat(_(u"1"), CODE_DELIMITER, _(u"Any hospital")))]

    for state_division_list in codes:
        _State_Division_Choices.append(choice_from_tuple(state_division_list[0]))
        _District_Choices.append((label_from_tuple(state_division_list[0]), []))
        for districts in state_division_list[1]:
            _District_Choices[-1][-1].append(choice_from_tuple(districts[0]))
            _Township_or_town_Choices.append((label_from_tuple(districts[0]), []))
            for township_or_town in districts[1]:
                _Township_or_town_Choices[-1][-1].append(choice_from_three_tuple(township_or_town))
                if len(township_or_town) > 3:
                    hospitals = [choice_from_tuple(hospital, True) for hospital in township_or_town[3:]]
                    if not isinstance(hospitals, list):
                        hospitals = [hospitals]
                    _Sub_code_No_Choices.append(
                        (
                            label_from_three_tuple(township_or_town),
                            hospitals
                        )
                    )

    _Sub_code_No_Choices.append((YANGON_HOSPITAL_NOT_MENTIONED_CODE, string_concat(_(u"99"), CODE_DELIMITER,
                                                                                  _(u"Not mentioned"))))

    return _State_Division_Choices, _District_Choices, _Township_or_town_Choices, _Sub_code_No_Choices


def _load_validators(codes):
    _State_Division_Dictionary = []
    _District_Dictionary = {}
    _Township_or_town_Dictionary = {}
    _Sub_code_No_Dictionary = {}

    for state_division_list in codes:
        state_division = state_division_list[0][0]
        _State_Division_Dictionary.append(state_division)
        _District_Dictionary[state_division] = []
        for districts in state_division_list[1]:
            district = districts[0][0]
            _District_Dictionary[state_division].append(district)
            _Township_or_town_Dictionary[district] = []
            for township_or_town in districts[1]:
                _Township_or_town_Dictionary[district].append(township_or_town[0])
                if len(township_or_town) > 3:
                    _Sub_code_No_Dictionary[township_or_town[0]] = [hospital[1] for hospital in township_or_town[3:]]
    return _State_Division_Dictionary, _District_Dictionary, _Township_or_town_Dictionary, _Sub_code_No_Dictionary


State_Division_Choices, District_Choices, Township_or_town_Choices, Sub_code_No_Choices = load_choices(CODES)

State_Division_Dictionary, District_Dictionary, Township_or_town_Dictionary, Sub_code_No_Dictionary = _load_validators(
    CODES)


def validate_location_codes(ST_DV, ST_DV_field, DIS=None, DIS_field=None, TWN=None, TWN_field=None):
    validation_errors = {}
    if ST_DV:
        if not ST_DV in State_Division_Dictionary:
            validation_errors[ST_DV_field] = [
                _(u'Invalid State Division value: %s' % ST_DV), ]
        else:
            if DIS:
                if not DIS in District_Dictionary.get(ST_DV, []):
                    validation_errors[DIS_field] = [_(u'This district belongs to another state division'), ]

                if TWN:
                    if not (TWN in Township_or_town_Dictionary.get(DIS, [])):
                        validation_errors[TWN_field] = [_(u'This township or town belongs to another district'), ]

    return validation_errors
