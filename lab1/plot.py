import matplotlib.pyplot as plt

intervalValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0007708235294, 0.002186743185, 0.003535238095, 0.004821012312, 0.006048342246, 0.007221124183, 0.008342915601, 0.009416971214, 0.01044627451, 0.01143356543, 0.01238136471, 0.01329199539, 0.01416760181, 0.01501016648, 0.01582152505, 0.01660337968, 0.01735731092, 0.01808478844, 0.01878718053, 0.01946576271, 0.02012172549, 0.02075618129, 0.02137017078, 0.02196466853, 0.02254058824, 0.02309878733, 0.0236400713, 0.02416519754, 0.02467487889, 0.02516978687, 0.02565055462, 0.02611777962, 0.02657202614, 0.02701382756, 0.02744368839, 0.02786208627, 0.02826947368, 0.0286662796, 0.02905291101, 0.02942975428, 0.02979717647, 0.03015552651, 0.0305051363, 0.03084632176, 0.03117938375, 0.031504609, 0.03182227086, 0.03213263016, 0.03243593583, 0.03273242564, 0.0330223268, 0.0333058565, 0.03358322251, 0.03385462366, 0.03412025031, 0.03438028483, 0.03463490196, 0.03488426925, 0.03512854742, 0.03536789067, 0.03560244706, 0.03583235877, 0.0360577624, 0.03627878926, 0.03649556561, 0.03670821289, 0.03691684795, 0.03712158329, 0.03732252723, 0.03751978413, 0.03771345455, 0.0379036354, 0.03809042017, 0.03827389901, 0.03845415893, 0.03863128389, 0.03880535497, 0.03897645048, 0.03914464606, 0.03931001483, 0.03947262745, 0.03963255226, 0.03978985535, 0.03994460067, 0.04009685009, 0.04024666353, 0.04039409897, 0.0405392126, 0.04068205882, 0.04082269038, 0.04096115837, 0.04109751235, 0.04123180036, 0.041364069, 0.04149436348, 0.04162272767, 0.04174920415, 0.04187383426, 0.04199665814, 0.04211771477, 0.04223704202, 0.04235467668, 0.04247065452, 0.04258501028, 0.04269777778, 0.04280898986, 0.04291867849, 0.04302687475, 0.0431336089, 0.04323891038, 0.04334280784, 0.04344532918, 0.04354650155, 0.0436463514, 0.04374490451, 0.04384218596, 0.04393822021, 0.0440330311, 0.04412664185, 0.0442190751, 0.04431035294, 0.04440049689, 0.04448952796, 0.04457746662, 0.04466433286, 0.04475014617, 0.04483492558, 0.04491868968, 0.04500145658, 0.045083244, 0.0451640692, 0.04524394909, 0.04532290014, 0.04540093846, 0.04547807978, 0.0455543395, 0.04562973262, 0.04570427385, 0.04577797753, 0.04585085771, 0.0459229281, 0.04599420214, 0.04606469295, 0.04613441337, 0.04620337596, 0.046271593, 0.04633907653, 0.04640583831, 0.04647188986, 0.04653724245, 0.04660190712, 0.04666589467, 0.04672921569, 0.04679188052, 0.04685389933, 0.04691528205, 0.04697603842, 0.04703617796, 0.04709571004, 0.04715464381, 0.04721298824, 0.04727075212, 0.04732794409, 0.04738457259, 0.04744064591, 0.04749617217, 0.04755115934, 0.04760561523, 0.04765954751, 0.04771296369, 0.04776587115, 0.04781827711, 0.04787018868, 0.04792161281, 0.04797255635, 0.04802302599, 0.04807302832, 0.0481225698, 0.04817165677, 0.04822029546, 0.04826849198, 0.04831625233, 0.04836358241, 0.048410488, 0.04845697479, 0.04850304837, 0.04854871421, 0.04859397771, 0.04863884417, 0.04868331878, 0.04872740665, 0.04877111281, 0.04881444219, 0.04885739965, 0.04889998994, 0.04894221777, 0.04898408774, 0.04902560437, 0.04906677212, 0.04910759537, 0.04914807843, 0.04918822553, 0.04922804084, 0.04926752844, 0.04930669238, 0.04934553661, 0.04938406504, 0.0494222815, 0.04946018975, 0.04949779353, 0.04953509647, 0.04957210218, 0.04960881419, 0.04964523599, 0.04968137101, 0.04971722261, 0.04975279412, 0.04978808881, 0.0498231099, 0.04985786055, 0.04989234389, 0.04992656299, 0.04996052088, 0.04999422053, 0.05002766488, 0.05006085683, 0.0500937992, 0.05012649482, 0.05015894644, 0.05019115679, 0.05022312854, 0.05025486434, 0.05028636678, 0.05031763844, 0.05034868184, 0.05037949947, 0.05041009378, 0.05044046719, 0.05047062209, 0.05050056083, 0.05053028571, 0.05055979904, 0.05058910305, 0.05061819996, 0.05064709196, 0.05067578122, 0.05070426985, 0.05073255995, 0.05076065359, 0.05078855282, 0.05081625963, 0.05084377603, 0.05087110395, 0.05089824533, 0.05092520208, 0.05095197607, 0.05097856916, 0.05100498316, 0.0510312199, 0.05105728113, 0.05108316863, 0.05110888411, 0.05113442929, 0.05115980586, 0.05118501548, 0.05121005979, 0.05123494041, 0.05125965894, 0.05128421696, 0.05130861603, 0.05133285769, 0.05135694345, 0.05138087481, 0.05140465326, 0.05142828025, 0.05145175724, 0.05147508563, 0.05149821052, 0.05152130226, 0.05154424922, 0.05156694118, 0.05158949176, 0.05161201315, 0.0516343951, 0.05165652869, 0.05167852607, 0.05170049802, 0.05172233557, 0.05174393113, 0.05176539542, 0.05178683779, 0.0518081506, 0.0518292275, 0.05185017781, 0.05187110955, 0.05189191631, 0.051912493, 0.05193294757, 0.0519533867, 0.05197370525, 0.05199379931, 0.05201377551, 0.05203373925, 0.05205358658, 0.05207321477, 0.05209272918, 0.05211223393, 0.05213162626, 0.0521508046, 0.05216987303, 0.05218893445, 0.05220788726, 0.05222663102, 0.05224526857, 0.05226390163, 0.0522824297, 0.05230075347, 0.05231897458, 0.05233719356, 0.05235531103, 0.05237322876, 0.05239104722, 0.05240886578, 0.05242658616, 0.05244411118, 0.05246154018, 0.05247897139, 0.05249630761, 0.05251345269, 0.05253050483, 0.05254756121, 0.05256452563, 0.05258130297, 0.05259799035, 0.05261468386, 0.05263128834, 0.05264770964, 0.05266404382, 0.05268038593, 0.0526966418, 0.05271271827, 0.05272871034, 0.05274471204, 0.05276063018, 0.05277637255, 0.05279203314, 0.05280770497, 0.0528232958, 0.05283871437, 0.05285405367, 0.05286940573, 0.05288467927, 0.05289978391, 0.05291481169, 0.05292985369, 0.05294481952, 0.05295961973, 0.05297434538, 0.05298908661, 0.05300375395]
intervals = [i for i in range(0,(10**7)+1, 25000)]
plt.plot(intervals, intervalValues)
plt.axis([-166666,10**7,-0.001,0.06])
plt.ylabel('Błąd względny')
plt.xlabel('Liczba operacji')
plt.show()

